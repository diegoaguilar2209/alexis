---
type: llm
---

PASS if the reply asks at most 5 numbered clarifying questions, each one or two lines long, about things not already stated (such as KPI target, users, deadline, data volume or context), and does not ask about facts the user already gave (Postgres, Databricks, Power BI, daily cadence). Stated assumptions are fine and do not count as questions.
FAIL if the reply writes pipeline or DAX code, has more than 5 questions, has questions longer than two lines, or asks about the sources and tools the user already named.
