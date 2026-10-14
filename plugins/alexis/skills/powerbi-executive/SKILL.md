---
name: powerbi-executive
description: Audit and redesign a Power BI report to executive, consulting-grade standard - semantic model, DAX measures, table structure and dashboard design (action titles, one message per page, restrained palette, theme JSON). Use when the user shares a Power BI model, PBIP/TMDL files, DAX or screenshots and wants it reviewed, fixed or made "McKinsey-style", elegant or world-class.
argument-hint: "[report goal and audience]"
---

# Power BI executive review

Takes whatever the user can share about a Power BI report and returns a prioritized audit plus a concrete redesign: model fixes, DAX fixes, page-by-page layout, and a theme file. Reply in the user's language.

This skill decides WHAT good looks like. For editing the model or report files themselves, use the tools below when installed (check `/plugin` and `/mcp`):

- **Power BI Modeling MCP** (`microsoft/powerbi-modeling-mcp`): read and change the semantic model, run DAX against it. Needs Power BI Desktop, so on WSL run that session on the Windows side.
- **Microsoft `powerbi-authoring` plugin** (`microsoft/skills-for-fabric`): semantic model authoring, PBIR report authoring and validation, report design brief and planner.
- PBIP project files (TMDL for the model, PBIR for the report) can be read and edited directly as text when the user saves the report as a Power BI Project.

## 1. Intake: get the material (ask once, accept what exists)

Best to worst:
1. PBIP folder (Save as Power BI Project): `*.SemanticModel/definition/*.tmdl` and `*.Report/definition/` — full fidelity.
2. Live model through the Power BI Modeling MCP.
3. Exports: DAX measures (DAX query `EVALUATE INFO.VIEW.MEASURES()`), tables and columns (`INFO.VIEW.TABLES()`, `INFO.VIEW.COLUMNS()`), relationships (`INFO.VIEW.RELATIONSHIPS()`), plus screenshots of every page.
4. Screenshots only: design review only, say so.

Also ask, in the same message: audience, the decision the report supports, the 3-5 KPIs that matter, refresh cadence, and brand colors if any.

## 2. Audit (score each area, findings with evidence)

Use `references/model-review.md` and `references/dax-patterns.md` for the checklists.

| Area | What to check |
| --- | --- |
| Model | Star schema, one-direction relationships, date table marked, no bidirectional filters without reason, no high-cardinality text in facts, hidden technical columns |
| DAX | Measures not calculated columns, variables, DIVIDE, time intelligence on the date table, no nested iterators over large tables, consistent formatting and folders, descriptions |
| Naming | Business names, consistent units and formats, `_Measures` table |
| Design | Against `references/design-system.md`: action titles, hierarchy, chart choice, color discipline, density, accessibility |
| Performance | Visual count per page, slicers, high-cardinality visuals; suggest Performance Analyzer runs |

Output a table: area, score 1-5, top findings with file/measure/page reference, fix, effort (S/M/L).

## 3. Redesign

1. **Storyline**: one sentence per page with the message it must deliver. Page 1 is the executive summary: the 3-5 KPIs with variance vs target and prior period, and the one chart that explains the main movement.
2. **Wireframe per page**: on the 12-column grid from the design system, list each visual with position, chart type, measure, and its action title. Draw it as a Mermaid block or an ASCII grid.
3. **DAX**: write the new or corrected measures, formatted, with descriptions and display folders. Validate them against the model when the MCP is available.
4. **Theme**: start from `assets/executive-theme.json`, swap in brand colors if given (keep one accent color and grays), and save it as `<report>-theme.json` for View → Themes → Browse for themes.
5. **Before/after**: for each page, what changes and why it reads faster.

## 4. Apply (only with the user's go-ahead)

With PBIP files or the MCP: commit the current state first, apply model and DAX changes, re-run the measures to confirm values did not change unintentionally (compare totals before/after), then layout changes. Without them: deliver the measures and a step-by-step change list.

## Rules

- Never change a measure's business logic silently: list every value-changing fix separately and get approval.
- Numbers on the redesign must come from the user's model, not invented examples.
- Work and client reports: keep the material local; do not paste data into public places.
