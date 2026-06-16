# A0 Agent Browser Plugin

Native A0 tools for [Vercel Agent Browser](https://vercel.com) CLI, enabling CDP-based browser automation directly from your Agent Zero agents.

## What This Plugin Adds

- **First-class A0 tools** for opening pages, clicking elements, typing, taking screenshots, evaluating JavaScript, and more.
- **CDP integration** — connect to any Chrome/Chromium instance via Chrome DevTools Protocol (e.g., your local Chrome or a headless server).
- **Anti-bot friendly** — since it can drive your real Chrome on macOS, it bypasses many detection systems that block headless browsers.

## Prerequisites

- `agent-browser` CLI installed globally: `npm install -g agent-browser`
- A Chrome/Chromium instance running with `--remote-debugging-port=9222`

## Installation

### From GitHub (Plugin Hub)

1. Open Agent Zero **Plugins** -> **Browse**
2. Search for "A0 Agent Browser"
3. Click **Install**

### Manual Installation

```bash
git clone https://github.com/<your-username>/a0-agent-browser.git
cd a0-agent-browser
# Copy plugin to A0 plugins directory
cp -r . /a0/usr/plugins/agent_browser
```

Restart Agent Zero after installation.

## Quick Start

1. Start Chrome with CDP enabled:
   ```bash
   chrome --remote-debugging-port=9222
   ```

2. In any Agent Zero chat, the tools are automatically available:
   - `agent_browser_open`
   - `agent_browser_click`
   - `agent_browser_type`
   - `agent_browser_snapshot`
   - `agent_browser_screenshot`
   - `agent_browser_eval`
   - `agent_browser_get`
   - `agent_browser_close`

## Configuration

Optional `default_config.yaml`:

```yaml
cdp_endpoint: "localhost:9222"
```

Override per-project via Agent Zero Settings.

## Tools Reference

| Tool | Description |
|------|-------------|
| `agent_browser_open` | Open a URL |
| `agent_browser_click` | Click an element by selector or @ref |
| `agent_browser_type` | Type text into an element |
| `agent_browser_snapshot` | Get accessibility tree (snapshot with @refs) |
| `agent_browser_screenshot` | Take a page screenshot |
| `agent_browser_eval` | Evaluate JavaScript in the page |
| `agent_browser_get` | Get page info (text, html, url, title) |
| `agent_browser_close` | Close the browser session |

## License

MIT
