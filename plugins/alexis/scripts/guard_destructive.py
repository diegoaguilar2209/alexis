"""PreToolUse hook: blocks destructive operations in shell commands and MCP calls.

Reads the hook event from stdin (JSON with tool_name and tool_input).
Exits 2 with a message on stderr to block; 0 to allow.
To allow destructive operations for one session, the user (never Claude) starts
Claude Code with ALEXIS_ALLOW_DESTRUCTIVE=1.
"""
import json
import os
import re
import sys

SQL_PATTERNS = [
    (r"\bDROP\s+(TABLE|VIEW|SCHEMA|DATABASE|CATALOG|VOLUME)\b", "DROP of objects"),
    (r"\bTRUNCATE\s+(TABLE\s+)?\w", "TRUNCATE"),
    (r"\bDELETE\s+FROM\s+[\w.`\"]+(?![^;]*\bWHERE\b)", "DELETE without WHERE"),
    (r"\bUPDATE\s+[\w.`\"]+\s+SET\b(?![^;]*\bWHERE\b)", "UPDATE without WHERE"),
    (r"\bALTER\s+TABLE\s+[\w.`\"]+\s+DROP\b", "ALTER TABLE ... DROP"),
    (r"\b(INSERT\s+OVERWRITE|CREATE\s+OR\s+REPLACE\s+TABLE)\b[\s\S]*\bprod", "overwrite in production"),
]

SHELL_PATTERNS = [
    (r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*f?\s+(/|~|\$HOME)(\s|$)", "rm -rf on root or home"),
    (r"\bgit\s+push\b[^\n]*\s(--force|-f)(\s|$)", "git push --force"),
    (r"\bgit\s+reset\s+--hard\s+origin", "git reset --hard to remote"),
    (r"\bdatabricks\s+bundle\s+(deploy|destroy)\b[^\n]*(-t|--target)\s*=?\s*prod", "bundle deploy/destroy to prod"),
    (r"\bdatabricks\s+(fs\s+rm|workspace\s+delete|catalogs\s+delete|schemas\s+delete)\b", "delete in Databricks"),
    (r"\bbq\s+rm\b", "delete in BigQuery"),
    (r"\baws\s+s3\s+(rm|rb)\b[^\n]*--recursive", "recursive delete in S3"),
    (r"\baz\s+(group|storage\s+account)\s+delete\b", "Azure resource deletion"),
]


def find_issue(text: str, patterns):
    for pattern, label in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE):
            return label
    return None


def main() -> int:
    if os.environ.get("ALEXIS_ALLOW_DESTRUCTIVE") == "1":
        return 0
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    tool = event.get("tool_name", "")
    tool_input = event.get("tool_input", {}) or {}

    if tool == "Bash":
        text = str(tool_input.get("command", ""))
        issue = find_issue(text, SHELL_PATTERNS) or find_issue(text, SQL_PATTERNS)
    elif tool.startswith("mcp__"):
        text = json.dumps(tool_input, ensure_ascii=False)
        issue = find_issue(text, SQL_PATTERNS)
    else:
        return 0

    if issue:
        print(
            f"Blocked by ALEXIS: {issue}. "
            "This is a destructive or production operation. "
            "Propose a safe alternative (dev environment, explicit WHERE, backup) "
            "or ask the user to run it themselves.",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
