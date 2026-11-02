# ALEXIS eval suite

Each case checks that a skill fires on natural phrasing and that its output meets the skill's promise. Run from `plugins/alexis/`:

```bash
claude plugin eval . --runs 1 --ablation none --judge-model sonnet   # quick check
claude plugin eval . --judge-model sonnet       # full: 3 runs per case, with vs. without the plugin
```

Every run is a real model call billed to your plan or API key. `results/` is git-ignored.
A new skill needs at least one trigger case here; a skill change must not lower its case score.

Use `--judge-model sonnet`: the default small judge misreads long, correct answers (seen with `data-contract`).

## Eval cost policy

- Changing a skill: run only its cases (`--case '<skill>-*'`), `--runs 1`.
- Before merging: the quick suite (`--runs 1 --ablation none`).
- The full suite (3 runs, with vs. without the plugin) only before a release.
- Always pass `--max-cost-usd` (e.g. 3 for a partial run, 10 for the quick suite) so a run aborts instead of overspending.
