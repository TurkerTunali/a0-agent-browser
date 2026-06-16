"""Setup script for agent_browser plugin."""
import subprocess
import sys

def main():
    print("Checking agent-browser CLI...")
    result = subprocess.run(["agent-browser", "--version"], capture_output=True, text=True)
    if result.returncode != 0:
        print("ERROR: agent-browser CLI is not installed or not in PATH.")
        print("Install with: npm install -g agent-browser")
        return 1
    print(f"Found agent-browser: {result.stdout.strip()}")
    print("Setup complete.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
