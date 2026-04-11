# Tutorial Mission 03 — Refactor a Module (Artillery Barrage)

## Mission type: Squad B (Artillery)

> *"This is not a fix. This is a coordinated bombardment. THE FORGE plans. THE EXECUTOR applies. Nobody does both."*

---

## Scenario

A module in your project needs a major refactor — maybe a framework migration, an API redesign, or a large-scale pattern change affecting 10+ files. This is Squad B territory with strict role separation.

**Difficulty:** ⭐⭐⭐ Hard  
**Time:** ~45 minutes  
**Stratagems used:** Eagle Smoke (ESS), Resupply (RSP), Orbital Barrage (ORB) or Eagle Airstrike (EAS) ×N, Shield Generator (SHG), Autocannon (ACN), Eagle Rearm (ERM)

---

## Pre-drop checklist

- [ ] `AGENTS.md` exists with current stack
- [ ] `PROJECT_LOG.md` has latest handoff
- [ ] You know what needs refactoring and roughly how many files
- [ ] You have tests (or accept the risk — mark as DEBT if not)

---

## Mission briefing

### Objective 0 — Deploy smoke cover

**Before anything else**, create a safety branch:

```text
🚀 GO — Squad B mission. Major refactor.

First: call Eagle Smoke Strike (ESS).
Create branch: refactor/[describe-what-you're-changing]
Base: main (or your default branch)
```

**Expected result:** You're on a feature branch. Main is safe.

---

### Objective 1 — THE FORGE: plan the batches

This is the **planning phase** — no code changes yet:

```text
Activate THE FORGE role.

I need to refactor [describe the change].
Affected area: [module/directory]

Plan the operation:
1. Map all files that need to change
2. Group them into batches of 3-5 files (dependency order)
3. For each batch: list the files, describe the change, rate risk (LOW/MEDIUM/HIGH)
4. Identify the test strategy per batch

Show me the batch plan. Do NOT start applying yet.
```

**Expected result:** A clear batch-by-batch plan. Review it. Adjust if needed. Say `🚀 GO` only when satisfied.

---

### Objective 2 — THE EXECUTOR: apply batch by batch

**Critical rule:** The agent switches from FORGE to EXECUTOR role. In a real multi-agent setup, this would be a different agent entirely.

```text
Activate THE EXECUTOR role.
Apply BATCH 1 from the plan above.

After applying:
1. Show me the diffs
2. Run tests
3. Report: 📋 SITREP — BATCH 1 status

Do NOT proceed to BATCH 2 until I say 🚀 GO.
```

**Repeat for each batch.** Between batches, you review and approve:

```text
🟢 GREEN — BATCH 1 looks good. 🚀 GO — BATCH 2.
```

or

```text
🔴 RED — BATCH 1 broke tests. ⏸️ HOLD — fix before continuing.
```

**Expected result:** Each batch applied, tested, and approved sequentially.

---

### Objective 3 — Clean up and fortify

After all batches are applied:

```text
Final pass:
1. Call Autocannon (ACN) — lint and format all changed files
2. Call Shield Generator (SHG) — add or update tests for the refactored code
3. Run the full test suite — not just per-batch tests
4. Report: 📋 SITREP — final status
```

**Expected result:** Clean, formatted, tested code. Full suite green.

---

### Objective 4 — Extract

```text
Eagle Rearm (ERM) — close this mission.

Debrief:
- Score each batch + overall objectives
- Update PROJECT_LOG.md with the full refactor record
- Note which batches were smooth and which needed rework
- Produce HANDOFF_JSON
```

---

## Debrief

### Expected final state

```
Objective 0 (smoke):    PASS — on feature branch
Objective 1 (plan):     PASS — batch plan approved
Objective 2 (execute):  PASS — all batches applied and tested
Objective 3 (fortify):  PASS — lint clean, tests green
Objective 4 (extract):  PASS — PROJECT_LOG complete

mission_status: 🟢 GREEN
```

### Key lesson: FORGE ≠ EXECUTOR

The single most important Squad B rule: **the planner should not be the applier in the same run.** In a single-agent setup, you enforce this by doing Objective 1 (plan) completely before allowing Objective 2 (apply). In a multi-agent setup, use different sessions.

Why? Because the planner sees the whole picture. The executor gets tunnel vision on the current file. Mixing the roles leads to scope creep, missed dependencies, and friendly fire.

### What you learned

- How Squad B batches large work into manageable 3–5 file groups
- How the FORGE/EXECUTOR split prevents scope creep
- How sequential batch approval catches problems early
- How Autocannon + Shield Generator fortify after a refactor

---

## Stratagem chain used

```
ESS (branch)  →  RSP (context)
                     ↓
              ORB (batch plan — FORGE)
                     ↓
         EAS × N (apply batches — EXECUTOR)
              ↓ review after each ↓
              ACN (lint/format)
                     ↓
              SHG (test coverage)
                     ↓
              ERM (close + handoff)
```

---

## Next mission

Try [Tutorial 04 — Pre-Release Audit](tutorial-04-audit.md) to learn Squad D (Defense) operations.

---

*Promptdivers — plan the barrage, then fire. Never the reverse. FOR DEMOCRACY.*
