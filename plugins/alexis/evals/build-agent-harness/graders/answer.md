---
type: llm
---

PASS if the reply recommends a concrete approach that fits Azure + Databricks + Teams (for example a Databricks Genie space or managed MCP for the data, plus Microsoft Foundry Agent Service / Microsoft Agent Framework or Copilot Studio to publish in Teams), explains why over at least one alternative, and addresses that each user must query with their own identity/permissions. It should also mention evals or security (prompt injection, least privilege) as part of building it.
FAIL if it only lists frameworks without choosing, ignores Teams or Databricks, or proposes a shared admin credential.
