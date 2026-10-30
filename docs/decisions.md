# Decisiones

## 2026-10-30

- Template: pip-compile vía `astral-sh/uv-pre-commit` (0.13.6), no pip-tools. Razón: el hook de pip-tools 7.4.1 falla con el pip actual. Dos hooks: `requirements.in` y `requirements-dev.in`, ambos con `--python-version 3.12`.
- Template: gitleaks con el hook oficial v8.30.1 y `language_version` fijo. pre-commit descarga su propio Go, así que no depende del equipo ni necesita `language: system` (que no es portable).
- Template CI: gitleaks escanea el historial completo (`gitleaks detect`) con el binario de la release oficial.
- Template CI: pre-commit corre con `uvx pre-commit` y `actions/cache@v6`, no con `pre-commit/action`, porque ese action empaqueta `actions/cache@v4` (Node 20, deprecado).
- Template: Python 3.12 fijo (CLAUDE.md, pyupgrade `--py312-plus`, comandos).
- Template: `claude-code-action` fijada a SHA `6d5ae526…` (v1.0.265). Dependabot propone las subidas.
- Template: el propio template pasa prettier, para que el primer commit de un proyecto nuevo no falle.
- Acciones de este repo: `checkout@v7`, `setup-python@v7`, `setup-node@v7`, `setup-uv@v10.3.3`, `actions/cache@v6`.
