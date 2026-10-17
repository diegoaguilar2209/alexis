# ALEXIS eval suite

Each case checks that a skill fires on natural phrasing and that its output meets the skill's promise. Run from `plugins/alexis/`:

```bash
claude plugin eval . --runs 1 --ablation none --judge-model sonnet   # quick check
claude plugin eval . --judge-model sonnet       # full: 3 runs per case, with vs. without the plugin
```

Every run is a real model call billed to your plan or API key. `results/` is git-ignored.
A new skill needs at least one trigger case here; a skill change must not lower its case score.

Use `--judge-model sonnet`: the default small judge misreads long, correct answers (seen with `data-contract`).
