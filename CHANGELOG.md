# Changelog

All notable changes to ALEXIS. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

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
