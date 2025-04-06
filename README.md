## POST /api/v1/agents/command

## Note:
To enable, function_tool, tool, and handoffs, you need to set official OPENAI_API_KEY

### Description:
This endpoint allows you to interact with the assistant agent to process a command by providing a prompt. The assistant will generate a response based on the provided prompt.

### Request Body:
A JSON object containing the prompt for the agent. The prompt should describe the task or query you want the assistant to process.

#### Example Request:
```json
{
  "prompt": "Create a breakfast plan for a single day"
}
```

#### Example Response:
```json
{
  "output": "Here’s a simple breakfast plan for a single day: 1. Scrambled eggs with toast, 2. Fresh fruit salad, 3. Coffee or juice."
}
```

## POST http://0.0.0.0:9000/api/v1/agents/functional

#### Example Request:
```json
{
  "prompt": "What's the weather in Tokyo?"
}
```

#### Example Response:
```json
{
  "output": "# The weather in Tokyo is sunny."
}
```

## POST http://0.0.0.0:9000/api/v1/agents/handoffs

#### Example Request:
```json
{
  "prompt": "Hola, ¿cómo estás?"
}
```

#### Example Response:
```json
{
  "output": "¡Hola! Estoy bien, gracias por preguntar. ¿Y tú, cómo estás?"
}
```

## MCP Servers 

### Filesystem Tools:
- read_file
- read_multiple_files
- write_file
- edit_file
- create_directory
- list_directory
- directory_tree
- move_file
- search_files
- get_file_info
- list_allowed_directories

### PostgreSQL Tools:
- Read only query