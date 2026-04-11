# Tutorial Mission 05 — Total Democracy (Crisis Response)

## Mission type: Operation Total Democracy

> *"Everything is on fire. Production is down. The CEO is in the chat. This is not a drill."*

---

## Scenario

A critical production incident has occurred. Multiple systems are affected. Normal squad boundaries don't apply — this is **TOTAL DEMOCRACY**, where all resources align on a single objective: **restore service**.

**Difficulty:** ⭐⭐⭐⭐ Helldive  
**Time:** ~60 minutes (simulated; real incidents vary)  
**Stratagems used:** ALL AVAILABLE — this is the loadout where everything drops

---

## Pre-drop checklist

- [ ] `AGENTS.md` exists (you're going to need it)
- [ ] You understand the production architecture (at least roughly)
- [ ] You have access to logs/monitoring (or can describe the symptoms)

---

## Trigger

In any session, say:

```text
TOTAL DEMOCRACY

Production incident:
- What's broken: [describe the symptoms]
- When it started: [approximate time]
- Impact: [who/what is affected]
- Severity: CRITICAL
```

The agent should immediately switch to `protocols/operation-total-democracy.md` mode.

---

## Phase 1 — Triage (first 5 minutes)

### Step 1: Rapid assessment

```text
🚨 ALERT — TOTAL DEMOCRACY active.

Immediate triage:
1. What service/module is most likely the cause?
2. What changed recently? (last deploy, last merge, config change)
3. Can we reproduce locally?
4. What's the blast radius? (one endpoint? entire API? database?)

Do NOT start fixing yet. I need a SITREP first.
```

**Expected result:** One-paragraph situation assessment with most likely root cause.

### Step 2: Classify the threat

```text
Classify this incident:
- Terminid (bug introduced)? → Squad C will fix, Squad D verifies
- Automaton (infra/CI/deploy failure)? → Check deployment pipeline, rollback candidate
- Illuminate (AI-generated code that passed review but is wrong)? → Mind control protocol

Which front are we fighting?
```

---

## Phase 2 — Contain (next 10 minutes)

### Step 3: Decide strategy

```text
Based on triage, pick ONE of:

A) ROLLBACK — revert the last deploy (safest if the cause is recent)
B) HOTFIX — surgical fix, deploy immediately (if root cause is identified)
C) CIRCUIT BREAKER — disable the broken feature, keep rest alive
D) ESCALATE — beyond what we can fix in code (infra, vendor, data corruption)

Which strategy? Show your reasoning.
```

### Step 4: Execute containment

```text
🚀 GO — execute [strategy chosen above].

Rules:
- No scope creep. Fix the incident. NOTHING ELSE.
- If the fix touches >3 files, use Eagle Airstrike (EAS) with explicit file list
- If rollback: show me the exact commands
- If hotfix: show me the diff BEFORE applying
- If circuit breaker: show me what gets disabled

⏸️ HOLD after showing the plan — I approve before you apply.
```

---

## Phase 3 — Verify (next 15 minutes)

### Step 5: Confirm resolution

```text
Containment applied. Now verify:

1. Is the service responding? (expected behavior)
2. Run the relevant tests
3. Check logs — any more errors appearing?
4. Shield Generator (SHG) — add a regression test for this specific failure

📋 SITREP — is the fire out?
```

### Step 6: Smoke test

```text
Run a broader smoke test:
- Hit the main endpoints / flows
- Check related services haven't been affected
- Verify no data corruption occurred
- Confirm metrics/monitoring show recovery

🟢 or 🟡 or 🔴?
```

---

## Phase 4 — Debrief (remaining time)

### Step 7: Post-incident debrief

```text
The fire is (hopefully) out. Full debrief:

1. Timeline: what happened, minute by minute
2. Root cause: what actually broke and why
3. Detection: how did we find out? Could we have found out sooner?
4. Response: what we did, in what order
5. Prevention: what changes prevent this from recurring?
   - New tests added (Shield Generator)?
   - New monitoring/alerts (Guard Dog)?
   - New pre-commit checks (Tesla Tower)?
   - Architecture changes needed (Orbital Barrage for future Squad B)?

Create a POST-INCIDENT REPORT in PROJECT_LOG.md.
```

### Step 8: Close Total Democracy

```text
Eagle Rearm (ERM) — end Operation Total Democracy.

Update PROJECT_LOG.md with:
- Full incident timeline
- HANDOFF_JSON with mission_status: [GREEN if resolved, RED if ongoing]
- DEBT items for follow-up work
- next_recommended: which squad should handle the follow-ups

TOTAL DEMOCRACY is over. Resume normal operations.
```

---

## Debrief

### Expected final state

```
Phase 1 (triage):      PASS — root cause identified quickly
Phase 2 (contain):     PASS — service restored
Phase 3 (verify):      PASS — tests + monitors confirm resolution
Phase 4 (debrief):     PASS — post-incident report filed

mission_status: 🟢 GREEN (resolved) or 🟡 YELLOW (mitigated, follow-up needed)
```

### Key lessons

- **Triage before treatment.** Do not start coding until you understand the problem.
- **Rollback is always an option.** If the last deploy is the cause, revert first, investigate second.
- **One fix, one objective.** Total Democracy focuses *everything* on one problem — no side quests.
- **Prevention > response.** The best part of the debrief is the "how do we prevent this" section.
- **Log everything.** In a crisis, memory fails. Write it down as you go.

### What you learned

- How to trigger and run Operation Total Democracy
- How incident triage maps to the three fronts (Terminids/Automatons/Illuminate)
- How containment strategies work (rollback/hotfix/circuit breaker/escalate)
- How post-incident debriefs drive improvements
- Why Shield Generator + Guard Dog should be called after every incident

---

## The meta-lesson

In Helldivers, TOTAL DEMOCRACY missions are chaotic. Everyone drops at once. Friendly fire is frequent. But the objective is clear and the team converges on it.

In software, production incidents work the same way. The Promptdivers framework doesn't make incidents disappear — it gives you **a common protocol so everyone knows their role**, even when things are on fire.

---

*Promptdivers — FOR SUPER EARTH. FOR DEMOCRACY. o7*
