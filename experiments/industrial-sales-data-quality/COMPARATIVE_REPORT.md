## Scope

Compare two prompt/agent styles over the same end-to-end workflow:

- **Agent A (normal)**: direct responses, higher narrative output.
- **Agent B (with `/promptdivers-orchestrator`)**: Token Gate + artifact-first delivery (scripts + JSON + plots).

Domain: **industrial machinery sales** (construction/mining) + parts + services, by country/branch.

## What was delivered (artifact checklist)

### Step 0 — Dirty dataset generator
- **Generator script**: `experiments/industrial-sales-data-quality/generate_dirty_sales_machinery.py`
- **Dirty classes forced**: E1..E10 (≥20 each) + probabilistic noise
- **Output**: `dirty_industrial_sales.csv` + `dirty_industrial_sales.sample120.csv`

### Step 1 — Profiling
- **Profiler script**: `experiments/industrial-sales-data-quality/profile_dirty_industrial_sales.py`
- **Outputs**: `profile_out/metrics.json` + `profile_out/plots/*.png`

### Step 2 — Cleaning + quarantine
- **Cleaner script**: `experiments/industrial-sales-data-quality/clean_dirty_industrial_sales.py`
- **Outputs**: `clean_out/industrial_sales_clean.csv`, `clean_out/industrial_sales_quarantine.csv`, `clean_out/dq_report.json`

### Step 3 — Figures + dashboard
- **Report figures script**: `experiments/industrial-sales-data-quality/make_report_figures.py`
- **Outputs**: `report_out/plots/*.png` + `report_out/dq_dashboard.json`

### Steps 4–5 — Human-facing templates + rendered reports
- **Templates**:
  - `experiments/industrial-sales-data-quality/templates/REPORT.template.md`
  - `experiments/industrial-sales-data-quality/templates/AUDIT_REPORT.template.md`
  - `experiments/industrial-sales-data-quality/templates/RECOMMENDATIONS.template.md`
- **Renderer**: `experiments/industrial-sales-data-quality/render_templates.py`
- **Rendered outputs** (after running `run_all.py`):
  - `report_out/REPORT.md`
  - `report_out/AUDIT_REPORT.md`
  - `report_out/RECOMMENDATIONS.md`

### Ops / reproducibility helpers
- **One-shot runner**: `experiments/industrial-sales-data-quality/run_all.py`
- **Pinned deps**: `experiments/industrial-sales-data-quality/requirements.txt`
- **A/B scorecard template**: `experiments/industrial-sales-data-quality/ab_scorecard.template.csv`

## Comparison (A vs B)

This repo cannot observe UI token counts directly. For a fair comparison:

- **Token economy proxy**:
  - A: typically higher **chat output** (narrative repeated per step)
  - B: higher **initial overhead** (Token Gate brief) but lower repeated output because artifacts carry the payload across steps

### Dimension 1 — Token economy
- **Agent A (normal)**:
  - Good when the task is one-shot and needs no artifact.
  - Cost grows across phases: each step re-states constraints/methods.
- **Agent B (orchestrator)**:
  - Best for multi-step workflows because the content moves into scripts/JSON.
  - Token Gate overhead is amortized across steps.

**Expected winner (this workflow)**: **B** (amortized cost across steps 0→5).

### Dimension 2 — Efficiency & effectiveness
Scored by verifiable criteria:

- **Reproducibility**: can re-run to get same outputs?
- **Auditability**: are there file outputs with evidence?
- **Robustness**: does it handle dirty classes explicitly?
- **Actionability**: is there a pipeline to produce clean/quarantine datasets?

**Agent A (normal)**:
- Strength: immediate explanatory narrative.
- Weakness: evidence often lives only in text unless artifacts are produced intentionally.

**Agent B (orchestrator)**:
- Strength: evidence-first; artifacts enable verification and iteration.
- Weakness: if overused, Token Gate can be overhead on trivial steps.

**Expected winner (this workflow)**: **B** (artifact-first is aligned with the objectives).

### Dimension 3 — Fun / interesting (without losing correctness)
- A can be more playful in prose but risks drifting.
- B can still be fun, but should keep “fun” constrained to templates or summaries, not core code.

**Best practice**: keep playful tone in the report templates; keep scripts strict.

## How to turn this into a measurable A/B

Run both styles against the same steps and record:

- Prompt length (words) + response length (words)
- Artifacts created (yes/no) + number of re-reads needed
- Time-to-first-runnable pipeline (manual stopwatch)
- Quality: does `dq_report.json` + plots align with expected dirty classes?

## Implemented improvements (repo)

These were the highest-leverage gaps for **auditability** + **token-efficient iteration**:

- **Broken-line visibility (heuristic)**:
  - Physical CSV scan: `experiments/industrial-sales-data-quality/io_utils.py`
  - Wired into profiling metrics: `profile_out/metrics.json` via `profile_dirty_industrial_sales.py`
  - Wired into DQ report: `clean_out/dq_report.json` via `clean_dirty_industrial_sales.py`
- **Numeric parsing diagnostics**:
  - Shared parser: `experiments/industrial-sales-data-quality/numeric_parsing.py`
  - Used by profiling + cleaning scripts (flags like percent/scientific/unit suffix/O-substitution/mixed-separator suspicion)
- **Template auto-fill**:
  - `experiments/industrial-sales-data-quality/render_templates.py`
- **Single entrypoint**:
  - `experiments/industrial-sales-data-quality/run_all.py`

### Installer updates (Windows + macOS/Linux)

Vendoring now includes `experiments/` so the lab ships with the pack copy:

- `install.sh` (`vendor_framework` copy list)
- `install.ps1` (`Vendor-FrameworkToProject` copy list)

