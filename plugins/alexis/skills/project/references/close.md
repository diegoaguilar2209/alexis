# Close and improve

Phase 6 of `/alexis:project`: end of a session, end of a milestone, or `/alexis:project close`. It keeps the project's memory in files the user controls, builds the evidence of impact, and makes ALEXIS better with every project.

## 1. Project log

Review the session and write ONLY what changes the project's future:

- `docs/decisions.md`: new entry at the top (`## YYYY-MM-DD`). Decisions with their reason, reusable learnings (a bug and its root cause, a pattern that worked), status (done, half-done) and the next 3 steps.
- `docs/impact.md`: one row per measurable result (date, result, metric, evidence). If there is no number yet, note which metric would prove it.
- `docs/plan.md`: the `Phase:` line and checkboxes are current.

## 2. Vault (if `ALEXIS_VAULT` is set in the user's CLAUDE.md)

- `<vault>/1-Projects/<project-name>.md`: status, decisions, `[[links]]`.
- If there was impact: one line in `<vault>/2-Areas/Career/Impact.md` with date, result and number.
- Work and client projects: only the result in general terms ("cut campaign cost 18%"), never data, table names, client names or credentials.

## 3. Improve the skills (evidence, not guesses)

Gather evidence from this session: corrections the user had to repeat, defaults that were wrong, steps that were slow or skipped, questions that should not have been asked, plus `/insights` (`~/.claude/usage-data/report.html`) and `/usage` if the complaint is about limits.

Classify each problem and pick the fix:

| Symptom | Fix |
| --- | --- |
| Same convention wrong twice in this project | One line in the project's `CLAUDE.md` or `.claude/rules/` (apply directly) |
| Same mistake across projects | One line in the user's `~/.claude/CLAUDE.md` (show diff, apply on approval) |
| An ALEXIS skill gave a wrong default, missed a step or asked too much | Edit that skill or its reference (show diff, apply on approval) |
| The same multi-step procedure repeated 3 times | A new reference or skill |
| Something must happen every time, no judgment needed | A hook |
| Context fills with output nobody rereads | A subagent, or a hook that filters output |
| Usage limits hit early | Cheaper model for subagents, `/clear` between tasks, fewer MCP servers |
| A skill triggers when it should not, or never | Rewrite its description, specific trigger first, and add an eval case |

For each: the evidence (quote or file), the exact diff, the expected effect. Every change to an ALEXIS skill comes with an eval case in `plugins/alexis/evals/` that would have caught the problem.

## 4. Share back

If a fix is generic (useful to anyone, no personal or employer data), offer to open a pull request to the ALEXIS repository: https://github.com/diegoaguilar2209/alexis

## Rules

- Short sentences; do not narrate what was done step by step.
- Propose, do not silently apply, anything outside the current project.
