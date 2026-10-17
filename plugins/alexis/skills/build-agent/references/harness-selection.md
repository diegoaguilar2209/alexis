# Harness selection

A harness is the runtime around the model: agent loop, tool calling, context management (compaction, memory), permissions, sessions, tracing, deployment. The model is interchangeable more often than the harness; pick the harness for where it runs and who maintains it.

These SDKs change monthly. Confirm current APIs with Context7 or the vendor docs before writing code.

## Matrix

| Harness | Languages | Strengths | Weak spots | Best fit |
| --- | --- | --- | --- | --- |
| Claude Agent SDK | Python, TypeScript | Claude Code's loop as a library: built-in file/shell/web tools, hooks, subagents, MCP, permissions, sessions, skills and plugins | Claude models only; you operate the process | Coding, data and OS-level agents; MCP-heavy agents; reusing Claude Code skills in production |
| Claude Managed Agents | Any (REST, SDKs, `ant` CLI) | Anthropic hosts the loop and sandbox (or self-hosted sandbox) | Less control over the runtime | Teams that want a hosted Claude agent without operating infra |
| Claude API + tool runner | All client SDK languages | Full control, minimal dependencies | You build the loop, memory and tracing | Augmented LLM and simple workflows |
| Microsoft Agent Framework | .NET, Python | Successor of Semantic Kernel + AutoGen; MCP and A2A; orchestration patterns; human-in-the-loop; Azure integration | Group-chat patterns are token-hungry; leans on Azure | Azure / M365 / Teams organizations |
| Microsoft Foundry Agent Service | Hosting platform | Hosted agents, bring-your-own harness (incl. Claude Agent SDK, LangGraph), Entra Agent ID, MCP tool catalog, publish to Teams and M365 Copilot | Azure-only; region/feature availability varies | Enterprise deployment with identity and governance |
| LangGraph | Python, TypeScript | Explicit state graph, checkpointing, crash recovery, time travel, approval interrupts; LangSmith tracing; model-agnostic | Upfront graph design; overkill for simple agents | Long-running stateful workflows with branches and approvals |
| Google ADK | Python, TypeScript, Java, Go | Native A2A with agent cards, OpenTelemetry, Vertex AI Agent Engine deploy | Strong GCP gravity | GCP shops, multi-language teams, cross-vendor agents |
| OpenAI Agents SDK | Python, TypeScript | Lightweight handoffs, parallel guardrails, built-in tracing | Little state persistence; linear handoffs | Triage and routing on OpenAI models |
| AWS Bedrock AgentCore | Platform (any framework) | Runtime, identity, memory, gateway (tools to MCP), observability | AWS-only | Deploying any of the above on AWS |
| Databricks Genie / Agent Bricks | Platform | Natural-language questions over Unity Catalog with governance; managed MCP servers (Genie, DBSQL, UC functions, vector search) | Scope limited to Databricks data | "Ask the data" agents over governed tables |
| CrewAI, Pydantic AI, smolagents | Python | Fast prototypes (CrewAI), typed outputs (Pydantic AI), tiny code agents (smolagents) | Less control or persistence for production | Prototypes; Pydantic AI as a typed component inside another orchestrator |

## Questions that decide it
1. Where must it run (Azure, AWS, GCP, Databricks, on-prem, a laptop)? The platform usually decides the hosting.
2. Which models are allowed by the organization?
3. Does it need durable state across hours or days, with approvals? → LangGraph or a platform with durable execution.
4. Does it mostly read/write files, run code or use many MCP servers? → Claude Agent SDK.
5. What language does the team maintain?
6. Who operates it in production?

## Rule
One orchestration framework per agent. Wrapping a framework inside another doubles the failure modes and the tracing gaps. Mixing at the protocol level is fine: MCP for tools, A2A between independently deployed agents.

## Licensing note
Products built on the Claude Agent SDK must use API-key style authentication (Claude API, Bedrock, Vertex AI, Microsoft Foundry), not claude.ai consumer login or its rate limits.
