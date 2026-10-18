# Long-running and parallel agents

## Harness design (Anthropic, 2026)
- **Separate generator and evaluator.** Agents over-praise their own work; a skeptical evaluator is easier to tune than a self-critical generator.
- **Planner first:** expand a short request into a product spec (deliverables, high-level design), not a detailed technical plan that cascades errors.
- **Contracts:** before each chunk of work, generator and evaluator agree in a file on what "done" means and how it will be tested.
- **Test the running thing:** the evaluator exercises the real app or pipeline (Playwright, real queries) with hard per-criterion thresholds.
- **Context resets vs compaction:** resets with structured handoff files give a clean slate; compaction keeps continuity. Newer models need resets less — measure.
- **Every harness piece encodes an assumption about what the model cannot do.** Re-test and remove scaffolding when the model changes; cost of a full harness was ~20x a solo run, worth it only beyond what the model does reliably alone.

## Architecture: brain, hands, session (Managed Agents)
- Three parts with stable interfaces: **session** (append-only event log, stored outside), **harness** (stateless loop; can crash and resume from the log), **sandbox** (disposable container where code runs).
- Tools share one interface (`execute(name, input) -> string`); sandboxes are provisioned only when needed.
- **Credentials never enter the sandbox:** a proxy injects them from a vault. Generated code can't leak what it can't see.
- Keep the full history durably and query slices of it instead of irreversibly compacting.
- Be opinionated about interfaces, not implementations.

## Durable execution
Agent steps are slow, paid and have side effects; a crash must not re-run completed steps.
| Option | Fit |
| --- | --- |
| DBOS | Library, checkpoints in your existing Postgres; minimal new infra |
| Temporal | Mature external orchestrator; polyglot; heavier to operate |
| Restate | Lightweight durable runtime; growing agent integrations |
| LangGraph checkpointers | Already on LangGraph |
| Platform-native | Foundry, Bedrock AgentCore, Managed Agents session logs |
Make every write tool idempotent (idempotency key) so replays are safe.

## Many agents in parallel
Lessons from a team of parallel Claudes building a C compiler (~2,000 sessions, ~$20K):
- Coordination can be as simple as lock files in a shared repo plus git; specialized roles (cleanup, performance, docs) help.
- **The verifier must be nearly perfect** or agents confidently solve the wrong problem. Tests print little, log detail to files, mark errors for grep, offer a fast sampled mode.
- Parallelism fails when every agent hits the same blocker; split the problem with an oracle (a reference implementation) first.
- READMEs and progress files let each fresh agent orient itself.
- Passing tests is not proof; humans still verify before deployment.

In Claude Code: `/alexis:autopilot`, dynamic workflows (`/alexis:migrate`, `/alexis:audit-model`) and `alexis-wt` worktrees apply these patterns.
