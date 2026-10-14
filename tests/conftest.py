import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "plugins" / "alexis" / "scripts"
TOOLS = ROOT / "tools"


def run_hook(script: str, event: dict, env=None):
    return subprocess.run(
        ["bash", str(SCRIPTS / "run-py.sh"), script],
        input=json.dumps(event),
        capture_output=True,
        text=True,
        env=env,
    )
