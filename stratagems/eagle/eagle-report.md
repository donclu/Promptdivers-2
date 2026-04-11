# Eagle Report — Eagle

## Code: `ERP`

> "Drop in hot. Deliver the report. Extract before anyone asks for revisions."

---

## When to call

- You need to produce a **formal deliverable** from work already done: report, executive summary, memo, writeup.
- Turning raw findings (intel dossier, data analysis, audit results) into **stakeholder-ready** output.
- Generating docs in a specific format: Markdown report, slide outline, PDF-ready content.
- Writing changelogs, release notes, or project summaries from session history.

---

## Inputs

1. **Source material** — what has already been produced (analysis, audit, data, PROJECT_LOG).
2. **Audience** — who reads this? (Technical team / leadership / external / public)
3. **Format** — Markdown report / slide outline / executive brief / detailed technical doc.
4. **Voice** — formal, casual, Helldivers-themed, or calibrated (use onboarding-calibration.md).
5. **Length** — brief (1 page) / standard (3-5 pages) / detailed (longer).

---

## Steps

1. **Gather source material:**
   - Read PROJECT_LOG for session history
   - Read any analysis, audit, or dossier outputs from this or previous sessions
   - Collect relevant metrics, screenshots, diff summaries

2. **Structure the report:**
   ```markdown
   ## [REPORT TITLE]
   Date: [date]
   Author: [CODENAME] for [human/team]

   ### Executive Summary
   [3 sentences max: what was done, what was found, what's recommended]

   ### Background
   [Context the reader needs]

   ### Findings / Results
   [Tables, metrics, key observations — with evidence]

   ### Recommendations
   [Actionable next steps, prioritized]

   ### Appendix (optional)
   [Raw data, detailed tables, full test results]
   ```

3. **Apply voice calibration (if audience is non-technical):**
   - Check `docs/onboarding-calibration.md` — was AI-likeness/creativity set?
   - If set to LOW AI-likeness: load humanizer principles — vary rhythm, drop connector words, sound human
   - If set to HIGH AI-likeness: keep structured and polished

4. **Review and verify:**
   - Every metric cited has a source
   - Every recommendation has supporting evidence
   - No jargon the audience won't understand (or define it)
   - Length matches the request

5. **Log:** `Stratagem: ERP — Report on [topic] for [audience]. Format: [type]. Length: [pages]`

---

## Outputs

- Formatted report document (Markdown or specified format)
- Source attribution for all claims
- Ready for human review and distribution

---

## Cooldown / limits

- No cooldown — generate reports as needed.
- **Do not fabricate data.** If a metric isn't available, say so — don't approximate.
- If voice calibration wasn't done: default to professional but clear. Ask if unsure.
- For public-facing reports: always have human review before distribution.

---

*"Eagle Report — the pen is mightier than the stratagem. Almost."*
