# Tutorial Mission 02 — Fix a Bug (Surgical Strike)

## Mission type: Squad C (Surgical)

> *"One bug. One file. One clean shot. In and out — no collateral damage."*

---

## Scenario

You have a project with `AGENTS.md` already set up (from Tutorial 01 or manually). A bug has been reported: something is broken and you know roughly where. Time to deploy Squad C for a surgical fix.

**Difficulty:** ⭐⭐ Medium  
**Time:** ~20 minutes  
**Stratagems used:** Resupply (RSP), Orbital Precision Strike (OPS) or Eagle Airstrike (EAS), Shield Generator (SHG), Eagle Rearm (ERM)

---

## Pre-drop checklist

- [ ] Project has `AGENTS.md` (run Tutorial 01 if not)
- [ ] You have a known bug to fix (or pick one from your issue tracker)
- [ ] `PROJECT_LOG.md` exists

---

## Mission briefing

### Objective 1 — Identify the target

Start with a Resupply to make sure context is fresh:

```text
🚀 GO — Squad C mission. Bug fix.

First: Resupply (RSP) — re-read AGENTS.md and PROJECT_LOG.md.

Bug description: [paste your bug description here]

Identify: which file(s) contain the bug? Show me the specific lines.
Keep scope to max 5 files. If it's bigger, ESCALATE.
```

**Expected result:** Agent identifies 1–5 files and pinpoints the problematic code.

---

### Objective 2 — Apply the fix

Based on the scope, choose the right stratagem:

```text
🎯 ON TARGET — fix identified in [file(s)].

If 1 file: call in Orbital Precision Strike (OPS).
If 2-4 files: call in Eagle Airstrike (EAS).

Apply the fix. Show me the diff before committing.
```

**Expected result:** Clean diff showing the fix. No extra changes, no scope creep.

---

### Objective 3 — Defend the fix (add tests)

Don't leave liberated territory undefended:

```text
Now call Shield Generator (SHG) on the fix.

Add test(s) that:
1. Reproduce the original bug (test should FAIL on old code)
2. Verify the fix works (test should PASS on new code)
3. Cover any edge cases exposed by this bug

Run the tests. Show me results.
```

**Expected result:** New test(s) that lock in the fix. All passing.

---

### Objective 4 — Extract

```text
Eagle Rearm (ERM) — close this mission.

Debrief:
- Score each objective
- Update PROJECT_LOG.md
- Produce HANDOFF_JSON
```

**Expected result:** Clean session close with scored debrief.

---

## Debrief

### Expected final state

```
Objective 1 (identify):     PASS — bug located in ≤5 files
Objective 2 (fix):          PASS — clean diff, no scope creep
Objective 3 (test):         PASS — regression test added and passing
Objective 4 (extract):      PASS — PROJECT_LOG updated, HANDOFF_JSON valid

mission_status: 🟢 GREEN
```

### What you learned

- How Squad C keeps scope tight (max 5 files)
- How stratagems chain naturally: RSP → OPS/EAS → SHG → ERM
- How Shield Generator prevents the same bug from returning
- How Eagle Rearm creates continuity for the next session

---

## Stratagem chain used

```
RSP (Resupply)  →  OPS/EAS (fix)  →  SHG (test)  →  ERM (close)
     ↑                                                    ↓
   context                                            handoff
```

---

## Next mission

Try [Tutorial 03 — Refactor a Module](tutorial-03-refactor.md) to learn Squad B (Artillery) and the Forge/Executor split.

---

*Promptdivers — one shot, one kill, one test. FOR DEMOCRACY.*
