import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.analysis import router as analysis_router
from app.routes.health import router as health_router


def allowed_origins() -> list[str]:
    configured = os.getenv("FRONTEND_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173")
    return [origin.strip() for origin in configured.split(",") if origin.strip()]


app = FastAPI(
    title="Twitter Emotion Analysis API",
    version="1.0.0",
    description="Fetch public X posts and analyze sentiment and lightweight emotions.",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins(),
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)
app.include_router(health_router)
app.include_router(analysis_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"name": "Twitter Emotion Analysis API", "docs": "/docs"}
