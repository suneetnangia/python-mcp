from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")


@mcp.tool
def greet(name: str) -> str:
    """Greets a person by name with a friendly hello message.

    Args:
        name: The name of the person to greet

    Returns:
        A personalized greeting message
    """
    return f"Hello, {name} from MCP server!"


if __name__ == "__main__":
    mcp.run(transport="http")
