# Data agents ("ask your data") and retrieval

## Semantic layer before raw text-to-SQL
- The failure that matters: raw text-to-SQL fails **silently** with plausible wrong numbers; a semantic layer fails **visibly** (out of scope) and never returns invalid data.
- dbt Labs benchmark (2026, reproducible: `dbt-labs/dbt-llm-sl-bench`; note the vendor sells a semantic layer): after modeling, text-to-SQL 84–90% vs semantic layer 98–100% on in-scope questions. Higher reasoning effort added latency, not accuracy.
- Architecture:
  1. Accuracy-critical (KPIs, board, regulatory, finance): the agent may only query governed metrics (dbt Semantic Layer, Databricks metric views / Genie with curated instructions, Power BI semantic model, Cube, Snowflake semantic views).
  2. Exploration: try the semantic layer first; if out of scope, check whether a small model change closes the gap; only then fall back to text-to-SQL with curated schema context, clearly labeled as unverified.
- One definition per metric (use `/alexis:metric-definition`); the agent cites which definition it used.

## Making text-to-SQL safer when you need it
- Retrieve only relevant tables/columns (catalog descriptions, sample values, join paths) instead of the whole schema.
- Curated example question → SQL pairs from the real workload (verified queries).
- Read-only credentials of the end user; row limits; query cost limits; `EXPLAIN` or dry run before execution.
- Validate results: row counts, null checks, reconciliation against a known total.
- Show the SQL and the definitions used next to the answer.

## Databricks specifics
- Genie spaces: curate tables, instructions, example SQL and trusted assets; benchmark questions in the space's evaluation tab.
- Managed MCP (Genie, DBSQL, Unity Catalog functions, Vector Search) exposes them to any MCP agent with Unity Catalog permissions of the calling user.
- Similar on other clouds: Gemini Enterprise querying BigQuery/AlloyDB/Spanner through MCP with each user's credentials (preview, Oct 2026).

## Retrieval (RAG) choices
| Situation | Default |
| --- | --- |
| General Q&A over documents | Hybrid search (BM25 + embeddings) + reranker, contextual chunk headers, agentic search (the agent reformulates and searches again) |
| Multi-hop questions over entities and relations | GraphRAG for the high-value subset only; indexing is expensive (hours, >$13 per million tokens reported) |
| Structured data | Query it (above); do not embed tables |
| Very large corpora with exact terms (codes, IDs) | Keep lexical search in the mix; embeddings miss exact identifiers |

Evidence: a 2026 benchmark found agentic search closes most of the gap between dense RAG and GraphRAG on general QA; GraphRAG still leads on multi-hop (arXiv 2604.09666).

Evaluate retrieval separately (recall@k, citation correctness) from generation.
