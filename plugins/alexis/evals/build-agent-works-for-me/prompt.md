---
description: An agent that works locally but fails for other users should get an identity/permissions-first diagnosis.
tags: [build-agent, trigger, debug]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---

I built an agent in Azure AI Foundry that queries our SQL data and answers questions. It works perfectly when I test it, but when my colleagues use it from Teams it says it can't find any data or returns errors. What's going on and how do I fix it?
