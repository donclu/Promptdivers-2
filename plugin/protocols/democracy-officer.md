# Democracy Officer — meta-audit protocol

> "Are we actually spreading democracy, or just saying we are?"

---

## What is the Democracy Officer

In the Helldivers-inspired **metaphor** of this framework, a “Democracy Officer” is the role that ensures Super Earth's values are upheld in the field. In agent work, this is a **meta-audit**: checking whether the Promptdivers framework itself is being followed — not just the code.

---

## When to run

- Before a public release or milestone.
- When multiple agents/sessions have been working and consistency needs checking.
- The human says `scope check` or `debt` and wants a thorough answer.
- Periodically (e.g., every 5–10 sessions) as hygiene.

---

## Checklist

### 1. AGENTS.md audit
- [ ] `AGENTS.md` exists and is current (stack matches reality).
- [ ] Permissions block is accurate — no drift from what agents actually do.
- [ ] Model (nave) declaration matches what was used recently.
- [ ] Critical path map matches current repo structure.

### 2. PROJECT_LOG audit
- [ ] Latest session has a summary entry.
- [ ] HANDOFF_JSON exists and has required fields.
- [ ] `mission_status` is set (GREEN/YELLOW/RED).
- [ ] `open_tasks` is up to date.
- [ ] No orphaned `DEBT-xxx` items (all tracked debt acknowledged).

### 3. Session hygiene
- [ ] Recent sessions used appropriate squads (not Squad C for 20-file changes).
- [ ] THE FORGE and THE EXECUTOR were **not** the same agent in Squad B work.
- [ ] Escalations included evidence.
- [ ] Debriefs had verifiable evidence (not "we basically passed").

### 4. Illuminate checks
- [ ] No unreviewed agent output was merged.
- [ ] Agent actions are logged (no shadow operations).
- [ ] Sensitive data was not sent to cloud models without AGENTS.md permission.
- [ ] Agent claims were verified for high-risk areas (security, data, external APIs).

### 5. Framework adoption
- [ ] Tactical signals are being used (not just long prose).
- [ ] Keywords (`status`, `save`, `debrief`) are being honored.
- [ ] DO NOT TOUCH lists are defined in active missions.
- [ ] Scope lock is respected (no silent expansion).

---

## Output

```markdown
## 📋 DEMOCRACY OFFICER REPORT
Date: [timestamp]
Project: [name]

### Score: [Democracy Level]
- 🥇 Super Earth Hero (all checks green)
- 🥈 Skull Admiral (minor gaps)
- 🥉 Helldiver (significant gaps)
- 💀 Cadet (framework barely adopted)

### Findings
| Check | Status | Notes |
|-------|--------|-------|
| AGENTS.md current | ✅ / 🟡 / 🔴 | [note] |
| PROJECT_LOG maintained | ✅ / 🟡 / 🔴 | [note] |
| Squad discipline | ✅ / 🟡 / 🔴 | [note] |
| Illuminate compliance | ✅ / 🟡 / 🔴 | [note] |
| Framework adoption | ✅ / 🟡 / 🔴 | [note] |

### Recommendations
1. [action item]
2. [action item]
```

---

## Who runs it

- **THE SENTINEL** (Squad D) can run this as part of a health check.
- Any agent can **self-check** by reading this protocol.
- The human can request it at any time with: `"Run Democracy Officer check."`

---

*Promptdivers — democracy requires accountability. Even for the agents.*
