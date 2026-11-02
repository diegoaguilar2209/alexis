# Research: market, leaders and product strategy

Phase 2 of `/alexis:project` for products. Goal: know what the world's best already do, how they make money, how the customer lives the problem, and what architecture is worth paying for at each stage. Every present-day fact is looked up, never recalled.

## 0. Setup

- Write to `docs/research.md` (create `docs/` if needed). If `ALEXIS_VAULT` is set, link it from `<vault>/3-Ideas/<idea>.md`.
- Put an outline with all section headings first, then fill one section at a time so the user can redirect early.
- If web tools are unavailable, say so in the first line and label every figure "approximate, unverified". Never present memory as a sourced fact.

## 1. Landscape (who wins, worldwide and locally)

- List the global leader per vertical and the regional and local players in the target country. Search each player separately: one combined query gives shallow results.
- Use subagents in parallel for the per-player research when there are more than 3 players; each returns figures with URL and date.
- Prefer primary sources: SEC/regulator filings, earnings releases, official pricing pages, funding announcements. Use reviews and blogs only for pricing when nothing official exists, and say so.
- Output: one table — player · vertical and countries · scale (locations, ARR, GPV, customers, with date) · how it charges · source link.
- Look for the gap: which countries or segments each player reports as its markets, and where the target country is missing.

## 2. Reverse engineering of the top 2

For the two players the user would most want to beat:

- **Money:** the revenue model and take-rate math (e.g. revenue ÷ processed volume tells you whether it is a software or a payments business).
- **Growth loop:** what more customers produce (subscriptions → payment volume → lending, or supply → marketplace demand).
- **Product decisions that matter:** offline mode, own hardware, marketplace, AI agents. Read their docs and engineering job posts, which reveal the stack.
- **Tensions and weaknesses** a newcomer can exploit (e.g. a marketplace that sends a merchant's client to a competitor).
- **Close with "copy / don't copy yet"**, each with a one-line reason.

## 3. Think like the customer

- Make one table per vertical: who (owner, cashier, staff, end customer) · moment of the day · what hurts today · how the product resolves it.
- Derive 4–6 design rules from it. Examples: never block a sale; onboarding under 15 minutes; usable one-handed by staff with low digital literacy; which channel is primary (WhatsApp, app, web).
- Mark local realities that change the product: informality, dominant wallets, tax receipts, connectivity.

## 4. Product

- A table with core + vertical modules + country adapters + intelligence layer.
- MVP for ONE vertical: what is in, what is explicitly out.
- 3–4 differentiators against the leaders, each tied to a finding from sections 1–3.
- One north-star metric that measures real adoption and turns into revenue.

## 5. Architecture with cost-benefit

- **Stages by scale** (e.g. 0–500 customers, 500–10k, 10k+): components and approximate infra cost per month in USD. Current prices are looked up; label estimates as estimates.
- **No-regret disciplines from day one** (cheap now, expensive to retrofit): multi-tenant isolation (RLS), idempotency keys on money movements, transactional outbox, offline-first where sales happen, country adapters, money as integers, observability.
- **For every heavy tool the user mentions** (Kafka, Flink, Kubernetes, microservices): its minimum monthly cost vs the stage-1 alternative, and the concrete triggers that justify adopting it. No "machine gun to kill an ant".
- **Draw the stage-1 architecture as a Mermaid diagram**, then add a recommended stack table (piece · choice · why).

## 6. Business model, go-to-market, roadmap

- Pricing benchmarks from section 1, a proposed model (free tier, subscription, payments margin, usage add-ons) and third-party unit costs (payment fees, tax-receipt provider, messaging).
- First-customer channel that does not depend on ads.
- Roadmap in phases, each with a numeric gate (e.g. "50 active, 20 paying").

## 7. Risks and open decisions

- A table of risks with their mitigation. Always include funded competitors and the employer-conflict check from `validate.md`.
- Open decisions, each with your recommendation.

## 8. Sources and handoff

- End with a Sources list of pages actually opened, with an as-of date at the top of the document.
- Run the `verifier` subagent over the document: every figure must match its source, and no section may contradict another.
- Handoff: phase 3 (validate) uses this document; phase 4 (spec) inherits it instead of re-deriving it.

## Rules

- Specifics over adjectives: numbers with units, names, dates.
- Short sentences, tables for comparisons, prose only for reasoning.
- Do not inflate: one mention of a figure in a blog is not a market fact.
- Never use employer or client data. Research only public sources.
