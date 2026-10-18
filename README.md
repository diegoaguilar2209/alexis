# ALEXIS

**A**gentic **L**ayer for **EX**ecution, **I**nsight and **S**ystems — an opinionated Claude Code system for building data solutions, from idea to verified delivery.

*Alexis* comes from the Greek *alexein*, "to defend": it builds with you and guards you against destructive mistakes.

[Español](README.es.md)

## Why

Claude Code is powerful out of the box. What separates great results from average ones is the system around it: a method that plans before coding, verification that Claude cannot skip, guardrails, the right model for each task, and memory between sessions. ALEXIS packages that system for data work — pipelines, dashboards, agents, SQL and executive decks — so you can install it in minutes and adapt it.

## What you get

| Piece | What it does |
| --- | --- |
| `/alexis:new-project` | Tell it your idea → short interview → spec, repo scaffold, CLAUDE.md, evals and plan |
| `/alexis:autopilot` | Claude builds, tests, fixes and iterates alone until measurable criteria pass (`/goal` + verification + checkpoints) |
| `/alexis:hackathon` | Playbook from Claude Code hackathon winners: judges → spec → evals → parallel build → audit → demo |
| `/alexis:powerbi-executive` | Audit and redesign Power BI reports: model, DAX, tables and consulting-grade design, plus a theme file |
| `/alexis:build-agent` | Design, build and ship AI agents: pattern (workflow vs agent), harness choice (Claude Agent SDK, Microsoft Agent Framework, LangGraph, ADK...), tool design, context engineering, agent evals, OWASP agentic security, deployment (Azure Foundry → Teams, Databricks Genie, AWS, GCP) and "works for me, fails for others" diagnosis |
| `/alexis:tech-radar` | What is new and what actually works in AI, agents, Claude Code or data platforms: primary sources, Adopt/Trial/Assess/Hold ratings, and concrete edits to your project or to ALEXIS. A monthly routine runs it on ALEXIS itself |
| `/alexis:data-contract` | Schema, keys, allowed values and freshness for a shared table, enforced by generated tests |
| `/alexis:metric-definition` | One definition per KPI, traced from the DAX measure to the SQL, with mismatches flagged |
| `/alexis:exec-deck` | Conclusion-first executive presentations with traceable numbers |
| `/alexis:validate-idea` | Filter startup and paid-app ideas before building: customer, who pays, distribution, cheapest experiment |
| `/alexis:session-log` | Log decisions, measurable impact and next steps at the end of a session (project + Obsidian) |
| `/alexis:improve` | Improve your setup from evidence: friction, repeated corrections, usage breakdown |
| Workflows | `/alexis:audit-model` (one reviewer per file, each finding verified by a second agent) and `/alexis:migrate` (one agent per file in its own worktree, then a checker) |
| Evals | Every skill has cases run with `claude plugin eval`: does it fire on natural phrasing, and does its output keep its promise |
| Subagents | `verifier` (fresh-eyes audit), `sql-reviewer`, `data-validator`, `agent-reviewer` — each pinned to a cost-effective model |
| Safety | Deterministic permission rules + a hook that blocks DROP, TRUNCATE, DELETE/UPDATE without WHERE, prod deploys, force push and cloud deletions, including through MCP |
| Quality | After every edit, your repo's pre-commit runs on that file; project template with pre-commit, pip-tools and CI |
| `alexis-statusline` | Model, effort, context bar, **5-hour and weekly plan usage with reset times**, session cost |
| `alexis-wt` | One git worktree + one tmux window + one Claude Code session per workstream |
| `alexis-goal` | Headless goal runs with live logs |
| Routine templates | Cloud routines for PR review, documentation drift, post-deploy checks and ALEXIS upkeep |
| Telemetry | Local OpenTelemetry + Prometheus + Loki + Grafana stack for token and cost history |
| Obsidian vault starter | Long-term memory and a career impact log |

## Install

