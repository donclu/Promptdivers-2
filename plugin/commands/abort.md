---
description: Stop the current operation, report, and roll back if safe
---

Stop making further changes immediately.

1. Report what was done so far and why the abort was triggered.
2. If the working tree has uncommitted, reversible changes and rollback is safe, offer to revert — do not force-revert without confirmation.
3. Log the abort in `PROJECT_LOG.md` with the reason.
