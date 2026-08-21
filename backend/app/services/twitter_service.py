import os
from dataclasses import dataclass
from datetime import datetime, timezone

import tweepy


@dataclass
class SourcePost:
    id: str
    text: str
    created_at: datetime
    author: str | None = None


DEMO_POSTS = [
    "Stock market is booming today!",
    "I lost money in stocks, very disappointing.",
    "Stocks are moving sideways, no major changes.",
    "Great time to invest in long-term stocks.",
    "Market crash fears are increasing.",
    "The latest product update is amazing and so much faster.",
    "I am worried about the pricing changes and support response.",
]


class TwitterServiceError(RuntimeError):
    def __init__(self, message: str, status_code: int = 502):
        super().__init__(message)
        self.status_code = status_code


class TwitterService:
    def __init__(self) -> None:
        self.bearer_token = os.getenv("TWITTER_BEARER_TOKEN", "").strip()
        self.max_results = max(10, min(int(os.getenv("TWITTER_MAX_RESULTS", "50")), 100))

    @property
    def demo_mode(self) -> bool:
        return not bool(self.bearer_token)

    def search(self, query: str) -> list[SourcePost]:
        if self.demo_mode:
            now = datetime.now(timezone.utc)
            return [SourcePost(str(index), text, now) for index, text in enumerate(DEMO_POSTS, start=1)]

        try:
            client = tweepy.Client(bearer_token=self.bearer_token, wait_on_rate_limit=False)
            response = client.search_recent_tweets(
                query=f"{query} -is:retweet",
                max_results=self.max_results,
                tweet_fields=["created_at", "author_id"],
            )
        except tweepy.TooManyRequests as exc:
            raise TwitterServiceError("Twitter/X rate limit reached. Please try again later.", 429) from exc
        except tweepy.Unauthorized as exc:
            raise TwitterServiceError("Twitter/X authentication failed. Check the bearer token.", 401) from exc
        except tweepy.TweepyException as exc:
            raise TwitterServiceError("Twitter/X could not be reached right now.", 502) from exc

        if not response.data:
            return []
        return [
            SourcePost(
                id=str(tweet.id),
                text=tweet.text,
                created_at=tweet.created_at or datetime.now(timezone.utc),
                author=str(tweet.author_id) if tweet.author_id else None,
            )
            for tweet in response.data
        ]
