---
paths:
  - "**/*.sql"
---

# SQL rules

- Declare the grain in a comment at the top: `-- grain: 1 row per <key>`.
- CTEs named for what they do (`active_customers`, not `t1`).
- No `SELECT *` outside bronze.
- Every JOIN states the expected cardinality in a comment and is validated (no row duplication).
- Filter on the partition column when the table is partitioned.
- Dates in UTC unless the spec says otherwise; cut-off date as a parameter, never `current_date()` inside gold logic.
