from fastmcp import FastMCP
import random
import json

mcp = FastMCP(name="Ash Simple Server")

@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """
    Roll n_dice 6-sided dice and return the results.
    """
    return [random.randint(1,6) for _ in range(n_dice)]

@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.
    """
    return a+b

#Info about server
@mcp.resource("info://server")
def server_info() -> str:
    """Get information about this server."""
    info ={
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP Server with math tools",
        "tools": ["rolldice","add"],
        "author": "Ashwin"
    }
    return json.dumps(info, indent=2)

if __name__=="__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)