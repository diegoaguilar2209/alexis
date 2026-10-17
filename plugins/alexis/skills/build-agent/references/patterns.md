# Agent patterns

Source: Anthropic, "Building effective agents". Workflows = LLMs and tools orchestrated through predefined code paths. Agents = the LLM directs its own process and tool use. Start with the simplest; add complexity only when an eval shows it is needed.

## Building block: augmented LLM
One model call with retrieval, tools and memory. Most "agents" in companies are this plus a good tool. Use it until it fails an eval.

## Prompt chaining
Fixed sequence; each step's output feeds the next, with programmatic gates between steps (validate, stop early).
- Fit: document → outline → check outline → draft; SQL generation → validation → explanation.
- Trade: more latency for higher accuracy per step.

## Routing
Classify the input, send it to a specialized prompt/model/tool set.
- Fit: support triage, cheap model for easy questions and strong model for hard ones.
- Watch: the classifier must be evaluated on its own.

## Parallelization
- Sectioning: split into independent subtasks run at once (one model answers, another screens for policy).
- Voting: same task several times, aggregate (code vulnerability review, content moderation thresholds).

## Orchestrator-workers
A central model breaks down the task at run time and delegates to workers, then synthesizes.
- Fit: changes across many files, research across many sources.
- Difference from parallelization: subtasks are not known in advance.

## Evaluator-optimizer
One model produces, another evaluates against explicit criteria, loop until pass or max iterations.
- Fit: translation nuance, complex search, writing with a clear rubric.
- Needs: criteria a model can apply, and evidence that feedback improves results.

## Autonomous agent
Loop: plan → act with tools → observe environment feedback → repeat until done or stopped.
- Fit: open-ended problems where steps cannot be predicted (coding, operations).
- Needs: ground truth from the environment at each step (tests, query results), stop conditions (max turns, budget), checkpoints for human review, a sandbox.
- Cost: higher, and errors compound. Only in trusted environments with guardrails.

## Multi-agent
Several agents with separate contexts. Worth it when subtasks are parallel and each needs a clean context (research), or when security boundaries differ per agent. Not worth it for tightly coupled work: coordination costs tokens and adds failure modes (cascading errors, ASI07/ASI08). Prefer one agent with sub-agents that return condensed summaries.

## Three principles
1. Simplicity in the design.
2. Transparency: show the agent's plan and steps.
3. Craft the agent-computer interface (tools) with documentation and testing.

## Decision checklist
- Can a single call with retrieval pass the evals? Stop there.
- Are the steps known in advance? Workflow, not agent.
- Does every step have verifiable feedback? If not, an autonomous loop will drift.
- What does a wrong action cost? High cost → approval gates or suggest-only autonomy.
