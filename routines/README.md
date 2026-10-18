# Routine templates

Routines are Claude Code sessions that run in Anthropic's cloud on a schedule, an API call or a GitHub event, without your laptop ([docs](https://code.claude.com/docs/en/routines.md)). They are in research preview and need a Pro, Max, Team or Enterprise plan.

Create one with `/schedule` in Claude Code (or at claude.ai/code/routines), select the repository, and paste the prompt from the template. Runs use your subscription usage; keep the connector list to what the routine needs.

| Template | Trigger | What it does |
| --- | --- | --- |
| [pr-review.md](pr-review.md) | GitHub: `pull_request.opened`, not draft | Reviews the PR with the data checklist and the `sql-reviewer` subagent |
| [docs-drift.md](docs-drift.md) | Schedule: weekly | Finds docs that no longer match merged changes and opens a PR |
| [post-deploy-check.md](post-deploy-check.md) | API: called by your CD pipeline | Runs smoke checks and validates key tables after a deploy |
| [alexis-radar.md](alexis-radar.md) | Schedule: monthly, on the ALEXIS repo | Runs `/alexis:tech-radar` on AI, agents and data platforms and opens a PR with proposed updates |
| [alexis-upkeep.md](alexis-upkeep.md) | Schedule: weekly, on the ALEXIS repo | Checks Claude Code release notes for changes that affect ALEXIS and opens an issue |

Routines run unattended and cannot ask you anything: every prompt below states its own success criteria and its limits.
