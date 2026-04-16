from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, Tuple

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class NumericParseStats:
    parsed_ok: int
    parsed_fail: int
    had_percent: int
    had_scientific: int
    had_unit_suffix: int
    had_o_substitution: int
    mixed_separator_suspect: int


_PERCENT_RE = re.compile(r"%")
_SCI_RE = re.compile(r"(?i)[e][+-]?\d+")
_UNIT_SUFFIX_RE = re.compile(r"(?i)(kg|lb|lbs|hrs?|h)\s*$")


def _strip_known_units_keep_percent_marker(
    s: pd.Series,
) -> Tuple[pd.Series, pd.Series, pd.Series, pd.Series]:
    raw = s.astype("string").fillna("").str.strip()
    had_percent = raw.str.contains(_PERCENT_RE, na=False)
    had_sci = raw.str.contains(_SCI_RE, na=False)

    # remove percent sign for parsing, but keep had_percent flag
    s2 = raw.str.replace(_PERCENT_RE, "", regex=True)

    # Detect trailing unit tokens like12kg / 8h (common in dirty generator)
    had_unit = s2.str.contains(_UNIT_SUFFIX_RE, na=False)
    s3 = s2.str.replace(_UNIT_SUFFIX_RE, "", regex=True)

    return s3, had_percent, had_sci, had_unit


def parse_numeric_messy(series: pd.Series) -> Tuple[pd.Series, NumericParseStats]:
    raw = series.astype("string")
    s0 = raw.fillna("").str.strip()

    had_o_sub = s0.str.contains("O", na=False)
    s1 = s0.str.replace("O", "0")

    s2, had_percent, had_sci, had_unit = _strip_known_units_keep_percent_marker(s1)

    # remove remaining alphabetic tokens (e.g., stray letters), but keep digits / separators / e
    s3 = s2.str.replace(r"[a-zA-Z]+", "", regex=True)
    s3 = s3.str.replace(r"\s+", "", regex=True)

    # Mixed separator suspicion: more than one '.' or more than one ',' after cleanup
    dot_count = s3.str.count(r"\.")
    comma_count = s3.str.count(r",")
    mixed_suspect = (dot_count > 1) | (comma_count > 1)

    has_dot = s3.str.contains(r"\.")
    has_comma = s3.str.contains(r",")
    eu_mask = has_dot & has_comma & (s3.str.rfind(",") > s3.str.rfind("."))

    eu = s3.where(eu_mask, "")
    eu = eu.str.replace(".", "", regex=False).str.replace(",", ".", regex=False)

    us_mask = has_comma & (~eu_mask)
    us = s3.where(us_mask, "")
    us = us.str.replace(",", "", regex=False)

    plain_mask = ~(eu_mask | us_mask)
    plain = s3.where(plain_mask, "")

    merged = pd.Series(np.where(eu_mask, eu, np.where(us_mask, us, plain)), index=series.index)
    merged = merged.replace({"": np.nan, "-": np.nan, "nan": np.nan, "NaN": np.nan})

    parsed = pd.to_numeric(merged, errors="coerce")

    ok = int(parsed.notna().sum())
    fail = int(series.shape[0] - ok)

    return parsed, NumericParseStats(
        parsed_ok=ok,
        parsed_fail=fail,
        had_percent=int(had_percent.sum()),
        had_scientific=int(had_sci.sum()),
        had_unit_suffix=int(had_unit.sum()),
        had_o_substitution=int(had_o_sub.sum()),
        mixed_separator_suspect=int(mixed_suspect.fillna(False).sum()),
    )


def numeric_stats_to_dict(st: NumericParseStats) -> Dict[str, int]:
    return {
        "parsed_ok": st.parsed_ok,
        "parsed_fail": st.parsed_fail,
        "had_percent": st.had_percent,
        "had_scientific": st.had_scientific,
        "had_unit_suffix": st.had_unit_suffix,
        "had_o_substitution": st.had_o_substitution,
        "mixed_separator_suspect": st.mixed_separator_suspect,
    }
