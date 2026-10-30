# Changelog

All notable changes to ALEXIS. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Changed
- README (English and Spanish) rewritten: goal, quick start, how it works, every piece grouped by stage, repository structure, recommended plugins (official and community) and tested platforms (Windows with WSL2).

### Added
- `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1).

## [2.3.0] - 2026-10-17

### Added
- Skill `tech-radar`: researches recent primary sources, rates findings Adopt/Trial/Assess/Hold with evidence and proposes concrete edits; routine `alexis-radar` runs it monthly on ALEXIS and opens a PR.
- `build-agent` references from the October 2026 radar: `advanced-tools.md` (tool search, programmatic tool calling, code execution with MCP, tool use examples, MCP 2026-07-28 stateless spec, A2A, MCP Apps / AG-UI / A2UI, agent payments, SKILL.md portability), `data-agents.md` (semantic layer before text-to-SQL, Genie, RAG choices incl. agentic search vs GraphRAG), `long-running.md` (generator/evaluator harness, stateless harness + session log + sandbox, durable execution, parallel agents).
- Evals: `tech-radar-trigger`, `build-agent-data-kpi`.

### Changed
- `build-agent`: pass^k for user-facing agents, capability vs regression evals, automatic prompt optimization (GEPA/DSPy), OpenTelemetry GenAI conventions, agent registries (Agent 365), model-agnostic design with open-weight options.
- `metric-definition`: publish definitions to the semantic layer that agents query.

## [2.2.0] - 2026-10-17

### Added
- Skill `build-agent`: from spec to production agent. Pattern choice (augmented LLM, chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, autonomous), harness selection matrix, tool design (agent-computer interface), context engineering, agent evals, OWASP Top 10 for Agentic Applications 2026 controls, cost/model routing, deployment on Azure Foundry (Teams, M365 Copilot), Databricks, AWS, GCP and Anthropic, and a "works for me, fails for others" diagnosis.
- Subagent `agent-reviewer` for an independent review before real users.
- Project template: `evals/agent-cases.yaml` with refusal, prompt-injection and permission-boundary cases.
- Evals: `build-agent-harness`, `build-agent-works-for-me`, `build-agent-pattern`.

### Changed
- `new-project` agent archetype hands off to `build-agent`; project CLAUDE.md calls `agent-reviewer` after agent changes.

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
