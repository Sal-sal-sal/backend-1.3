from fastapi import APIRouter
from src.agents.openai_agent import run_agent_with_search
from src.models.schemas import AgentRequest, AgentResponse

router = APIRouter()

@router.post("/openai")
async def interact_with_openai(request: AgentRequest):
    print(f"\nReceived request: {request.query}\n")
    gpt_response = run_agent_with_search(request.query)
    return AgentResponse(
        response=gpt_response,
        confidence=1.0,
        source="openai"
    )   