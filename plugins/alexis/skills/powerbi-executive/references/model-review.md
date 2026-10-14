# Semantic model review checklist

## Structure
- [ ] Star schema: facts hold keys and numeric columns; dimensions hold descriptive attributes.
- [ ] No snowflaked dimensions unless justified; flatten small lookups.
- [ ] One dedicated date table, marked as date table, continuous, covering the full fact range.
- [ ] Relationships one-to-many, single direction (dimension → fact). Bidirectional only with a written reason.
- [ ] No ambiguous paths; inactive relationships used only through USERELATIONSHIP in measures.
- [ ] Role-playing dates handled with inactive relationships or separate date tables, documented.

## Columns
- [ ] Technical keys and helper columns hidden.
- [ ] Correct data types; numeric keys over text keys; no high-cardinality text or GUIDs in facts unless needed.
- [ ] Summarize by = None for numeric attributes that are not additive (IDs, years, rates).
- [ ] Sort-by columns set (month name by month number).
- [ ] Calculated columns only when they must filter or slice; otherwise a measure or upstream logic.

## Measures
- [ ] All reported numbers come from explicit measures (no implicit aggregation).
- [ ] A `_Measures` table with display folders by topic.
- [ ] Every measure has a description in business language and a format string.
- [ ] Base measures defined once and reused (e.g. [Revenue], then [Revenue LY], [Revenue YoY %]).

## Size and refresh
- [ ] Remove unused columns and tables (check with VertiPaq Analyzer or the model's statistics).
- [ ] Incremental refresh for large facts; query folding preserved in Power Query.
- [ ] Storage mode chosen deliberately (Import, DirectQuery, Direct Lake) and documented.

## Governance
- [ ] Row-level security roles tested with "View as".
- [ ] Naming: business-friendly, consistent singular/plural, no prefixes like `dim_`/`fact_` in visible names.
- [ ] Lineage to source documented (source table per fact).
