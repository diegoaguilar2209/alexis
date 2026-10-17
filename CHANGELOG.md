# Changelog

All notable changes to ALEXIS. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [2.1.0] - 2026-10-17

### Added
- Eval suite (`plugins/alexis/evals/`, 11 cases) run with `claude plugin eval`, including a Spanish trigger case and a must-not-trigger case; manual/weekly `evals` GitHub workflow with a Sonnet judge.
- Workflows: `audit-model` (review per file + adversarial verification) and `migrate` (one agent per file in its own worktree + checker).
- Skills: `data-contract`, `metric-definition`.
- Project template: `claude-review.yml` PR review with `claude-code-action`.
- Routine templates: PR review, documentation drift, post-deploy check, ALEXIS upkeep.
- `telemetry/`: local OpenTelemetry collector + Prometheus + Loki + Grafana.
- `docs/demo.tape` to record the README demo with VHS.
- Installer: `pyright-lsp`, `context7`, `security-guidance` in core; `pr-review-toolkit`, `semgrep` in `--full`.
- Status line warns at 80% of the 5-hour window (`ALEXIS_STATUSLINE_ALERT`).

### Changed
- `new-project` asks at most 5 single-ask questions and states the rest as assumptions (found by evals; kickoff case now passes 2 of 3 runs, up from 0).
- `autopilot` description rewritten around the user's phrasing; trigger rate on the eval went from 1/3 to 3/3. Autopilot now chooses between `/goal` and a workflow.

## [2.0.0] - 2026-10-14

First public release.

### Added
- Skills: `new-project`, `autopilot`, `hackathon`, `powerbi-executive`, `exec-deck`, `validate-idea`, `session-log`, `improve`.
- Subagents: `verifier`, `sql-reviewer`, `data-validator`, pinned to cost-effective models.
- Safety hook for destructive SQL, shell and cloud operations (including MCP calls); validation hook that runs the repo's pre-commit after each edit.
- Project template: CLAUDE.md, spec, decisions, impact, evals, permissions, pre-commit, pip-tools and CI.
- Tools: `alexis-statusline` (context, 5-hour and weekly usage with resets), `alexis-wt` (worktree + tmux), `alexis-goal` (headless goals).
- Obsidian vault starter, user CLAUDE.md template, installer for Linux/macOS/WSL2 and Windows.
- CI: plugin validation, repository checks, shellcheck, tests; weekly template autoupdate; release workflow.
