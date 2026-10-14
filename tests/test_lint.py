import os
import shutil
import subprocess

import pytest
from conftest import run_hook

pytestmark = pytest.mark.skipif(not shutil.which("black"), reason="black not installed")


def test_flags_unformatted_python(tmp_path):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    bad = tmp_path / "bad.py"
    bad.write_text('x = {"a":1}\n')
    result = run_hook("lint_on_edit.py", {"tool_input": {"file_path": str(bad)}})
    assert result.returncode == 2
    assert "Validation found problems" in result.stderr


def test_passes_clean_python(tmp_path):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    ok = tmp_path / "ok.py"
    ok.write_text('x = {"a": 1}\n')
    assert run_hook("lint_on_edit.py", {"tool_input": {"file_path": str(ok)}}).returncode == 0


def test_skip_switch(tmp_path):
    bad = tmp_path / "bad.py"
    bad.write_text('x = {"a":1}\n')
    env = {**os.environ, "ALEXIS_SKIP_VALIDATION": "1"}
    assert run_hook("lint_on_edit.py", {"tool_input": {"file_path": str(bad)}}, env).returncode == 0


def test_missing_file_is_ignored():
    assert run_hook("lint_on_edit.py", {"tool_input": {"file_path": "/nope/x.py"}}).returncode == 0
