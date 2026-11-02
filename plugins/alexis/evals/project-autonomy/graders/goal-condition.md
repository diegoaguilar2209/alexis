---
type: llm
---

The workspace in this test is intentionally empty, so it is fine (and good) if the reply notes that the module or tests are missing and asks how to proceed.

PASS if the reply proposes a /goal condition (or an equivalent completion condition) that contains all three: (1) the verification commands `pytest -q tests/ingestion` and `pre-commit run --all-files`, (2) a constraint not to touch the reporting folder and not to weaken or skip tests, and (3) a stop budget such as a turn limit.
FAIL only if one of those three elements is missing, or if the reply edits code before proposing the condition.
