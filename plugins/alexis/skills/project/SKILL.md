---
name: project
description: Use for any project from idea to verified delivery - "tengo una idea", "quiero crear una app", "empecemos un proyecto", "entro a una hackathon", "valida esta idea", "¿vale la pena construirlo?", "is this worth building?", "how should I spend the 48 hours", "investiga el mercado", "sigue tú / me voy", "I'm going to step away, keep working on your own until it's done", "build it alone, don't stop until tests pass", "cierra la sesión" - or /alexis:project. One command that understands, researches, validates, plans, and after one approval builds alone with native subagents until the evals pass, then logs and improves the skills. Re-running it resumes from where the project stands.
argument-hint: "[idea | continue | close]"
---

# Project: from idea to verified delivery

One command for the whole life of a project. Claude decides what each phase needs and asks the user only what it cannot decide. Reply in the user's language.

```text
understand → research → validate → spec + plan ──▶ APPROVAL ──▶ build alone (subagents, /goal, verifier) ──▶ close + improve
```

## 0. Where are we? (always first)

Read `docs/plan.md`. Its first line is `Phase: <understand|research|validate|plan|build|done>`.

- No file, but the user pasted a plan in the message: treat the pasted text as `docs/plan.md` and resume from its `Phase:` line. Never stop because the file is missing from the workspace; write it there when you start working.
- No file and nothing pasted: start at phase 1.
- File exists: resume that phase and say in one line where you are and what comes next.
- `$ARGUMENTS` = `close`: go to phase 6.
- `$ARGUMENTS` = `continue`, or "me voy / sigue tú": go to phase 5 if the plan is approved.

Update the `Phase:` line whenever a phase ends.

## Autonomy policy

Ask the user only at these moments:

1. **One round of questions** in phase 1, and only what is missing.
2. **One approval** at the end of phase 4 (spec, plan and goal condition together).
3. **Hard stops:**
   - anything irreversible or in production;
   - spending money, creating accounts or using credentials;
   - a legal or employer-conflict risk;
   - a change of scope;
   - missing access;
   - the same error three times.

Everything else: take the most reasonable decision, write one line in `docs/decisions.md` (decision + reason) and keep going. A decision that can be undone with a commit is never a reason to stop.

## 1. Understand

- Read `$ARGUMENTS`, the conversation and any `@file` given (briefs, research, notes).
- If the request already lets you act (an explicit research, validation or hackathon-plan request, or enough detail to classify), run the requested phase first and ask nothing, or ask after delivering it.
- Otherwise ask, in a single message, at most 5 numbered questions. Each one asks a single thing in one line of at most 20 words (no "and"/"or" chains, no option lists, no examples). Ask about KPI target, users, deadline, data volume or context; never about the tools, sources or cadence already stated, and no technical-design questions (those become stated assumptions). Never ask about tools, sources or platforms the user already named. Choose them from:
  - problem and KPI;
  - end user and how they consume the result;
  - context (work, personal product, course, hackathon with deadline and judging criteria);
  - data and platform;
  - deliverables and date.
- Skip anything already answered. Whatever is still unknown becomes a one-line stated assumption.
- Classify the project in one line: one or more of `product` (to sell), `pipeline`, `dashboard`, `agent`, `analysis`, `platform`, `hackathon`.
- The classification decides which of phases 2–3 apply and how deep:

| Type | Research (2) | Validate (3) | Extra |
| --- | --- | --- | --- |
| product | Full: references/research.md | Full: references/validate.md | |
| hackathon | Judges and rules only | Skip | references/hackathon.md drives the plan |
| work: pipeline, dashboard, analysis, platform | Skip unless the user asks | Skip | Data platform conventions |
| agent | Patterns only | Only if it is sold | Phase 5 hands design to `/alexis:build-agent` |

## 2. Research (product, or when asked)

Follow `references/research.md`. Output: `docs/research.md` with sources.

If the user already brought research (`@docs/research.md` or a strategy document), do not redo it. Check it for gaps and only research those.

## 3. Validate (product)

Follow `references/validate.md`. Output:

- the verdict;
- the employer-conflict check;
- the cheapest experiment with a numeric success criterion;
- a note in `<vault>/3-Ideas/` if `ALEXIS_VAULT` is set.

Act on the verdict:

- **Drop:** stop here.
- **Validate before building:** the experiment becomes the first block of the plan, unless the user has already run it. Product code waits for its result, but the scaffold can be built.
- **Build an MVP:** continue to phase 4.

