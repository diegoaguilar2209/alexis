---
type: llm
---

PASS if the reply warns that raw text-to-SQL can return plausible but wrong numbers and recommends routing accuracy-critical questions through governed metric definitions or a semantic layer (e.g. dbt Semantic Layer, metric views, Genie with curated definitions, Power BI semantic model), with text-to-SQL only as a labeled fallback; and includes evaluation with known-answer questions plus read-only, per-user permissions.
FAIL if it designs free text-to-SQL as the main path for board numbers without a semantic layer or governed metrics.
