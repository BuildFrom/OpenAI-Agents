from fastapi import FastAPI

from .routes import agent

def router(app: FastAPI) -> None:
    v1 = "/api/v1"
    app.include_router(agent.router, prefix=v1, tags=["agent"])
