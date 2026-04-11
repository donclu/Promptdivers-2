# Tutorial Mission 04 — Pre-Release Audit (Hold the Line)

## Mission type: Squad D (Defense)

> *"Nothing ships until THE SENTINEL clears it. No exceptions."*

---

## Scenario

Your project is ready for release — or so you think. Squad D's job is to verify that every claim of "done" has evidence, every test passes, and no Illuminate threats are hiding in reviewed-but-wrong output.

**Difficulty:** ⭐⭐ Medium  
**Time:** ~30 minutes  
**Stratagems used:** Resupply (RSP), Democracy Officer, Fortify (FRT), Shield Generator (SHG), Eagle Rearm (ERM)

---

## Pre-drop checklist

- [ ] Project has `AGENTS.md` with current stack
- [ ] Project has `PROJECT_LOG.md` with recent session history
- [ ] Codebase is in a "we think it's ready" state
- [ ] You have a test suite (even partial)

---

## Mission briefing

### Objective 1 — Democracy Officer check

Start with the meta-audit:

```text
🚀 GO — Squad D mission. Pre-release audit.

Run the Democracy Officer protocol (protocols/democracy-officer.md).

Check:
1. Is AGENTS.md current and accurate?
2. Is PROJECT_LOG complete and up to date?
3. Are there unresolved DEBT items?
4. Were recent sessions properly debriefed?
5. Any Illuminate violations? (unreviewed AI output merged)

Give me the Democracy Officer report with the score.
```

**Expected result:** Structured report showing the project's "democracy level" — Cadet through Super Earth Hero.

---

### Objective 2 — Code health check

```text
Now audit the code itself:

1. Run the full test suite. Report results.
2. Run linter. Report issues.
3. Check for any TODO/FIXME/HACK comments — list them.
4. Check for hardcoded secrets or credentials (grep for patterns).
5. Check dependency health: any outdated? Any with known vulnerabilities?
6. Rate each front:
   - Terminids (bugs): how many known bugs / failing tests?
   - Automatons (brittle automation): is CI/CD solid? Any manual steps?
   - Illuminate (AI risk): any unverified AI-generated code?

Classify each area:
🟢 LIBERATED — clean, tested, documented
🟡 CONTESTED — working but has issues
🔴 ENEMY HELD — broken, untested, or unknown
```

**Expected result:** A per-module health report using Promptdivers territory classification.

---

### Objective 3 — Fill critical gaps

Based on the audit, fix the most critical issues:

```text
From the audit above, pick the top 3 most critical issues.

For documentation gaps: call Fortify (FRT).
For missing tests: call Shield Generator (SHG).
For lint issues: call Autocannon (ACN).
For anything bigger: log as DEBT and recommend the right squad.

Fix what you can. Log what you can't.
```

**Expected result:** Top gaps addressed or properly documented as DEBT with clear next steps.

---

### Objective 4 — Generate Galactic War Map

```text
Using all findings from this audit, generate a Galactic War Map for this project.
Use the template from templates/galactic-war-map.template.md.

Fill in:
- Territory status for each module
- Campaign score
- Threat index
- Progression level

Save as GALACTIC_WAR_MAP.md at the project root.
```

**Expected result:** A visual campaign dashboard showing the true state of the project.

---

### Objective 5 — Ship/No-ship decision

```text
Based on everything above, give me a ship/no-ship decision:

🟢 SHIP — all critical areas liberated, tests pass, no Illuminate violations
🟡 SHIP WITH CAUTION — some contested territory, document known issues in release notes
🔴 DO NOT SHIP — enemy-held critical territory, high-risk issues unresolved

Include your reasoning and what would change a 🟡 to a 🟢.
```

---

## Debrief

```text
Eagle Rearm (ERM) — close this mission.
Debrief + PROJECT_LOG update + HANDOFF_JSON.
```

### Expected final state

```
Objective 1 (democracy officer):  PASS/PARTIAL — depends on project state
Objective 2 (code health):        PASS — full audit produced
Objective 3 (gap fill):           PASS/PARTIAL — top issues addressed or logged
Objective 4 (war map):            PASS — GALACTIC_WAR_MAP.md created
Objective 5 (ship decision):      PASS — clear recommendation with evidence

mission_status: depends on findings
```

### What you learned

- How Squad D provides quality gates before release
- How the Democracy Officer audits framework adoption itself
- How the Galactic War Map visualizes project health
- How to make evidence-based ship/no-ship decisions
- How DEBT items track what you choose not to fix right now

---

## Next mission

Try [Tutorial 05 — Total Democracy](tutorial-05-total-democracy.md) if you're brave enough for a crisis scenario.

---

*Promptdivers — the line holds here. FOR DEMOCRACY.*
