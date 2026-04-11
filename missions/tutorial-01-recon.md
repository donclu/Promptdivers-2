# Tutorial Mission 01 — Recon an Unknown Repo

## Mission type: Squad A (Advance)

> *"You've been dropped into hostile territory. No map. No intel. Just a folder full of code and a mission brief that says 'figure it out.'"*

---

## Scenario

You've been assigned to a new project. The repo exists but has **no `AGENTS.md`**, no documentation, and the previous developer left without a handoff. Your job: map the terrain so the next squad can operate effectively.

**Difficulty:** ⭐ Easy (perfect first mission)  
**Time:** ~15 minutes  
**Stratagems used:** Resupply (RSP), Hellpod (HPD), Fortify (FRT)

---

## Pre-drop checklist

- [ ] You have a project repo (any language, any size)
- [ ] Promptdivers is installed (global skills or pack copy)
- [ ] Your IDE has access to an AI agent (Claude Code, Cursor, etc.)

---

## Mission briefing

### Objective 1 — Read the terrain

Paste this into your agent:

```text
Read this project from root. I need a full INTEL REPORT:
1. What language/framework is this?
2. What does it do? (one paragraph)
3. What's the directory structure? (tree, max 3 levels)
4. What are the entry points? (main files, routes, CLI commands)
5. What testing exists? (framework, coverage if visible)
6. What's the dependency situation? (count, any outdated/vulnerable?)
7. Classify threats using Promptdivers fronts:
   - Terminids (bugs): any obvious issues?
   - Automatons (brittle automation): CI/CD? Scripts? Manual steps?
   - Illuminate (ungoverned AI): any AI-assisted code without review markers?
```

**Expected result:** The agent produces a structured intel report. Save it — you'll use it for Objective 2.

---

### Objective 2 — Plant the flag (create AGENTS.md)

Now use that intel to bootstrap the project's agent brief:

```text
Using the intel report above, create an AGENTS.md for this project.
Use the Promptdivers template from this repository as the base.
Fill in: stack, permissions, critical path map, known issues.
Set Model (nave) to AUTO for now.
```

**Expected result:** An `AGENTS.md` file at the project root, populated with real data.

---

### Objective 3 — Set up memory

```text
Create a PROJECT_LOG.md from the Promptdivers template.
Log this session as the first entry: "Initial recon — Squad A."
Include the INTEL_REPORT findings as the Summary.
Create a HANDOFF_JSON block with mission_last: "A" and mission_status: "GREEN" if everything went well.
```

**Expected result:** `PROJECT_LOG.md` at the project root with a valid first entry.

---

## Debrief

After completing all three objectives, say `debrief` to the agent. It should:

1. Score each objective PASS/PARTIAL/FAIL
2. Set mission_status
3. If anything was PARTIAL or FAIL, suggest the next stratagem

### Expected final state

```
📁 your-project/
├── AGENTS.md          ✅ Created with real stack data
├── PROJECT_LOG.md     ✅ First entry logged
└── ... (existing files)
```

### What you learned

- How Squad A works (map before you code)
- How AGENTS.md provides context for every future session
- How PROJECT_LOG creates continuity between sessions
- How the debrief protocol closes a mission cleanly

---

## Next mission

Try [Tutorial 02 — Fix a Bug](tutorial-02-bugfix.md) to learn Squad C (Surgical) operations.

---

*Promptdivers — know the ground before you fight on it. FOR DEMOCRACY.*
