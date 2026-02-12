import tweepy
from textblob import TextBlob
import pandas as pd
from datetime import datetime

BEARER_TOKEN = "PASTE_YOUR_TOKEN_HERE"

client = tweepy.Client(bearer_token=BEARER_TOKEN)

search_term = "stocks"
tweets_amount = 20

rows = []

try:
    response = client.search_recent_tweets(
        query=search_term,
        max_results=tweets_amount,
        tweet_fields=["text"]
    )

    if response.data:
        tweets = [t.text for t in response.data]
    else:
        raise Exception("No tweets returned")

except Exception as e:
    print("Twitter API failed, using sample data")
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
