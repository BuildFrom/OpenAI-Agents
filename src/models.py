

from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str

class MyGuardrailOutput(BaseModel):
    is_general: bool
    reasoning: str


class UserContext(BaseModel):
    name: str | None = None
