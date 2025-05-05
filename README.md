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

Below are example configurations for running the project with MCP. Update the directory path as needed for your environment. These integrations allow you to execute terminal commands directly through MCP, enabling automated project management and script execution.

### Local Integration

```json
"mcp-commands": {
    "command": "uv",
    "args": ["--directory", "/path/to/simple-mcp/", "run", "main.py"]
}
```

### Docker Integration

Add this configuration to your Claude Desktop config file (`claude_desktop_config.json`):

```json
"mcp-commands-docker": {
    "command": "/Applications/Docker.app/Contents/Resources/bin/docker",
    "args": ["run", "-i", "--rm", "--init", "-e", "DOCKER_CONTAINER=true", "simple-mcp"]
}
```

Important: You must pre-build the Docker image before running the container:

```bash
# Build the Docker image
docker build -t simple-mcp .
```

## Tools

- **Terminal Command Execution:** Run terminal commands through MCP integration.
- **List Files:** List files in a specified directory via MCP.

## Resources

- **README Resource Exposure:** Access the contents of the README.md file as an MCP resource. Useful for programmatically retrieving documentation or displaying project information in other tools.


