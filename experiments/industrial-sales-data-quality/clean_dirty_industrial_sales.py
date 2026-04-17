import argparse
import json
import os
import re
from dataclasses import dataclass, asdict
from typing import Dict, Tuple

import numpy as np
import pandas as pd

from io_utils import analyze_csv_physical_lines, csv_line_stats_to_dict, reconcile_rows_read_vs_physical
from numeric_parsing import parse_numeric_messy


INVISIBLE_RE = re.compile(r"[\u0000\u200b\ufeff\u00a0\t]")
MOJIBAKE_RE = re.compile(r"[Ã��]")


@dataclass
class DQCounts:
    rows_in: int = 0
    rows_read: int = 0
    rows_quarantine: int = 0
    rows_clean: int = 0

    invoice_id_missing: int = 0
    invoice_id_dupe: int = 0

    date_parse_fail: int = 0
    unit_price_parse_fail: int = 0
    qty_parse_fail: int = 0

    invisibles_in_customer_name: int = 0
    mojibake_in_customer_name: int = 0

    country_branch_mismatch: int = 0
    sku_mismatch_service: int = 0
    sku_mismatch_parts: int = 0
    sku_mismatch_machine: int = 0

    unit_price_negative: int = 0
    unit_price_zero: int = 0
    qty_negative: int = 0
    qty_zero: int = 0

    # physical CSV scan + pandas reconciliation (best-effort)
    csv_physical_lines_body: int = 0
    csv_estimated_bad_lines: int = 0
    pandas_estimated_dropped_rows: int = 0

    # numeric parsing diagnostics (row-level counts / suspicion tallies)
    unit_price_had_percent: int = 0
    unit_price_had_scientific: int = 0
    unit_price_had_unit_suffix: int = 0
    unit_price_had_o_substitution: int = 0
    unit_price_mixed_separator_suspect: int = 0

    qty_had_percent: int = 0
    qty_had_scientific: int = 0
    qty_had_unit_suffix: int = 0
    qty_had_o_substitution: int = 0
    qty_mixed_separator_suspect: int = 0


def ensure_dir(p: str) -> None:
    os.makedirs(p, exist_ok=True)


def strip_invisibles(s: pd.Series) -> pd.Series:
    s = s.astype("string")
    return s.fillna("").str.replace(INVISIBLE_RE, "", regex=True).str.strip()


def detect_invisibles(s: pd.Series) -> int:
    s = s.astype("string")
    return int(s.fillna("").str.contains(INVISIBLE_RE).sum())


def detect_mojibake(s: pd.Series) -> int:
    s = s.astype("string")
    return int(s.fillna("").str.contains(MOJIBAKE_RE).sum())


def parse_dates_messy(series: pd.Series) -> pd.Series:
    raw = series.astype("string").fillna("").str.strip()
    iso = pd.to_datetime(raw, errors="coerce", format="%Y-%m-%d")
    dmy = pd.to_datetime(raw, errors="coerce", dayfirst=True)
    mdy = pd.to_datetime(raw, errors="coerce", dayfirst=False)
    return iso.fillna(dmy).fillna(mdy)


def validate_country_branch(country: pd.Series, branch: pd.Series) -> pd.Series:
    c = strip_invisibles(country).str.upper()
    b = strip_invisibles(branch).str.upper()
    # Extract country prefix from branch code and compare
    b_country = b.str.extract(r'^([^-]+)', expand=False)
    return b_country == c


