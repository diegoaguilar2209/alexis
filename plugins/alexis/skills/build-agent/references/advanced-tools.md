# Advanced tool use and protocols (state as of Oct 2026)

Check the vendor docs before using: several items are beta or in active spec change.

## Many tools: load on demand
- **Tool search** (Claude API, beta `advanced-tool-use-2025-11-20`): mark tools `defer_loading: true`; the model searches (regex, BM25 or custom) and loads only matching definitions. Anthropic reports ~85% less upfront context (77K → 8.7K tokens) and MCP-eval accuracy up from 79.5% to 88.1% on Opus 4.5. Use with 10+ tools, several MCP servers, or >10K tokens of definitions. Claude Code does this natively for MCP tools.
- Same idea elsewhere: expose a small "router" tool set and load the rest by category.

## Many calls: let the model write code
- **Programmatic tool calling**: the model writes a script that calls your tools inside a sandbox; only the script's output returns to context. Anthropic reports 37% fewer tokens on complex research tasks and fewer inference round trips. Use for 3+ dependent calls, large intermediate data, filtering or fan-out over many items.
- **Code execution with MCP**: present MCP servers as code APIs (files the agent can import) instead of loading all definitions; reported example 150K → 2K tokens. Needs a hardened sandbox (see security.md ASI05) — that cost is the trade-off.
- For data agents this is the default shape: query → process in code → return a summary, never stream thousands of rows through the model.

## Tool use examples
Add 1–5 `input_examples` per complex tool (nested objects, many optional parameters, domain conventions). Reported accuracy on complex parameters 72% → 90%.

## MCP specification 2026-07-28
- **Stateless core:** no `initialize` handshake, no `Mcp-Session-Id`; any instance serves any request behind a plain load balancer. Stateful servers return an explicit handle the model passes back.
- **Multi round-trip:** server asks for input by returning `InputRequiredResult` instead of holding an SSE stream (elicitation without sticky sessions).
- **Required `Mcp-Method` / `Mcp-Name` headers** for gateways; `ttlMs` / `cacheScope` for caching lists; W3C Trace Context in `_meta`.
- **Extensions:** **Tasks** (long-running work: `tasks/get|update|cancel`) and **MCP Apps** (sandboxed interactive HTML UI returned by a tool).
- **Auth:** aligned with OAuth 2.0 / OIDC practice (issuer validation, step-up scopes).
- **JSON Schema 2020-12** for tool input/output schemas.
- **Deprecated (12-month window):** Roots, Sampling, Logging. Error "resource not found" moved to `-32602`.
- New servers: build stateless from day one; use `outputSchema` so clients can validate results.

## Agent-to-agent (A2A)
Linux Foundation project, 150+ organizations, integrated in major clouds. MCP connects an agent to tools and data; A2A connects independently deployed agents owned by different teams or vendors (agent cards, long-running tasks). Not needed inside one codebase or one team: a function call or a queue is simpler. A2A is not a security model; identity, authorization and audit still have to be designed.

## Agent UI
- **MCP Apps:** the tool returns an interactive UI (forms, charts) rendered sandboxed in the client.
- **AG-UI:** event protocol between an agent backend and a web frontend (streaming, state sync, human-in-the-loop); CopilotKit and several frameworks implement it.
- **A2UI:** declarative UI descriptions an agent can emit for the client to render.
Pick the one the target client supports; for Teams, Adaptive Cards remain the native option.

## Agent payments
AP2 (Google-led, with mandates signed by the user) and ACP (OpenAI/Stripe agentic commerce) let agents pay under explicit user authorization. Treat as Assess: only relevant if the agent buys or sells, and always behind human-approved mandates and spend limits.

## Skills as a portable format
SKILL.md (folder with frontmatter `name` + `description`, plus scripts and references, loaded by progressive disclosure) is supported natively by Claude Code, OpenAI Codex CLI, GitHub Copilot, Gemini CLI and JetBrains Junie, and through adapters elsewhere. Package domain know-how for an agent as skills, not as an ever-growing system prompt; the Claude Agent SDK loads them like Claude Code.
