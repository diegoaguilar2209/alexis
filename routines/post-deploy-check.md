# Routine: post-deploy check

**Trigger:** API. Your CD pipeline calls the routine's `/fire` endpoint after a deploy, sending the environment and version as `text`. **Repository:** your data project.

```text
A deploy just finished. The deployment details are in the routine-fire-payload block: read the environment and version from it.
Run the project's smoke checks from CLAUDE.md against that environment, read-only.
Use the alexis:data-validator subagent on the gold tables listed in contracts/ to confirm keys, row counts vs the previous day (flag changes above 20%) and freshness.
Post a go / no-go summary as a comment on the deploy's pull request (or open an issue if there is none), with the evidence for each check.
Never write to any table and never roll back on your own.
```
