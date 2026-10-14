---
name: new-project
description: Kick off a new data project (pipeline, dashboard, agent, analysis, platform or hackathon) from a plain-language idea - short interview, spec, repo scaffold, CLAUDE.md, evals and plan. Use when the user says they are starting a new project or runs /alexis:new-project.
argument-hint: "[short project description]"
---

# New data project

Goal: go from "I have an idea" to a repo ready to build, with spec, plan and evals, in under 20 minutes. No product code in this phase. Reply in the user's language.

## Step 1. Understand (one round of questions)

Read what the user already said ($ARGUMENTS and the conversation). Ask ONLY what is missing, in a single message, at most 5 questions, from this list:

1. Business problem and the KPI that must move (with a number if one exists).
2. End user and how they consume the result (dashboard, API, chat agent, deck, table).
3. Context: work, personal, course or hackathon (deadline and judging criteria).
4. Data: sources, volume, frequency, platform (Databricks, BigQuery, Snowflake, Postgres, files).
5. Deliverables and date.

If the description already answers something, do not ask it. For a hackathon, also ask for the rules and judging criteria. If the project is meant to make money and has not gone through `/alexis:validate-idea`, suggest it before the spec.

## Step 2. Classify and pick an archetype

Classify into one or more: `pipeline`, `dashboard`, `agent`, `analysis`, `platform`, `hackathon`. Say it in one line with the reason.

Recommend only the tools that apply (check `/plugin` and `/mcp` for what is already installed):

| Archetype | Skills / plugins | MCP |
| --- | --- | --- |
| pipeline | Databricks AI Tools (bundles, pipelines, jobs, Unity Catalog), dbt agent skills | Databricks SQL |
| dashboard | `/alexis:powerbi-executive`, `data:build-dashboard`, Microsoft `powerbi-authoring` | Power BI Modeling MCP |
| agent | Databricks Genie/apps skills, `mcp-builder` | Databricks Genie / Unity Catalog functions |
| analysis | `data:explore-data`, `data:analyze`, `data:statistical-analysis`, `data:validate-data` | The data platform's MCP |
| platform | The infrastructure conventions in the user's CLAUDE.md | AWS / Azure / GCP MCP if it deploys to the cloud |
| hackathon | `/alexis:hackathon` | The minimum needed |

## Step 3. Repo scaffold

If there is no git repo, run `git init` first (pre-commit needs it). Then copy `${CLAUDE_PLUGIN_ROOT}/templates/project/` into the current directory without overwriting existing files, and fill every `<...>` placeholder with what you know:

- `CLAUDE.md`: context, architecture, conventions, commands. Max 150 lines.
- `docs/spec.md`: the full spec (Step 4).
- `docs/decisions.md`: first entry with the architecture decision.
- `docs/impact.md`: the KPI baseline row.
- `evals/cases.md`: at least 5 cases with input and expected result.
- `.claude/settings.json`: deterministic permissions against production and secrets.
- `.claude/rules/`: keep only the rules for this project's stack; delete the rest.
- `.mcp.json.example`: copy to `.mcp.json` with only the servers this project uses; credentials always via environment variables.
- `.gitignore`, `.pre-commit-config.yaml`, `.github/workflows/ci.yml`: run `pre-commit install`.
- `requirements.in` / `requirements-dev.in` (Python projects): create the `env/` virtualenv, install pip-tools, add direct dependencies to the `.in` files, compile with `pip-compile`, install with `pip-sync`. Never a loose `pip install`.

Suggested layout per archetype:

- pipeline: `src/`, `sql/{bronze,silver,gold}/`, `tests/`, `resources/` (bundles)
- dashboard: `model/` (PBIP/TMDL), `sql/`, `docs/kpis.md`
- agent: `agent/`, `tools/`, `prompts/`, `evals/`
- analysis: `notebooks/`, `sql/`, `outputs/`
- platform (repo named `<layer>-<technology>`): one parameterized `docker-compose.yml`, `.env.local`, `.env.example`, `config/`, `docker/`, `ansible/`, `docs/{architecture,runbook}.md`, `tests/smoke.sh`

## Step 4. Spec (docs/spec.md)

Write it with the user, not for them: propose each section and adjust with their answer.

1. Problem and target KPI (baseline → goal).
2. Users and how they consume the result.
3. In scope and out of scope (explicit).
4. Data: sources, grain, keys, known quality issues.
5. Architecture (Mermaid diagram).
6. Measurable acceptance criteria.
7. Risks and assumptions.

## Step 5. Plan and start

1. If Superpowers is installed, use its `writing-plans` skill on the spec; otherwise write `docs/plan.md` with small tasks, each with its verification command.
2. First commit with the scaffold: `chore: project scaffold` (let pre-commit validate it).
3. If the plan has independent workstreams, suggest opening them in parallel with `alexis-wt <stream> "<task>"`.
4. To build unattended, suggest `/alexis:autopilot` with the plan and the evals.
5. Close with: archetype, files created, the first 3 tasks and any missing plugin/MCP with its exact install command.

## Rules

- Existing or team repo: do not impose your own pre-commit, CI or layout; respect the repo's standards and propose only what is missing.
- Work repos: never copy data, sensitive table names or credentials into personal repos; MCP servers read-only with the user's own identity.
- No product code in this skill. End at the plan.
