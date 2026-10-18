# Routine: ALEXIS radar (maintainers)

**Trigger:** schedule, monthly (first Monday). **Repository:** the ALEXIS repository. Complements the weekly upkeep routine, which only tracks Claude Code release notes.

```text
Run /alexis:tech-radar "AI agents, LLM tooling and data platforms" with a 45-day window, comparing against this repository (plugins/alexis/skills, agents, templates).
Keep only Adopt and Trial findings that ALEXIS does not cover yet and that have a primary source.
Write docs/radar/<YYYY-MM>-ai.md.
If there is at least one gap, open one pull request titled "Radar <YYYY-MM>: <n> proposed updates" that adds the radar file and the proposed skill/reference edits, plus an eval case for each changed skill. Do not merge.
If there are no gaps, commit nothing and end with "No relevant changes".
Never add personal data, employer data or credentials.
```
