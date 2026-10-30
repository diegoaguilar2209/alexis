# <Project name>

## Context

- Goal: <business problem in one line>.
- KPI: <metric> from <baseline> to <target> by <date>.
- End user: <who> consumes it via <dashboard / API / agent / deck>.
- Context: <work | personal | hackathon (deadline)>.

## Stack

- Data platform: <Databricks (Unity Catalog) | BigQuery | Snowflake | Postgres>.
- Languages: Python 3.12, SQL (<dialect>), PySpark.
- Visualization: <Power BI | other>.

## Architecture

- Medallion: bronze (raw) → silver (clean, typed, deduplicated) → gold (business model).
- Catalogs/schemas: `<dev_catalog>` for development. Never write to production from Claude Code.
- Details and diagram: @docs/spec.md

## Conventions

- SQL: snake_case, descriptive CTE names, no `SELECT *` in silver and gold.
- Python: type hints, pure functions for transformations, black + isort + mypy (via pre-commit), logging instead of print.
- Every gold table declares its key and has tests for uniqueness, nulls and row count vs source.
- Commits: `type: description` (feat, fix, refactor, docs, chore, test).

## Commands

- Environment: `uv venv env && source env/bin/activate`
- Dependencies: edit `requirements.in` → `uv pip compile requirements.in -o requirements.txt --python-version 3.12` (same for `requirements-dev.in`) → `uv pip sync requirements.txt requirements-dev.txt`
- Quality: `pre-commit run --all-files`
- Tests: `pytest -q`
- Evals: `python evals/run.py`
- Deploy dev: `databricks bundle deploy -t dev`

## Workflow

1. Spec and plan before code (docs/spec.md, docs/plan.md).
2. Tests and evals before calling anything done.
3. After changing SQL: `sql-reviewer`. After changing an agent, its prompts or tools: `agent-reviewer`. Before publishing numbers: `data-validator`. Before "done": `verifier`.
4. Unattended work: `/alexis:autopilot`. End of session: `/alexis:session-log`.

## Compact instructions

When compacting, keep: current task and plan position, failing test output, decisions taken, files changed.
