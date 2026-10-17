---
description: DAX with known anti-patterns should be audited and fixed.
tags: [powerbi, trigger]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---

Can you review my Power BI measures and tell me how to make this report executive-grade? Here they are:

Margin % = ([Revenue] - [Cost]) / [Revenue]
Revenue LY = CALCULATE([Revenue], FILTER(ALL(Sales), Sales[Year] = 2025))
Safe Ratio = IFERROR([Orders] / [Visits], 0)

I also have a calculated column Sales[MarginPct] = (Sales[Amount] - Sales[Cost]) / Sales[Amount], and my page title is just "Sales".
