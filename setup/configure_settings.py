"""Merge ALEXIS defaults into ~/.claude/settings.json without overwriting user choices.

- Adds the ALEXIS status line if no statusLine is configured (use --force to replace one).
- Backs up the original file to settings.json.bak-<timestamp> before writing.
"""
import json
import shutil
import sys
import time
from pathlib import Path

SETTINGS = Path.home() / ".claude" / "settings.json"
STATUSLINE = {
    "type": "command",
    "command": "~/.local/bin/alexis-statusline",
    "refreshInterval": 60,
}


def main() -> int:
    force = "--force" in sys.argv
    SETTINGS.parent.mkdir(parents=True, exist_ok=True)
    data = {}
    if SETTINGS.exists():
        try:
            data = json.loads(SETTINGS.read_text() or "{}")
        except json.JSONDecodeError:
            print(f"  {SETTINGS} is not valid JSON; not touching it. Add the statusLine manually (see README).")
            return 0
        shutil.copy2(SETTINGS, SETTINGS.with_name(f"settings.json.bak-{int(time.time())}"))

    if "statusLine" in data and not force:
        print("  A statusLine is already configured; kept yours (re-run with --force to use ALEXIS's).")
        return 0

    data["statusLine"] = STATUSLINE
    SETTINGS.write_text(json.dumps(data, indent=2) + "\n")
    print(f"  Status line configured in {SETTINGS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
