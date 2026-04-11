# Tutorial Mission 07 — Research & Prompt Design (Intelligence + Forge)

## Mission type: CONSULT + WRITE archetype

> *"Before the boots hit the ground, intelligence prepares the battlefield. Before the prompt hits the model, the Forge shapes the weapon."*

---

## Scenario

You need to research a topic thoroughly, produce an intelligence dossier, and then design a prompt or template based on what you learned. This covers the "thinking work" that Promptdivers supports: consulting, research, knowledge synthesis, and prompt engineering.

**Difficulty:** ⭐⭐ Medium  
**Time:** ~30 minutes  
**Stratagems used:** Intel Dossier (IDR), Prompt Forge (PFG), Eagle Report (ERP), Eagle Rearm (ERM)

---

## Pre-drop checklist

- [ ] You have a research question or topic to investigate
- [ ] You know who the deliverable is for (yourself, team, client)
- [ ] Optional: access to web search or documentation

---

## Mission briefing

### Objective 1 — Research the topic

```text
🚀 GO — Intelligence gathering mission.

Call Intel Dossier (IDR):
- Research question: "[Your question — e.g., 'What's the best approach for implementing RAG in our Python project?']"
- Scope: REVIEW (thorough but not exhaustive)
- Sources: [web, docs, existing code, papers — whatever applies]
- Audience: [who needs this intel]

Use the Intel Dossier template (templates/intel-dossier.template.md).

I need:
1. Executive summary
2. Key findings with confidence ratings
3. Options matrix if comparing alternatives
4. Risks and unknowns
5. Recommendation
6. Sources for every claim
```

**Expected result:** A structured Intel Dossier document with actionable findings.

---

### Objective 2 — Design a prompt from the research

Now use what you learned to create something useful:

```text
Call Prompt Forge (PFG):

Based on the Intel Dossier above, I need a [choose one]:

A) System prompt for [purpose — e.g., "an agent that reviews our database migrations"]
B) Template for [purpose — e.g., "our team's project kickoff document"]
C) Workflow prompt for [purpose — e.g., "data validation pipeline instructions"]

Spec:
- Purpose: [what should it achieve]
- Target model: [Claude / GPT / any / unknown]
- Audience: [who uses the prompt]
- Constraints: [length, tone, format]

Follow the Prompt Forge steps:
1. Write the prompt spec
2. Research patterns (what techniques fit?)
3. Draft the prompt
4. Create a test matrix (3 variations)
5. Iterate on failures
6. Package the final version
```

**Expected result:** A tested, versioned prompt with a test matrix showing it works.

---

### Objective 3 — Package as a deliverable

```text
Call Eagle Report (ERP):

Create a final deliverable package that includes:
1. The Intel Dossier (research)
2. The designed prompt (output)
3. Test results
4. Usage instructions — how to use the prompt

Format: Markdown document
Audience: [team / client / self — for future reference]
```

**Expected result:** A self-contained package that someone else (or future-you) can use.

---

### Objective 4 — Extract

```text
Eagle Rearm (ERM) — close this mission.
Log everything. Save the prompt with version number.
```

---

## Debrief

### Expected final state

```
Objective 1 (research):     PASS — Intel Dossier produced with sources
Objective 2 (prompt design): PASS — Prompt tested with 3+ variations
Objective 3 (deliverable):  PASS — Package ready for use
Objective 4 (extract):      PASS — Logged and versioned

mission_status: 🟢 GREEN
```

### Stratagem chain used

```
IDR (research)  →  PFG (design prompt from findings)
                        ↓
                   ERP (package deliverable)
                        ↓
                   ERM (log + handoff)
```

### What you learned

- How Intel Dossier structures research with sources and confidence ratings
- How Prompt Forge turns knowledge into tested, versioned prompts
- How Eagle Report packages work into stakeholder-ready deliverables
- How the full-spectrum doctrine applies beyond just code

---

*Promptdivers — intelligence + forge = weapons-grade prompts. FOR DEMOCRACY.*
