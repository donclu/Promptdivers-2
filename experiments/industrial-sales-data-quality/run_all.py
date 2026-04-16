from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_step(*, step_no: int, label: str, cmd: list[str]) -> tuple[bool, str]:
    print("+", " ".join(cmd), flush=True)
    try:
        proc = subprocess.run(cmd, text=True, capture_output=True, check=True)
        out = (proc.stdout or "").strip()
        err = (proc.stderr or "").strip()
        msg = "\n".join([s for s in [out, err] if s])
        return True, msg
    except subprocess.CalledProcessError as e:
        out = (e.stdout or "").strip()
        err = (e.stderr or "").strip()
        msg = "\n".join([s for s in [out, err] if s]) or str(e)
        print(f"🔴 RED — Step {step_no} failed ({label}): {msg}", file=sys.stderr)
        return False, msg


def main() -> None:
    ap = argparse.ArgumentParser(description="Run industrial sales dirty-data pipeline steps 0→3 (+ optional template render).")
    ap.add_argument("--repo_root", default=".", help="Repository root (defaults to cwd).")
    ap.add_argument("--rows", type=int, default=65000)
    ap.add_argument("--seed", type=int, default=1337)
    ap.add_argument("--sample", type=int, default=120)
    ap.add_argument("--strict_quarantine", action="store_true")
    ap.add_argument("--skip_render", action="store_true")
    ap.add_argument(
        "--stop_on_error",
        action="store_true",
        default=True,
        help="Stop immediately on the first failing step (default: True).",
    )
    ap.add_argument(
        "--continue_on_error",
        action="store_true",
        help="Continue running remaining steps even if one fails (overrides --stop_on_error).",
    )
    args = ap.parse_args()

    root = Path(args.repo_root).resolve()
    exp = root / "experiments" / "industrial-sales-data-quality"

    dirty = root / "dirty_industrial_sales.csv"
    profile_out = root / "profile_out"
    clean_out = root / "clean_out"
    report_out = root / "report_out"

    py = sys.executable

    stop_on_error = bool(args.stop_on_error) and (not bool(args.continue_on_error))
    failures: list[tuple[int, str, str]] = []

    steps: list[tuple[int, str, list[str]]] = []
    steps.append(
        (
            0,
            "generate dirty CSV",
            [
                py,
                str(exp / "generate_dirty_sales_machinery.py"),
                "--out",
                str(dirty),
                "--rows",
                str(args.rows),
                "--seed",
                str(args.seed),
                "--sample",
                str(args.sample),
            ],
        )
    )
    steps.append((1, "profile dirty CSV", [py, str(exp / "profile_dirty_industrial_sales.py"), "--csv", str(dirty), "--outdir", str(profile_out)]))

    clean_cmd = [py, str(exp / "clean_dirty_industrial_sales.py"), "--csv", str(dirty), "--outdir", str(clean_out)]
    if args.strict_quarantine:
        clean_cmd.append("--strict_quarantine")
    steps.append((2, "clean + quarantine", clean_cmd))

    steps.append(
        (
            3,
            "make report figures",
            [
                py,
                str(exp / "make_report_figures.py"),
                "--clean_csv",
                str(clean_out / "industrial_sales_clean.csv"),
                "--dq_json",
                str(clean_out / "dq_report.json"),
                "--outdir",
                str(report_out),
            ],
        )
    )

    if not args.skip_render:
        steps.append(
            (
                4,
                "render templates",
                [
                    py,
                    str(exp / "render_templates.py"),
                    "--dq_json",
                    str(clean_out / "dq_report.json"),
                    "--metrics_json",
                    str(profile_out / "metrics.json"),
                    "--templates_dir",
                    str(exp / "templates"),
                    "--outdir",
                    str(report_out),
                    "--warn_unresolved",
                ],
            )
        )

    for step_no, label, cmd in steps:
        ok, msg = run_step(step_no=step_no, label=label, cmd=cmd)
        if not ok:
            failures.append((step_no, label, msg))
            if stop_on_error:
                sys.exit(1)

    if failures:
        print("", file=sys.stderr)
        print("🔴 RED — Pipeline finished with failures:", file=sys.stderr)
        for step_no, label, msg in failures:
            print(f"- Step {step_no} ({label}): {msg}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
