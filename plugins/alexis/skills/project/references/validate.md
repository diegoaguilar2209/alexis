# Validate: should this be built?

Phase 3 of `/alexis:project` for products meant to make money. Building is no longer the hard part; ideas die from picking the wrong problem and having no way to reach customers. Say "no" fast to weak ideas and "yes, validate it like this" to strong ones. If `docs/research.md` exists, answer from it.

## 1. Questions (answer with evidence, not opinions)

| Question | Strong signal | Weak signal |
| --- | --- | --- |
| Who exactly has the problem? | Role, business type, country, size | "Companies", "everyone" |
| How do they solve it today and what does it cost? | Spreadsheets + measurable hours, expensive tools | They don't (maybe it doesn't hurt) |
| Who pays and from which budget? | An existing budget line or current spend | A budget would have to be created |
| Why this founder? | Direct experience, access to customers, data | "I can code it" |
| How do the first 10 customers arrive? | Own network, community, door-to-door, audience | Ads, "it will go viral" |
| What stops a big platform from giving it away tomorrow? | Domain depth, local regulation, integrations, relationships | It is a generic AI feature |
| What local reality could kill it? | Checked: informality, dominant payment methods, regulation, connectivity | Not considered |

## 2. Employer conflict filter (mandatory, a hard stop if it fails)

- Does it use knowledge, code, data or methods created for an employer or client? If yes, stop until the user checks the contract (intellectual property, non-compete, exclusivity).
- Is the target customer, partner or competitor related to the employer (e.g. a payment method owned by the employer's group)? Flag it explicitly.
- Build on personal time, with personal equipment and accounts.

## 3. Verdict

One of three, with the reason in 3 lines:

- **Drop**: the problem does not hurt or nobody pays.
- **Validate before building**: define the experiment.
- **Build an MVP**: only with customer commitments already (pre-sale, signed pilot, letter of intent).

## 4. Cheapest experiment

Something doable in 2 weeks or less, before product code:

- 10 conversations with target customers (5-question script about their problem, without pitching the solution).
- A landing page with a real price and a pay or "book a demo" button.
- Manual service first (the "product" is the founder + Claude Code), then automate what repeats.

Fix a numeric success criterion in advance (e.g. 3 of 10 accept a paid pilot).

## 5. Record

If `ALEXIS_VAULT` is set in the user's CLAUDE.md, save the analysis to `<vault>/3-Ideas/<idea>.md` with the verdict and a review date. Then write the verdict and the experiment at the top of `docs/spec.md` (risks) and as the first block of `docs/plan.md` when the verdict is "validate before building".
