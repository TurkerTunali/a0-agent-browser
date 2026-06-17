"""Open a URL using Playwright connected to a remote CDP endpoint."""
from helpers.tools import Tool, ToolArgument
import os

class AgentBrowserOpenTool(Tool):
    name = "agent_browser_open"
    description = "Open a URL in a browser via Chrome DevTools Protocol (CDP)."
    arguments_schema = {
        "url": ToolArgument(type="string", required=True, description="URL to open."),
        "cdp": ToolArgument(type="string", required=False, default="", description="CDP endpoint, e.g. http://localhost:9222."),
    }

    async def run(self, agent_context, url: str, cdp: str = ""):
        try:
            from playwright.sync_api import sync_playwright

            cdp_url = cdp if cdp else os.environ.get("CDP_URL", "http://localhost:9222")
            if not cdp_url.startswith("http://") and not cdp_url.startswith("ws://"):
                cdp_url = f"http://{cdp_url}"

            with sync_playwright() as p:
                browser = p.chromium.connect_over_cdp(cdp_url)
                if browser.contexts and browser.contexts[0].pages:
                    page = browser.contexts[0].pages[0]
                else:
                    page = browser.new_page()

                page.goto(url)
                title = page.title()
                browser.close()

                return {"success": True, "stdout": f"Navigated to: {title}", "stderr": ""}
        except ImportError:
            return {
                "success": False,
                "stdout": "",
                "stderr": "Playwright not installed. Run: pip install playwright && python -m playwright install chromium"
            }
        except Exception as e:
            return {"success": False, "stdout": "", "stderr": str(e)}