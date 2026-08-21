from datetime import datetime
from typing import Dict, List

from pydantic import BaseModel, Field


class PostAnalysis(BaseModel):
    id: str
    text: str
    created_at: datetime
    sentiment: str
    emotion: str
    polarity: float = Field(ge=-1, le=1)
    subjectivity: float = Field(ge=0, le=1)
    confidence: float = Field(ge=0, le=1)
    author: str | None = None


class SentimentSummary(BaseModel):
    positive: int
    negative: int
    neutral: int


class AnalysisResponse(BaseModel):
    query: str
    total_posts: int
    demo_mode: bool
    sentiment: SentimentSummary
    emotions: Dict[str, int]
    average_polarity: float
    average_subjectivity: float
    posts: List[PostAnalysis]


class HealthResponse(BaseModel):
    status: str
    twitter_configured: bool
    demo_mode: bool
    version: str
