# Factions and objectives — the three fronts

Promptdivers uses a **Helldivers-style** picture of the battlefield. It is a **metaphor**: it helps teams classify work and tone, not replace real threat models or incident response.

---

## The real objective: gain ground for Super Earth

This framework is **not** only about killing bugs.

**Super Earth** = a healthy product and codebase your team can defend and extend.  
**Winning territory** = shipping **solutions**: features users need, reliability that holds, automation that helps, and agent workflows that are **governed** (briefs, reviews, logs).

**Trailer energy (official Super Earth tone):** Every advance is sold like the *Helldivers* ads—**managed democracy** rolling forward, **happy productive life** for citizens (your team and users), bugs and hostile automation driven back into the sea. In this repo the “explosions” are green CI, clear specs, and sleep. It is half joke, half goal: **less firefighting, more room for actual life.**

Every squad mission should be clear whether you are:

- **Holding** what you have (Squad D, hotfixes), or  
- **Advancing** (Squad A → B/C): new capability, reduced risk, clearer architecture.

If you only extinguish fires and never advance the map, you are stuck in permanent defense—still “democratic,” but not expanding managed democracy.

---

## Front 1 — Terminids (the bugs)

**In-universe:** endless swarms, corrosion, things that eat your lines.

**In software:**

- Defects, regressions, memory leaks, race conditions  
- Flaky tests and “sometimes green” CI  
- Performance cliffs and unexplained errors in production  

**Typical response:** Squad C (surgical) or Squad B when the infestation spans many files.

---

## Front 2 — Automatons (bad “classic” automation)

**In-universe:** rigid industrial war machines—predictable until they aren’t.

**In software:**

- Brittle shell/Make/cron jobs nobody dares touch  
- Copy-paste “RPA” that breaks on UI or data drift  
- Pipelines full of implicit state and silent failures  
- “We automated it” but only **one** person understands the ritual  

**Typical response:** Squad A to map the ritual, then B to replace with observable, testable automation—or C if the blast radius is small.

---

## Front 3 — Illuminate (the AI hazard)

**In-universe:** an advanced, manipulative faction—hard to see clearly, easy to underestimate.

**In software (this is about *risk patterns*, not “AI bad”):**

- **Unreviewed** generated code merged as if it were obvious  
- Agents run **without** `AGENTS.md`, permissions, or audit trail  
- Prompts or tools that can **leak secrets** or bypass policy  
- “The model said it was fine” replacing verification  
- Shadow workflows: side-channel agents, unlogged changes, no handoff  

**Typical response:** Squad D (review + standards), Squad A (brief and boundaries), then B/C to implement **governed** AI-assisted workflows—THE AUTHENTIC and THE AUDITOR stay essential.

The Illuminate front is **the same fight** as managed democracy: **use AI like a stratagem**—called in with context, verified, and scoped—not like uncontrolled sorcery.

---

## How squads map to the war

| Situation | Think of it as… | Squad bias |
|-----------|------------------|------------|
| Single defect, tight scope | Terminid hunt | C |
| Wide refactor / migration | Major offensive | B (after A if needed) |
| Unknown repo / new doctrine | Recon advance | A |
| PR review, hygiene, pre-release | Hold the line | D |
| AI or automation governance | Illuminate **or** Automaton intel | A → D, then B/C |

---

## One-line briefing for agents

> We fight **three fronts**—bugs, hostile automation, and ungoverned AI—by **clearing threats** and **taking ground**: shipped value, clearer systems, and documented operations—so Super Earth can **impose managed democracy** on the repo and your team gets the **happy, boring life** the trailer promised (green CI, honest docs, weekends). **FOR DEMOCRACY.**

---

*Promptdivers — Super Earth expands when you ship and document, not only when you close tickets.*
