---
description: Replay tagged operational events for training (induction Phase 4)
---

Run Phase 4 of `${CLAUDE_PLUGIN_ROOT}/protocols/induction.md`: read tagged `experience/operational/` events, predict the outcome before revealing it, then compare. Log predictions in the drill log. Pass gate: ≥2 of 3 predictions broadly correct (squad route, rung, or correction type).
