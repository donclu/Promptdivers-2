# Data Strike — Offensive

## Code: `DSK`

> "The numbers don't lie. But they don't talk unless you make them."

---

## When to call

- You have **data files** (CSV, Excel, JSON, databases) that need analysis.
- Building or debugging a **data pipeline** (ETL, cleaning, transformation, validation).
- Producing **metrics, summaries, or visualizations** from raw data.
- Cross-referencing multiple data sources to find patterns or discrepancies.
- Validating data quality: duplicates, missing values, outliers, inconsistencies.

---

## Inputs

1. **Data sources** — paths to files, database connections, API endpoints.
2. **Objective** — what question are you trying to answer with this data?
3. **Output format** — table, chart description, report, cleaned file, new dataset.
4. **Constraints** — sensitive data? Size limits? Required format?

---

## Steps

1. **Reconnaissance — understand the data:**
   ```
   - File format and encoding
   - Row count, column count
   - Column names and types
   - Sample rows (first 5 + last 5)
   - Missing values per column
   - Unique value counts for categorical columns
   ```

2. **Data cleaning (if needed):**
   - Standardize date formats
   - Handle missing values (drop, fill, flag)
   - Remove duplicates
   - Fix encoding issues
   - Normalize text (case, whitespace, accents)

3. **Transformation:**
   - Apply business rules (categorization, filtering, calculated fields)
   - Join/merge multiple sources
   - Aggregate (group by, pivot, rollup)
   - Derive new metrics

4. **Validation:**
   - Row count check: input vs output
   - Null check on critical columns
   - Range check on numeric columns
   - Referential integrity across sources
   - Sample verification: manually check 3-5 random rows

5. **Produce output:**
   - Clean dataset file (if the goal is a cleaned dataset)
   - Summary tables with key metrics
   - Written narrative of findings (pair with humanizer for stakeholder-facing)
   - Visualization descriptions (chart type, axes, key insights)

6. **Log:** `Stratagem: DSK on [data sources]. Rows processed: [N]. Output: [description]`

---

## Outputs

- Cleaned/transformed dataset
- Analysis summary with key findings
- Validation report (row counts, null checks, spot checks)
- Code/script used (for reproducibility)

---

## Cooldown / limits

- No cooldown — use for any data task.
- **Always validate output.** Data transformations are a prime Mind Control vector — the results can look right while being wrong.
- **Never expose sensitive data** in logs or chat. Apply AGENTS.md permissions.
- For large pipelines (>5 transformation steps): use Squad B batch approach.
- Save the transformation script — data work must be **reproducible**.

---

## Pairing with other stratagems

```
IDR (research the data domain) → DSK (analyze the data)
                                     → FRT (document the pipeline)
                                     → SHG (add validation tests)
                                     → ERM (log findings + handoff)
```

---

*"Data Strike — in Super Earth, truth is measured, not guessed."*
