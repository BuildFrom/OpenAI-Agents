from agents import Agent, Runner, function_tool
from fastapi import APIRouter, HTTPException

from src.extensions.utils import get_llm
from src.models import PromptRequest

router = APIRouter()

model = get_llm()

# -------------

simple_agent = Agent(
    name="Simple Assistant",
    instructions="You are a helpful assistant.",
    model=model
)

@router.post("/agents/simple")
async def run_simple_agent(request: PromptRequest):
    try:
        result = await Runner.run(simple_agent, request.prompt)
        return {"output": result.final_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------------

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

weather_agent = Agent(
    name="Weather Assistant",
    instructions="You are a helpful assistant.",
    model=model,
    tools=[get_weather],
)

@router.post("/agents/functional")
async def run_weather_agent(request: PromptRequest):
    try:
        result = await Runner.run(weather_agent, request.prompt)
        return {"output": result.final_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------------

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You only speak Spanish.",
    model=model
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
    model=model
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    model=model,
    handoffs=[spanish_agent, english_agent],
)

@router.post("/agents/handoffs")
async def run_triage_agent(request: PromptRequest):
    try:
        result = await Runner.run(triage_agent, request.prompt)
        return {"output": result.final_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
