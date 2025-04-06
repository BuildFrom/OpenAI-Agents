from uuid import uuid4

from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.mcp import MCPServerStdio
from fastapi import HTTPException
from fastapi.responses import JSONResponse

# ------------------------ #

def get_llm():
    try:
        model = OpenAIChatCompletionsModel(
            model="gemma3",
            openai_client=AsyncOpenAI(
                base_url="http://localhost:11434/v1",
                api_key="ollama",
            ),
        )
        return model
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in getting model: {str(e)}")

async def mcp_server(command: str, args: list[str]):
    """Generic initializer for any MCP server"""
    async with MCPServerStdio(params={"command": command, "args": args}) as server:
        tools = await server.list_tools()
        tool_details = [{"name": tool.name, "description": tool.description} for tool in tools]
        return tools, tool_details


def get_uuid():
    return str(uuid4())[:8]


def response(content, status_code):
    return JSONResponse(content=content, status_code=status_code)


def error(status_code, detail):
    return response({"error": detail}, status_code)


# ------------------------ #
