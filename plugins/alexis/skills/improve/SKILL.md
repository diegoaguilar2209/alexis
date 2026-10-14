---
name: improve
description: Improve the user's Claude Code setup from evidence - reads recent friction (session logs, /insights report, repeated corrections) and proposes concrete edits to CLAUDE.md, skills, hooks or settings, optionally as a contribution to ALEXIS. Use when the user asks to improve their setup, says Claude keeps making the same mistake, or runs /alexis:improve.
disable-model-invocation: true
---

# Improve the setup

A setup gets better only from evidence of where it failed. Reply in the user's language.

## 1. Gather evidence (read, do not guess)

- The `/insights` report if it exists: `~/.claude/usage-data/report.html` (suggest the user run `/insights` first if it is missing or older than a week).
- Learnings in `docs/decisions.md` of the current project and, if `ALEXIS_VAULT` is set, recent notes in `<vault>/1-Projects/`.
- What the user tells you went wrong.
- `/usage` breakdown if the complaint is about limits: which skills, subagents or MCP servers drive usage.

## 2. Classify each problem and pick the right fix

| Symptom | Fix |
| --- | --- |
| Claude got the same convention wrong twice | One line in CLAUDE.md (project or user) |
| The same multi-step procedure pasted 3 times | A new skill |
| Something must happen every time, no judgment needed | A hook |
| Context fills up with output nobody rereads | A subagent, or a hook that filters output |
| Usage limits hit early | Model routing (cheaper model for subagents/skills), `/clear` between tasks, fewer MCP servers, CLI over MCP |
| A skill triggers when it should not, or never | Rewrite its description: specific trigger first |

## 3. Propose

For each problem: evidence (quote or file), the fix, the exact diff, and expected effect. Apply only what the user approves.

## 4. Share back

If a fix is generic (useful to anyone, no personal or employer data), offer to draft a pull request or issue for the ALEXIS repository: https://github.com/diegoaguilar2209/alexis
