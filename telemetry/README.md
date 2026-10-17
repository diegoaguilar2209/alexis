# Usage telemetry

The status line shows the current session and your plan limits. This stack keeps the history: tokens and cost per day, model and tool, sessions and lines changed, so model-routing decisions use data.

```bash
docker compose -f telemetry/docker-compose.yml up -d
source telemetry/claude-otel.env
claude
```

Open Grafana at http://localhost:3000, add a dashboard with Import and use a community Claude Code dashboard (for example ID 25052 or 25340 on grafana.com), pointing it at the Prometheus and Loki data sources already provisioned.

Claude Code's telemetry reference: https://code.claude.com/docs/en/monitoring-usage
Telemetry stays on your machine; nothing here sends data anywhere else. Prompt text is not exported unless you opt in.
