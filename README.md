# A0 Agent Browser Plugin

Native A0 tools for CDP-based browser automation directly from your Agent Zero agents.

## What This Plugin Adds

- **First-class A0 tools** for opening pages via Chrome DevTools Protocol (CDP).
- **Remote Chrome support** -- connect to Chrome running on another machine via SSH reverse tunnel.
- **Anti-bot friendly** -- since it can drive your real Chrome on macOS, it bypasses many detection systems.

## Prerequisites

- Playwright installed in the Agent Zero environment:
  ```bash
  pip install playwright
  python -m playwright install chromium
  ```
- A Chrome/Chromium instance running with `--remote-debugging-port=9222`

## Installation

### From GitHub (Plugin Hub)

1. Open Agent Zero **Plugins** -> **Browse**
2. Search for "A0 Agent Browser"
3. Click **Install**

### Manual Installation

```bash
git clone https://github.com/TurkerTunali/a0-agent-browser.git
cd a0-agent-browser
cp -r . /a0/usr/plugins/agent_browser
```

## Usage

### Local Chrome (same machine)

Start Chrome with remote debugging:
```bash
/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --remote-debugging-port=9222
```

Then from Agent Zero:
```
Open https://google.com in the browser
```

### Remote Chrome via SSH Reverse Tunnel

If your Chrome is running on your Mac and Agent Zero is in a Docker container on a VPS:

1. **On your Mac**, create the reverse tunnel:
   ```bash
   ssh -f -R '*:9222:127.0.0.1:9222' root@vps_ip -N
   ```

2. **In Agent Zero**, the plugin automatically connects to `localhost:9222` (forwarded via Docker bridge to your VPS).

3. **Navigate**:
   ```
   agent_browser_open url=https://google.com cdp=172.17.0.1:9222
   ```

## Contributing

PRs welcome! Please ensure the `plugin.yaml` name field matches the repo name.
