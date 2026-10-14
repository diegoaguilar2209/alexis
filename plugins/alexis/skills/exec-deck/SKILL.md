---
name: exec-deck
description: Build executive presentations for data work (results, proposals, steering committees, business cases) with conclusion-first narrative, one message per slide and traceable numbers. Use for any deck aimed at leadership, a committee or judges.
argument-hint: "[topic and audience]"
---

# Executive deck

The `pptx` skill (or a Slides artifact type if available) handles the format. This skill handles the narrative. Reply in the user's language.

## 1. Before designing

Define and confirm with the user in one message:

- Audience and the decision they must make at the end.
- The core message in one sentence with a number ("The new model cut digital campaign cost 18% in 8 weeks").
- Duration and max slides (rule of thumb: 1 slide per 2 minutes).

## 2. Structure (pyramid principle)

1. Title slide with the core message as the title.
2. Executive summary: conclusion, 3 findings with numbers, the decision requested.
3. Minimal context: problem and baseline.
4. Findings: one slide per finding.
5. Recommendation and next steps (owner and date).
6. Appendix: methodology, assumptions, data details.

## 3. Slide rules

- The title is a sentence with the conclusion, not a topic ("Campaign cost fell 18% with the new model", not "Results").
- One chart or one hero number per slide.
- Source and data cut-off date in the footer, always.
- Max 30 words outside the chart.
- Charts: bars to compare, line for trends, waterfall to explain changes in a total; no 3D, no pies with more than 3 parts.

## 4. Quality control

- Every number in the deck is traceable to a query or file (listed in speaker notes).
- Run the `data-validator` subagent on the calculations before closing.
- Read only the titles in order: they must tell the whole story.
