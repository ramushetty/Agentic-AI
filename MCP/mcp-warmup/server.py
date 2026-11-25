from fastmcp import FastMCP

mcp = FastMCP("warm-up server")

@mcp.tool
def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}! Welcome to MCP"

@mcp.tool
def add(a:int, b:int) -> int:
    """add two numbers together"""
    return a+b

if __name__ == "__main__":
    mcp.run()

# uv run python server.py

# npx @modelcontextprotocol/inspector uv run python server.py