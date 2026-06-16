"""Client for Vercel Agent Browser CLI."""
import subprocess
import json
import shlex
from typing import Optional, Dict, Any

class AgentBrowserError(Exception):
    """Error from agent-browser CLI."""
    pass

def _run(command: list[str], cdp: Optional[str] = None):
    """Run an agent-browser command."""
    base = ["agent-browser"]
    if cdp:
        base.extend(["--cdp", cdp])
    base.extend(command)

    result = subprocess.run(base, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        raise AgentBrowserError(f"agent-browser failed: {result.stderr}")
    return result.stdout

def open_url(url: str, cdp: Optional[str] = None) -> str:
    return _run(["open", url], cdp)

def click(selector: str, cdp: Optional[str] = None) -> str:
    return _run(["click", selector], cdp)

def type_text(selector: str, text: str, cdp: Optional[str] = None) -> str:
    return _run(["type", selector, text], cdp)

def snapshot(cdp: Optional[str] = None) -> str:
    return _run(["snapshot"], cdp)

def screenshot(path: str, cdp: Optional[str] = None) -> str:
    return _run(["screenshot", path], cdp)

def evaluate(js: str, cdp: Optional[str] = None) -> str:
    return _run(["eval", js], cdp)

def get_info(what: str, cdp: Optional[str] = None) -> str:
    return _run(["get", what], cdp)

def close(cdp: Optional[str] = None) -> str:
    return _run(["close"], cdp)
