# Resupply — Support

## Code: `RSP`

> "Ammunition low. Calling in a fresh drop of context."

---

## When to call

- The agent's context is **stale** — working off old assumptions or outdated file state.
- A long session has drifted and the agent needs to **re-anchor** to the brief.
- Files have changed externally (human edited, another agent modified, git pull).
- After a break or session resume — something feels off.

---

## Inputs

1. **Trigger** — why context needs refreshing (stale, external changes, session resume, confusion).
2. **Scope** — what to re-read (all, or specific files).

---

## Steps

1. **Re-read `AGENTS.md`** — stack, permissions, constraints. Has anything changed?
2. **Re-read `PROJECT_LOG.md`** — especially the latest session entry and HANDOFF_JSON.
3. **Check target files** — have they been modified since last read? If file modification tracking is available, use it.
4. **Compare** current understanding with fresh state:
   - Any **assumptions** that are now wrong? List them.
   - Any **new constraints** from log updates?
   - Any **drift** from agreed scope?
5. **Emit SITREP** with fresh state:
   ```
   📋 SITREP — Resupply complete
   - AGENTS.md: [fresh | stale in: X]
   - Stack: [confirmed | changed: Y]
   - Target files: [unchanged | modified since last read]
   - Scope: [still locked | drifted: Z]
   ```
6. **Log:** `Stratagem: RSP — context refreshed. Changes: [list or none]`.

---

## Outputs

- Updated internal state aligned with current repo reality.
- SITREP with delta (what changed since last read).
- Any invalidated work flagged.

---

## Cooldown / limits

- No cooldown — call whenever uncertain.
- **Call this before any destructive action** if the session has been running for more than ~30 minutes.
- This is a **read-only** stratagem — it changes no files.

---

*"Resupply — the best soldiers know when to reload."*
