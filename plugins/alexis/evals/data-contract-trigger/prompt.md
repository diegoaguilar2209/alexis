---
description: A request to protect a shared table from silent breakage should produce a contract and enforcing tests.
tags: [data-contract, trigger]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---

Our gold table sales.orders_daily (one row per order_id, with amount, status in [paid, refunded], updated_at) feeds three dashboards and a forecasting model. It broke twice last month when someone changed a column. How do I make sure this doesn't happen again?
