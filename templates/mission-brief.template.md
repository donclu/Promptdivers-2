# Mission brief — template

Copy/paste this into a chat message, `NEXT_MISSION.md`, or a session block in `PROJECT_LOG.md`.
Keep it short: objectives + scope boundaries + evidence rules.

```text
COMMS_MODE: STANDARD | RADIO
TOKEN_BUDGET: LOW | MED | HIGH
PARALLELISM: OFF | 2_AGENTS | 3_AGENTS

SQUAD: A | B | C | D
NAVE: CLASS A | CLASS B | CLASS C | AUTO

DO_NOT_TOUCH:
  - [paths or globs]

OBJECTIVES:
  - OBJECTIVE: [short label]
    DONE_WHEN: [observable condition]
    SCOPE: [paths]
    EVIDENCE: [tests, output, file paths]

  - OBJECTIVE: [...]
    DONE_WHEN: [...]
    SCOPE: [...]
    EVIDENCE: [...]

CONSTRAINTS:
  - No invented APIs/paths/flags: if unsure, search + cite.
  - If scope grows beyond ~5 files (or risk rises): ESCALATE.
  - End-of-phase: run debrief (PASS/PARTIAL/FAIL) + update PROJECT_LOG/HANDOFF_JSON.
```

**Canonical debrief:** `protocols/mission-debrief.md`  
**Pre-drop (if planet state exists):** `protocols/pre-drop.md`

