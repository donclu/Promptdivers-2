---
description: Update PROJECT_LOG + handoff so a fresh agent/session can continue
---

Append to `PROJECT_LOG.md`: decisions made, bugs fixed, discoveries, patterns to avoid this session.

Update the handoff block (shape in `${CLAUDE_PLUGIN_ROOT}/templates/project-log.template.md`) so a new agent can resume cold.

If objectives were explicit for this session, include a short debrief (PASS/PARTIAL/FAIL per objective) per `${CLAUDE_PLUGIN_ROOT}/protocols/mission-debrief.md` before closing the log entry — see `/debrief` for the full scored version.
