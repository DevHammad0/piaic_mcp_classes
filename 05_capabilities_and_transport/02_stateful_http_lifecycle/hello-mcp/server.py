from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server - stateful for lifecycle demonstration
mcp = FastMCP("weather", stateless_http=True)


@mcp.tool()
async def get_forecast(city: str) -> str:
    """Get weather forecast for a city.

    Args:
        city: The name of the city
    """
    return f"The weather in {city} will be warm and sunny today! 🌤️"


@mcp.tool()
async def server_status() -> str:
    """Get server status and 2025-06-18 compliance info."""
    return """Server Status: ✅ Running
MCP Version: 2025-06-18
Session Mode: Stateful (FastMCP managed)
Lifecycle: Full support (Init → Operation → Shutdown)"""


# Export the app for Uvicorn
mcp_app = mcp.streamable_http_app()


if __name__ == "__main__":
    import uvicorn
    print("Starting server...")
    uvicorn.run("server:mcp_app", host="0.0.0.0", port=8000, reload=True)