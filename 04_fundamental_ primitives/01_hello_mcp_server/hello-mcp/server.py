from mcp.server.fastmcp import FastMCP


mcp = FastMCP("hello-mcp", stateless_http=True)

@mcp.tool(
    name="greet", 
    description="Greet a person by name"
    )
def greet(name: str) -> str:
    return f"Hello, {name}!"


mcp_app = mcp.streamable_http_app()
