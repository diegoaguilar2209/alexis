---
name: build-agent
description: Use when the user wants to design, build, debug, evaluate, secure or deploy an AI agent or LLM app with tools - chatbots over data, copilots, RAG assistants, multi-agent systems, MCP servers for an agent, Teams/Slack bots, Azure AI Foundry or Bedrock or Vertex agents. Also when choosing a harness or framework (Claude Agent SDK, LangGraph, Microsoft Agent Framework, Google ADK, OpenAI Agents SDK), or when an agent "works for me but fails for others", loops, hallucinates tool calls or costs too much.
argument-hint: "[what the agent must do, or the problem with an existing agent]"
---

# Build an AI agent

Goal: an agent that does one job reliably, measured by evals, safe against misuse, cheap enough to run, and deployable where its users already are. Reply in the user's language. Read the references only when you reach the step that needs them.

Mindset: the simplest thing that passes the evals wins. Most "agents" should be a workflow; most failures are context or tool design, not the model.

## Step 0. Triage the request

- **New agent** → Steps 1–8 in order.
- **Existing agent misbehaving** → read its code, prompts and tool definitions first, then jump to the matching section: wrong answers or loops → Step 4 (tools) and Step 5 (context); works locally but fails for other users or in the cloud → `references/deployment.md` § "Works for me, fails for others"; too slow or expensive → Step 7; security worry → Step 6. Always end by adding the failure as an eval case (Step 3).
- **Only choosing a framework** → Step 2 and stop.

## Step 1. Spec the job, then pick the pattern

Get these in one round of at most 4 single-ask questions (state assumptions for the rest): the task and who triggers it; the systems it must read or change; where users will talk to it (Teams, web, Slack, API, scheduled); what a wrong action costs.

Write `docs/agent-spec.md`: job in one sentence, users and channel, inputs, outputs, tools with read/write scope, autonomy level (suggest only / act with approval / act alone), success metric, and the hard "never do" list.

Then choose the lightest pattern that can work (details: `references/patterns.md`):

| Need | Pattern |
| --- | --- |
| One call with retrieval or a couple of tools | Augmented LLM (no agent loop) |
| Fixed steps known in advance | Prompt chaining with code gates between steps |
| Different request types need different handling | Routing (cheap model classifies, specialists answer) |
| Independent subtasks, or several opinions needed | Parallelization (sectioning or voting) |
| Subtasks only known at run time | Orchestrator-workers |
| Clear quality bar and useful feedback | Evaluator-optimizer loop |
| Open-ended, steps unpredictable, trusted environment | Autonomous agent loop with guardrails and stop conditions |

Say the chosen pattern and why the simpler ones are not enough, in two lines.

## Step 2. Choose the harness

The harness is everything around the model: the loop, tools, context management, permissions, memory, tracing. Choose by where it must run and what the team can maintain (full matrix: `references/harness-selection.md`):

- Claude models, code/file/shell/OS work, MCP-heavy, want Claude Code's loop as a library → **Claude Agent SDK** (Python/TypeScript). Hosted by Anthropic instead → **Claude Managed Agents**.
- Azure / Microsoft 365 / Teams shop, .NET or Python, enterprise identity → **Microsoft Agent Framework** deployed on **Microsoft Foundry Agent Service** (it also hosts other harnesses, including the Claude Agent SDK).
- Long stateful flows with checkpoints, retries, human approval gates, model-agnostic → **LangGraph**.
- Google Cloud, multi-language, agent-to-agent (A2A) discovery → **Google ADK** on Vertex AI Agent Engine.
- AWS → **Bedrock AgentCore** (runtime, identity, memory, gateway) with any of the above.
- Simple handoffs/triage on OpenAI models → **OpenAI Agents SDK**.
- Questions over governed tables in Databricks → **Genie space** via managed MCP before writing any agent code.
- Hackathon or demo in hours → the harness the user already knows; never learn a new one under a deadline.

Do not mix two orchestration frameworks in one agent. Record the choice in `docs/decisions.md` with the rejected options.

## Step 3. Evals before code

