from mcp.server.fastmcp import FastMCP
import subprocess
from typing import List, Dict, Optional
import asyncio

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
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {
            "stdout": stdout.decode(),
            "stderr": stderr.decode(),
            "return_code": str(process.returncode)
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
    mcp.run("stdio")
