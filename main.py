import tweepy
from textblob import TextBlob
import pandas as pd
from datetime import datetime

import os
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN", "").strip()

search_term = os.getenv("TWITTER_SEARCH_TERM", "stocks")
tweets_amount = 20

rows = []

try:
    if not BEARER_TOKEN:
        raise RuntimeError("TWITTER_BEARER_TOKEN is not configured")
    response = client.search_recent_tweets(query=search_term, max_results=tweets_amount, tweet_fields=["text"])
    if not response.data:
        raise RuntimeError("No tweets returned")
    tweets = [tweet.text for tweet in response.data]

except (RuntimeError, tweepy.TweepyException) as error:
    print(f"Twitter API unavailable ({error}), using sample data")
    tweets = [
        "Stock market is booming today!",
        "I lost money in stocks, very disappointing.",
        "Stocks are moving sideways, no major changes.",
        "Great time to invest in long-term stocks.",
        "Market crash fears are increasing."
    ]

for text in tweets:
    analysis = TextBlob(text)
    polarity = analysis.polarity
    subjectivity = analysis.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    rows.append({
        "tweet": text,
        "sentiment": sentiment,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "date": datetime.now().date()
    })

df = pd.DataFrame(rows)
df.to_csv("twitter_sentiment.csv", index=False)

print("twitter_sentiment.csv created with", len(df), "records")
