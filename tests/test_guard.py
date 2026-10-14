import os

import pytest
from conftest import run_hook

BLOCK = [
    ("Bash", {"command": "databricks bundle deploy -t prod"}),
    ("Bash", {"command": "databricks bundle deploy --target prod"}),
    ("Bash", {"command": "git push --force origin main"}),
    ("Bash", {"command": "rm -rf ~"}),
    ("Bash", {"command": "bq rm -t ds.table"}),
    ("Bash", {"command": "aws s3 rm s3://bucket --recursive"}),
    ("Bash", {"command": 'psql -c "DELETE FROM t; SELECT 1 WHERE true"'}),
    ("mcp__db__query", {"query": "DROP TABLE dev.s.t"}),
    ("mcp__db__query", {"query": "TRUNCATE TABLE sales"}),
    ("mcp__db__query", {"query": "DELETE FROM dev.s.t"}),
    ("mcp__db__query", {"query": "UPDATE t SET a = 1"}),
]
ALLOW = [
    ("Bash", {"command": "pytest -q"}),
    ("Bash", {"command": "databricks bundle deploy -t dev"}),
    ("Bash", {"command": "git push origin feature-x"}),
    ("Bash", {"command": "rm -rf build/"}),
    ("mcp__db__query", {"query": "SELECT * FROM truncate_log WHERE id = 1"}),
    ("mcp__db__query", {"query": "DELETE FROM dev.s.t WHERE id = 1"}),
    ("mcp__db__query", {"query": "UPDATE t SET a = 1 WHERE id = 2"}),
    ("Read", {"file_path": "DROP TABLE.md"}),
]


@pytest.mark.parametrize("tool,tool_input", BLOCK)
def test_blocks_destructive(tool, tool_input):
    result = run_hook("guard_destructive.py", {"tool_name": tool, "tool_input": tool_input})
    assert result.returncode == 2, result.stderr
    assert "Blocked by ALEXIS" in result.stderr


@pytest.mark.parametrize("tool,tool_input", ALLOW)
def test_allows_safe(tool, tool_input):
    result = run_hook("guard_destructive.py", {"tool_name": tool, "tool_input": tool_input})
    assert result.returncode == 0, result.stderr


def test_override_allows():
    env = {**os.environ, "ALEXIS_ALLOW_DESTRUCTIVE": "1"}
    result = run_hook("guard_destructive.py", {"tool_name": "Bash", "tool_input": {"command": "bq rm -t x.y"}}, env)
    assert result.returncode == 0


def test_bad_json_is_ignored():
    import subprocess
    from conftest import SCRIPTS

    result = subprocess.run(["bash", str(SCRIPTS / "run-py.sh"), "guard_destructive.py"], input="nope", capture_output=True, text=True)
    assert result.returncode == 0
