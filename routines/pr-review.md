# Routine: data PR review

**Trigger:** GitHub event `pull_request.opened` (filter: is draft = false). **Repository:** your data project.

```text
Review the pull request that triggered this run, as a senior analytics engineer.
Use the alexis:sql-reviewer subagent on every changed .sql and PySpark file.
Check: join cardinality and grain, NULL handling, filters lost in LEFT JOINs, writes to production, committed credentials or data files, tests weakened or skipped, SELECT * outside bronze.
Leave inline comments only for real problems, then one summary comment ending with "Ready to merge" or "Changes required".
Do not push commits. Do not approve or merge.
Success: the summary comment is posted.
```
