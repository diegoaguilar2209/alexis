# Routine: documentation drift

**Trigger:** schedule, weekly (pick a few minutes past the hour, e.g. Monday 9:07). **Repository:** your data project.

```text
List the pull requests merged into the default branch in the last 7 days.
For each one, find documentation that it made wrong: README, docs/, docs/metrics/, contracts/, runbooks, CLAUDE.md commands.
If you find drift, fix the docs on a branch named claude/docs-drift-<date> and open one pull request listing each fix and the PR that caused it.
If nothing drifted, do nothing and end with "No drift".
Never change code, only documentation.
```
