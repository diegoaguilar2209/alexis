# Build alone

Phase 5 of `/alexis:project`. After the user approved the spec and plan, Claude builds, tests and fixes until each milestone's measurable criteria pass, without asking for each step. The only reasons to stop are the hard stops in the skill's autonomy policy.

## 1. Preconditions (check, do not assume)

- `docs/plan.md` approved, with milestones and verification commands.
- At least one command proves progress: tests, evals, build, lint/typecheck, `pre-commit run --all-files`, a smoke test. If none exists, the first task is to write the failing tests or eval cases for the milestone.
- Git is clean. Create the branch `build/<milestone>`.
- Recommend auto mode (Shift+Tab until it shows), so tool calls do not wait for approval. The project's `.claude/settings.json` deny rules and the ALEXIS safety hook stay active in auto mode.

## 2. Goal condition (one per milestone)

```
/goal <milestone> is done: `<verification command>` exits 0 and <acceptance criteria / eval score> hold.
Constraints: do not edit tests or eval cases to make them pass; do not touch <out-of-scope paths>; no production resources.
Work in small steps: after each step run the verification, then commit with a conventional message.
Stop after <N> turns (default 30) or if blocked by missing access, and report what is left.
```

Keep it under 4,000 characters. When a milestone's goal is met, write the next milestone's condition and start it; do not ask.

## 3. The loop each turn

1. Pick the next unchecked task from the plan.
2. Implement the smallest change that moves the verification forward.
3. Run the verification and read the actual output (never summarize from memory).
4. Red: diagnose the root cause before changing code, one hypothesis at a time. Green: commit (`feat:`/`fix:` + what changed).
5. Update `docs/plan.md` checkboxes; one line per decision in `docs/decisions.md`.

## 4. Parallel work with native subagents

Claude Code spawns and orchestrates subagents natively; there is no need for manual worktrees or tmux windows.

- Parallelize only tasks marked independent in the plan that do not touch the same files, schema or migration. The shared foundation (schema, core types, CI) is built first, sequentially.
- Each subagent runs with `isolation: "worktree"` and receives a self-contained brief: the task, the files it owns, the verification command, the conventions file, and the specialist skill to load (e.g. `/alexis:build-agent`, `/alexis:data-contract`). It starts cold, so the brief must carry the context.
- Ask for a short result: what changed, verification output, open issues. You (the orchestrator) review, merge into the build branch and run the full verification.
- Many independent items of the same change (dozens of files) → the `/alexis:migrate` workflow. A review of a whole model → `/alexis:audit-model`. Workflows spend more: start on a small slice.

## 5. Fresh-eyes review

- Every ~5 green commits, and before calling a milestone done: the `verifier` subagent audits against spec, plan and evals.
- Area reviewers when their area changed: `sql-reviewer` (SQL), `data-validator` (numbers to be published), `agent-reviewer` (agents, prompts, tools).
- Fix what they find before continuing.

## 6. Anti-loop rules

- Same error three times in a row: stop changing code, write down what was tried, switch strategy (read the docs, isolate a minimal repro). If still stuck, it is a hard stop: ask the user.
- Never weaken a test, skip it, or hard-code expected outputs.
- Do not expand scope. New ideas go to `docs/plan.md` under "Later".
- A verification that needs credentials or a service that is not available is a hard stop: report it instead of mocking it in production code.

## 7. Usage limits and long runs

- On Pro or Max plans, when a 5-hour or weekly limit stops the run, Claude Code waits in the open session and continues after the reset (interactive sessions). Keep the terminal open; tmux helps. An active goal is restored with `claude --continue`.
- Headless runs (`-p`) and API keys do not wait. For unattended headless runs use `alexis-goal`, which runs `claude -p "/goal ..."` with streaming logs.
- Check spend with `/goal` (no arguments) and `/usage`. The ALEXIS status line shows context and limits.

## 8. Finish

When every milestone is met: run the full verification once more, set `Phase: done`, run phase 6 (close), and give the user a summary — what was built, verification output, commits on the branch, anything left in "Later". Never merge to `main` without the user.
