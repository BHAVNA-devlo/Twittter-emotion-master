# Twitter Emotion Analysis API

FastAPI backend for fetching public X/Twitter posts and returning sentiment plus lightweight, explainable emotion analysis.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

Without `TWITTER_BEARER_TOKEN`, the API runs in clearly marked demo mode using sample posts. With a token, `GET /api/analyze?query=college` calls the X API v2 recent-search endpoint.

## Endpoints

- `GET /api/health` reports API status and whether X credentials are configured.
- `GET /api/analyze?query=college` returns sentiment counts, emotion counts, polarity, subjectivity, and analyzed posts.
- `/docs` exposes FastAPI Swagger documentation.

TextBlob supplies sentiment polarity and subjectivity. Emotion labels are an explainable keyword classifier, not a trained emotion model; replace `emotion_service.py` with a trained model when model-backed emotion inference is required.
