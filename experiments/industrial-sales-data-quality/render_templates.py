from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict


_PLACEHOLDER_RE = re.compile(r"\{([a-zA-Z0-9_]+)\}")


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def flatten_metrics(metrics: Dict[str, Any]) -> Dict[str, Any]:
    flat: Dict[str, Any] = {}
    shape = metrics.get("shape") or {}
    if isinstance(shape, dict):
        flat["profile_rows"] = shape.get("rows")
        flat["profile_cols"] = shape.get("cols")

    phys = metrics.get("csv_physical") or {}
    if isinstance(phys, dict):
        flat["csv_bytes"] = phys.get("bytes")
        flat["csv_lines_body"] = phys.get("lines_body")
        flat["csv_estimated_bad_lines"] = phys.get("estimated_bad_lines")
        flat["csv_field_sep_tab"] = phys.get("field_sep_tab")
        flat["csv_field_sep_semicolon"] = phys.get("field_sep_semicolon")

    recon = metrics.get("csv_reconcile") or {}
    if isinstance(recon, dict):
        flat["pandas_estimated_dropped_rows_profile"] = recon.get("estimated_dropped_rows")

    return flat


def render_template(template_text: str, ctx: Dict[str, Any]) -> str:
    def repl(m: re.Match) -> str:
        key = m.group(1)
        if key not in ctx or ctx[key] is None:
            return "{" + key + "}"
        return str(ctx[key])

    return _PLACEHOLDER_RE.sub(repl, template_text)


def unresolved_placeholders(rendered_text: str) -> set[str]:
    return set(_PLACEHOLDER_RE.findall(rendered_text))


def pct(n: Any, d: Any) -> Any:
    try:
        n_i = int(n)
        d_i = int(d)
        if d_i <= 0:
            return None
        return round((n_i / d_i) * 100.0, 2)
    except Exception:
        return None


def enrich_ctx_with_percentages(ctx: Dict[str, Any]) -> None:
    rows_read = ctx.get("rows_read")
    for k in [
        "date_parse_fail",
        "unit_price_parse_fail",
        "qty_parse_fail",
        "invoice_id_missing",
        "invoice_id_dupe",
        "country_branch_mismatch",
        "sku_mismatch_service",
        "sku_mismatch_parts",
        "sku_mismatch_machine",
    ]:
        ctx[f"{k}_pct"] = pct(ctx.get(k), rows_read)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dq_json", required=True)
    ap.add_argument("--metrics_json", required=True)
    ap.add_argument("--templates_dir", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument(
        "--warn_unresolved",
        action="store_true",
        help="Print warnings if placeholders remain after render (recommended).",
    )
    args = ap.parse_args()

    dq_path = Path(args.dq_json)
    metrics_path = Path(args.metrics_json)
    tpl_dir = Path(args.templates_dir)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    dq = load_json(dq_path)
    metrics = load_json(metrics_path)

    ctx: Dict[str, Any] = {}
    ctx.update(dq)
    ctx.update({f"profile_{k}": v for k, v in flatten_metrics(metrics).items()})
    enrich_ctx_with_percentages(ctx)

    mapping = {
        "REPORT.template.md": "REPORT.md",
        "AUDIT_REPORT.template.md": "AUDIT_REPORT.md",
        "RECOMMENDATIONS.template.md": "RECOMMENDATIONS.md",
    }

    for src_name, dest_name in mapping.items():
        src = tpl_dir / src_name
        dest = outdir / dest_name
        text = src.read_text(encoding="utf-8")
        rendered = render_template(text, ctx)
        missing = unresolved_placeholders(rendered)
        if args.warn_unresolved and missing:
            print(
                f"[render_templates] WARNING: unresolved placeholders in {dest_name}: {sorted(missing)}",
                file=sys.stderr,
            )
        dest.write_text(rendered, encoding="utf-8")

    print(f"Wrote rendered reports to {outdir}")


if __name__ == "__main__":
    main()
