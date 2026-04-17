import argparse
import json
import os
import re
from dataclasses import dataclass
from typing import Dict, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from io_utils import analyze_csv_physical_lines, csv_line_stats_to_dict, reconcile_rows_read_vs_physical
from numeric_parsing import numeric_stats_to_dict, parse_numeric_messy


INVISIBLE_RE = re.compile(r"[\u0000\u200b\ufeff\u00a0\t]")
MOJIBAKE_RE = re.compile(r"[Ã��]")


@dataclass
class ParseStats:
    parsed_ok: int
    parsed_fail: int


def ensure_dir(p: str) -> None:
    os.makedirs(p, exist_ok=True)


def detect_invisibles(s: pd.Series) -> int:
    s = s.astype("string")
    return int(s.fillna("").str.contains(INVISIBLE_RE).sum())


def detect_mojibake(s: pd.Series) -> int:
    s = s.astype("string")
    return int(s.fillna("").str.contains(MOJIBAKE_RE).sum())


def strip_invisibles(s: pd.Series) -> pd.Series:
    s = s.astype("string")
    return s.fillna("").str.replace(INVISIBLE_RE, "", regex=True).str.strip()


def parse_dates_messy(series: pd.Series) -> Tuple[pd.Series, ParseStats]:
    raw = series.astype("string").fillna("").str.strip()
    iso = pd.to_datetime(raw, errors="coerce", format="%Y-%m-%d")
    dmy = pd.to_datetime(raw, errors="coerce", dayfirst=True)
    mdy = pd.to_datetime(raw, errors="coerce", dayfirst=False)
    parsed = iso.fillna(dmy).fillna(mdy)
    parsed_ok = int(parsed.notna().sum())
    parsed_fail = int(series.shape[0] - parsed_ok)
    return parsed, ParseStats(parsed_ok=parsed_ok, parsed_fail=parsed_fail)


