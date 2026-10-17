---
name: metric-definition
description: Use when a KPI or business metric must mean the same thing everywhere - define it once (formula, grain, filters, owner) and trace it from the DAX measure or dashboard to the SQL that computes it, flagging mismatches. Also when two reports show different numbers for the "same" metric.
argument-hint: "[metric name]"
---

# Metric definition

Most "the numbers don't match" problems are two definitions of one metric. This skill makes one definition the source of truth and checks every implementation against it. Reply in the user's language.

## 1. Find every implementation

Search the project for the metric: DAX measures (`.tmdl`, exported measures), SQL views and models, dbt metrics or semantic layer, notebooks, and dashboard specs. List each with its location.

## 2. Write the definition

Add or update `docs/metrics/<metric>.md`:

| Field | Value |
| --- | --- |
| Name | Business name, e.g. "Monthly Churn Rate" |
| Definition | One sentence a non-technical reader understands |
| Formula | Numerator / denominator in plain terms |
| Grain | e.g. per customer per calendar month |
| Filters | Inclusions and exclusions (test accounts, refunds, internal users) |
| Time logic | Calendar vs fiscal, as-of date, late-arriving data handling |
| Owner | Who decides changes |
| Source of truth | The one implementation everything else must match |

## 3. Trace and compare

For each implementation, compare formula, filters, grain and time logic against the definition. Where a read-only connection exists, compute the metric with each implementation for the same period and show the numbers side by side.

Output a table: implementation, location, matches definition (yes/no), difference, value for the test period.

## 4. Fix

Propose changes so every implementation matches the source of truth, with the corrected DAX or SQL. Apply only with the user's approval, and record value-changing fixes in `docs/decisions.md` so consumers know why a number moved.
