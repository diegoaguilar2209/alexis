# Routine: ALEXIS upkeep (maintainers)

**Trigger:** schedule, weekly. **Repository:** the ALEXIS repository.

```text
Read the Claude Code changelog and "What's new" pages published in the last 7 days (https://code.claude.com/docs).
List changes that affect ALEXIS: plugin manifest or skill frontmatter fields, hooks events and exit codes, status line JSON fields, /goal, workflows, routines, plugin eval, permission rules, model aliases.
For each, say which ALEXIS file is affected and what should change.
If there is at least one, open a single issue titled "Upkeep: Claude Code changes week of <date>" with that list. Do not change code.
If there are none, end with "No relevant changes".
```
