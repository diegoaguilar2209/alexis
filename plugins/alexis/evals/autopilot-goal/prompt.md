---
description: A request to work unattended should produce a verifiable goal with constraints and a budget.
tags: [autopilot, trigger]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---

I'm going to step away. Keep working on the ingestion module on your own until it's done. The acceptance criteria: `pytest -q tests/ingestion` passes and `pre-commit run --all-files` is clean. Don't touch the reporting folder. Before you start, show me exactly how you'll run.
