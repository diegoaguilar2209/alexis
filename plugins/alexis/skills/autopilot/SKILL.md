---
name: autopilot
description: Let Claude build, test, fix and iterate on its own until measurable acceptance criteria pass - turns a plan into a /goal condition with verification, checkpoints and a stop budget. Use when the user wants Claude to work unattended, "build it alone", "keep going until it works", or runs /alexis:autopilot.
argument-hint: "[what to finish, or a section of docs/plan.md]"
---

# Autopilot

Claude Code can keep working without you prompting each step: `/goal` sets a completion condition, and after every turn a separate evaluator model checks whether it holds. If not, Claude starts another turn with the evaluator's reason as guidance. This skill writes a goal that converges instead of looping, and sets up the guardrails so you can walk away. Reply in the user's language.

## 1. Preconditions (check, do not assume)

- A spec or plan exists (`docs/spec.md`, `docs/plan.md`) or the user stated the target in $ARGUMENTS. If neither, stop and run `/alexis:new-project` first.
- There is at least one command that proves progress: tests (`pytest -q`), evals (`python evals/run.py`), a build, `pre-commit run --all-files`, `docker compose config -q`, a smoke test. If none exists, the FIRST task is to write the failing tests or eval cases for the target.
- Git is clean or the user agreed to continue from the current state. Create a branch: `git switch -c autopilot/<topic>`.
- Permissions allow the work unattended. Recommend auto mode (Shift+Tab until it shows) so tool calls do not wait for approval. The project's `.claude/settings.json` deny rules and the plugin's safety hook stay active in auto mode.

## 2. Write the goal condition

A good condition has one measurable end state, the command that proves it, constraints, and a budget. Template:

```
/goal <target> is done: `<verification command>` exits 0 and <eval score or acceptance criteria> hold.
Constraints: do not edit tests or eval cases to make them pass; do not touch <out-of-scope paths>; no production resources.
Work in small steps: after each step run the verification, then commit with a conventional message.
Stop after <N> turns (default 30) or if blocked by missing access, and report what is left.
```

Show the condition to the user and start it with `/goal`. Keep it under 4,000 characters.

## 3. The loop Claude follows each turn

1. Pick the next unchecked task from the plan.
2. Implement the smallest change that moves the verification forward.
3. Run the verification command and read the actual output (do not summarize from memory).
4. Red: diagnose the root cause before changing code; one hypothesis at a time. Green: commit (`feat:`/`fix:` + what changed).
5. Every ~5 green commits, or before declaring done, delegate a fresh-eyes audit to the `verifier` subagent: it checks the work against the spec and evals without having written it.
6. Update `docs/plan.md` checkboxes and append one line per decision to `docs/decisions.md`.

## 4. Anti-loop rules

- Same error three times in a row: stop changing code, write down what was tried, and switch strategy (read the docs, isolate a minimal repro, or ask the user).
- Never weaken a test, skip it, or hard-code expected outputs to get to green.
- Do not expand scope. New ideas go to `docs/plan.md` under "Later".
- If a verification needs credentials or a service that is not available, the goal is blocked: report it instead of mocking it in production code.

## 5. Usage limits and long runs

- On a claude.ai Pro or Max plan, when a 5-hour or weekly usage limit stops the run, Claude Code waits in the open session and continues automatically after the reset (on by default in interactive sessions, v2.1.234+). Keep the terminal open; in tmux, detach and come back. An active goal is restored if the session is resumed with `claude --continue`.
- That automatic wait is not available in `-p` (headless) runs or with API keys. For unattended headless runs use `alexis-goal`, which runs `claude -p "/goal ..."` with streaming logs.
- Check spend with `/goal` (no arguments: turns, time, tokens) and `/usage`. The ALEXIS status line shows context use and the 5-hour and weekly limits.

## 6. Finish

When the evaluator reports the goal met: run the full verification once more, run `/alexis:session-log`, and give the user a summary: what was built, verification output, commits on the branch, anything left in "Later". Do not merge to main without the user.
