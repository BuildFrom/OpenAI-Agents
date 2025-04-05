## POST /api/v1/agents/command

### Description:
This endpoint allows you to interact with the assistant agent to process a command by providing a prompt. The assistant will generate a response based on the provided prompt.

### Request Body:
A JSON object containing the prompt for the agent. The prompt should describe the task or query you want the assistant to process.

#### Example Request:
```json
{
  "prompt": "Create a breakfast plan for a single day"
}

#### Example Response:
```json
{
  "output": "Here’s a simple breakfast plan for a single day: 1. Scrambled eggs with toast, 2. Fresh fruit salad, 3. Coffee or juice."
}
