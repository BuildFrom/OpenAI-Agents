from agents import Agent, Runner
from fastapi import APIRouter, HTTPException
from src.extensions.utils import get_llm
from src.models import PromptRequest

router = APIRouter()

model = get_llm()

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=model
)

@router.post("/agents/command")
async def run_agent(request: PromptRequest):
    try:
        result = await Runner.run(agent, request.prompt)
        return {"output": result.final_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