## 4. Spec, scaffold and plan

1. **Scaffold.** Run `git init` if there is no repo. Copy `${CLAUDE_PLUGIN_ROOT}/templates/project/` without overwriting existing files, and fill every `<...>` placeholder. Then adapt it to the stack:
   - **Python data project:** keep it as is.
   - **Other stacks (TypeScript, mobile, Go…):**
     - Python files only where Python lives (e.g. `data/`).
     - Write a `.claude/rules/<stack>.md` with this project's conventions.
     - CI with that stack's lint, typecheck and tests.
     - Delete the rules that do not apply.
   - **Existing or team repo:** respect its standards and add only what is missing.
2. **`docs/spec.md`.** Cover:
   - problem and KPI (baseline → target);
   - users;
   - in and out of scope;
   - data;
   - architecture (Mermaid);
   - measurable acceptance criteria;
   - risks and assumptions.

   Inherit from `docs/research.md` instead of re-deriving it.
3. **`evals/cases.md`.** At least 5 real cases with input and expected result. For a hackathon, 8–12.
4. **`docs/plan.md`.**
   - `Phase: plan` on the first line.
   - Milestones in order, each made of small tasks with their verification command.
   - Mark the tasks that are independent of each other, plus which specialist skill each one needs (e.g. `build-agent`, `data-contract`, `metric-definition`, `powerbi-executive`, `exec-deck`). Phase 5 parallelizes from these marks.
   - Use Superpowers `writing-plans` if installed.
5. **Goal condition** for the first milestone (template in `references/build.md`).
6. **First commit:** `chore: project scaffold`.
7. **APPROVAL.** In one message, show:
   - the type;
   - files created;
   - milestones;
   - the goal condition;
   - assumptions taken;
   - missing plugins or MCP servers, with their exact install command.

   Ask once: "¿Apruebas y arranco solo?". Corrections are applied, then you start without asking again.

## 5. Build alone

Follow `references/build.md`. In short:

- Set `Phase: build` and create the branch `build/<milestone>`.
- Recommend auto mode (Shift+Tab).
- Start the goal with `/goal`.
- **Each turn:** take the next task, make the smallest change, run the verification and read its real output. Green → commit. Red → find the root cause, one hypothesis at a time.
- **Independent tasks:** run them in parallel with native subagents. Each one works in its own worktree (`isolation: "worktree"`), gets a self-contained brief (task, files, verification command, skill to load) and returns a short result. You merge and verify. Never parallelize tasks that touch the same files or the same migration.
- **Every ~5 green commits, and before declaring a milestone done:** the `verifier` subagent audits with fresh eyes. Also use `sql-reviewer`, `data-validator` or `agent-reviewer` when their area changed.
- **Milestone met:** run the full verification once more, write a short entry in `docs/decisions.md`, then start the next milestone without asking — only hard stops pause the work. Never merge to `main` without the user.

## 6. Close and improve

Run at the end of every session, when the plan is done, or with `/alexis:project close`. Follow `references/close.md`:

1. Write decisions, learnings, status and the next 3 steps to `docs/decisions.md`.
2. Record measurable impact in `docs/impact.md` and, if `ALEXIS_VAULT` is set, in the vault.
3. **Improve the skills.** For each friction seen this session (repeated corrections, wrong defaults, missing rules), propose the exact edit to:
   - the project's `CLAUDE.md` or `.claude/rules/`;
   - the user's `CLAUDE.md`;
   - or the ALEXIS skill that caused it.

   Apply project-level edits directly. Skill and user-level edits are shown as a diff for approval. Generic fixes are offered as a PR to ALEXIS.

## Rules

- When the user asks for a plan, a verdict or an autonomous run, deliver it in the same reply: the time split with evals before features and a reserved demo block (hackathon); one verdict plus the employer-conflict check and a numeric experiment (validate); the exact `/goal` condition with verification commands, constraints (including what not to touch and never weakening tests) and a turn budget (autonomous run) — even if the workspace is empty. Missing files are reported, not a reason to skip the deliverable.

- Present-day facts (prices, players, versions, laws) are looked up, never recalled. If there is no web access, say so and mark those facts "approximate".
- Never use employer or client data, names or code in personal projects.
- Do not expand scope while building. New ideas go to `docs/plan.md` under "Later".
- Never weaken a test, skip it, or hard-code expected outputs to reach green.
