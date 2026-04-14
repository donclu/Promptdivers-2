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

