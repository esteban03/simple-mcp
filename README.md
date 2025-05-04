# Simple MCP

A testbed for evaluating the capabilities of MCP using the official Python SDK. It is intended for experimentation, integration, and demonstration of MCP features.

## Getting Started

To start the project, create a virtual environment using `uv` and install the dependencies as follows:

```bash
# Create and activate a virtual environment with uv
uv venv .venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Run the project
uv run main.py
```

## Package Management

The project uses `uv` with `uvx` as the package manager for efficient dependency management and environment handling.

## MCP Integration

Below is an example configuration for running the project with MCP. Update the directory path as needed for your environment. This integration allows you to execute terminal commands directly through MCP, enabling automated project management and script execution.

```json
"mcp-commands": {
    "command": "uv",
    "args": ["--directory", "/path/to/simple-mcp/", "run", "main.py"]
}
```

## Functionalities & Tools

This project serves as a playground for testing various MCP functionalities. The current include:

- **Terminal Command Execution** - Run terminal commands through MCP integration

