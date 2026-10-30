# ALEXIS

[![CI](https://github.com/diegoaguilar2209/alexis/actions/workflows/ci.yml/badge.svg)](https://github.com/diegoaguilar2209/alexis/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/diegoaguilar2209/alexis)](https://github.com/diegoaguilar2209/alexis/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**A Claude Code plugin that takes data projects from idea to verified delivery** — pipelines, dashboards, AI agents, SQL and executive decks.

[Español](README.es.md)

## Goal

Claude Code is powerful out of the box, but good results depend on the system around it: plan before coding, verify before calling something done, block destructive mistakes, use the right model for each task, and remember decisions between sessions. ALEXIS packages that system for data work so anyone can install it in minutes.

*Alexis* comes from the Greek *alexein*, "to defend": it builds with you and guards you against destructive mistakes. The name is an acronym for **A**gentic **L**ayer for **EX**ecution, **I**nsight and **S**ystems.

## Quick start

```bash
git clone https://github.com/diegoaguilar2209/alexis.git ~/dev/alexis
cd ~/dev/alexis
bash setup/install.sh          # ALEXIS + recommended plugins + tools
bash setup/install.sh --full   # also Azure, GitHub, dbt, Power BI and Databricks plugins
```

Then start a project:

```bash
mkdir ~/dev/churn-model && cd ~/dev/churn-model && git init && claude
```

```text
/alexis:new-project Predict customer churn from transactions and show it in Power BI
/alexis:autopilot      # Claude builds until tests and evals pass
/alexis:session-log    # record decisions and impact when you stop
```

Only want the plugin? `claude plugin marketplace add diegoaguilar2209/alexis` and `claude plugin install alexis@alexis`.

## How it works

```text
 idea ──▶ /alexis:new-project ──▶ spec + repo + CLAUDE.md + evals + plan
                                         │
                                         ▼
          /alexis:autopilot ──▶ build ─▶ test ─▶ fix ─▶ commit   (loops until the goal is met)
                                         │
                       verifier subagent audits with fresh eyes
                                         │
                                         ▼
          /alexis:session-log ──▶ decisions, impact and next steps (repo + Obsidian)

 Always on: safety hook (blocks DROP, force push, prod deploys…) · lint after every edit · status line with usage limits
```

## What's inside

### Skills (slash commands)

| Stage | Command | What it does |
| --- | --- | --- |
| Start | `/alexis:new-project` | Short interview → spec, repo scaffold, CLAUDE.md, evals and plan |
| | `/alexis:validate-idea` | Tests a startup or paid-app idea before you build: customer, who pays, distribution, cheapest experiment |
| | `/alexis:hackathon` | Hackathon playbook: judges → spec → evals → parallel build → audit → demo |
| Build | `/alexis:autopilot` | Works alone toward measurable criteria, with verification and checkpoints |
| | `/alexis:build-agent` | Designs, builds, evaluates, secures and deploys AI agents (pattern, harness, tools, evals, OWASP, Azure/Databricks/AWS/GCP) |
| Data quality | `/alexis:data-contract` | Schema, keys, allowed values and freshness of a shared table, enforced by tests |
| | `/alexis:metric-definition` | One definition per KPI, traced from the DAX measure to the SQL |
| Deliver | `/alexis:powerbi-executive` | Audits and redesigns Power BI reports: model, DAX and consulting-grade design |
| | `/alexis:exec-deck` | Conclusion-first executive presentations with traceable numbers |
| Improve | `/alexis:session-log` | Logs decisions, measurable impact and next steps |
| | `/alexis:improve` | Improves your setup from evidence: friction, repeated corrections, usage |
| | `/alexis:tech-radar` | What's new and what actually works in AI, agents and data platforms, rated Adopt/Trial/Assess/Hold |

### Workflows, subagents and hooks

| Piece | What it does |
| --- | --- |
| `/alexis:audit-model` | Workflow: one reviewer agent per file; each finding is verified by a second agent |
| `/alexis:migrate` | Workflow: one agent per file in its own git worktree, then a checker |
| `verifier` | Subagent: audits finished work with fresh eyes before it is called done |
| `sql-reviewer`, `data-validator`, `agent-reviewer` | Subagents: review SQL, validate data outputs, review an agent before real users. Each runs on a cost-effective model |
| Safety hook | Blocks DROP, TRUNCATE, DELETE/UPDATE without WHERE, prod deploys, force push and cloud deletions, including through MCP |
| Lint hook | After every edit, runs your repo's pre-commit on that file |

### Command-line tools

| Tool | What it does |
| --- | --- |
| `alexis-statusline` | Status line: model, effort, context bar, 5-hour and weekly usage with reset times |
| `alexis-wt` | One git worktree + one tmux window + one Claude Code session per workstream |
| `alexis-goal` | Headless runs toward a goal, with live logs |

## Recommended plugins

`setup/install.sh` also installs plugins we consider important for this way of working. Some are official, some come from the community. Review them before installing, like anything that runs with your permissions.

| Plugin | Source | Why |
| --- | --- | --- |
| `superpowers` | Community ([obra/superpowers](https://github.com/obra/superpowers)) | Proven engineering method: brainstorming, plans, TDD, systematic debugging |
| `data` | Anthropic ([knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)) | Data exploration, analysis, SQL, visualization and validation |
| `document-skills` | Anthropic ([skills](https://github.com/anthropics/skills)) | Word, Excel, PowerPoint and PDF files |
| `pyright-lsp`, `context7`, `security-guidance` | Anthropic official marketplace | Python code intelligence, current library docs, secure-coding guidance |
| With `--full` | Official and vendor marketplaces | Azure, Microsoft Docs, GitHub, PR review, Semgrep, dbt, Power BI authoring, Databricks AI Tools |

## Repository structure

```text
plugins/alexis/
  skills/          One folder per slash command (SKILL.md + references)
  agents/          Subagents: verifier, sql-reviewer, data-validator, agent-reviewer
  workflows/       Multi-agent workflows: audit-model, migrate
  hooks/           Hook wiring (safety before tool calls, lint after edits)
  scripts/         The hooks' code: plain Python you can audit
  templates/project/  What new-project copies into your repo: CLAUDE.md, permissions, rules, pre-commit, CI, evals
  evals/           Eval cases for every skill (claude plugin eval)
setup/             Installers and settings configuration
templates/user/    Starter ~/.claude/CLAUDE.md (your personal preferences)
tools/             alexis-statusline, alexis-wt, alexis-goal
routines/          Cloud routine templates: PR review, docs drift, post-deploy check, monthly radar
telemetry/         Local OpenTelemetry + Prometheus + Loki + Grafana stack for token and cost history
vault/             Obsidian vault starter: long-term memory and career impact log
tests/             Tests for hooks and tools
```

## Requirements and platforms

[Claude Code](https://code.claude.com/docs), Git, Python 3 and bash. Optional: tmux, pre-commit, black, isort, sqlfluff, Databricks CLI.

**Tested on Windows with WSL2 (Ubuntu).** Linux and macOS should work but are not tested yet; `setup/install.ps1` (native Windows) is untested. Reports and fixes are welcome.

## Evals: proof that each skill helps

Every skill ships with eval cases in `plugins/alexis/evals/`. `claude plugin eval` runs them in isolated sessions, checks that the skill fires on natural phrasing (English and Spanish), and grades the output against a rubric, optionally comparing it with the same prompt without ALEXIS.

```bash
cd plugins/alexis
claude plugin eval . --runs 1 --ablation none --judge-model sonnet   # quick check
claude plugin eval . --judge-model sonnet                            # full, with vs. without ALEXIS
```

The suite has already caught real problems: the kickoff skill asked too many questions, and autopilot fired only 1 time in 3 on "I'm stepping away, keep going" until its description was rewritten (now 3 in 3). A GitHub workflow runs the suite on demand or weekly with your `ANTHROPIC_API_KEY` secret.

## Models, tokens and limits

- **Model routing**: subagents and light skills are pinned to cheaper models (`sonnet`, `haiku`). Recommended: `sonnet` for daily work, `opusplan` for complex features (Opus plans, Sonnet executes); lower `/effort` before switching to a bigger model.
- **Meter**: the status line shows context use and, on Pro/Max plans, the 5-hour and weekly usage with reset times. At 80% of the 5-hour window it warns you to save state.
- **When you hit a limit**: on Pro/Max, an open interactive session waits and resumes after the reset (Claude Code v2.1.234+). Keep the terminal open; tmux helps. Headless (`-p`) runs and API keys do not wait.
- **History**: `telemetry/` shows tokens and cost per day, model and tool.

## Staying current

CI validates the plugin (`claude plugin validate --strict`), skill frontmatter, shell scripts and hook tests on every push. Dependabot keeps GitHub Actions current, a weekly workflow updates the project template's pre-commit hooks, and each `vX.Y.Z` tag publishes a release from the [CHANGELOG](CHANGELOG.md). Update with `git pull` and restart Claude Code.

## Security

Skills and hooks run with your permissions: read what you install. The safety hook matches text patterns, so it catches common destructive commands, not every possible one. The real protection is credentials: connect Claude Code with read-only identities and development environments, never production write access. See [SECURITY.md](SECURITY.md).

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

[MIT](LICENSE)
