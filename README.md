# A0 Agent Browser Plugin

Native A0 tools for CDP-based browser automation directly from your Agent Zero agents.

## What This Plugin Adds

- **First-class A0 tools** for opening pages via Chrome DevTools Protocol (CDP).
- **Remote Chrome support** -- connect to Chrome running on another machine via SSH reverse tunnel.
- **Anti-bot friendly** -- since it can drive your real Chrome on macOS, it bypasses many detection systems.

## What This Plugin Adds

- **First-class A0 tools** for opening pages via Chrome DevTools Protocol (CDP).
- **Remote Chrome support** -- connect to Chrome running on another machine via SSH reverse tunnel.
- **Anti-bot friendly** -- since it can drive your real Chrome on macOS, it bypasses many detection systems.

## Why Use This Plugin? (Advantages Over Native A0 Browsers)

| Feature | A0 Agent Browser (This Plugin) | Native A0 `browser` Tool | CamoFox Browser |
|---|---|---|---|
| **Detection Avoidance** | ✅ Real Chrome via CDP — extremely hard to detect | ❌ Headless Playwright — easily fingerprinted | ✅ Anti-detection but complex setup |
| **IP Reputation** | ✅ Residential IP via SSH tunnel to your Mac | ❌ VPS/Server IP — often blocked | ⚠️ Runs in Docker — server IP |
| **Performance** | ✅ Rust binary (~ms startup) | ⚠️ Full Playwright/Chromium stack | ⚠️ Node.js + Playwright overhead |
| **Browser Fidelity** | ✅ Real Chrome on real OS — cookies, localStorage, extensions work natively | ⚠️ Headless quirks, missing behaviors | ✅ Real Chrome but in container |
| **Architecture** | ✅ Server-side AI logic + local browser presence | ❌ All in-container | ⚠️ All in-container |
| **Dependencies** | ✅ Zero runtime deps (single binary) | ❌ Playwright, Node.js, Chromium | ❌ Playwright, Node.js, Chromium |
| **Setup Complexity** | ⚠️ Requires SSH tunnel + Chrome on Mac | ✅ Works out of the box | ⚠️ Complex, version-sensitive |
| **Visual Feedback** | ❌ No screenshots returned to A0 | ✅ Screenshots, rendered content | ✅ Screenshots, resources extraction |
| **Commands Supported** | ⚠️ Currently `open` only (extensible) | ✅ Full automation (click, type, scroll, etc.) | ✅ Full automation |

**In short:** Use this plugin when you need **stealth, residential IP, and real Chrome behavior** — e.g., sites with aggressive bot detection, IP-based geo-blocking, or complex JS that breaks in headless mode. Use the native `browser` tool for quick internal scraping, screenshots, and form filling where detection doesn't matter.

## Prerequisites

- **Vercel `agent-browser` CLI** installed (Rust binary, no Node.js/Playwright needed):
  ```bash
  # Install globally via npm (downloads prebuilt binary)
  npm install -g agent-browser@latest
  # Or download directly from GitHub Releases
  ```
- A Chrome/Chromium instance running with `--remote-debugging-port=9222`
- For remote Mac access: SSH reverse tunnel (see Usage below)

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
