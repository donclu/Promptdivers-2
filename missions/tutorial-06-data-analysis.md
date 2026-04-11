# Tutorial Mission 06 — Data Analysis (Intelligence Operations)

## Mission type: DATA archetype (Squad C + Support)

> *"Raw data is enemy territory. Analyzed data is liberated intelligence."*

---

## Scenario

You have data files that need analysis — CSVs, Excel files, JSON dumps, or database exports. You need to clean the data, find patterns, produce metrics, and deliver a report to stakeholders. This mission teaches you to chain data-focused stratagems.

**Difficulty:** ⭐⭐ Medium  
**Time:** ~30 minutes  
**Stratagems used:** Resupply (RSP), Intel Dossier (IDR), Data Strike (DSK), Eagle Report (ERP), Eagle Rearm (ERM)

---

## Pre-drop checklist

- [ ] You have data files to analyze (CSV, Excel, JSON, or similar)
- [ ] You know what questions you need to answer with this data
- [ ] `AGENTS.md` exists in your project (or create one)

---

## Mission briefing

### Objective 1 — Understand the data landscape

```text
🚀 GO — Data analysis mission.

Resupply (RSP) — refresh context from AGENTS.md.

Then call Intel Dossier (IDR) — SCAN level:
- Research question: "What does this dataset contain and what can we learn from it?"
- Scope: SCAN (quick overview, not deep dive yet)
- Sources: [path(s) to your data file(s)]

I need:
1. File format, encoding, size
2. Column names, types, sample values
3. Row count
4. Missing values per column
5. Initial observations — anything surprising?
```

**Expected result:** A structured overview of your data. You understand what you're working with before diving in.

---

### Objective 2 — Clean and transform

```text
Now call Data Strike (DSK) on the data:

1. Clean the data:
   - Fix date formats (standardize to YYYY-MM-DD or DD-MM-YYYY as needed)
   - Handle missing values: [drop / fill with X / flag]
   - Remove duplicates if any
   - Fix text encoding issues

2. Transform:
   - [Your specific business rules here, e.g.:]
   - Categorize rows by [column] into [categories]
   - Calculate [new metric] from [columns]
   - Filter out rows where [condition]
   - Group by [column] and aggregate [metric]

3. Validate:
   - Input rows: [count] → Output rows: [count]
   - Spot-check 3 random rows
   - No nulls in critical columns: [list them]

Show me the results as a summary table.
```

**Expected result:** Clean dataset with transformations applied and validated.

---

### Objective 3 — Analyze and find insights

```text
Continue with Data Strike (DSK):

Answer these questions from the clean data:
1. [Your specific analysis question — e.g., "Which center has the highest attendance?"]
2. [Second question — e.g., "What's the trend over time?"]
3. [Third question — e.g., "Are there outliers or anomalies?"]

For each answer:
- Show the data that supports it (table or metric)
- Rate confidence: HIGH/MEDIUM/LOW
- Note any caveats or limitations
```

**Expected result:** Evidence-based answers to your questions with data tables.

---

### Objective 4 — Produce the deliverable

```text
Call Eagle Report (ERP):

Create a report from this analysis for [your audience]:
- Audience: [leadership / technical team / public]
- Format: Markdown report
- Voice: [formal / professional / Helldivers-themed]
- Length: [brief / standard]

Include:
- Executive summary (3 sentences)
- Key findings table
- Recommendations based on the data
- Source data description
```

**Expected result:** A stakeholder-ready report document.

---

### Objective 5 — Extract

```text
Eagle Rearm (ERM) — close this mission.

Debrief + PROJECT_LOG update.
Save the analysis script/steps for reproducibility.
```

---

## Debrief

### Expected final state

```
Objective 1 (understand):   PASS — data landscape mapped
Objective 2 (clean):        PASS — data cleaned and validated
Objective 3 (analyze):      PASS — questions answered with evidence
Objective 4 (report):       PASS — deliverable produced
Objective 5 (extract):      PASS — session logged, script saved

mission_status: 🟢 GREEN
```

### Stratagem chain used

```
RSP (context) → IDR (understand data) → DSK (clean + analyze)
                                              ↓
                                         ERP (produce report)
                                              ↓
                                         ERM (log + handoff)
```

### What you learned

- How Intel Dossier structures research before diving into data
- How Data Strike handles the full pipeline: clean → transform → validate → analyze
- How Eagle Report turns raw analysis into stakeholder-ready deliverables
- How to maintain reproducibility by saving scripts

---

## Next mission

Combine what you've learned: try running a **full audit** (Tutorial 04) that includes a **data analysis** component — for example, analyzing test coverage data, performance metrics, or error logs.

---

*Promptdivers — the truth is in the data, Helldiver. Go find it. FOR DEMOCRACY.*
