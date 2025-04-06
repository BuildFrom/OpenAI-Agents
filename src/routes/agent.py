# For concurrent ops, use asyncio

from agents import Agent, Runner
from fastapi import APIRouter, HTTPException

from src.extensions.utils import get_llm, mcp_server
from src.models import PromptRequest

router = APIRouter()
model = get_llm()

async def filesystem_server():
    return await mcp_server(
        "npx",
        ["-y", "@modelcontextprotocol/server-filesystem", "src"]
    )


async def postgres_server():
    postgres_url = "postgresql://user:pass@localhost:5432/dbname"
    return await mcp_server(
        "npx",
        ["-y", "@modelcontextprotocol/server-postgres", postgres_url]
    )


def log_tools(label: str, tool_details: list[dict], readonly: bool = False):
    print(f"{label}:")
    for tool in tool_details:
        prefix = "Read only " if readonly else ""
        print(f"- {prefix}{tool['name']}")


# https://openai.github.io/openai-agents-python/mcp
def create_agent(tools):
    return Agent(
        name="Simple Assistant",
        instructions="You are a helpful assistant.",
        model=model,
        # TODO: Handle Coroutines properly
        # mcp_servers=[filesystem_server, postgres_server],
    )

@router.post("/agents/simple")
async def run_simple_agent(request: PromptRequest):
    try:
        fs_tools, fs_tool_details = await filesystem_server()
        log_tools("Filesystem Tools", fs_tool_details)

        pg_tools, pg_tool_details = await postgres_server()
        log_tools("PostgreSQL Tools", pg_tool_details, readonly=True)

        all_tools = fs_tools + pg_tools
        agent = create_agent(all_tools)

        result = await Runner.run(agent, request.prompt)
        return {"output": result.final_output}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
