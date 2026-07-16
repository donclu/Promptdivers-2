---
description: One-session override to Elite-level caps (does not change permanent rank)
---

Grant Elite-level caps for the CURRENT SESSION ONLY, per the escape hatch in `${CLAUDE_PLUGIN_ROOT}/protocols/promotion.md`:

- `max_echelon_rung` → 3, `escalation_budget` → 8, `requires_approval_for` → `[RED_flag]` only.
- Does NOT update `tenure_level` in `${CLAUDE_PLUGIN_ROOT}/AGENT_PROFILE.md`.

THE DEMOCRACY OFFICER logs the override immediately in `experience/integrity/feedback-ledger.yaml` (type: `boundary`). Caps revert automatically at session end — no accumulation toward promotion.
