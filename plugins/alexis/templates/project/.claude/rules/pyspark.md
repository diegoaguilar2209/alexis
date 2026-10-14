---
paths:
  - "src/**/*.py"
  - "**/pipelines/**/*.py"
---

# PySpark / Databricks rules

- Transformations as pure functions `DataFrame -> DataFrame`, testable with small data.
- Explicit schemas (`StructType`) when reading bronze.
- Prefer native `pyspark.sql.functions` over Python UDFs.
- Delta writes with `MERGE` or a bounded `replaceWhere`; never a full `overwrite` of silver/gold without agreement.
- Always three-part table names `catalog.schema.table`, with the catalog parameterized per environment.
- Jobs and pipelines defined in Databricks Asset Bundles (`resources/`), not by hand in the UI.
