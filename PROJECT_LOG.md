# PROJECT_LOG — Promptdivers (pack)

Running log for humans and agents. Append new sessions at the **bottom**.

---

## Active constraints

- Current release target: next patch release after 3.3.0
- Branch / environment: `main`
- Anything fragile: installer + docs must stay cross-platform (Bash + PowerShell)

---

## Session: 2026-04-14 — Windows install + pack consistency

### Summary
- Added a PowerShell installer (`install.ps1`) so Windows/PowerShell users can install skills without needing Bash.
- Added `/explain` audit artifacts for the pack review.
- Documented Windows install path in `README.md`, `README-ES.md`, and `docs/MULTI_AGENT_SETUP.md`.
- Dogfooded the pack against itself: added `GALACTIC_WAR_MAP.md`, shipped `.cursor/rules/promptdivers-2.mdc`, and aligned “Helldivers” phrasing to explicit metaphor (no invented canon).
- Release hygiene prepared for `3.3.1` (VERSION/README badge/CHANGELOG) and added `RELEASING.md`.
- Added **parallelism doctrine** for “one planet, multiple missions”: `PRD` (Parallel Drop), `PARALLELISM` budget, and guidance for SOS vs RNF vs ESCALATE when blocked vs wide vs high-risk.

### Decisions
- Keep `install.sh` as the canonical Bash path; `install.ps1` mirrors behavior for PowerShell.
- Prefer conservative “lore”: Helldivers terms are metaphor; avoid asserting in-game canon where not needed.

### Files / areas
- `install.ps1` — PowerShell installer
- `install.sh` — pointer for Windows users
- `README.md`, `README-ES.md`, `docs/MULTI_AGENT_SETUP.md`, `CHANGELOG.md`
- `explain/` — audit artifacts

### DEBT
- [DEBT-001] Add a short “accuracy policy” for Helldivers naming (metaphor vs canon) and run a consistency sweep focused on game naming.
- [DEBT-002] Decide whether to ship a default `.github/copilot-instructions.md` template (or make health-check treat it as optional).

### Follow-ups
- [x] Add `GALACTIC_WAR_MAP.md` at repo root (dogfood) from template
- [x] Add “SOLO vs RNF vs SOS vs ESCALATE” rule to `QUICK_REFERENCE.md`
- [x] Fix “Strategem” spelling typo in `docs/roles-and-field-operatives.md`

---

## HANDOFF_JSON

```json
{
  "schema": "promptdivers-handoff/v2",
  "updated": "2026-04-14T00:00:00Z",
  "mission_last": "D",
  "squad_files_used": ["squads/squad-d-defense.md"],
  "model_used": "AUTO",
  "model_rationale": "documentation + small scripting; prefer fast verification loop",
  "planet_status": {
    "active_fronts": ["Automatons", "Illuminate"],
    "hottest_sector": "installers + docs",
    "threat_level": "MEDIUM"
  },
  "objective": "Make installation and docs consistent across Windows/macOS/Linux without breaking existing usage.",
  "mission_status": "YELLOW",
  "debrief_summary": "Windows install is unblocked (install.ps1) + pack dogfoods itself (GALACTIC_WAR_MAP, Cursor rule). Remaining follow-ups: Copilot instructions template, lore naming sweep in revisa.json.",
  "open_tasks": [
    "Add optional .github/copilot-instructions.md template (or document why it is omitted)",
    "Lore audit `revisa.json` against a conservative ‘metaphor only’ policy (avoid asserting canonicity/mechanics)"
  ],
  "missions_queued": [
    {
      "priority": "primary",
      "squad": "D",
      "nave": "AUTO",
      "objective": "Close loose ends: Cursor rule presence vs docs; optional Copilot instructions; Helldivers naming/lore accuracy policy",
      "spawned_by": null
    }
  ],
  "next_recommended": {
    "squad": "D",
    "nave": "AUTO",
    "reason": "small consistency edits + link hygiene"
  }
}
```

---

*Promptdivers — memory is a weapon.*

---

## Session: 2026-04-15 — Self-audit + onboarding brief + accuracy policy

### Summary
- Added a pack **self-audit** checklist and linked it from field docs.
- Added a **mission brief template** to make “first 10 minutes” copy/paste deterministic.
- Implemented **DEBT-001** with a compact accuracy/metaphor policy; tightened wording that could read as game-canon.
- Reduced duplication by making Reinforce stratagem an **action card** pointing to canonical `protocols/reinforce.md`.

### Decisions
- Canonical governance lives in `protocols/`; `stratagems/` are thin action cards pointing back to protocols when overlap grows.

### Files / areas
- `protocols/pack-self-audit.md` — new dogfooding checklist
- `protocols/accuracy-policy.md` — new metaphor/canon accuracy policy (DEBT-001)
- `templates/mission-brief.template.md` — new brief template
- `FIRST_MISSION.md`, `missions/README.md` — onboarding pointers
- `QUICK_REFERENCE.md` — link to self-audit
- `protocols/tactical-signals.md`, `protocols/friendly-fire.md`, `stratagems/support/reinforce.md` — consistency + de-duplication

### DEBT
- [x] DEBT-001 — accuracy policy shipped (`protocols/accuracy-policy.md`)

---

## Session: 2026-04-15 — Orchestrator Token Gate + Ministry phrasing

### Summary
- Added a **Token Gate** to `promptdivers-orchestrator`: always **normalize a normal user prompt** into a compact brief, then decide **DIRECT vs orchestrator minimum** to reduce token burn.
- When recommending aborting orchestrator, the skill now asks for explicit consent using the **Ministry of Truth** phrasing (abort vs “vamos con todo” override).
- Documented the Token Gate as a checklist item in `docs/prompt-economics.md`.

### Decisions
- Treat “orchestrator” as **opt-in by value**: normalize first, then escalate only when ambiguity/risk/complexity justify it.

### Files / areas
- `skills/promptdivers-orchestrator/SKILL.md`
- `docs/prompt-economics.md`

---

## Session: 2026-04-15 — Industrial sales dirty-data A/B (artifact-first)

### Summary
- Added an **end-to-end dirty data experiment** for industrial machinery sales (construction/mining), designed for **A (normal) vs B (orchestrator)** prompt comparisons.
- Delivered a reproducible pipeline: **generate → profile → clean/quarantine → plots/dashboard**, plus report/audit/recommendation templates.
- Documented the A/B comparison criteria in a single markdown artifact.
- Hardened auditability: **physical CSV line heuristics** + **pandas row reconciliation**, richer **numeric parse diagnostics**, **`run_all.py`**, template **`render_templates.py`**, pinned **`requirements.txt`**, and an **A/B scorecard** template.
- Updated **vendoring installers** (`install.sh`, `install.ps1`) to include `experiments/` in the framework copy.

### Files / areas
- `experiments/industrial-sales-data-quality/` (scripts + templates)
- `install.sh`, `install.ps1` (vendor copy list)
- `PROJECT_LOG.md` (this entry)


