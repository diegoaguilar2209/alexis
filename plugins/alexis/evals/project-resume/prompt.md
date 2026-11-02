---
description: Continuing a project whose plan is already approved should resume building without re-asking the kickoff questions.
tags: [project, resume, autonomy]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---

Me voy un rato, sigue tú con el proyecto donde quedó.

Este es mi docs/plan.md (la spec ya la aprobé el 30 de octubre):

Phase: build

## Milestone 1: ingestion
- [x] Schema for raw transactions (verify: pytest -q tests/schema)
- [ ] Daily loader (verify: pytest -q tests/loader)
- [ ] Dedup step (verify: pytest -q tests/dedup)

## Milestone 2: gold table
- [ ] Fraud rate by merchant (verify: pytest -q tests/gold)
