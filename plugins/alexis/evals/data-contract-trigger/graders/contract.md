---
type: llm
---

PASS if the reply proposes a written contract for sales.orders_daily covering the key (order_id unique and not null), allowed values for status, a freshness rule, an owner or change policy for breaking changes, and tests that enforce it automatically in the pipeline or CI.
FAIL if it only gives general advice without concrete rules for this table, or has no automated enforcement.
