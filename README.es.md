# ALEXIS

**A**gentic **L**ayer for **EX**ecution, **I**nsight and **S**ystems: un sistema opinado para Claude Code que lleva soluciones de data de la idea a la entrega verificada.

*Alexis* viene del griego *alexein*, "defender": construye contigo y te protege de errores destructivos.

[English](README.md)

## Por qué

Claude Code es potente de fábrica. Lo que separa un gran resultado de uno promedio es el sistema alrededor: un método que planifica antes de programar, verificación que Claude no puede saltarse, guardrails, el modelo correcto para cada tarea y memoria entre sesiones. ALEXIS empaqueta ese sistema para trabajo de data (pipelines, dashboards, agentes, SQL y presentaciones ejecutivas) para instalarlo en minutos y adaptarlo.

## Qué incluye

| Pieza | Qué hace |
| --- | --- |
| `/alexis:new-project` | Cuentas tu idea → entrevista breve → spec, estructura del repo, CLAUDE.md, evals y plan |
| `/alexis:autopilot` | Claude construye, prueba, corrige e itera solo hasta cumplir criterios medibles (`/goal` + verificación + checkpoints) |
| `/alexis:hackathon` | Método de los ganadores de hackatones de Claude Code: jurado → spec → evals → paralelo → auditoría → demo |
| `/alexis:powerbi-executive` | Audita y rediseña reportes de Power BI: modelo, DAX, tablas y diseño de nivel consultora, con archivo de tema |
| `/alexis:build-agent` | Diseña, construye y despliega agentes de IA: patrón (workflow vs agente), elección de harness (Claude Agent SDK, Microsoft Agent Framework, LangGraph, ADK...), diseño de herramientas, ingeniería de contexto, evals de agentes, seguridad OWASP agéntica, despliegue (Azure Foundry → Teams, Databricks Genie, AWS, GCP) y diagnóstico de "a mí me funciona, a otros no" |
| `/alexis:data-contract` | Esquema, llaves, valores permitidos y frescura de una tabla compartida, con tests que lo hacen cumplir |
| `/alexis:metric-definition` | Una sola definición por KPI, trazada de la medida DAX al SQL |
| `/alexis:exec-deck` | Presentaciones ejecutivas con la conclusión primero y números trazables |
| `/alexis:validate-idea` | Filtra ideas de startup o apps pagadas antes de construir |
| `/alexis:session-log` | Registra decisiones, impacto medible y próximos pasos al cerrar la sesión |
| `/alexis:improve` | Mejora tu configuración a partir de evidencia |
| Workflows | `/alexis:audit-model` y `/alexis:migrate`: decenas de agentes en paralelo con verificación cruzada |
| Evals | Cada skill tiene casos que se corren con `claude plugin eval`: si se activa con frases naturales y si cumple lo que promete |
| Rutinas | Plantillas de rutinas en la nube: revisión de PR, documentación desactualizada, chequeo post-deploy |
| Telemetría | Stack local OpenTelemetry + Grafana con el historial de tokens y costo |
| Subagentes | `verifier` (auditoría con ojos frescos), `sql-reviewer`, `data-validator`, `agent-reviewer`, cada uno con un modelo costo-eficiente |
| Seguridad | Permisos deterministas + hook que bloquea DROP, TRUNCATE, DELETE/UPDATE sin WHERE, deploys a prod, force push y borrados en la nube, también vía MCP |
| Calidad | Tras cada edición corre el pre-commit de tu repo sobre ese archivo; plantilla con pre-commit, pip-tools y CI |
| `alexis-statusline` | Modelo, esfuerzo, barra de contexto, **uso de 5 horas y semanal con hora de reinicio**, costo de la sesión |
| `alexis-wt` | Un worktree + una ventana de tmux + una sesión de Claude Code por frente |
| `alexis-goal` | Ejecuciones headless hacia un objetivo con logs en vivo |
| Bóveda de Obsidian | Memoria de largo plazo y registro de impacto profesional |

## Instalación

```bash
git clone https://github.com/diegoaguilar2209/alexis.git
cd alexis
bash setup/install.sh          # base
bash setup/install.sh --full   # + Azure, Microsoft Docs, GitHub, dbt, Power BI, Databricks
```

Luego completa la sección "About me" de `~/.claude/CLAUDE.md` e indica el idioma en que quieres las respuestas.

## Tokens, modelos y límites

- **Ruteo de modelos**: subagentes y skills livianas usan modelos más baratos (`sonnet`, `haiku`). Recomendado: `sonnet` en el día a día, `opusplan` para funcionalidades complejas y bajar `/effort` antes de subir de modelo.
- **Medidor**: el status line muestra el contexto usado y, en planes Pro/Max, el uso de la ventana de **5 horas** y la **semanal** con su hora de reinicio. `/usage` muestra qué consume más.
- **Si se acaba el límite**: en Pro/Max, Claude Code espera en la sesión abierta y continúa la tarea solo cuando el límite se reinicia (sesiones interactivas, v2.1.234+). Deja la terminal abierta (tmux ayuda). Con `/usage-credits` puedes seguir con uso pagado. Las ejecuciones headless (`-p`) y las API keys no esperan.

El resto de la documentación está en el [README en inglés](README.md).
