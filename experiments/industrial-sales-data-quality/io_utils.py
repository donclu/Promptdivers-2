from __future__ import annotations

import csv
import os
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(frozen=True)
class CsvLineStats:
    file_path: str
    bytes: int
    lines_total: int
    lines_body: int  # excluding header
    lines_empty_body: int
    field_sep_comma: int
    field_sep_semicolon: int
    field_sep_tab: int
    comma_fields_ne10: int
    estimated_bad_lines: int


def _open_text(path: str):
    # utf-8-sig handles BOM if present
    return open(path, "r", encoding="utf-8-sig", newline="")


def analyze_csv_physical_lines(csv_path: str, expected_fields: int = 10) -> CsvLineStats:
    """
    Physical scan of a CSV file without pandas.

    Notes:
    - This is a heuristic for "broken lines" when the generator mixes delimiters.
    - `estimated_bad_lines` = body lines that are not clearly10 comma-separated fields.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(csv_path)

    size = os.path.getsize(csv_path)

    total = 0
    body = 0
    empty_body = 0

    sep_comma = 0
    sep_semicolon = 0
    sep_tab = 0

    comma_fields_ne10 = 0

    with _open_text(csv_path) as f:
        for line in f:
            total += 1
            if total == 1:
                continue  # header
            body += 1
            s = line.rstrip("\r\n")
            if s.strip() == "":
                empty_body += 1
                comma_fields_ne10 += 1
                continue

            if "\t" in s:
                sep_tab += 1
            if ";" in s:
                sep_semicolon += 1
            if "," in s:
                sep_comma += 1

            # Prefer csv.reader so commas inside quotes don't inflate field counts.
            # If a line uses a non-comma delimiter, treat it as suspicious for a comma-CSV.
            if "\t" in s or ";" in s:
                comma_fields_ne10 += 1
                continue

            try:
                parsed = next(csv.reader([s], delimiter=",", quotechar='"', escapechar="\\"))
                if len(parsed) != expected_fields:
                    comma_fields_ne10 += 1
            except Exception:
                comma_fields_ne10 += 1

    est_bad = comma_fields_ne10

    return CsvLineStats(
        file_path=csv_path,
        bytes=size,
        lines_total=total,
        lines_body=body,
        lines_empty_body=empty_body,
        field_sep_comma=sep_comma,
        field_sep_semicolon=sep_semicolon,
        field_sep_tab=sep_tab,
        comma_fields_ne10=comma_fields_ne10,
        estimated_bad_lines=est_bad,
    )


def csv_line_stats_to_dict(stats: CsvLineStats) -> Dict[str, object]:
    return {
        "file_path": stats.file_path,
        "bytes": stats.bytes,
        "lines_total": stats.lines_total,
        "lines_body": stats.lines_body,
        "lines_empty_body": stats.lines_empty_body,
        "field_sep_comma": stats.field_sep_comma,
        "field_sep_semicolon": stats.field_sep_semicolon,
        "field_sep_tab": stats.field_sep_tab,
        "comma_fields_ne10": stats.comma_fields_ne10,
        "estimated_bad_lines": stats.estimated_bad_lines,
    }


def reconcile_rows_read_vs_physical(
    *,
    rows_read_by_pandas: int,
    physical_body_lines: int,
    estimated_bad_lines: int,
) -> Dict[str, Optional[int]]:
    """
    Best-effort reconciliation:
    - If pandas skipped bad lines, `rows_read_by_pandas` may be < `physical_body_lines`.
    """
    dropped = None
    if physical_body_lines >= 0 and rows_read_by_pandas >= 0:
        dropped = max(0, int(physical_body_lines) - int(rows_read_by_pandas))

    return {
        "physical_body_lines": int(physical_body_lines),
        "pandas_rows_read": int(rows_read_by_pandas),
        "pandas_minus_physical": int(rows_read_by_pandas - physical_body_lines),
        "estimated_dropped_rows": dropped,
        "estimated_bad_lines_heuristic": int(estimated_bad_lines),
    }
