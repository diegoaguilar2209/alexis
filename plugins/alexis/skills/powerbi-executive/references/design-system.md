# Executive dashboard design system

Consulting-grade reports share one principle: the reader gets the message before reading the chart. Everything below serves that.

## Page structure

- **Action title** at the top of every page and visual: a full sentence with the conclusion and a number. "Net revenue grew 12% YoY, driven by digital channels" — not "Revenue".
- **Subtitle line** under the action title: scope, unit, period, source ("USD millions · Jan–Sep 2026 · Source: Finance DWH").
- **One message per page.** If a page needs two messages, it is two pages.
- **Reading order** follows the logic: summary KPIs top-left, the explaining chart below or right, detail last.
- **Footer**: data source, refresh time, definitions link.

## Grid and spacing

- Canvas 1280 × 720 (16:9). Margins 32 px. 12-column grid, 16 px gutters.
- KPI cards: one row, 3-5 cards, equal widths, aligned to the grid.
- Generous white space: if the page feels full, remove a visual rather than shrinking fonts.
- Align every visual edge to the grid; no visual borders or shadows; separate with space, not boxes.

## Typography

- One font family (Segoe UI in Power BI is fine). Sizes: action title 20, visual title 14 semibold, labels 10-11, KPI value 28-32.
- Sentence case everywhere. No all-caps titles.
- Numbers right-aligned in tables, consistent decimals, units in titles not in every cell.

## Color

- Grays carry the structure; ONE accent color carries the message (the bar, line or cell the title talks about).
- Semantic colors only for meaning: good, bad, neutral (variance vs target). Never decorative.
- Max 3-4 categorical colors on a chart; group the rest as "Other".
- Check contrast (text 4.5:1) and do not rely on red/green alone: add sign, arrow or label.

## Chart choice

| Message | Chart |
| --- | --- |
| Change over time | Line (many periods) or column (few periods) |
| Ranking / comparison | Sorted horizontal bar |
| What drove the change between two totals | Waterfall (bridge) |
| Actual vs target | Bullet chart or bar with target marker; variance as a separate signed bar |
| Part of whole (2-3 parts) | Stacked bar; avoid pies beyond 3 slices |
| Distribution | Histogram or box plot |
| Two measures relationship | Scatter with labeled outliers |
| Exact values to look up | Table or matrix with conditional formatting, sparingly |

Avoid: 3D, gauges, donuts with many slices, dual axes with unrelated scales, maps without a geographic question.

## KPI cards

Value, label, variance vs target and vs prior period (signed, colored by meaning), and a sparkline when trend matters. Same layout on every card.

## Interaction

- Slicers in one consistent place (top bar or a collapsible pane), only those that matter, with clear defaults.
- Tooltips add context (definition, prior value) rather than repeating the value.
- Drill-through for detail pages instead of crowding the summary.
- Bookmarks only for genuine alternate views, labeled clearly.

## Review checklist

- [ ] Read only the titles in order: do they tell the full story?
- [ ] Every number traceable to a measure with a description.
- [ ] One accent color per page, used for the message.
- [ ] No visual without a purpose stated in its title.
- [ ] Works at 100% zoom on a laptop and in the mobile layout if it will be used on phones.
