from pydantic import BaseModel
from typing import List, Optional
 
class AgentRequest(BaseModel):
    query: str
    parameters: Optional[dict] = None

class AgentResponse(BaseModel):
    response: str
    confidence: float
    source: str

class Interaction(BaseModel):
    request: AgentRequest
    response: AgentResponse

class BatchRequest(BaseModel):
    requests: List[AgentRequest]

class BatchResponse(BaseModel):
    responses: List[AgentResponse]