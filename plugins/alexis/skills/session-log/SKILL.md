---
name: session-log
description: At the end of a work session, record decisions, learnings, measurable impact and next steps in the project's docs and, if configured, the user's Obsidian vault. Use when the user says "wrap up", "log this session" or runs /alexis:session-log.
disable-model-invocation: true
model: haiku
effort: low
---

# Session log

Keeps the project's memory in files the user controls, so the next session starts with context, and builds session by session the evidence of impact (what matters in a performance review, a pitch or a CV). Reply in the user's language.

## What to record

Review the session and write ONLY what changes the project's future:

- Decisions and their reason (one line each).
- Reusable learnings (a bug and its root cause, a pattern that worked).
- Status: what is done, what is half-done.
- Next 3 steps.
- Impact, only if there was a measurable result: what changed, how much (number and unit), for whom and how it was measured. If there is no number yet, note which metric would prove it.

## Where

1. `docs/decisions.md` in the project: new entry at the top with the date (`## YYYY-MM-DD`).
2. `docs/impact.md` in the project: one row per measurable result (date, result, metric, evidence).
3. If the user's `~/.claude/CLAUDE.md` defines `ALEXIS_VAULT`:
   - Note in `<vault>/1-Projects/<project-name>.md` (status, decisions, `[[links]]`).
   - If there was impact, one line in `<vault>/2-Areas/Career/Impact.md` with date, result and number.
4. If a learning applies to every project, propose (do not apply) a change to the user's CLAUDE.md or suggest `/alexis:improve`.

## Rules

- Work and client projects: in a personal vault only the result in general terms ("cut campaign cost 18%"), never data, table names, client names or credentials.
- Short sentences; do not narrate what was done step by step.
