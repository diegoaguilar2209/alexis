---
name: data-contract
description: Use when a table or dataset is consumed by others and must not break silently - define a data contract (schema, keys, nulls, allowed values, freshness SLA, owner) and generate the tests that enforce it in the pipeline. Also when the user asks for data quality rules, schema checks or "make sure this table doesn't break".
argument-hint: "[table or dataset name]"
---

# Data contract

A contract is a promise from the producer of a table to its consumers. It is only real when tests enforce it on every run. Reply in the user's language.

## 1. Gather (read before asking)

Read the table's definition (SQL model, PySpark job, dbt model or DDL) and a sample if a read-only connection exists. Ask only what the code cannot tell you: who consumes it, how fresh it must be, and who owns it.

## 2. Write the contract

Create `contracts/<table>.yaml`:

```yaml
table: <catalog.schema.table>
owner: <team or person>
consumers: [<dashboard, model, team>]
grain: one row per <key columns>
freshness: { column: <updated_at>, max_delay: 26h }
columns:
  - { name: <id>, type: bigint, nullable: false, unique: true }
  - { name: <status>, type: string, nullable: false, allowed: [active, closed] }
  - { name: <amount>, type: decimal(18,2), nullable: false, min: 0 }
checks:
  - { name: row_count_vs_source, rule: "abs(count - source_count) / source_count <= 0.005" }
change_policy: breaking changes (drop/rename/type change) need a new version and consumer sign-off
```

## 3. Enforce it

Generate tests in the stack the project already uses, in this order of preference:
- dbt: `schema.yml` tests (`not_null`, `unique`, `accepted_values`, `dbt_utils.expression_is_true`) and source freshness.
- Databricks: Delta constraints (`CHECK`, `NOT NULL`) for hard rules plus a validation step in the job; Lakeflow expectations if the pipeline uses them.
- Plain Python/SQL: a `tests/contracts/test_<table>.py` that runs the checks read-only and fails with the violated rule.

Wire the tests into CI or the job so a violation stops the run before consumers see bad data.

## 4. Verify

Run the tests once against current data. A contract that fails on day one is a finding, not a test to loosen: report the violations to the user before adjusting anything.

## Rules

- Contract files contain no data samples, credentials or personal data.
- Never relax a rule to make a test pass without the user's explicit decision, recorded in `docs/decisions.md`.
