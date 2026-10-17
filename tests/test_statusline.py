import json
import subprocess
import time

from conftest import TOOLS


def render(payload) -> str:
    raw = payload if isinstance(payload, str) else json.dumps(payload)
    out = subprocess.run([str(TOOLS / "alexis-statusline")], input=raw, capture_output=True, text=True, check=True)
    return out.stdout


def test_subscriber_shows_limits():
    now = int(time.time())
    line = render({
        "model": {"display_name": "Opus"},
        "context_window": {"used_percentage": 42},
        "rate_limits": {
            "five_hour": {"used_percentage": 67.2, "resets_at": now + 3600},
            "seven_day": {"used_percentage": 12, "resets_at": now + 300000},
        },
    })
    assert "Opus" in line and "42%" in line and "5h 67%" in line and "7d 12%" in line


def test_api_user_shows_cost():
    line = render({"model": {"display_name": "Sonnet"}, "cost": {"total_cost_usd": 0.734}})
    assert "$0.73" in line


def test_missing_fields_and_bad_input():
    assert "Claude" in render({})
    assert render("not json").strip() == "alexis"


def test_alert_at_80_percent():
    now = int(time.time())
    line = render({"model": {"display_name": "Opus"}, "rate_limits": {"five_hour": {"used_percentage": 86, "resets_at": now + 600}}})
    assert line.index("! 5h 86%") < line.index("Opus")
