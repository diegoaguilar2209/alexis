# Agent security

Prompt injection remains the top risk for LLM apps in OWASP's 2026 lists. An agent with tools turns a bad answer into a bad action. Design so that a fully manipulated model still cannot do serious harm.

## OWASP Top 10 for Agentic Applications (2026) → controls

| ID | Risk | Controls |
| --- | --- | --- |
| ASI01 | Agent goal hijack (instructions hidden in data, emails, pages, tool output) | Treat external content as data; separate untrusted content in the prompt; no write tools in the same turn as untrusted content without approval; output validation |
| ASI02 | Tool misuse and exploitation | Least-privilege tools, parameter validation, allowlists, dry runs, rate limits, approval for destructive calls |
| ASI03 | Identity and privilege abuse | On-behalf-of user identity, per-agent identity (e.g. Entra Agent ID), short-lived scoped tokens, no shared admin credentials |
| ASI04 | Agentic supply chain (models, MCP servers, tool definitions, RAG sources) | Only official or reviewed MCP servers and packages, pinned versions, review tool descriptions for hidden instructions, signed artifacts |
| ASI05 | Unexpected code execution | Sandbox (container, no network by default, resource limits), never `eval` model output on the host |
| ASI06 | Memory and context poisoning | Validate memory writes, provenance on stored facts, per-user isolation, expiry, admin review |
| ASI07 | Insecure inter-agent communication | Authenticated and signed A2A messages, mutual TLS, no privilege inheritance across agents |
| ASI08 | Cascading failures | Timeouts, retries with backoff, circuit breakers, budgets per request, fail closed |
| ASI09 | Human-agent trust exploitation | Show evidence and sources with each proposed action, clear diff of what will change, no "approve all" defaults |
| ASI10 | Rogue agents (drift from purpose) | Narrow scope, monitoring of actions against the spec, kill switch, periodic eval runs in production |

## Must-haves before real users
- Deterministic guardrails outside the model (permission rules, hooks, policy engine). A system prompt is not a control.
- Human approval for irreversible, external or financial actions.
- Data access filtered by the end user's permissions at the source (row-level security, Unity Catalog grants), not by the prompt.
- Secrets in a vault or managed identity; never in prompts, logs, traces or eval files.
- PII handling: minimize what enters context, redact in logs, respect retention.
- Audit log of every tool call: user, agent, tool, parameters, result, timestamp.
- Red-team eval cases: injection in documents, in tool output, in user input; data exfiltration attempts (links, images, encoded text); privilege escalation.

## Lethal trifecta check
If an agent has (1) access to private data, (2) exposure to untrusted content and (3) a way to send data out (web requests, email, links), an injection can exfiltrate data. Remove at least one of the three, or put approval in front of the outbound channel.
