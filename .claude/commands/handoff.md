---
description: Produce a structured handoff for another agent/session
---

Emit a handoff matching the `HANDOFF_JSON` shape in `templates/project-log.template.md`: open files, decisions, `[DEBT-xxx]` items, mission queue (`missions_queued`), and next mission recommendation.

If a mission was scored this session, carry over `objectives` / `mission_status` / `debrief_summary` from the last `/debrief`. This command is about continuity, not scoring — do not duplicate the full debrief protocol here.
