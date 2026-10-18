---
name: tech-radar
description: Use when the user asks what is new, state of the art, most innovative or best practice right now in AI, agents, LLM tooling, Claude Code or data platforms, or wants to know whether their setup, ALEXIS or a project is falling behind - researches recent primary sources, rates each finding Adopt/Trial/Assess/Hold with evidence, and proposes concrete changes.
argument-hint: "[domain, e.g. 'AI agents', 'Claude Code', 'Databricks', or a project path]"
---

# Tech radar

Purpose: nobody should have to ask for each improvement by name. This skill scans what changed, separates signal from hype, and turns the signal into specific edits. Reply in the user's language.

## 1. Scope

From $ARGUMENTS and the conversation, fix: the domain, the time window (default: last 90 days), and the target to compare against (ALEXIS itself, the current project, or the user's general practice). State it in one line; do not ask unless the domain is unclear.

## 2. Research (primary sources first)

Search in parallel and read, in this order of trust:
1. Vendor engineering blogs, docs and changelogs (Anthropic engineering and docs, Claude Code changelog, OpenAI, Google, Microsoft, AWS, Databricks, dbt Labs, Model Context Protocol spec and blog).
2. Papers with code or reproducible benchmarks (arXiv, conference proceedings).
3. Standards bodies and foundations (Linux Foundation, OWASP, OpenTelemetry).
4. Practitioner write-ups with concrete numbers.
Skip listicles and vendor marketing without evidence. Note when a source sells the thing it praises.

Default checklist for "AI agents": models and pricing, harnesses and SDKs, protocols (MCP, A2A, UI protocols), tool use techniques, context and memory, evals, prompt optimization, retrieval, data agents and semantic layers, security, identity and governance, observability, durable execution, deployment platforms, cost.

## 3. Rate each finding

| Ring | Meaning |
| --- | --- |
| Adopt | Proven with evidence; use by default now |
| Trial | Promising with evidence; use on one real project and measure |
| Assess | Worth understanding; no action yet |
| Hold | Hype, superseded, or risky; avoid or migrate away |

For each: one-line what it is, the evidence (number + source), the ring, and who it matters for. Prefer fewer, well-evidenced findings over a long list.

## 4. Compare and propose

Read the target (for ALEXIS: `plugins/alexis/skills/**`, `agents/`, `templates/`, `README.md`). For every Adopt or Trial finding, say whether the target already covers it. For each gap, propose the exact change: file, section, and the text or code to add. Group by impact.

## 5. Deliver

- Write `docs/radar/<YYYY-MM>-<domain>.md` with the table, the gaps and the sources.
- Apply changes only with the user's approval. When improving ALEXIS itself, add or update eval cases for any changed skill and run them.
- End with the top 3 changes and the sources list.

## Rules

- Every claim carries a source link and a date. No source, no "verified" label.
- No web access (search or fetch fails): still deliver the full radar in the same reply from what you know, with every row marked "unverified — knowledge up to <your cutoff>", and list the 3–5 items most worth verifying first. Never stop with nothing, and do not end with a question.
- Mark preview/beta features as such and say how stable they are.
- Do not chase novelty: a finding replaces existing practice only if its evidence beats what is there.
