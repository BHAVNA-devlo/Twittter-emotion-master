import os

from fastapi import APIRouter

from app.models.schemas import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/api/health", response_model=HealthResponse)
def health() -> HealthResponse:
    configured = bool(os.getenv("TWITTER_BEARER_TOKEN", "").strip())
    return HealthResponse(
        status="ok",
        twitter_configured=configured,
        demo_mode=not configured,
        version="1.0.0",
    )
