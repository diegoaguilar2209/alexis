# Deployment

Deploy where users already work. Check current platform docs before building: regions, features and names change often (use the `microsoft-docs` MCP for Azure, Context7 for SDKs).

## Azure (Microsoft Foundry)
- **Foundry Agent Service:** hosted agents with threads, tools and tracing. Build with Microsoft Agent Framework, or bring your own harness as a hosted container (LangGraph, Claude Agent SDK and others).
- **Models:** Azure OpenAI models and Claude models available in Microsoft Foundry; choose per task (see SKILL.md Step 7).
- **Identity:** Microsoft Entra; give the agent its own identity (Entra Agent ID) and call data with on-behalf-of user tokens so each user sees only what they are allowed to.
- **Tools:** MCP servers (Foundry tool catalog or your own), Azure AI Search for RAG, Azure Functions or Logic Apps for actions, Fabric / Databricks for data.
- **Channels:** publish to Microsoft Teams and Microsoft 365 Copilot from Foundry, or through Copilot Studio / Azure Bot Service.
- **Observability:** Foundry tracing (OpenTelemetry) into Application Insights; Foundry evaluations for quality and safety.
- **Infra as code:** Bicep or Terraform; dev and prod in separate resource groups or subscriptions.

### Agent governance (Microsoft)
Agent 365 is becoming the registry and control plane for agents in Microsoft tenants (the agent registry is moving there from Entra). Each agent gets an Entra Agent ID, owner, permissions and lifecycle; expect security teams to require registration before production.

## Observability standard
OpenTelemetry GenAI semantic conventions (still "Development" status, names may change): spans `invoke_agent`, `invoke_workflow`, `execute_tool` (name includes the tool), `gen_ai.*` attributes for provider, model, tokens (including cache and reasoning tokens) and finish reasons; MCP conventions link client and server spans. Emit these instead of custom names so traces work in Datadog, Grafana, Application Insights, Langfuse and others. Content capture is off by default; keep it off for sensitive data.

## Databricks
- Questions over governed tables: Genie space first; expose it to other agents through Databricks managed MCP (Genie, DBSQL, Unity Catalog functions, Vector Search).
- Custom agents: Agent Bricks / Mosaic AI Agent Framework, served with Model Serving, traced with MLflow, evaluated with MLflow agent evaluation.
- Permissions come from Unity Catalog; use the user's identity, not a service principal with broad grants.

## AWS
Bedrock AgentCore (runtime, identity, memory, gateway, observability) with any framework; Bedrock Knowledge Bases for RAG; Guardrails for content filters.

## Google Cloud
Google ADK deployed on Vertex AI Agent Engine; A2A for cross-agent calls; Vertex AI Search for RAG.

## Anthropic
Claude Managed Agents for a hosted loop and sandbox, or the Claude Agent SDK in your own container (Cloud Run, Azure Container Apps, ECS, Kubernetes).

## Works for me, fails for others
The most common enterprise failure. Diagnose in this order:
1. **Identity:** locally the agent runs with the developer's credentials (az login, personal token, admin role); in production it runs with a managed identity or the end user's token that lacks grants. Check which identity each tool call uses and its permissions on each data source.
2. **Data permissions:** row-level security, Unity Catalog grants, SharePoint/Graph permissions or Power BI RLS filter data per user. Test with a real non-admin test user.
3. **Consent and scopes:** Entra app needs admin consent for delegated Graph/API scopes; Teams app needs to be allowed by the tenant policy.
4. **Network:** private endpoints, firewall, VNet integration, allowed IPs; local laptop on VPN reaches what the cloud resource cannot.
5. **Configuration drift:** environment variables, model deployment names, API versions, region availability differ between dev and prod.
6. **Channel differences:** Teams message size and card limits, timeouts on long tool calls (make them async), authentication prompts (SSO) in the channel.
7. **Concurrency and quotas:** tokens-per-minute limits, rate limits per user, shared state between users (memory or thread leakage).
Add a test user and a "runs as" log line to every tool call; most of these become obvious.

## Production checklist
- Separate dev/test/prod; no agent writes to prod without approval.
- Secrets in Key Vault / Secrets Manager / Secret Manager; managed identities.
- Tracing, cost dashboards and alerts (spend, error rate, latency).
- Evals in CI on every prompt/tool/model change; scheduled evals in production.
- Versioned prompts and tools; rollback path.
- Feedback loop from users into the eval set.
- Runbook: how to disable the agent or a single tool fast.
