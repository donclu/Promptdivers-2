---
description: Pelican window — score objectives PASS/PARTIAL/FAIL, set mission_status, route failures
---

Run the scored close-out in `${CLAUDE_PLUGIN_ROOT}/protocols/mission-debrief.md` (or load the `promptdivers-pelican` skill if installed):

1. Score each objective: PASS / PARTIAL / FAIL, with evidence.
2. Set `mission_status`: GREEN (all PASS) / YELLOW (PARTIAL only) / RED (any FAIL).
3. If not GREEN, route to the stratagem map (Squad B, `sdd-workflow`, `app-auditor`, etc.).
4. Persist `objectives`, `mission_status`, `debrief_summary` in `PROJECT_LOG.md` / `HANDOFF_JSON`.
