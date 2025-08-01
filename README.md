# Python MCP Server

A simple Python implementation of a Model Context Protocol (MCP) server using FastMCP.

## Features

- **MCP Server**: Implements the Model Context Protocol with a greeting tool
- **FastMCP Framework**: Built using the FastMCP library for simplified development

## Project Structure

```
python-mcp/
├── .vscode/
│   └── mcp.json                # MCP client configuration
├── server.py                   # Main MCP server implementation
├── test_server.py             # Test script
├── requirements.txt           # Python dependencies
├── config.ini                # Server configuration
├── Makefile                  # Common development tasks
└── README.md                # This file
```

## Getting Started

1. Open this project in VS Code
2. Install the "Dev Containers" extension if not already installed
3. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) and select "Dev Containers: Reopen in Container"
4. Wait for the container to build and dependencies to install automatically

## Running the Server

Start the server:

```bash
make run
# or
python server.py
```

The server will start on `http://localhost:8000`

## Calling the MCP server

1. Open Copilot chat, switch to `Agent` mode.
2. Type Prompt: `Say hello to Robert`

## Available Tools

**greet** - Greets a person by name

Parameters: `name` (string, required)

Example: `greet("Alice")` returns `"Hello, Alice from MCP server!"`

## Testing

Run tests to verify the server:

```bash
make test
# or
python -m pytest -v
```

## Development

### Commands

- `make test` - Run tests
- `make format` - Format code with Black  
- `make lint` - Lint code with Flake8
- `make clean` - Remove temporary files

### Adding Tools

Add new tools by decorating functions with `@mcp.tool`:

```python
@mcp.tool
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers."""
    return a + b
```

## Configuration

MCP client configuration (`.vscode/mcp.json`):

```json
{
  "servers": {
    "python-mcp": {
      "url": "http://localhost:8000/mcp/"
    }
  }
}
```
