from pydantic import BaseModel
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class AgentRequest:
    agent_id: str
    query: str
    parameters: Optional[dict] = None

@dataclass
class AgentResponse:
    agent_id: str
    response: str
    status: str
    timestamp: str

class AgentStatus(BaseModel):
    agent_id: str
    is_active: bool
    last_active: str

class AgentInteraction(BaseModel):
    request: AgentRequest
    response: AgentResponse
    status: str
    interaction_time: str