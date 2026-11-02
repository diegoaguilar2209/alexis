# Decisiones

## 2026-11-01

- Un solo comando, `/alexis:project`, para todo el ciclo de un proyecto. Razón: `new-project`, `validate-idea`, `hackathon`, `autopilot`, `session-log` e `improve` eran etapas de un mismo flujo, y obligaban al usuario a saber qué comando tocaba. Ahora Claude decide la profundidad de cada fase según el tipo de proyecto.
- Autonomía: una sola aprobación (spec + plan + condición de objetivo) y luego construye solo. Se detiene solo ante paradas duras. Las decisiones reversibles se registran en `docs/decisions.md` en vez de preguntarse.
- El estado vive en la línea `Phase:` de `docs/plan.md`. Es legible por humanos, versionado con git y permite retomar sin memoria de sesión.
- Se elimina `alexis-wt`. Claude Code orquesta subagentes nativos con `isolation: "worktree"`, así que tmux + worktrees manuales ya no aportan. `alexis-goal` se mantiene para corridas headless.
- Se mantienen las skills especialistas (`build-agent`, `data-contract`, `metric-definition`, `powerbi-executive`, `exec-deck`, `tech-radar`) como skills separadas: son conocimiento de dominio que `project` carga cuando una tarea lo necesita, y también se usan solas.
- Cada mejora a una skill de ALEXIS que proponga el cierre trae un caso de eval que habría detectado el problema.

## 2026-10-30

- Template: pip-compile vía `astral-sh/uv-pre-commit` (0.13.6), no pip-tools. Razón: el hook de pip-tools 7.4.1 falla con el pip actual. Dos hooks: `requirements.in` y `requirements-dev.in`, ambos con `--python-version 3.12`.
- Template: gitleaks con el hook oficial v8.30.1 y `language_version` fijo. pre-commit descarga su propio Go, así que no depende del equipo ni necesita `language: system` (que no es portable).
- Template CI: gitleaks escanea el historial completo (`gitleaks detect`) con el binario de la release oficial.
- Template CI: pre-commit corre con `uvx pre-commit` y `actions/cache@v6`, no con `pre-commit/action`, porque ese action empaqueta `actions/cache@v4` (Node 20, deprecado).
- Template: Python 3.12 fijo (CLAUDE.md, pyupgrade `--py312-plus`, comandos).
- Template: `claude-code-action` fijada a SHA `6d5ae526…` (v1.0.265). Dependabot propone las subidas.
- Template: el propio template pasa prettier, para que el primer commit de un proyecto nuevo no falle.
- Acciones de este repo: `checkout@v7`, `setup-python@v7`, `setup-node@v7`, `setup-uv@v10.3.3`, `actions/cache@v6`.
