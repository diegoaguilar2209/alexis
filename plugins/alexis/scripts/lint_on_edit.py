"""PostToolUse hook: validates the file Claude just edited with the project's own tools.

Order of preference:
1. If the repo has .pre-commit-config.yaml and pre-commit is installed, run
   `pre-commit run --files <file>` (respects the project's configuration).
2. Otherwise, use the tool for the file type, if installed:
   - .py                       -> black --check and isort --check-only (black profile)
   - .sql                      -> sqlfluff lint (repo .sqlfluff dialect; databricks if none)
   - Dockerfile / *.Dockerfile -> hadolint
   - docker-compose*.yml       -> docker compose config -q
   - ansible/**/*.yml          -> ansible-lint
On errors, exit 2 so Claude sees them and fixes them. No tool available: do nothing.
Set ALEXIS_SKIP_VALIDATION=1 to disable it for a session.
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd, cwd=None):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120, cwd=cwd)
    except (OSError, subprocess.TimeoutExpired):
        return 0, ""
    return result.returncode, (result.stdout + result.stderr).strip()


def find_repo_root(path: Path):
    for parent in [path.parent, *path.parents]:
        if (parent / ".git").exists():
            return parent
    return None


def choose_commands(path: Path):
    name = path.name.lower()
    suffix = path.suffix.lower()
    cmds = []
    if suffix == ".py":
        if shutil.which("black"):
            cmds.append(["black", "--check", "--diff", "--quiet", str(path)])
        if shutil.which("isort"):
            cmds.append(["isort", "--check-only", "--diff", "--profile", "black", str(path)])
    elif suffix == ".sql" and shutil.which("sqlfluff"):
        # Respect the repo's .sqlfluff dialect; default to databricks
        root = find_repo_root(path)
        has_cfg = root is not None and (root / ".sqlfluff").exists()
        cmd = ["sqlfluff", "lint", str(path)]
        cmds.append(cmd if has_cfg else cmd + ["--dialect", "databricks"])
    elif (name == "dockerfile" or name.endswith(".dockerfile")) and shutil.which("hadolint"):
        cmds.append(["hadolint", str(path)])
    elif name.startswith("docker-compose") and suffix in (".yml", ".yaml") and shutil.which("docker"):
        cmds.append(["docker", "compose", "-f", str(path), "config", "-q"])
    elif "ansible" in path.parts and suffix in (".yml", ".yaml") and shutil.which("ansible-lint"):
        cmds.append(["ansible-lint", str(path)])
    return cmds


def main() -> int:
    if os.environ.get("ALEXIS_SKIP_VALIDATION") == "1":
        return 0
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    raw = str((event.get("tool_input") or {}).get("file_path", ""))
    if not raw or not os.path.isfile(raw):
        return 0
    path = Path(raw).resolve()

    root = find_repo_root(path)
    if root and (root / ".pre-commit-config.yaml").exists() and shutil.which("pre-commit"):
        code, out = run(["pre-commit", "run", "--files", str(path)], cwd=root)
    else:
        code, out = 0, ""
        for cmd in choose_commands(path):
            c, o = run(cmd, cwd=str(root) if root else None)
            if c != 0:
                code, out = c, (out + "\n" + o).strip()

    if code != 0 and out:
        print(f"Validation found problems in {path.name}:\n{out[:3000]}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
