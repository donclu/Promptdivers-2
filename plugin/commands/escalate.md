---
description: Escalation ladder — structured escalation to the human or a higher squad
---

Follow `${CLAUDE_PLUGIN_ROOT}/protocols/escalation.md`. Required in the escalation message:

- Evidence (logs, errors, diffs, stack traces) — no escalation without it.
- Severity: LOW / MEDIUM / HIGH / CRITICAL.
- What squad/rung is currently blocked and why.

If this is a production incident or the human invokes it directly, also check `${CLAUDE_PLUGIN_ROOT}/protocols/operation-total-democracy.md` — see `/total-democracy`.
