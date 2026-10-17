# Agent evals

An agent without evals is a demo. Evals decide every change to prompts, tools, models and harness.

## Case design
- 10+ cases at first, 50+ before production; grow with every production failure.
- Realistic, multi-step tasks (not "call tool X"): they should need several tool calls and some judgment.
- Cover: happy paths, ambiguous requests (should ask or state an assumption), missing or dirty data, requests it must refuse, a prompt-injection string inside a tool result or document, permission boundaries (user A must not see user B's data), long conversations, each tool at least once.
- Synthetic data only in the repo.

## What to grade
| Layer | Check | Grader |
| --- | --- | --- |
| Outcome | Final answer correct / task done | Exact match, tolerance, or LLM judge with a rubric |
| Trajectory | Right tools, no forbidden tools, no redundant calls | Deterministic checks on the transcript |
| Safety | Refused what it must, no data leak, no action without approval | Deterministic checks + adversarial cases |
| Cost | Tokens, dollars, turns | Thresholds per case |
| Latency | Time to first token and to completion | Thresholds per case |
| Retrieval (RAG) | Right sources retrieved and cited | recall@k, citation check |

Prefer deterministic graders; use an LLM judge only for open answers, with a strong judge model, a written rubric, and a sample of judgments reviewed by a human.

## Run discipline
- Baseline first, then change one thing at a time.
- Run each case 3+ times: agents are non-deterministic; report the pass rate, not one run.
- Keep a results table per run: score, cost, latency, model, prompt version.
- A change ships only if the score does not drop and cost/latency stay within budget.
- Read failed transcripts; the fix is usually in tools or context.

## Tools
- Claude Agent SDK or Claude Code: `claude plugin eval` style cases (prompt + graders) or a pytest harness that runs the agent and asserts on the transcript.
- LangSmith (LangGraph), Azure AI Foundry evaluations, Vertex AI evaluation, Langfuse, promptfoo, DeepEval, Inspect: pick the one the platform already has.
- Production: sample real traces weekly, label failures, and add them as cases.

## Case file
Use `templates/project/evals/agent-cases.yaml` from the ALEXIS plugin as the starting point.
