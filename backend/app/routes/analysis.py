from collections import Counter

from fastapi import APIRouter, HTTPException, Query

from app.models.schemas import AnalysisResponse, PostAnalysis, SentimentSummary
from app.services.emotion_service import EMOTION_LABELS, classify_emotion
from app.services.sentiment_service import analyze_sentiment
from app.services.twitter_service import TwitterService, TwitterServiceError
from app.utils.text_processing import clean_text

router = APIRouter(tags=["analysis"])
twitter_service = TwitterService()


@router.get("/api/analyze", response_model=AnalysisResponse)
def analyze(query: str = Query(min_length=1, max_length=120)) -> AnalysisResponse:
    normalized_query = query.strip()
    if not normalized_query:
        raise HTTPException(status_code=422, detail="Query cannot be empty.")

    try:
        source_posts = twitter_service.search(normalized_query)
    except TwitterServiceError as exc:
        raise HTTPException(status_code=exc.status_code, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Analysis could not be completed.") from exc

    if not source_posts:
        raise HTTPException(status_code=404, detail=f"No public posts found for '{normalized_query}'.")

    analyzed_posts: list[PostAnalysis] = []
    for source_post in source_posts:
        text = clean_text(source_post.text)
        if not text:
            continue
        try:
            sentiment = analyze_sentiment(text)
            analyzed_posts.append(
                PostAnalysis(
                    id=source_post.id,
                    text=text,
                    created_at=source_post.created_at,
                    author=source_post.author,
                    sentiment=str(sentiment["sentiment"]),
                    emotion=classify_emotion(text, str(sentiment["sentiment"])),
                    polarity=float(sentiment["polarity"]),
                    subjectivity=float(sentiment["subjectivity"]),
                    confidence=float(sentiment["confidence"]),
                )
            )
        except Exception as exc:
            raise HTTPException(status_code=500, detail="A post could not be processed by the NLP pipeline.") from exc

    if not analyzed_posts:
        raise HTTPException(status_code=404, detail="No analyzable posts were returned.")

    sentiment_counts = Counter(post.sentiment.lower() for post in analyzed_posts)
    emotion_counts = Counter(post.emotion for post in analyzed_posts)
    emotions = {emotion: emotion_counts.get(emotion, 0) for emotion in EMOTION_LABELS}
    return AnalysisResponse(
        query=normalized_query,
        total_posts=len(analyzed_posts),
        demo_mode=twitter_service.demo_mode,
        sentiment=SentimentSummary(
            positive=sentiment_counts.get("positive", 0),
            negative=sentiment_counts.get("negative", 0),
            neutral=sentiment_counts.get("neutral", 0),
        ),
        emotions=emotions,
        average_polarity=round(sum(post.polarity for post in analyzed_posts) / len(analyzed_posts), 4),
        average_subjectivity=round(sum(post.subjectivity for post in analyzed_posts) / len(analyzed_posts), 4),
        posts=analyzed_posts,
    )
