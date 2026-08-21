from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_reports_demo_mode_without_token() -> None:
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_analysis_returns_typed_demo_payload() -> None:
    response = client.get("/api/analyze", params={"query": "stocks"})
    assert response.status_code == 200
    payload = response.json()
    assert payload["query"] == "stocks"
    assert payload["total_posts"] == len(payload["posts"])
    assert set(payload["emotions"]) == {"Joy", "Sadness", "Anger", "Fear", "Surprise", "Love", "Neutral"}


def test_empty_query_is_rejected() -> None:
    response = client.get("/api/analyze", params={"query": "   "})
    assert response.status_code == 422
