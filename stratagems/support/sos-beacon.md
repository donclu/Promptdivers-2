# SOS Beacon — Support

## Code: `SOS`

> "All channels open. Requesting immediate human assistance."

---

## When to call

- The agent is **stuck** — can't proceed without human input.
- A decision requires **judgment** that the agent shouldn't make alone (architecture, business logic, legal).
- Something **unexpected** happened and the agent doesn't have enough context to decide.
- The task is **escalation-worthy** but specific — not a full squad escalation (use `ESCALATE` for that).

---

## Inputs

1. **What I tried** — summary of approaches already attempted.
2. **Why I'm stuck** — specific blocker.
3. **What I need from you** — concrete question(s) for the human.

---

## Steps

1. **Stop work** on the blocked area. Do not guess or improvise.
2. **Formulate the SOS** using this template:
   ```markdown
   ## 🚨 SOS BEACON
   **From:** [CODENAME]
   **Time:** [timestamp]
   **Block severity:** LOW | MEDIUM | HIGH

   ### What I was doing
   [One paragraph]

   ### What went wrong / what I don't know
   [Specific issue]

   ### What I tried
   1. [Attempt 1 — result]
   2. [Attempt 2 — result]

   ### What I need from you
   - [ ] Decision: [specific question]
   - [ ] Information: [what's missing]
   - [ ] Permission: [what I need approval for]

   ### Meanwhile
   [What I can work on while waiting, or "nothing — fully blocked"]
   ```
3. **Emit** `⏸️ HOLD` signal.
4. **If there's unblocked work**, continue on that while waiting.
5. **When human responds**, acknowledge with `o7` and resume.
6. **Log:** `Stratagem: SOS — blocked on [issue]. Resolved: [Y/N]`.

---

## Outputs

- Structured SOS message with specific asks.
- Agent paused on blocked work, optionally continuing unblocked tasks.

---

## Cooldown / limits

- No cooldown — call whenever genuinely stuck.
- **Do not overuse** — if you're sending SOS every 5 minutes, the brief is inadequate. Call Resupply or recommend Squad A re-brief.
- Prefer **one compound SOS** over three small ones — batch your questions.

---

*"SOS Beacon — asking for help is democratic, not weak."*
