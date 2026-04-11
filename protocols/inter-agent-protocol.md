# Inter-agent protocol

All agents in a Promptdivers operation use a **shared message grammar** so sessions, subagents, and humans can scan traffic quickly.

**Tactical layer:** Prefer a **signal lead** (emoji + one line) before detail—same idea as in-game pings when the squad does not share one language. See [tactical-signals.md](tactical-signals.md).

---

## Format

```text
[CODENAME] → [DESTINATION] | TYPE | Message body
```

Optional compact prefix (human or agent):

```text
[SIGNAL] [CODENAME] → [DESTINATION] | TYPE | Message body
```

Example: `🟢 [THE AUDITOR] → [HUMAN] | CONFIRM | PR approved; notes below.`

- **CODENAME** — who sends (e.g. `THE AUTHENTIC`, `THE FORGE`, `THE MARKSMAN`).
- **DESTINATION** — who should act (`THE EXECUTOR`, `THE AUDITOR`, `ALL`, `HUMAN`).
- **TYPE** — one of the types below.
- **Message body** — concrete, short, actionable.

---

## Message types

| Type | Meaning |
|------|---------|
| `SITREP` | What is true right now |
| `INTEL` | Facts, constraints, file paths, risks (no request yet) |
| `REQUEST` | Please do X next |
| `CONFIRM` | X is done / approved / rejected with reason |
| `ESCALATE` | Beyond current squad; needs human or heavier squad |
| `ABORT` | Stop; unsafe or wrong operation |

---

## ESCALATE requirements

Every `ESCALATE` must include:

1. **Situation** — what the squad was doing  
2. **Problem** — what broke or does not fit  
3. **Evidence** — logs, errors, stack traces, file paths  
4. **Suggested level** — see `escalation.md`  
5. **Severity** — LOW / MEDIUM / HIGH / CRITICAL  

---

## Example thread

```text
[THE AUTHENTIC] → [THE SCOUT] | INTEL |
  Brief loaded. Stack: […]. Goal: […]. Map: services/, apps/web/, packages/core/.
  GO.

[THE SCOUT] → [THE ARCHITECT] | SITREP |
  INTEL_REPORT ready. Unknown: auth refresh flow in packages/core. GO.

[THE FORGE] → [THE EXECUTOR] | REQUEST |
  Drafts in /drafts/batch-1. Apply in order. Do not run migrations until CONFIRM.

[THE EXECUTOR] → [THE FORGE] | ESCALATE |
  Migration conflicts with local schema. Evidence: … Suggested: Squad C for migration only.
```

---

*Promptdivers — clear comms save lives (and rollbacks).*