Create `evals/agent-cases.yaml` from `${CLAUDE_PLUGIN_ROOT}/templates/project/evals/agent-cases.yaml`: at least 10 realistic multi-step cases — happy paths, ambiguous requests, missing data, a request it must refuse, a prompt-injection attempt inside tool output, and one case per tool. Each case states the expected outcome and the checks (final answer, tools called, tools NOT called, max turns, max cost). How to grade: `references/agent-evals.md`.

Run the baseline (even a stub) so every later change is measured, not guessed.

## Step 4. Design the tools (the agent-computer interface)

Tools are the agent's UI; spend more time here than on the prompt. Rules (full guide: `references/tool-design.md`):

1. Few tools that match whole tasks (`schedule_meeting`, not `list_users` + `list_events` + `create_event`).
2. Namespaced, unambiguous names (`crm_search_customers`); descriptions written like docs for a new hire: when to use it, when not, each parameter with an example.
3. Return meaningful, compact context: names over UUIDs, a `response_format` (concise/detailed) option, pagination and truncation with a hint on how to get more.
4. Errors that teach: say what was wrong and what to try next.
5. Poka-yoke: make wrong calls impossible (absolute paths, enums, validated IDs, dry-run for writes).
6. Read and write tools separated; every write tool idempotent and confirmable.
7. Expose tools through MCP when more than one client will use them; keep them in-process when only this agent does.

## Step 5. Engineer the context

Context is a finite attention budget (guide: `references/context-engineering.md`):

- System prompt at the right altitude: role, goal, constraints, output format, in clear sections. No brittle if-else lists, no vague platitudes.
- 2–4 diverse canonical examples beat a list of edge-case rules.
- Just-in-time retrieval: give the agent identifiers and search tools instead of pasting whole documents.
- Long tasks: compaction, a structured notes file the agent keeps updated, and sub-agents that return condensed summaries.
- Memory only for what must survive sessions, scoped per user, with a way to inspect and delete it.

## Step 6. Secure it

Treat every model input that a third party can influence (web pages, emails, documents, tool results, other agents) as untrusted. Map the design against the OWASP Top 10 for Agentic Applications (`references/security.md`) and apply at minimum:

- Least privilege per tool, per user: the agent acts with the end user's identity (on-behalf-of), never a shared admin credential.
- Deterministic guardrails outside the model: allowlists, permission rules, hooks, output validation, rate and spend limits. A prompt is not a security control.
- Human approval for irreversible or external actions (payments, emails, deletes, production writes).
- Sandboxed code execution, no network unless needed.
- Secrets only in a vault or environment, never in prompts, logs or traces.
- Log every tool call with user, inputs and outcome.

## Step 7. Cost, latency and models

- Route by difficulty: small fast model for classification, extraction and routing; strong model only for planning and hard reasoning.
- Prompt caching for the stable prefix (system prompt, tool definitions, examples).
- Cap turns, tokens and spend per request; return a partial answer with a clear message when a cap is hit.
- Measure cost and latency per eval case and keep them in the eval report.

## Step 8. Deploy, observe, improve

Deploy where users already are (guide: `references/deployment.md`, including Azure Foundry → Teams/M365 Copilot, Databricks Genie/MCP, AWS and GCP paths). Before calling it done:

- Tracing on (OpenTelemetry or the platform's native tracing): every turn, tool call, tokens and cost.
- A feedback signal (thumbs, correction) that flows back into `evals/agent-cases.yaml`.
- Versioned prompts and tools; a change ships only if the eval score does not drop.
- Ask the `agent-reviewer` subagent for an independent review of the design, tools and security before the first real users.

## Close

Report: pattern and harness with reasons, files created, eval score (with cost and latency), open risks, and the exact next step. Keep `docs/agent-spec.md` and `docs/decisions.md` current.

## Rules

- No real customer or employer data in prompts, examples, evals or traces committed to a repo; use synthetic data.
- Never give an agent write access to production without human approval in the loop and the user's explicit decision.
- Verify framework APIs against current docs (Context7 or the vendor docs) before writing code: these SDKs change monthly.
