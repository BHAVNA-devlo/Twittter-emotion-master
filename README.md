# Twitter Emotion Analysis

A full-stack portfolio application that analyzes public Twitter/X conversations for sentiment, polarity, subjectivity, and explainable emotion signals.

## Existing architecture and upgrade

The original project was a Python CLI in `main.py`: it queried Twitter/X with Tweepy, classified each post with TextBlob, and wrote `twitter_sentiment.csv`. The useful TextBlob behavior and sample-data fallback are preserved. The project now adds a FastAPI API and a Vite React analytics frontend:

```text
React + Vite frontend
        |
        v
FastAPI REST API
        |
        v
Tweepy -> Twitter/X API v2
        |
        v
TextBlob sentiment + explainable emotion classifier
        |
        v
Typed JSON response -> dashboard charts and post list
```

## Features

- Topic search through `GET /api/analyze?query=...`
- Positive, negative, and neutral sentiment counts
- TextBlob polarity and subjectivity per post
- Explainable Joy, Sadness, Anger, Fear, Surprise, Love, and Neutral labels
- Responsive React dashboard with charts, loading, error, and demo states
- FastAPI Swagger documentation
- Secure environment-based Twitter/X credentials
- Render and Docker deployment files

> Emotion labels are intentionally documented as a lightweight keyword classifier. TextBlob does not perform true emotion classification.

## Tech stack

- Backend: Python, FastAPI, Pydantic, Tweepy, TextBlob
- Frontend: React, TypeScript, Vite, Recharts, Axios, Framer Motion, Lucide
- Deployment: Render backend, Vercel-compatible frontend, optional Docker image

## Local setup

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

Backend URLs:

- API: http://localhost:8000
- Swagger: http://localhost:8000/docs
- Health: http://localhost:8000/api/health

If no bearer token is configured, the backend returns clearly marked demo data so the UI can be tested without external credentials.

### Frontend

In another terminal:

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

Frontend: http://localhost:5173

Set `VITE_API_BASE_URL` in `frontend/.env` when the API is deployed. The frontend communicates with FastAPI only; Twitter/X credentials never enter browser code.

## Environment variables

Backend `.env`:

```text
TWITTER_BEARER_TOKEN=your_token_here
TWITTER_MAX_RESULTS=50
FRONTEND_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

Frontend `.env`:

```text
VITE_API_BASE_URL=http://localhost:8000
```

Never commit `.env`, API tokens, or passwords.

## API response

`GET /api/analyze?query=college` returns a typed object containing the query, total posts, demo mode, sentiment counts, emotion counts, averages, and a list of analyzed posts.

## Deployment

### Backend on Render

The root `render.yaml` defines a Python web service rooted at `backend/`. Add `TWITTER_BEARER_TOKEN` and `FRONTEND_ORIGINS` as Render environment variables. Set `FRONTEND_ORIGINS` to the deployed Vercel URL.

### Frontend on Vercel

Import the repository, set the project root to `frontend`, and add `VITE_API_BASE_URL` pointing to the Render API URL. Vercel will use `npm run build` and publish `frontend/dist`.

### Docker

```bash
docker build -t twitter-emotion-api ./backend
docker run --env-file backend/.env -p 8000:8000 twitter-emotion-api
```

## Validation

```bash
cd frontend && npm run build
cd ../backend && python -m compileall app
```

## Future improvements

- Replace the keyword emotion classifier with a hosted or locally deployable trained model.
- Add persisted analysis history and background jobs for large searches.
- Add authentication and workspace-level access control.
- Add automated backend tests and frontend interaction tests.

## Screenshots

The frontend includes a landing page, analysis workspace, analytics dashboard, post explorer, history, and settings views. Screenshots can be added here after deployment.
