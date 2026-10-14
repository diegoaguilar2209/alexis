# Contributing to ALEXIS

Thanks for helping. ALEXIS improves from evidence: real friction in real sessions.

## What makes a good contribution
- A skill for a procedure people repeat, with a clear trigger in its `description` (the first sentence decides when Claude uses it).
- A fix for a hook false positive or false negative, with a test case in `tests/`.
- A better default in the templates, explained by the failure it prevents.

## Rules
- No personal, employer or client data anywhere — examples use generic names.
- Skills stay under 500 lines; move detail to `references/`.
- Pin subagents and light skills to the cheapest model that does the job well (`model`, `effort` in frontmatter).
- Prefer official sources (Anthropic, Microsoft, Databricks, dbt Labs) for anything you recommend installing.

## Before opening a PR
```bash
claude plugin validate ./plugins/alexis --strict
claude plugin validate .
python scripts/check_repo.py
pytest -q tests
```
Then try the change in a real Claude Code session and add a line to `CHANGELOG.md` under "Unreleased".

## Releasing (maintainers)
1. Move "Unreleased" entries under a new version in `CHANGELOG.md`.
2. Bump `version` in `plugins/alexis/.claude-plugin/plugin.json`.
3. Tag `vX.Y.Z` and push the tag; the release workflow publishes the notes.