def robust_numeric_summary(x: pd.Series) -> Dict:
    x = x.dropna()
    if x.empty:
        return {"count": 0}

    q = x.quantile([0.01, 0.05, 0.5, 0.95, 0.99]).to_dict()
    q1 = float(x.quantile(0.25))
    q3 = float(x.quantile(0.75))
    iqr = q3 - q1
    lo = q1 - 1.5 * iqr
    hi = q3 + 1.5 * iqr
    outliers = int(((x < lo) | (x > hi)).sum())

    return {
        "count": int(x.shape[0]),
        "min": float(x.min()),
        "max": float(x.max()),
        "mean": float(x.mean()),
        "std": float(x.std(ddof=1)) if x.shape[0] > 1 else 0.0,
        "q01": float(q.get(0.01, np.nan)),
        "q05": float(q.get(0.05, np.nan)),
        "q50": float(q.get(0.5, np.nan)),
        "q95": float(q.get(0.95, np.nan)),
        "q99": float(q.get(0.99, np.nan)),
        "iqr": float(iqr),
        "tukey_outliers": outliers,
        "tukey_lo": float(lo),
        "tukey_hi": float(hi),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="dirty_industrial_sales.csv")
    ap.add_argument("--outdir", default="profile_out")
    ap.add_argument("--max_rows", type=int, default=0)
    args = ap.parse_args()

    ensure_dir(args.outdir)
    plots_dir = os.path.join(args.outdir, "plots")
    ensure_dir(plots_dir)

    phys = analyze_csv_physical_lines(args.csv, expected_fields=10)

    df = pd.read_csv(
        args.csv,
        sep=",",
        engine="python",
        dtype="string",
        on_bad_lines="skip",
    )
    if args.max_rows and args.max_rows > 0:
        df = df.head(args.max_rows)

    metrics = {}
    metrics["shape"] = {"rows": int(df.shape[0]), "cols": int(df.shape[1])}
    metrics["columns"] = list(df.columns)
    metrics["csv_physical"] = csv_line_stats_to_dict(phys)
    metrics["csv_reconcile"] = reconcile_rows_read_vs_physical(
        rows_read_by_pandas=int(df.shape[0]),
        physical_body_lines=int(phys.lines_body),
        estimated_bad_lines=int(phys.estimated_bad_lines),
    )

    col_profile = {}
    for c in df.columns:
        s = df[c].astype("string")
        empty = int(s.fillna("").str.strip().eq("").sum())
        col_profile[c] = {
            "nulls": int(s.isna().sum()),
            "empty_or_ws": empty,
            "nunique": int(s.dropna().nunique()),
        }

    for c in ["invoice_id", "branch_code", "customer_name", "sku_or_service_code"]:
        if c in df.columns:
            col_profile[c]["invisibles_rows"] = detect_invisibles(df[c])
            col_profile[c]["mojibake_rows"] = detect_mojibake(df[c])

    metrics["col_profile"] = col_profile

    parsed = {}
    if "unit_price" in df.columns:
        unit_price_num, st = parse_numeric_messy(df["unit_price"])
        df["_unit_price_num"] = unit_price_num
        parsed["unit_price"] = numeric_stats_to_dict(st)
        metrics["unit_price_summary"] = robust_numeric_summary(unit_price_num)
        metrics["unit_price_flags"] = {
            "negatives": int((unit_price_num < 0).sum()),
            "zeros": int((unit_price_num == 0).sum()),
        }

    if "qty_or_hours" in df.columns:
        qty_num, st = parse_numeric_messy(df["qty_or_hours"])
        df["_qty_num"] = qty_num
        parsed["qty_or_hours"] = numeric_stats_to_dict(st)
        metrics["qty_or_hours_summary"] = robust_numeric_summary(qty_num)
        metrics["qty_or_hours_flags"] = {
            "negatives": int((qty_num < 0).sum()),
            "zeros": int((qty_num == 0).sum()),
        }

    if "invoice_date" in df.columns:
        dts, st = parse_dates_messy(df["invoice_date"])
        df["_invoice_dt"] = dts
        parsed["invoice_date"] = {"parsed_ok": st.parsed_ok, "parsed_fail": st.parsed_fail}
        if st.parsed_ok:
            metrics["invoice_date_range"] = {
                "min": str(dts.min().date()) if pd.notna(dts.min()) else None,
                "max": str(dts.max().date()) if pd.notna(dts.max()) else None,
            }

    metrics["parsed"] = parsed

    def top_counts(col: str, n=10):
        if col not in df.columns:
            return []
        vc = df[col].astype("string").fillna("").value_counts().head(n)
        return [{"value": k, "count": int(v)} for k, v in vc.items()]

    for col in ["country", "branch_code", "line_type", "sku_or_service_code"]:
        metrics[f"top_{col}"] = top_counts(col)

    coherence = {}
    if "country" in df.columns and "branch_code" in df.columns:
        country = strip_invisibles(df["country"])
        branch = strip_invisibles(df["branch_code"])
        # Extract country prefix from branch code and compare
        branch_country = branch.str.extract(r'^([^-]+)', expand=False)
        coherence["country_branch_mismatch"] = int((branch_country != country.astype(str)).sum())

    if "line_type" in df.columns and "sku_or_service_code" in df.columns:
        lt = strip_invisibles(df["line_type"])
        sku = strip_invisibles(df["sku_or_service_code"])
        svc_bad = int(((lt == "SERVICE") & (~sku.str.startswith("SV-"))).sum())
        parts_bad = int(((lt == "PARTS") & (~sku.str.startswith("PART-"))).sum())
        mach_bad = int(((lt == "MACHINE") & (~sku.str.match(r"^(EXC|WHL|BLD|DRL)-"))).sum())
        coherence["sku_mismatch"] = {"service_bad": svc_bad, "parts_bad": parts_bad, "machine_bad": mach_bad}

    metrics["coherence"] = coherence

    metrics_path = os.path.join(args.outdir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    sns.set_theme(style="whitegrid")

    if "country" in df.columns:
        plt.figure(figsize=(8, 4))
        sns.countplot(data=df, x="country", order=df["country"].value_counts().index)
        plt.title("Count by country (raw)")
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, "count_country.png"), dpi=160)
        plt.close()

    if "line_type" in df.columns:
        plt.figure(figsize=(8, 4))
        sns.countplot(data=df, x="line_type", order=df["line_type"].value_counts().index)
        plt.title("Count by line_type (raw)")
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, "count_line_type.png"), dpi=160)
        plt.close()

    if "_unit_price_num" in df.columns:
        x = df["_unit_price_num"].dropna()
        if not x.empty:
            plt.figure(figsize=(8, 4))
            sns.histplot(x=x, bins=60, log_scale=(False, True))
            plt.title("unit_price (parsed) histogram (log y)")
            plt.tight_layout()
            plt.savefig(os.path.join(plots_dir, "hist_unit_price_logy.png"), dpi=160)
            plt.close()

            plt.figure(figsize=(8, 2.8))
            sns.boxplot(x=x)
            plt.title("unit_price (parsed) boxplot")
            plt.tight_layout()
            plt.savefig(os.path.join(plots_dir, "box_unit_price.png"), dpi=160)
            plt.close()

    if "_qty_num" in df.columns:
        x = df["_qty_num"].dropna()
        if not x.empty:
            plt.figure(figsize=(8, 4))
            sns.histplot(x=x, bins=60)
            plt.title("qty_or_hours (parsed) histogram")
            plt.tight_layout()
            plt.savefig(os.path.join(plots_dir, "hist_qty_or_hours.png"), dpi=160)
            plt.close()

            plt.figure(figsize=(8, 2.8))
            sns.boxplot(x=x)
            plt.title("qty_or_hours (parsed) boxplot")
            plt.tight_layout()
            plt.savefig(os.path.join(plots_dir, "box_qty_or_hours.png"), dpi=160)
            plt.close()

    sample_df = df.sample(min(2000, df.shape[0]), random_state=1)
    plt.figure(figsize=(10, 4))
    sns.heatmap(sample_df.isna(), cbar=False)
    plt.title("Missingness heatmap (sample)")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "missingness_heatmap_sample.png"), dpi=160)
    plt.close()

    print(f"Wrote {metrics_path}")
    print(f"Wrote plots to {plots_dir}")
    print("Key signals:")
    print(" - shape:", metrics["shape"])
    print(" - parsed:", metrics.get("parsed", {}))
    print(" - coherence:", metrics.get("coherence", {}))


if __name__ == "__main__":
    main()

