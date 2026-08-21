from textblob import TextBlob


POSITIVE = "Positive"
NEGATIVE = "Negative"
NEUTRAL = "Neutral"


def analyze_sentiment(text: str) -> dict[str, float | str]:
    """Preserve the original TextBlob polarity and subjectivity behavior."""
    blob = TextBlob(text)
    polarity = float(blob.sentiment.polarity)
    subjectivity = float(blob.sentiment.subjectivity)
    if polarity > 0:
        sentiment = POSITIVE
    elif polarity < 0:
        sentiment = NEGATIVE
    else:
        sentiment = NEUTRAL
    confidence = min(1.0, abs(polarity) + 0.5) if sentiment != NEUTRAL else 0.5
    return {
        "sentiment": sentiment,
        "polarity": round(polarity, 4),
        "subjectivity": round(subjectivity, 4),
        "confidence": round(confidence, 4),
    }
