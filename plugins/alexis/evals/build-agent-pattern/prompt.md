---
description: A request that a fixed workflow solves should not get an over-engineered multi-agent design.
tags: [build-agent, trigger, pattern]
max_turns: 8
allowed_tools: [Read, Glob, Grep, Skill]
---

I want to build a multi-agent AI system for our support team: every incoming ticket should be classified into billing, technical or account, and then answered with a draft reply using our help-center articles. A human approves each reply before it is sent. How should I design the agents?
