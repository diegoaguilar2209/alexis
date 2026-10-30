# My Claude Code preferences

Copied to `~/.claude/CLAUDE.md` by `setup/install.sh`. Applies to every project. Keep it under ~120 lines: everything here is loaded on every request. Fill the `<...>` placeholders and delete what does not apply.

## About me
- Role: <e.g. analytics engineer / data architect, N years in <industry>>.
- Stack: <e.g. Python, SQL, PySpark, Databricks, Power BI, BigQuery, AWS>.
- Language: answer in <Spanish / English / ...>; code, comments and docs in <language>, unless the repo already uses another.

## Environment
- <e.g. WSL2 (Ubuntu) + vim + tmux>. Terminal first; do not assume an IDE or GUI.
- Parallel work: one tmux window per git worktree (`alexis-wt`).

## How to work with me
- Direct and concise: answer first, no preamble, no recap of what you did.
- Make reasonable decisions and tell me which ones; ask only when a decision is irreversible or changes scope.
- If what I ask is a bad idea, say so and why.
- Verify by running things, not by assuming. Never claim something passes without showing the output.

## My conventions (respect them)
- Python: virtualenv `env/`; dependencies with uv (`requirements.in` → `uv pip compile` → `uv pip sync`); never edit `requirements.txt` by hand or `pip install` loosely.
- Formatting: black + isort (black profile) + pyupgrade; types with mypy; enforced by pre-commit.
- Config: `.env` per environment for services; versions always pinned, never `latest`.
- Secrets never in Git: `.secrets/*.example` as templates.
- Comments explain why, not what.
- Commits: `type: description` (feat, fix, refactor, docs, chore, test).

## Quality bar
- Tests and evals before "done"; CI runs pre-commit and tests on every push.
- Large files (models, datasets) out of Git (LFS or releases).
- Before committing, check for AI copy-paste leftovers (citation markers, text from another conversation).

## Models and tokens
- Default `sonnet` for daily work; `opusplan` (Opus plans, Sonnet executes) for complex features; `opus` or `fable` only for the hardest problems. Lower `/effort` before switching to a bigger model.
- Exploration, log reading and test runs go to subagents so verbose output stays out of the main context.
- `/clear` between unrelated tasks; `/compact <what to keep>` in long ones.
- Prefer CLIs (`gh`, `az`, `gcloud`, `databricks`) over MCP servers when both work; disable MCP servers I am not using.
- Watch the status line: context %, 5-hour and weekly plan usage. Plan heavy parallel work right after a 5-hour reset.

## ALEXIS
- New project: `/alexis:new-project`. Unattended build: `/alexis:autopilot`. Hackathon: `/alexis:hackathon`.
- Shared tables: `/alexis:data-contract`. KPIs that disagree: `/alexis:metric-definition`. Many files at once: `/alexis:migrate`, `/alexis:audit-model`.
- Power BI review/redesign: `/alexis:powerbi-executive`. Executive deck: `/alexis:exec-deck`. Idea to sell: `/alexis:validate-idea`.
- End of session: `/alexis:session-log`. Improve this setup: `/alexis:improve`.

## Safety (non-negotiable)
- Never write to or delete in production. Dev or local environments only.
- Never put employer or client data, credentials or internal names in personal repos or the personal vault.
- Third-party skills, plugins or MCP servers: official sources or reviewed before installing.

## Second brain
- ALEXIS_VAULT: <path to your Obsidian vault, e.g. /mnt/c/Users/<you>/Obsidian/Brain>
- Layout: 0-Inbox, 1-Projects, 2-Areas (Career/Impact.md), 3-Ideas, 4-Resources, 5-Archive.
- Before proposing something new, check the vault for an earlier note or decision on the topic.
