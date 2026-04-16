import argparse
import json
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def ensure_dir(p: str) -> None:
    os.makedirs(p, exist_ok=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clean_csv", default="clean_out/industrial_sales_clean.csv")
    ap.add_argument("--dq_json", default="clean_out/dq_report.json")
    ap.add_argument("--outdir", default="report_out")
    args = ap.parse_args()

    ensure_dir(args.outdir)
    plots = os.path.join(args.outdir, "plots")
    ensure_dir(plots)

    df = pd.read_csv(args.clean_csv)
    with open(args.dq_json, "r", encoding="utf-8") as f:
        dq = json.load(f)

    sns.set_theme(style="whitegrid")

    def savefig(name: str):
        plt.tight_layout()
        plt.savefig(os.path.join(plots, name), dpi=180)
        plt.close()

    for col, fname, title, topn in [
        ("country", "count_country.png", "Ventas (líneas) por país", 20),
        ("line_type", "count_line_type.png", "Distribución por tipo de línea", 20),
        ("branch_code", "count_branch_top20.png", "Top 20 sucursales por volumen", 20),
    ]:
        if col in df.columns:
            plt.figure(figsize=(10, 4))
            order = df[col].value_counts().head(topn).index
            sns.countplot(data=df, x=col, order=order)
            plt.xticks(rotation=35, ha="right")
            plt.title(title)
            savefig(fname)

    if "unit_price_num" in df.columns:
        x = df["unit_price_num"].dropna()
        if not x.empty:
            plt.figure(figsize=(10, 4))
            sns.histplot(x=x, bins=60, log_scale=(False, True))
            plt.title("unit_price_num: histograma (log y)")
            savefig("hist_unit_price_logy.png")

            plt.figure(figsize=(10, 3))
            sns.boxplot(x=x)
            plt.title("unit_price_num: boxplot")
            savefig("box_unit_price.png")

    if "qty_or_hours_num" in df.columns:
        x = df["qty_or_hours_num"].dropna()
        if not x.empty:
            plt.figure(figsize=(10, 4))
            sns.histplot(x=x, bins=60)
            plt.title("qty_or_hours_num: histograma")
            savefig("hist_qty_or_hours.png")

            plt.figure(figsize=(10, 3))
            sns.boxplot(x=x)
            plt.title("qty_or_hours_num: boxplot")
            savefig("box_qty_or_hours.png")

    keys = [
        "rows_read",
        "rows_clean",
        "rows_quarantine",
        "date_parse_fail",
        "unit_price_parse_fail",
        "qty_parse_fail",
        "invoice_id_missing",
        "invoice_id_dupe",
        "country_branch_mismatch",
        "sku_mismatch_service",
        "sku_mismatch_parts",
        "sku_mismatch_machine",
    ]
    dashboard = {k: dq.get(k, None) for k in keys}
    with open(os.path.join(args.outdir, "dq_dashboard.json"), "w", encoding="utf-8") as f:
        json.dump(dashboard, f, indent=2, ensure_ascii=False)

    print(f"Wrote plots to {plots}")
    print(f"Wrote dq dashboard to {os.path.join(args.outdir, 'dq_dashboard.json')}")


if __name__ == "__main__":
    main()