def validate_line_type_sku(line_type: pd.Series, sku: pd.Series) -> Tuple[pd.Series, Dict[str, pd.Series]]:
    lt = strip_invisibles(line_type).str.upper()
    sk = strip_invisibles(sku).str.upper()

    service_ok = ~(lt == "SERVICE") | sk.str.startswith("SV-")
    parts_ok = ~(lt == "PARTS") | sk.str.startswith("PART-")
    machine_ok = ~(lt == "MACHINE") | sk.str.match(r"^(EXC|WHL|BLD|DRL)-")

    all_ok = service_ok & parts_ok & machine_ok
    return all_ok, {"service_ok": service_ok, "parts_ok": parts_ok, "machine_ok": machine_ok}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="dirty_industrial_sales.csv")
    ap.add_argument("--outdir", default="clean_out")
    ap.add_argument("--rows_in", type=int, default=65000)
    ap.add_argument(
        "--strict_quarantine",
        action="store_true",
        help="If set, quarantine any parse/coherence/id failure.",
    )
    args = ap.parse_args()

    ensure_dir(args.outdir)

    phys = analyze_csv_physical_lines(args.csv, expected_fields=10)

    df = pd.read_csv(
        args.csv,
        sep=",",
        engine="python",
        dtype="string",
        on_bad_lines="skip",
    )

    dq = DQCounts(rows_in=args.rows_in, rows_read=int(df.shape[0]))
    dq.csv_physical_lines_body = int(phys.lines_body)
    dq.csv_estimated_bad_lines = int(phys.estimated_bad_lines)
    recon = reconcile_rows_read_vs_physical(
        rows_read_by_pandas=int(df.shape[0]),
        physical_body_lines=int(phys.lines_body),
        estimated_bad_lines=int(phys.estimated_bad_lines),
    )
    dq.pandas_estimated_dropped_rows = int(recon.get("estimated_dropped_rows") or 0)

    if "customer_name" in df.columns:
        dq.invisibles_in_customer_name = detect_invisibles(df["customer_name"])
        dq.mojibake_in_customer_name = detect_mojibake(df["customer_name"])
        df["customer_name_clean"] = strip_invisibles(df["customer_name"])
    else:
        df["customer_name_clean"] = ""

    for c in ["invoice_id", "country", "branch_code", "customer_id", "line_type", "sku_or_service_code"]:
        if c in df.columns:
            df[c] = strip_invisibles(df[c])

    if "country" in df.columns:
        df["country"] = df["country"].str.upper()
    if "line_type" in df.columns:
        df["line_type"] = df["line_type"].str.upper()

    df["_invoice_dt"] = parse_dates_messy(df["invoice_date"]) if "invoice_date" in df.columns else pd.NaT
    if "unit_price" in df.columns:
        up, up_st = parse_numeric_messy(df["unit_price"])
        df["_unit_price_num"] = up
        dq.unit_price_had_percent = int(up_st.had_percent)
        dq.unit_price_had_scientific = int(up_st.had_scientific)
        dq.unit_price_had_unit_suffix = int(up_st.had_unit_suffix)
        dq.unit_price_had_o_substitution = int(up_st.had_o_substitution)
        dq.unit_price_mixed_separator_suspect = int(up_st.mixed_separator_suspect)
    else:
        df["_unit_price_num"] = pd.Series(np.nan, index=df.index)

    if "qty_or_hours" in df.columns:
        qn, qn_st = parse_numeric_messy(df["qty_or_hours"])
        df["_qty_num"] = qn
        dq.qty_had_percent = int(qn_st.had_percent)
        dq.qty_had_scientific = int(qn_st.had_scientific)
        dq.qty_had_unit_suffix = int(qn_st.had_unit_suffix)
        dq.qty_had_o_substitution = int(qn_st.had_o_substitution)
        dq.qty_mixed_separator_suspect = int(qn_st.mixed_separator_suspect)
    else:
        df["_qty_num"] = pd.Series(np.nan, index=df.index)

    dq.date_parse_fail = int(df["_invoice_dt"].isna().sum())
    dq.unit_price_parse_fail = int(df["_unit_price_num"].isna().sum())
    dq.qty_parse_fail = int(df["_qty_num"].isna().sum())

    dq.unit_price_negative = int((df["_unit_price_num"] < 0).sum())
    dq.unit_price_zero = int((df["_unit_price_num"] == 0).sum())
    dq.qty_negative = int((df["_qty_num"] < 0).sum())
    dq.qty_zero = int((df["_qty_num"] == 0).sum())

    if "country" in df.columns and "branch_code" in df.columns:
        ok = validate_country_branch(df["country"], df["branch_code"])
        dq.country_branch_mismatch = int((~ok).sum())
        df["_ok_country_branch"] = ok
    else:
        df["_ok_country_branch"] = True

    if "line_type" in df.columns and "sku_or_service_code" in df.columns:
        ok, parts = validate_line_type_sku(df["line_type"], df["sku_or_service_code"])
        dq.sku_mismatch_service = int((~parts["service_ok"]).sum())
        dq.sku_mismatch_parts = int((~parts["parts_ok"]).sum())
        dq.sku_mismatch_machine = int((~parts["machine_ok"]).sum())
        df["_ok_sku"] = ok
    else:
        df["_ok_sku"] = True

    if "invoice_id" in df.columns:
        dq.invoice_id_missing = int(df["invoice_id"].fillna("").str.strip().eq("").sum())
        non_empty = df["invoice_id"].fillna("").str.strip()
        dupe_mask = non_empty.ne("") & non_empty.duplicated(keep=False)
        dq.invoice_id_dupe = int(dupe_mask.sum())
        df["_invoice_id_dupe"] = dupe_mask
    else:
        df["_invoice_id_dupe"] = False

    fail_any_parse = df["_invoice_dt"].isna() | df["_unit_price_num"].isna() | df["_qty_num"].isna()
    fail_coherence = (~df["_ok_country_branch"]) | (~df["_ok_sku"])
    fail_id = df["invoice_id"].fillna("").str.strip().eq("") | df["_invoice_id_dupe"]

    if args.strict_quarantine:
        quarantine_mask = fail_any_parse | fail_coherence | fail_id
    else:
        quarantine_mask = fail_coherence | fail_id

    quarantine = df[quarantine_mask].copy()
    clean = df[~quarantine_mask].copy()

    keep_cols = [
        "invoice_id",
        "invoice_date",
        "country",
        "branch_code",
        "customer_id",
        "customer_name",
        "line_type",
        "sku_or_service_code",
        "qty_or_hours",
        "unit_price",
    ]
    for c in keep_cols:
        if c not in df.columns:
            df[c] = ""

    clean_out = clean[keep_cols].copy()
    clean_out["invoice_date_iso"] = clean["_invoice_dt"].dt.date.astype("string")
    clean_out["qty_or_hours_num"] = clean["_qty_num"]
    clean_out["unit_price_num"] = clean["_unit_price_num"]
    clean_out["customer_name_clean"] = clean["customer_name_clean"]

    quarantine_out = quarantine[keep_cols].copy()
    quarantine_out["reason_parse_fail"] = fail_any_parse[quarantine_mask].astype("bool").values
    quarantine_out["reason_coherence_fail"] = fail_coherence[quarantine_mask].astype("bool").values
    quarantine_out["reason_id_fail"] = fail_id[quarantine_mask].astype("bool").values

    dq.rows_quarantine = int(quarantine_out.shape[0])
    dq.rows_clean = int(clean_out.shape[0])

    clean_path = os.path.join(args.outdir, "industrial_sales_clean.csv")
    quarantine_path = os.path.join(args.outdir, "industrial_sales_quarantine.csv")
    report_path = os.path.join(args.outdir, "dq_report.json")

    clean_out.to_csv(clean_path, index=False, encoding="utf-8")
    quarantine_out.to_csv(quarantine_path, index=False, encoding="utf-8")

    report_obj = asdict(dq)
    report_obj["csv_physical"] = csv_line_stats_to_dict(phys)
    report_obj["csv_reconcile"] = recon

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report_obj, f, indent=2, ensure_ascii=False)

    print(f"Wrote clean: {clean_path}")
    print(f"Wrote quarantine: {quarantine_path}")
    print(f"Wrote report: {report_path}")
    print("Rows:", {"read": dq.rows_read, "clean": dq.rows_clean, "quarantine": dq.rows_quarantine})


if __name__ == "__main__":
    main()

