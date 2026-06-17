"""Open a URL using Vercel Agent Browser connected to a remote CDP endpoint."""
from helpers.tools import Tool, ToolArgument
import os
import subprocess

class AgentBrowserOpenTool(Tool):
    name = "agent_browser_open"
    description = "Open a URL in a browser via Chrome DevTools Protocol (CDP) using Vercel Agent Browser."
    arguments_schema = {
        "url": ToolArgument(type="string", required=True, description="URL to open."),
        "cdp": ToolArgument(type="string", required=False, default="", description="CDP endpoint, e.g. http://localhost:9222."),
    }

    async def run(self, agent_context, url: str, cdp: str = ""):
        cdp_url = cdp if cdp else os.environ.get("CDP_URL", "http://localhost:9222")
        if not cdp_url.startswith("http://") and not cdp_url.startswith("ws://"):
            cdp_url = f"http://{cdp_url}"

        # Global flag --cdp must come before the 'open' subcommand
        cmd = ["agent-browser", "--cdp", cdp_url, "open", url]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                return {"success": True, "stdout": f"Opened {url} via agent-browser", "stderr": result.stderr}
            else:
                return {"success": False, "stdout": result.stdout, "stderr": result.stderr}
        except FileNotFoundError:
            return {
                "success": False,
                "stdout": "",
                "stderr": "agent-browser not found in PATH. Install with: npm install -g agent-browser"
            }
        except subprocess.TimeoutExpired:
            return {"success": False, "stdout": "", "stderr": "Command timed out after 30 seconds."}
        except Exception as e:
            return {"success": False, "stdout": "", "stderr": str(e)}