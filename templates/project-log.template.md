# PROJECT_LOG — [project name]

Running log for humans and agents. Append new sessions at the **top** or **bottom**—pick one convention for your team and keep it.

---

## Active constraints

- Current release target:
- Branch / environment:
- Anything fragile:

---

## Session: [YYYY-MM-DD] — [short title]

### Summary
[What changed in plain language]

### Decisions
- [Decision + why]

### Files / areas
- `path` — note

### DEBT
- [DEBT-xxx] description

### Follow-ups
- [ ] …

### Mission debrief (optional)

Use when this session had **explicit objectives**. See `protocols/mission-debrief.md` (Pelican window).

| Objective | Result | Evidence |
|-----------|--------|----------|
| [label] | PASS / PARTIAL / FAIL | path, test, or note |

**mission_status:** GREEN (all PASS) · YELLOW (any PARTIAL, no FAIL) · RED (any FAIL)

**Next stratagems:** if not GREEN, one line per failed/partial objective → squad or ecosystem skill (see protocol map).

---

## HANDOFF_JSON

Paste a compact machine-friendly blob for the next agent (optional but recommended).

```json
{
  "schema": "promptdivers-handoff/v2",
  "updated": "YYYY-MM-DDTHH:MM:SSZ",
  "mission_last": "C",
  "squad_files_used": ["squads/squad-c-surgical.md"],
  "model_used": "claude-sonnet",
  "model_rationale": "one line — why this ship was chosen",
  "token_budget": "LOW",
  "parallelism": "OFF",
  "planet_status": {
    "active_fronts": ["Terminids"],
    "hottest_sector": "src/auth/",
    "threat_level": "MEDIUM"
  },
  "objective": "one sentence (rollup; keep for quick reads)",
  "objectives": [
    {
      "id": "1",
      "label": "short label",
      "done_when": "observable done criterion",
      "result": "PASS",
      "evidence": "path, test line, or note"
    }
  ],
  "mission_status": "GREEN",
  "debrief_summary": "one line: outcome + what is next if not GREEN",
  "open_tasks": [],
  "debt": ["DEBT-001"],
  "do_not_touch": ["path/or/pattern"],
  "missions_queued": [
    {
      "priority": "primary",
      "squad": "C",
      "nave": "AUTO",
      "objective": "short sentence",
      "spawned_by": null
    },
    {
      "priority": "secondary",
      "squad": "D",
      "nave": "AUTO",
      "objective": "short sentence",
      "spawned_by": "primary"
    }
  ],
  "next_recommended": {
    "squad": "D",
    "nave": "gpt-4o-mini",
    "reason": "short string"
  }
}
```

`planet_status` captures the pre-drop terrain read (optional; omit when no GALACTIC_WAR_MAP exists).
`missions_queued` is the mission queue; `priority` values: `primary`, `secondary`, `tertiary`. `spawned_by` links sub-missions to the mission that revealed them. Add queue items during the mission whenever new work surfaces; do not break the active mission to start them. `next_recommended` is a shortcut to the first queued item — keep for backward compatibility, omit when `missions_queued` is provided. `objectives`, `mission_status`, `debrief_summary`, `model_used`, `model_rationale` are optional; omit for tiny sessions.

---

*Promptdivers — memory is a weapon.*
