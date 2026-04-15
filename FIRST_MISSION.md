# FIRST_MISSION.md — Welcome to Super Earth Engineering Command

![Promptdivers — squads, stratagems, managed democracy](Banner.png)

## *You've played Helldivers. Now you're the Helldiver.*

You already know how this works. You drop into a mission. Your squad has roles. You ping, you escalate, you extract. You don't improvise every call from scratch — you use the stratagem system.

**Promptdivers is the same thing, but for AI-assisted development** — a **framework** (Markdown doctrine + optional IDE **skills**) that your editor assistant follows.

Think of it this way: the **framework** is the stratagem grid and briefing; the **assistant** in Cursor / Claude Code / Copilot is the Helldiver that executes it. You are still High Command. The repo is the planet. The bugs, the brittle scripts, the ungoverned AI making stuff up with no oversight — those are the fronts.

---

## What is an "AI coding agent"?

It's an AI assistant (like Claude, Cursor, or GitHub Copilot) that works *inside your code editor* instead of in a chat window. You describe what you want, and it reads your files, writes code, runs commands, and reports back.

The problem is: without a clear brief, these agents improvise. They make assumptions. They touch files they shouldn't. They go out of scope. They're conscripts, not Helldivers.

**Promptdivers gives them doctrine.** A mission brief (`AGENTS.md`), a squad structure (Squads A–D), escalation protocols, and tactical signals — so the agent operates like a trained operative, not a random drop.

---

## The three fronts (what you're fighting)

| Front | In the game | In your project |
|-------|------------|-----------------|
| **Terminids** | Bug swarms | Software bugs, regressions, tests that fail, production fires |
| **Automatons** | Rigid war machines | Scripts and pipelines that "just run" and nobody understands or owns |
| **Illuminate** | Opaque advanced threat | AI doing things without a brief, without review, leaking data, making up answers |

Every time you open your editor and tell the agent to do something, you're fighting one of these fronts.

---

## The four squads (mission types)

Instead of picking a weapon loadout, you pick a squad based on the mission:

**Squad A — Advance:** *I don't know this codebase at all. Map it.*  
The agent reads everything, builds a map, and briefs you. No changes yet.

**Squad B — Artillery:** *This needs a big coordinated push. 10+ files.*  
Two roles that never overlap: THE FORGE (designs the plan) and THE EXECUTOR (applies it). Splitting them prevents chained mistakes.

**Squad C — Surgical:** *One bug. One feature. In and out.*  
Maximum precision, minimum scope. If it grows beyond 5 files, you ESCALATE.

**Squad D — Defense:** *Hold the line. Review, QA, pre-launch checks.*  
The squad that keeps territory you already gained from falling back to the enemy.

---

## Your first drop — step by step

### 1. Clone the pack and install

```bash
git clone https://github.com/your-org/promptdivers.git
cd promptdivers
./install.sh --project /path/to/your-project
```

This puts the agent brief files in your project and installs the skills in your IDE. One command.

### 2. Fill in the mission brief

Open `AGENTS.md` in your project. It's like a stratagem loadout — you tell the agent what kind of project this is, what it's allowed to do, and what the critical areas are.

Minimum to fill in (takes 2 minutes):

```markdown
## Project stack
Language:   Python / FastAPI
Framework:  SQLAlchemy + PostgreSQL
Current state: active development

## Critical paths
src/api/    ← main routes
src/models/ ← database models
```

### 3. Choose your squad and deploy

Open your IDE (Claude Code, Cursor, etc.) and say:

> *"New project, I don't know the codebase. Run Squad A."*

The agent activates THE SCOUT, reads your files, and comes back with an INTEL report: what it found, what's concerning, what the terrain looks like. No changes made — just recon.

### 3.5 Paste a mission brief (copy/paste template)

If you want the agent to behave like a trained operative immediately, paste a brief with objective criteria and scope boundaries:

- Template: [`templates/mission-brief.template.md`](templates/mission-brief.template.md)
- Scored close-out: [`protocols/mission-debrief.md`](protocols/mission-debrief.md)

### 4. Use tactical signals

The agent will signal its status like a squad mate:

```
🟢 GREEN — terrain mapped, ready for orders
📍 MARK — found something: src/api/users.py:88
🔴 RED — blocked: tests failing before I can proceed
⬆️ STEP UP — this is bigger than Squad C, escalating to B
```

You can ping back:

```
🚀 GO       ← proceed on what we agreed
⏸️ HOLD     ← wait, I need to check something
o7          ← acknowledged, continue
```

### 5. Close the mission

When you're done (or done for today), say:

```
debrief
```

The agent scores what happened (PASS / PARTIAL / FAIL for each objective), updates the `PROJECT_LOG.md` with a handoff block, and sets up the next session to continue exactly where this one ended. Like respawning with context.

---

## Common situations

**"I have no idea what this codebase does"**
→ Squad A. THE SCOUT maps it. No edits until you say so.

**"There's a bug in login that just appeared in prod"**
→ Squad C. THE MARKSMAN. Diagnose → root cause → minimal fix → verify.

**"We need to refactor the entire auth system"**
→ Squad B. THE FORGE designs it (no applying yet). You review. THE EXECUTOR applies it. Never the same agent in one run.

**"Everything is on fire"**
→ Say: `TOTAL DEMOCRACY`

---

## You don't need to understand everything

You don't need to read all the docs to start. `AGENTS.md` + one squad file is enough for your first real mission.

When you need more, it's there:
- Full signal grid → [protocols/tactical-signals.md](protocols/tactical-signals.md)
- All roles and codenames → [docs/roles-and-field-operatives.md](docs/roles-and-field-operatives.md)
- How to route more complex missions → [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- How to set this up in your specific IDE → [docs/MULTI_AGENT_SETUP.md](docs/MULTI_AGENT_SETUP.md)

---

## One more thing

The fun part is real. When your agent says:

```
o7 🎯 ON TARGET — proceeding on agreed scope only. FOR DEMOCRACY.
```

…it means it understood the scope, it's locked in, and it's not going to randomly touch six other files. That's the point. Managed democracy isn't a joke — it's the agent working with discipline instead of vibes.

**Welcome to Super Earth Engineering Command. Drop when ready.**

---

*Promptdivers — o7*
