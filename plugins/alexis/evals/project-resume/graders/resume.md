---
type: llm
---

The workspace itself may be empty; that is fine. The user pasted a docs/plan.md with "Phase: build", one task done and the rest pending, and an approved spec.
PASS if the reply recognizes the project is in the build phase, names the next pending task (the daily loader) and its verification command, and proceeds to work or states the goal condition it will run, WITHOUT asking the kickoff questions again (problem, users, KPI, data) and without asking for approval of the plan again.
FAIL if it restarts the interview, asks to approve the plan again, or ignores docs/plan.md.
