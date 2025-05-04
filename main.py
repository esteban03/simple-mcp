from mcp.server.fastmcp import FastMCP
import subprocess
import shlex
from typing import List, Dict, Optional

# Create an MCP server
mcp = FastMCP("TerminalCommand")

@mcp.tool()
async def run_command(command: str) -> Dict[str, str]:
    """
    Run a terminal command and return its output
    
    Args:
        command: The command to execute in the terminal
        
    Returns:
        Dictionary with stdout, stderr, and return code
    """
    try:
        args = shlex.split(command)
        process = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=30  # 30 second timeout for safety
        )
        
        return {
            "stdout": process.stdout,
            "stderr": process.stderr,
            "return_code": str(process.returncode)
        }
    except subprocess.TimeoutExpired:
        return {
            "stdout": "",
            "stderr": "Command timed out after 30 seconds",
            "return_code": "-1"
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": f"Error executing command: {str(e)}",
            "return_code": "-1"
        }

@mcp.tool()
async def list_files(directory: str = ".") -> Dict[str, List[str]]:
    """
    List files in a directory
    
    Args:
        directory: The directory to list files from (defaults to current directory)
        
    Returns:
        Dictionary with list of files
    """
    try:
        result = await run_command(f"ls -la {directory}")
        if result["return_code"] == "0":
            files = [line for line in result["stdout"].split("\n") if line.strip()]
            return {"files": files}
        else:
            return {"files": [], "error": result["stderr"]}
    except Exception as e:
        return {"files": [], "error": str(e)}

if __name__ == "__main__":
    # The MCP CLI will automatically detect and run the server
    # Run with: mcp dev terminal_mcp_server.py
    pass
