---
paths:
  - "model/**"
  - "**/*.tmdl"
  - "**/*.pbip"
  - "**/*.pbir"
---

# Power BI rules

- Star schema: facts with keys to dimensions; no bidirectional relationships without a written reason.
- Measures in a `_Measures` table, with display folders and a business description on each.
- DAX: variables for intermediate steps, `DIVIDE` instead of `/`, no calculated columns where a measure works.
- Measure names in business language ("Net Revenue", not "sum_rev_net").
- Commit the PBIP before bulk changes with the modeling MCP.
- Design: follow `/alexis:powerbi-executive` (action titles, one message per page, one accent color).
