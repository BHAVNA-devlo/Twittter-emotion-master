p# Twitter Sentiment Analysis

This project analyzes the sentiment of recent tweets about a given topic using the Twitter API v2 and TextBlob for natural language processing.

## Features
- Fetches recent tweets for a search term using Twitter API v2
- Cleans tweet text (removes retweets and mentions)
- Performs sentiment analysis using TextBlob
- Handles Twitter API rate limits gracefully
- Prints average sentiment polarity and the sentiment of the last tweet

## Requirements
- Python 3.7+
- Tweepy
- TextBlob

## Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Yashkatiyar24/Twitter-sentimental-analysis.git
   cd Twitter-sentimental-analysis
   ```
2. **Install dependencies:**
   ```bash
   pip install tweepy textblob
   python -m textblob.download_corpora
   ```
3. **Set your Twitter API Bearer Token:**
   - Open `main.py` and replace the value of `BEARER_TOKEN` with your own from the [Twitter Developer Portal](https://developer.twitter.com/).

## Usage
Run the script:
```bash
python main.py
```

You can change the search term by editing the `search_term` variable in `main.py`.

## Output Example
```
This is a tweet about stocks.
Another tweet about the market.
...
Sentiment: Sentiment(polarity=0.0, subjectivity=0.0)
Average polarity: 0.123
```

## Notes
- The script will automatically wait and retry if you hit the Twitter API rate limit.
- Only the most recent 100 tweets are fetched per run (Twitter API v2 limitation).

## License
This project is licensed under the MIT License.

