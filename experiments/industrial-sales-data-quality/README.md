# Industrial sales — dirty data pipeline (Prompt comparativa)

This experiment generates a **dirty** dataset (65,000 × 10) for industrial machinery sales (construction/mining), then runs:

- **Step 0**: data generation (dirty CSV + sample)
- **Step 1**: profiling (metrics + plots)
- **Step 2**: cleaning + quarantine (clean CSV + quarantine CSV + dq report)
- **Step 3**: report figures + dashboard
- **Step 4**: audit report template
- **Step 5**: recommendations template

It is designed to support a comparison between:

- **Agent A (normal)**: tends to produce narrative text (low artifact output)
- **Agent B (with `/promptdivers-orchestrator`)**: prefers **artifact-first** delivery (scripts + JSON + plots) to reduce repeated tokens across phases.

## Quickstart (macOS/Linux)

From repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r experiments/industrial-sales-data-quality/requirements.txt

python experiments/industrial-sales-data-quality/run_all.py --repo_root .
```

### Manual steps (optional)

```bash
python experiments/industrial-sales-data-quality/generate_dirty_sales_machinery.py \
  --out dirty_industrial_sales.csv --rows 65000 --seed 1337 --sample 120

python experiments/industrial-sales-data-quality/profile_dirty_industrial_sales.py \
  --csv dirty_industrial_sales.csv --outdir profile_out

python experiments/industrial-sales-data-quality/clean_dirty_industrial_sales.py \
  --csv dirty_industrial_sales.csv --outdir clean_out

python experiments/industrial-sales-data-quality/make_report_figures.py \
  --clean_csv clean_out/industrial_sales_clean.csv \
  --dq_json clean_out/dq_report.json \
  --outdir report_out

python experiments/industrial-sales-data-quality/render_templates.py \
  --dq_json clean_out/dq_report.json \
  --metrics_json profile_out/metrics.json \
  --templates_dir experiments/industrial-sales-data-quality/templates \
  --outdir report_out
```

## Quickstart (Windows — PowerShell)

From repo root:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -r experiments/industrial-sales-data-quality/requirements.txt

python experiments/industrial-sales-data-quality/run_all.py --repo_root .
```

## Outputs

- `dirty_industrial_sales.csv`
- `dirty_industrial_sales.sample120.csv`
- `profile_out/metrics.json`
- `profile_out/plots/*.png`
- `clean_out/industrial_sales_clean.csv`
- `clean_out/industrial_sales_quarantine.csv`
- `clean_out/dq_report.json`
- `report_out/plots/*.png`
- `report_out/dq_dashboard.json`
- `report_out/REPORT.md` (rendered)
- `report_out/AUDIT_REPORT.md` (rendered)
- `report_out/RECOMMENDATIONS.md` (rendered)

## Notes

- The generator **forces** at least 20 occurrences of each dirty-data class (invisibles, mojibake, cross-locale numerics, O↔0, NaN/%/units, multi-format/invalid dates, null/duplicate IDs, outliers, broken lines).
- The cleaning step supports two quarantine modes:
  - default: quarantine coherence/id failures, keep parse failures but flagged in derived columns
  - `--strict_quarantine`: quarantine any parse/coherence/id failure

### Installer note (vendoring)

If you vendor the pack into a consumer repo via:

- `./install.sh --project <dir> --vendor-framework`, or
- `pwsh -File ./install.ps1 -Project <dir> -VendorFramework`

…the `experiments/` directory is included in the vendored framework copy (so this dataset lab travels with the pack).

