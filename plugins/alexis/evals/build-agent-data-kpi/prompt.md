---
description: An agent that answers KPI questions for executives should route through governed metrics or a semantic layer, not raw text-to-SQL.
tags: [build-agent, trigger, data-agent]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---

I want to build an agent where our executives ask in plain language things like "what was net revenue by region last quarter?" and it writes SQL against our warehouse and answers. The numbers go into board decks, so they must be right. How should I build it?
