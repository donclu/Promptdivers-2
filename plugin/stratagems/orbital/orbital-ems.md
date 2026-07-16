# Orbital EMS — Orbital

## Code: `OEM`

> "All units freeze. Nobody moves until command says so."

---

## When to call

- The project is in a **critical state** where any further changes could make things worse.
- A review, audit, or approval is pending and **no edits should happen** until it's resolved.
- Pre-release freeze: the code is "locked" for testing.
- Two agents are conflicting — freeze to sort out the collision.

---

## Inputs

1. **Reason** — why the freeze is needed.
2. **Scope** — entire project or specific modules.
3. **Duration** — until when (human approval, test pass, review complete).
4. **Who can lift** — only the human? A specific condition?

---

## Steps

1. **Announce the freeze:**
   ```
   🚨 ALERT — Orbital EMS deployed
   SCOPE: [entire project / specific modules]
   REASON: [why]
   DURATION: Until [condition]
   NO CHANGES until human says 🚀 GO.
   ```
2. **Log the freeze** in PROJECT_LOG:
   ```markdown
   ### ⚡ SCOPE FREEZE
   - Active since: [timestamp]
   - Reason: [why]
   - Scope: [what's frozen]
   - Lift condition: [when it ends]
   ```
3. **While frozen:**
   - **Read-only operations are OK** (recon, analysis, review).
   - **No file mutations.** No commits. No applies.
   - **Planning is OK** — drafts and specs can be prepared for post-freeze.
   - **SOS Beacon OK** — you can still ask questions.
4. **To lift the freeze:**
   - Human says `🚀 GO` or the lift condition is met.
   - Log: `Freeze lifted at [timestamp]. Reason: [condition met]`.
5. **Log:** `Stratagem: OEM — freeze deployed. Scope: [X]. Lift: [condition]`.

---

## Outputs

- All agents and operations paused on the frozen scope.
- PROJECT_LOG records the freeze period.
- Clear lift condition documented.

---

## Cooldown / limits

- **Only the human can lift a freeze.** An agent cannot unilaterally decide the freeze is over.
- Read-only work continues — don't waste the wait time. Use it for planning, docs, or Resupply.
- If the freeze lasts more than one session, record it in HANDOFF_JSON so the next agent respects it.

---

*"Orbital EMS — sometimes the most democratic thing is to stop."*
