---
name: validate-idea
description: Rigorously evaluate a startup, app or paid product idea before building it - problem, customer, willingness to pay, competition, distribution and employer conflicts - and design the cheapest experiment to validate it. Use when the user proposes building something to sell or make money.
argument-hint: "[the idea in one or two sentences]"
---

# Validate an idea

Building is no longer the hard part: with Claude Code an MVP takes days. Ideas die from picking the wrong problem and having no way to reach customers. This skill says "no" fast to weak ideas and "yes, validate it like this" to strong ones. Reply in the user's language.

## 1. Questions (answer with evidence, not opinions)

| Question | Strong signal | Weak signal |
| --- | --- | --- |
| Who exactly has the problem? | Role, company type, country, size | "Companies", "everyone" |
| How do they solve it today and what does it cost? | Spreadsheets + measurable hours, expensive consultants | They don't (maybe it doesn't hurt) |
| Who pays and from which budget? | An existing budget line | A budget would have to be created |
| Why this founder? | Direct experience, access to customers, data | "I can code it" |
| How do the first 10 customers arrive? | Own network, community, audience | Ads, "it will go viral" |
| What stops a big platform from giving it away tomorrow? | Domain depth, data, local regulation, relationships | It is a generic AI feature |

## 2. Employer conflict filter (mandatory)

- Does it use knowledge, code, data or methods created for an employer or client? If yes, do not proceed before checking the contract (intellectual property, non-compete, exclusivity).
- Is the target customer a competitor or supplier of the employer? Flag it.
- Build on personal time, with personal equipment and accounts.

## 3. Verdict

One of three, with the reason in 3 lines:
- **Drop**: the problem does not hurt or nobody pays.
- **Validate before building**: define the experiment.
- **Build an MVP**: only with customer commitments already (pre-sale, signed pilot, letter of intent).

## 4. Cheapest experiment

Something doable in 2 weeks or less, before any product code:

- 10 conversations with target customers (5-question script about their problem, without pitching the solution).
- A landing page with a real price and a pay or "book a demo" button.
- Manual service first (the "product" is the founder + Claude Code), then automate what repeats.

A numeric success criterion decided in advance (e.g. 3 of 10 accept a paid pilot).

## 5. Record

Save the analysis to `<vault>/3-Ideas/<idea>.md` if `ALEXIS_VAULT` is set in the user's CLAUDE.md, with the verdict and a review date.
