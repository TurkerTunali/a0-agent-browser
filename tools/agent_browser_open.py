"""Open a URL using agent-browser."""
from helpers.tools import Tool, ToolArgument
import subprocess

class AgentBrowserOpenTool(Tool):
    name = "agent_browser_open"
    description = "Open a URL in the browser controlled by Vercel Agent Browser (CDP)."
    arguments_schema = {
        "url": ToolArgument(type="string", required=True, description="URL to open."),
        "cdp": ToolArgument(type="string", required=False, default="", description="CDP endpoint, e.g. localhost:9222."),
    }

    async def run(self, agent_context, url: str, cdp: str = ""):
        cmd = ["agent-browser", "open", url]
        if cdp:
            cmd.extend(["--cdp", cdp])
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return {"success": result.returncode == 0, "stdout": result.stdout, "stderr": result.stderr}
