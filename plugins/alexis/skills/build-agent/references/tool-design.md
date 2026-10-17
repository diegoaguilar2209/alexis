# Tool design (agent-computer interface)

Source: Anthropic, "Writing effective tools for agents" and "Building effective agents" (appendix on tools). Tools are a contract between a deterministic system and a non-deterministic agent: design them for the agent, not as thin wrappers over an API.

## Principles
1. **Choose the right tools.** Fewer, higher-impact tools. Build the tool a person would want for the whole task: `search_logs(query, around_event)` instead of `read_logs`; `get_customer_context(id)` instead of three lookups.
2. **Namespace.** Group by service and resource: `asana_projects_search`, `jira_issues_create`. Prevents the agent from confusing similar tools across servers.
3. **Return meaningful context.** Natural-language names and readable fields over UUIDs and internal codes. Drop low-signal fields (mime types, thumbnails).
4. **Response format option.** `response_format: "concise" | "detailed"` lets the agent choose the token cost; concise for browsing, detailed when it needs IDs for a follow-up call.
5. **Token efficiency.** Pagination, filtering, range selection and truncation with sensible defaults; when truncated, tell the agent how to narrow the query.
6. **Actionable errors.** Not a stack trace: "date must be YYYY-MM-DD; got 03/10. Example: 2026-03-10."
7. **Prompt-engineer descriptions.** Write like onboarding a new teammate: purpose, when to use and not use it, each parameter with type, format and example, side effects, and what it returns. Unambiguous parameter names (`user_id`, not `user`).
8. **Evaluate tools with realistic tasks.** Multi-step tasks that need several calls; read the transcripts for confusion (wrong tool, redundant calls, bad parameters) and fix the tool, then re-run.

## Poka-yoke (mistake-proofing)
- Absolute paths instead of relative ones.
- Enums for closed sets; validated IDs; ranges with limits.
- Writes support `dry_run: true` and return what would change.
- Idempotency keys for writes that might be retried.
- Destructive operations need an explicit confirmation parameter and, for production, a human.

## Format choices
Pick formats close to what models see in natural text: Markdown or simple JSON in responses; avoid formats that need escaping or counting (diff line numbers, JSON-in-strings for code).

## MCP or in-process
- MCP server: tools reused by several agents or clients (Claude Code, Foundry, Copilot Studio), or owned by another team. Use `mcp-builder` to scaffold, OAuth for user identity, and read-only scopes by default.
- In-process tools: used only by this agent, latency-sensitive, or needing in-memory state.

## Description template
```
<namespace>_<verb>_<object>
Purpose: <one sentence>.
Use when: <situations>. Do not use for: <situations + which tool instead>.
Parameters:
  - <name> (<type>, required|optional, default <x>): <meaning>. Example: <value>.
Returns: <shape, concise vs detailed>.
Side effects: <none | writes X; requires confirm=true>.
Errors: <common errors and how to fix the call>.
```

## Review checklist
- Could a new hire use each tool from its description alone?
- Any two tools the agent could confuse? Merge or rename.
- Largest possible response under ~25k tokens with defaults?
- Every write tool: dry run, idempotent, logged, least privilege?
