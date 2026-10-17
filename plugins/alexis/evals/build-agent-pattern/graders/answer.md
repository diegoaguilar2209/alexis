---
type: llm
---

PASS if the reply recognizes this as a workflow (routing: classify, then a specialized prompt with retrieval over help-center articles, then human approval) rather than a free-running multi-agent system, explains why the simpler design is better, and includes evaluation (labeled tickets to measure classification accuracy and draft quality) and treating ticket content as untrusted input (prompt injection).
FAIL if it designs several autonomous agents talking to each other without questioning the need, or has no evaluation plan.
