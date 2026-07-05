"""CMDB Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class ConfigurationItem(BaseModel):
    """ConfigurationItem for CMDB Agent."""
    ci_id: str
    name: str
    ci_type: str
    status: str
    owner: str
    relationships: list[dict]


class ChangeImpact(BaseModel):
    """ChangeImpact for CMDB Agent."""
    change_target: str
    affected_services: list[str]
    affected_users: int
    risk_level: str
    recommended_window: str

