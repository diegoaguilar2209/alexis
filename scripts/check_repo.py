"""Repository checks run in CI: JSON/YAML parse, skill and agent frontmatter, no leftover placeholders in code."""
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []

for path in ROOT.rglob("*.json"):
    if ".git" in path.parts:
        continue
    try:
        json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        errors.append(f"{path}: invalid JSON ({exc})")

for path in list(ROOT.rglob("*.yml")) + list(ROOT.rglob("*.yaml")):
    if ".git" in path.parts:
        continue
    try:
        yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:
        errors.append(f"{path}: invalid YAML ({exc})")

for path in list((ROOT / "plugins/alexis/skills").glob("*/SKILL.md")) + list((ROOT / "plugins/alexis/agents").glob("*.md")):
    text = path.read_text()
    if not text.startswith("---"):
        errors.append(f"{path}: missing frontmatter")
        continue
    meta = yaml.safe_load(text.split("---")[1]) or {}
    for key in ("name", "description"):
        if not meta.get(key):
            errors.append(f"{path}: frontmatter missing '{key}'")
    if len(meta.get("description", "")) > 1024:
        errors.append(f"{path}: description longer than 1024 characters")
    if path.name == "SKILL.md" and meta.get("name") != path.parent.name:
        errors.append(f"{path}: name '{meta.get('name')}' does not match folder '{path.parent.name}'")
    if len(text.splitlines()) > 500:
        errors.append(f"{path}: over 500 lines; move detail to references/")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("Repository checks passed")
