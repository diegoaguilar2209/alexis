# ALEXIS

[![CI](https://github.com/diegoaguilar2209/alexis/actions/workflows/ci.yml/badge.svg)](https://github.com/diegoaguilar2209/alexis/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/diegoaguilar2209/alexis)](https://github.com/diegoaguilar2209/alexis/releases)
[![Licencia: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Un plugin de Claude Code que lleva proyectos de datos de la idea a la entrega verificada**: pipelines, dashboards, agentes de IA, SQL y presentaciones ejecutivas.

[English](README.md)

## Objetivo

Claude Code es potente de fábrica, pero los buenos resultados dependen del sistema que lo rodea: planificar antes de programar, verificar antes de dar algo por terminado, bloquear errores destructivos, usar el modelo correcto para cada tarea y recordar decisiones entre sesiones. ALEXIS empaqueta ese sistema para trabajo de datos, para que cualquiera lo instale en minutos.

*Alexis* viene del griego *alexein*, "defender": construye contigo y te protege de errores destructivos. El nombre es un acrónimo de **A**gentic **L**ayer for **EX**ecution, **I**nsight and **S**ystems.

## Inicio rápido

```bash
git clone https://github.com/diegoaguilar2209/alexis.git ~/dev/alexis
cd ~/dev/alexis
bash setup/install.sh          # ALEXIS + plugins recomendados + herramientas
bash setup/install.sh --full   # además, plugins de Azure, GitHub, dbt, Power BI y Databricks
```

Luego empieza un proyecto:

```bash
mkdir ~/dev/modelo-churn && cd ~/dev/modelo-churn && git init && claude
```

```text
/alexis:project Predecir la fuga de clientes a partir de transacciones y mostrarlo en Power BI
/alexis:project continue   # retoma donde quedó el proyecto (p. ej. "me voy, sigue tú")
/alexis:project close      # registra decisiones e impacto, y mejora las skills
```

¿Solo el plugin? `claude plugin marketplace add diegoaguilar2209/alexis` y `claude plugin install alexis@alexis`.

## Cómo funciona

```text
 /alexis:project <idea>
   entender ─▶ investigar ─▶ validar ─▶ spec + plan + evals   (la profundidad depende del tipo de proyecto)
                                             │
                                             ▼
                                   UNA aprobación tuya
                                             │
                                             ▼
   construye solo: /goal ─▶ probar ─▶ corregir ─▶ commit, hito tras hito
   (las tareas independientes van a subagentes nativos, cada uno en su worktree;
    el subagente verifier audita con ojos frescos)
                                             │
                                             ▼
   cierre: decisiones, impacto (repo + Obsidian) y mejoras a las skills

 Siempre activo: hook de seguridad (bloquea DROP, force push, deploys a prod…) · lint tras cada edición · barra de estado con límites de uso
```

## Qué incluye

### Skills (comandos)

| Etapa | Comando | Qué hace |
| --- | --- | --- |
| Proyecto | `/alexis:project` | De la idea a la entrega verificada: entrevista, investigación y validación (productos), modo hackatón, spec, estructura del repo, evals y plan, una aprobación, y luego construye solo con subagentes; al cerrar registra el impacto y mejora las skills |
| Especialistas (los llama `project` o tú directamente) | `/alexis:build-agent` | Diseña, construye, evalúa, asegura y despliega agentes de IA (patrón, harness, herramientas, evals, OWASP, Azure/Databricks/AWS/GCP) |
| Calidad de datos | `/alexis:data-contract` | Esquema, llaves, valores permitidos y frescura de una tabla compartida, con tests que lo hacen cumplir |
| | `/alexis:metric-definition` | Una sola definición por KPI, trazada de la medida DAX al SQL |
| Entregar | `/alexis:powerbi-executive` | Audita y rediseña reportes de Power BI: modelo, DAX y diseño de nivel consultora |
| | `/alexis:exec-deck` | Presentaciones ejecutivas con la conclusión primero y números trazables |
| Mantenerse al día | `/alexis:tech-radar` | Qué hay de nuevo y qué funciona de verdad en IA, agentes y plataformas de datos, calificado Adoptar/Probar/Evaluar/Evitar |

### Workflows, subagentes y hooks

| Pieza | Qué hace |
| --- | --- |
| `/alexis:audit-model` | Workflow: un agente revisor por archivo; cada hallazgo lo verifica un segundo agente |
| `/alexis:migrate` | Workflow: un agente por archivo en su propio worktree de git, y luego un verificador |
| `verifier` | Subagente: audita el trabajo terminado con ojos frescos antes de darlo por hecho |
| `sql-reviewer`, `data-validator`, `agent-reviewer` | Subagentes: revisan SQL, validan resultados de datos y revisan un agente antes de que lo usen personas reales. Cada uno usa un modelo costo-eficiente |
| Hook de seguridad | Bloquea DROP, TRUNCATE, DELETE/UPDATE sin WHERE, deploys a producción, force push y borrados en la nube, también vía MCP |
| Hook de lint | Tras cada edición, corre el pre-commit de tu repo sobre ese archivo |

### Herramientas de terminal

| Herramienta | Qué hace |
| --- | --- |
| `alexis-statusline` | Barra de estado: modelo, esfuerzo, contexto, uso de 5 horas y semanal con hora de reinicio |
| `alexis-goal` | Ejecuciones headless hacia un objetivo, con logs en vivo |

## Plugins recomendados

`setup/install.sh` también instala plugins que consideramos importantes para esta forma de trabajar. Algunos son oficiales y otros de la comunidad. Revísalos antes de instalarlos, como todo lo que corre con tus permisos.

| Plugin | Origen | Para qué |
| --- | --- | --- |
| `superpowers` | Comunidad ([obra/superpowers](https://github.com/obra/superpowers)) | Método de ingeniería probado: brainstorming, planes, TDD, depuración sistemática |
| `data` | Anthropic ([knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)) | Exploración de datos, análisis, SQL, visualización y validación |
| `document-skills` | Anthropic ([skills](https://github.com/anthropics/skills)) | Archivos Word, Excel, PowerPoint y PDF |
| `pyright-lsp`, `context7`, `security-guidance` | Marketplace oficial de Anthropic | Inteligencia de código Python, documentación actual de librerías, guía de código seguro |
| Con `--full` | Marketplaces oficiales y de los proveedores | Azure, Microsoft Docs, GitHub, revisión de PR, Semgrep, dbt, Power BI authoring, Databricks AI Tools |

## Estructura del repo

```text
plugins/alexis/
  skills/          Una carpeta por comando (SKILL.md + referencias)
  agents/          Subagentes: verifier, sql-reviewer, data-validator, agent-reviewer
  workflows/       Workflows multiagente: audit-model, migrate
  hooks/           Conexión de los hooks (seguridad antes de cada herramienta, lint después de editar)
  scripts/         El código de los hooks: Python simple que puedes auditar
  templates/project/  Lo que /alexis:project copia a tu repo: CLAUDE.md, permisos, reglas, pre-commit, CI, evals
  evals/           Casos de evaluación de cada skill (claude plugin eval)
setup/             Instaladores y configuración de settings
templates/user/    ~/.claude/CLAUDE.md inicial (tus preferencias personales)
tools/             alexis-statusline, alexis-goal
routines/          Plantillas de rutinas en la nube: revisión de PR, docs desactualizadas, chequeo post-deploy, radar mensual
telemetry/         Stack local OpenTelemetry + Prometheus + Loki + Grafana con el historial de tokens y costo
vault/             Bóveda inicial de Obsidian: memoria de largo plazo y registro de impacto profesional
tests/             Tests de los hooks y herramientas
```

## Requisitos y plataformas

[Claude Code](https://code.claude.com/docs), Git, Python 3 y bash. Opcional: tmux, pre-commit, black, isort, sqlfluff, Databricks CLI.

**Probado en Windows con WSL2 (Ubuntu).** Linux y macOS deberían funcionar, pero aún no están probados; `setup/install.ps1` (Windows nativo) no está probado. Reportes y arreglos son bienvenidos.

## Evals: prueba de que cada skill ayuda

Cada skill trae casos de evaluación en `plugins/alexis/evals/`. `claude plugin eval` los corre en sesiones aisladas, comprueba que la skill se active con frases naturales (en inglés y español) y califica el resultado con una rúbrica, opcionalmente comparándolo con el mismo pedido sin ALEXIS.

```bash
cd plugins/alexis
claude plugin eval . --runs 1 --ablation none --judge-model sonnet   # chequeo rápido
claude plugin eval . --judge-model sonnet                            # completo, con vs. sin ALEXIS
```

La suite ya encontró problemas reales: la skill de inicio hacía demasiadas preguntas, y la skill de construcción autónoma se activaba solo 1 de cada 3 veces con "me voy, sigue tú" hasta que se reescribió su descripción (ahora 3 de 3). Ambos chequeos siguen vivos en los casos `project-*`. Un workflow de GitHub corre la suite a pedido o cada semana con tu secreto `ANTHROPIC_API_KEY`.

## Modelos, tokens y límites

- **Ruteo de modelos**: subagentes y skills livianas usan modelos más baratos (`sonnet`, `haiku`). Recomendado: `sonnet` en el día a día, `opusplan` para funcionalidades complejas (Opus planifica, Sonnet ejecuta); bajar `/effort` antes de subir de modelo.
- **Medidor**: la barra de estado muestra el contexto usado y, en planes Pro/Max, el uso de 5 horas y semanal con su hora de reinicio. Al 80% de la ventana de 5 horas avisa para guardar el estado.
- **Si se acaba el límite**: en Pro/Max, una sesión interactiva abierta espera y continúa después del reinicio (Claude Code v2.1.234+). Deja la terminal abierta; tmux ayuda. Las ejecuciones headless (`-p`) y las API keys no esperan.
- **Historial**: `telemetry/` muestra tokens y costo por día, modelo y herramienta.

## Mantenerse al día

En cada push, el CI valida el plugin (`claude plugin validate --strict`), el frontmatter de las skills, los scripts de shell y los tests de los hooks. Dependabot mantiene al día las GitHub Actions, un workflow semanal actualiza los hooks de pre-commit de la plantilla de proyecto, y cada tag `vX.Y.Z` publica un release desde el [CHANGELOG](CHANGELOG.md). Para actualizar: `git pull` y reiniciar Claude Code.

## Seguridad

Las skills y los hooks corren con tus permisos: revisa lo que instalas. El hook de seguridad busca patrones de texto, así que atrapa los comandos destructivos comunes, no todos los posibles. La protección real son las credenciales: conecta Claude Code con identidades de solo lectura y entornos de desarrollo, nunca con permisos de escritura en producción. Ver [SECURITY.md](SECURITY.md).

## Contribuir

Issues y pull requests son bienvenidos. Ver [CONTRIBUTING.md](CONTRIBUTING.md) y el [Código de conducta](CODE_OF_CONDUCT.md).

## Licencia

[MIT](LICENSE)