Requirements: [Claude Code](https://code.claude.com/docs), Git, Python 3, bash (Linux, macOS or WSL2). Optional: tmux, pre-commit, pip-tools, black, isort, sqlfluff, Databricks CLI.

```bash
git clone https://github.com/diegoaguilar2209/alexis.git
cd alexis
bash setup/install.sh          # core
bash setup/install.sh --full   # + Azure, Microsoft Docs, GitHub, dbt, Power BI authoring, Databricks AI Tools
```

The installer registers this clone as a plugin marketplace (do not move the folder afterwards), installs ALEXIS and the recommended plugins, links the `alexis-*` tools into `~/.local/bin`, adds the status line to `~/.claude/settings.json` (backing it up first, and only if you have none), and copies `templates/user/CLAUDE.md` to `~/.claude/CLAUDE.md` if you do not have one. Then fill in its "About me" section.

Only the plugin? `claude plugin marketplace add diegoaguilar2209/alexis` and `claude plugin install alexis@alexis`.

## Daily use

```text
mkdir churn-model && cd churn-model && claude
/alexis:new-project Predict customer churn from transactions and show it in Power BI
/alexis:autopilot   # let it build until tests and evals pass
/alexis:session-log # when you stop
```

## Evals: proof that each skill helps

Each skill ships with eval cases in `plugins/alexis/evals/`. `claude plugin eval` runs them in isolated sessions, checks that the skill fires on natural phrasing (in English and Spanish) and grades the output against a rubric, optionally comparing against the same prompt without ALEXIS.

```bash
cd plugins/alexis
claude plugin eval . --runs 1 --ablation none --judge-model sonnet   # quick check
claude plugin eval . --judge-model sonnet                            # full, with vs. without ALEXIS
```

The suite already caught real problems: the kickoff skill asked too many sub-questions, and the autopilot skill fired only 1 time in 3 on "I'm stepping away, keep going" until its description was rewritten (now 3 in 3). A manual or weekly GitHub workflow runs the suite with your `ANTHROPIC_API_KEY` secret.

## Autonomy: how Claude keeps working alone

`/alexis:autopilot` turns your plan into a `/goal` condition with a verification command, constraints and a turn budget. After every turn a separate evaluator model checks the condition; if it is not met, Claude continues with the evaluator's feedback. Claude commits each green step, a `verifier` subagent audits the work with fresh eyes, and anti-loop rules force a change of strategy after repeated failures. Run it in auto mode so tool calls do not wait for approval; the deny rules and the safety hook still apply. For many independent items (a migration across dozens of files, a review of a whole model), autopilot switches to a dynamic workflow that runs many agents in parallel and cross-checks their results.

For work that should happen without your laptop, `routines/` has templates for Claude Code cloud routines: PR review, documentation drift, post-deploy checks.

## Tokens, models and usage limits

- **Model routing**: subagents and light skills are pinned to cheaper models (`sonnet`, `haiku`) so they do not inherit Opus. The user CLAUDE.md template recommends `sonnet` for daily work, `opusplan` for complex features (Opus plans, Sonnet executes) and lowering `/effort` before switching to a bigger model.
- **History**: `telemetry/` runs a local OpenTelemetry + Grafana stack with tokens and cost per day, model and tool.
- **Meter**: the status line shows context use and, on Pro/Max plans, the rolling **5-hour** and **weekly** usage with their reset times. At 80% of the 5-hour window it leads with a warning to save state. `/usage` shows what is driving your usage (skills, subagents, MCP servers).
- **When you hit a limit**: on Pro/Max, Claude Code waits in the open session and continues the interrupted task automatically after the reset (interactive sessions, Claude Code v2.1.234+). Keep the terminal open (tmux helps). If the limit is a weekly one more than 24 hours away, or you prefer to keep working, `/usage-credits` lets you continue on paid usage. Headless (`-p`) runs and API keys do not wait.

## Power BI

`/alexis:powerbi-executive` accepts a PBIP project (TMDL + PBIR), a live model through the [Power BI Modeling MCP](https://github.com/microsoft/powerbi-modeling-mcp), DAX/`INFO.VIEW` exports or screenshots. It audits model, DAX and design, then delivers a storyline, page wireframes, corrected measures and a theme JSON. For editing report files it works with Microsoft's `powerbi-authoring` plugin ([skills-for-fabric](https://github.com/microsoft/skills-for-fabric)). For a deeper Power BI toolkit, see [power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development).

## Staying current

- CI validates the plugin with `claude plugin validate --strict`, checks every skill's frontmatter, lints the shell scripts and runs the hook tests on every push.
- A weekly workflow bumps the project template's pre-commit hooks and opens a PR; Dependabot keeps GitHub Actions current.
- Releases follow semantic versioning; each `vX.Y.Z` tag publishes the CHANGELOG section. Update with `git pull` and restart Claude Code.
- `/alexis:improve` turns your own friction into fixes, and generic ones can come back here as pull requests.

## Security

Skills and hooks run with your permissions. Read what you install. ALEXIS hooks are plain Python you can audit in `plugins/alexis/scripts/`. The real protection is credentials: connect Claude Code with read-only identities and development catalogs. See [SECURITY.md](SECURITY.md).

## Contributing

Issues and pull requests welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
