---
name: hackathon
description: Hackathon playbook for Claude Code - understand the judges, minimal spec, evals first, parallel workstreams, audits and demo. Use when the user enters a hackathon or a challenge with a deadline and judges, or runs /alexis:hackathon.
argument-hint: "[event name and deadline]"
---

# Hackathon mode

Based on what winners of the Claude Code "Built with Opus" hackathons did: spec before code, evals from the first commit, parallel work by domain, and time reserved for the demo. Reply in the user's language.

## 0. Time budget

From the deadline, split the total time and write it to `docs/hackathon-plan.md`:

| Phase | % of time |
| --- | --- |
| Understand the judges + spec | 15% |
| Eval + end-to-end skeleton | 15% |
| Parallel build | 45% |
| Audit and polish | 10% |
| Demo (video, README, pitch) | 15% |

## 1. Understand the judges

- Read the rules and judging criteria. Turn each criterion into a question the demo must answer.
- Define the "wow moment" in one sentence: what the judges see in the first 30 seconds.
- Pick a real problem the user knows deeply. Winners solved problems from their own domain.

## 2. Minimal spec (one page max)

Problem, user, wow moment, minimal demonstrable scope, out of scope, Mermaid architecture. Use `superpowers:brainstorming` if installed.

## 3. Evals first

Before any feature: `evals/cases.md` with 8-12 real cases and expected results, plus a script that runs them and prints a score. That number decides what works, not intuition.

## 4. End-to-end skeleton

An ugly but complete version (data → logic → interface) before deepening any part.

## 5. Parallel build

Split by domain (data, agent, UI, demo). Each domain in its own worktree with clean context: `alexis-wt data "<task>"`, `alexis-wt agent "<task>"`, one tmux window each. For long unattended stretches use `/alexis:autopilot` inside a worktree. Merge to `main` at least twice a day.

## 6. Audit

Before each new block, ask the `verifier` subagent to audit what exists against the spec and the eval ("what is wrong or missing?"). Fix before moving on.

## 7. Demo

- README: problem, demo GIF or video, how to run, architecture, eval results.
- Video max 3 minutes: problem (20 s), wow moment (60 s), how it works (60 s), impact (20 s).
- Reserve the last stretch only for this: it always takes longer than expected.

## Rules

- If Claude says something will not fit in the time, check it against the plan; sometimes it does fit.
- No features outside the minimal scope until the eval and the demo exist.
- Watch the 5-hour usage window on subscription plans: plan heavy parallel work right after a reset (the ALEXIS status line shows when it resets).
