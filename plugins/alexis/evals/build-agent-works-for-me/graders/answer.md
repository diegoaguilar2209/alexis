---
type: llm
---

PASS if the reply puts identity and permissions first (locally it runs with the developer's credentials; for colleagues it runs with a managed identity or their own token lacking grants, RLS or consent), gives an ordered diagnosis that also covers at least two of: Entra consent/scopes, network/private endpoints, configuration differences between environments, Teams channel limits or timeouts, and proposes a concrete check such as testing with a non-admin test user or logging which identity each tool call uses.
FAIL if it gives generic debugging advice without the identity/permissions angle.
