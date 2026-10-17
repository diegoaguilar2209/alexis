# Context engineering

Source: Anthropic, "Effective context engineering for AI agents". Context is a finite attention budget: as tokens grow, recall degrades (context rot). Goal: the smallest set of high-signal tokens that gets the desired behavior.

## System prompt
- Right altitude: specific enough to guide, general enough to give heuristics. Avoid both hard-coded if-else logic and vague "be helpful".
- Sections: role and goal, context, tools guidance, constraints and never-do list, output format. Markdown headers or XML tags.
- Start minimal with the best model, run the evals, add instructions only for observed failures.

## Examples
2–4 diverse, canonical examples of the expected behavior. Do not stuff every edge case as a rule; examples are "pictures worth a thousand words".

## Tools in context
Tool definitions are context too: minimal, non-overlapping set (see tool-design.md). If a human cannot say which tool to use in a situation, the agent cannot either.

## Retrieval
- Just-in-time: keep lightweight identifiers (paths, IDs, queries) and load data with tools when needed, like a person using a file system.
- Hybrid: preload what is always needed (CLAUDE.md-style project notes), explore the rest.
- RAG: chunk by meaning, keep source metadata, rerank, cite sources in the answer; evaluate retrieval separately (recall@k) from generation.

## Long-horizon tasks
- **Compaction:** summarize the history near the limit, keep decisions, open bugs and next steps; drop raw tool outputs first (tool-result clearing).
- **Structured notes:** the agent writes progress to a file (NOTES.md, todo list) outside the context window and re-reads it.
- **Sub-agents:** deep work in a clean context; return a condensed summary (1–2k tokens) to the lead agent.

## Memory
- Session memory (conversation) vs long-term memory (facts across sessions).
- Long-term memory scoped per user and tenant, with provenance, expiry and a way to inspect and delete. Never store secrets or sensitive personal data.
- Treat memory writes as an attack surface (ASI06 memory poisoning): validate what gets stored, and do not let tool output write memory directly.

## Caching
Order the prompt stable → variable (system prompt, tools, examples, then conversation) so prompt caching hits; do not inject timestamps or random IDs into the stable prefix.

## Symptoms → fix
| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Ignores an instruction | Buried in a long prompt or contradicted elsewhere | Shorten, move to a clear section, add an example |
| Calls the wrong tool | Overlapping tools or vague descriptions | Merge or rename, improve descriptions |
| Loops or repeats calls | No feedback on progress, unclear stop condition | Return progress in tool results, add stop conditions and max turns |
| Forgets earlier facts in long sessions | Context rot | Notes file, compaction, sub-agents |
| Invents data | Retrieval missing or answer not grounded | Require citations; "say you don't know" with an example |
