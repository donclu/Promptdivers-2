<div align="center">

<img src="Banner.png" alt="Promptdivers — squads, stratagems, and managed democracy for AI-assisted development" width="100%"/>

# Promptdivers

### *Managed democracy for AI-assisted development*

[![Version](https://img.shields.io/badge/version-3.3.1-brightgreen?style=flat-square)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![IDE](https://img.shields.io/badge/IDE-Claude%20Code%20%7C%20Cursor-purple?style=flat-square)](docs/MULTI_AGENT_SETUP.md)
[![Fronts](https://img.shields.io/badge/fronts-3%20active-red?style=flat-square)](docs/factions-and-objectives.md)
[![FOR DEMOCRACY](https://img.shields.io/badge/FOR-DEMOCRACY-gold?style=flat-square&logo=data:image/svg%2bxml;base64,)](README.md)

> Humanity did not crawl out of technical debt, unclear specs, and scope creep  
> just to surrender now. **We fight. For democracy.**

**English** · [Español — README-ES.md](README-ES.md)

</div>

---

## What is Promptdivers?

Promptdivers is a **portable framework** for AI-assisted development: Markdown doctrine (squads, protocols, stratagems), **IDE skills** that teach assistants *when* to load *what*, and templates (`AGENTS.md`, logs, missions). Your **AI assistant in the IDE** (Claude Code, Cursor, etc.) is the runtime; **this repo** is the playbook it follows.

Inspired by *Helldivers 2* — squads, stratagems, three fronts, escalation ladders — applied to how you run **assisted** coding work in real projects.

**Bundled skills (core + support):**

Core (enough for the full loop):
- `promptdivers-orchestrator` — routing + multi-domain hints + model fleet
- `promptdivers-tactical-signals` — pings and situation markers
- `promptdivers-pelican` — debrief / handoff scoring

Support (optional, Helldivers-flavored operators):
- `promptdivers-orbital-control` — parallelism + token budget planning (RNF/PRD)
- `promptdivers-ministry-of-truth` — claim integrity (no invented canon/APIs; evidence-first)
- `promptdivers-stratagem-terminal` — choose loadouts fast; point to the right stratagem docs

> **New here?** → [FIRST_MISSION.md](FIRST_MISSION.md) — onboarding for people new to IDE assistants.

---

## The Three Fronts

<div align="center">

| Front | Helldivers echo | What it really means |
|:-----:|:---------------:|:--------------------:|
| 🐛 **Terminids** | The bug swarms | Defects, regressions, flaky tests, production fires |
| 🤖 **Automatons** | Rigid war machines | Brittle scripts and pipelines nobody owns |
| 👁️ **Illuminate** | Opaque advanced threat | Ungoverned AI — unreviewed output, shadow agents |

</div>

**Winning** means lasting solutions: clean features, maintainable automation, and AI workflows with clear rules and review. See [docs/factions-and-objectives.md](docs/factions-and-objectives.md).

---

## The Four Squads

<div align="center">

| Squad | Mission | Deploy when |
|:-----:|:-------:|:-----------:|
| ⚡ **A — Advance** | Recon and base setup | New repo, unknown codebase, no brief yet |
| 🔥 **B — Artillery** | Large coordinated change | Refactors, migrations, >10 files |
| 🎯 **C — Surgical** | One shot, one problem | Small bug, tight feature, hotfix |
| 🛡️ **D — Defense** | Hold the line | PR review, pre-release, session hygiene |

</div>

**Production meltdown?** Say `TOTAL DEMOCRACY` → all squads, maximum priority.

---

## Install in One Command

```bash
git clone https://github.com/donclu/promptdivers.git
cd promptdivers
./install.sh
```

The script auto-detects your IDE (Claude Code, Cursor, or both) and installs the three skills globally. That's it.

**Windows / PowerShell:** `install.sh` is **Bash** — it does not run in PowerShell. Use [`install.ps1`](install.ps1) instead (same flags: `-Project`, `-Cursor`, `-Claude`, `-Help`):

```powershell
cd path\to\promptdivers
pwsh -File .\install.ps1
```

If execution is blocked: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`. You can also use **Git Bash** or **WSL** and run `./install.sh` as on Linux.

**Bootstrap a project at the same time:**
```bash
./install.sh --project /path/to/your-project
```

This copies `AGENTS.md`, `CLAUDE.md`, `QUICK_REFERENCE.md`, and a blank `PROJECT_LOG.md` into your project.

Manual install and IDE-specific setup → [docs/MULTI_AGENT_SETUP.md](docs/MULTI_AGENT_SETUP.md)

---

## How It Works — Three Layers

```
┌─────────────────────────────────────────────────────────┐
│  YOUR PROJECT (per repo)                                 │
│                                                          │
│  AGENTS.md ──── contract the assistant reads at start    │
│  CLAUDE.md      stub → AGENTS.md (Claude Code)           │
│  PROJECT_LOG.md session memory · handoffs                │
└─────────────────────────────────────────────────────────┘
                          │
                          │  skills + pack loaded on demand
                          ▼
┌─────────────────────────────────────────────────────────┐
│  YOUR IDE — global skills (~/.cursor/skills/ etc.)       │
│                                                          │
│  promptdivers-orchestrator   ← routes missions + fleet   │
│  promptdivers-pelican        ← debrief · handoff JSON    │
│  promptdivers-tactical-signals ← ping grid               │
└─────────────────────────────────────────────────────────┘
                          │
                          │  paths from skills → open these files
                          ▼
┌─────────────────────────────────────────────────────────┐
│  THE PACK (this repo — doctrine)                         │
│                                                          │
│  squads/*.md        playbooks A–D                        │
│  protocols/*.md     signals · escalation · debrief       │
│  stratagems/        concrete invokable actions           │
│  docs/              operating model · model fleet        │
└─────────────────────────────────────────────────────────┘
```

**Layer 1 — Project:** your stack, permissions, critical paths.  
**Layer 2 — Skills:** small `SKILL.md` bundles the IDE lazy-loads (framework hooks).  
**Layer 3 — Pack:** the full doctrine library the skills point into.

---

## Your First Mission — 5 Minutes

**Scenario:** you inherited a repo with no documentation and have no idea where to start.

**Step 1 — Drop in the files**
```bash
./install.sh --project ~/my-project
```

**Step 2 — Edit AGENTS.md** (30 seconds)
```markdown
## Project stack
Language:   TypeScript / Node 20
Framework:  Express + Prisma
Current state: active development

## Critical paths
src/api/      ← main API routes
src/db/       ← Prisma schema + migrations
```

**Step 3 — Open your IDE and say:**
```
I need to understand this codebase. Run Squad A.
```

**Step 4 — Check status at any time:**
```
status
```

**Step 5 — Close the session:**
```
debrief
```

**That's the loop:** Planet check → Squad → Work → Debrief.

---

## Human Keywords

<div align="center">

| You say | What happens |
|:-------:|:-------------|
| `status` | SITREP — where we are right now |
| `save` | Update `PROJECT_LOG`, produce handoff block |
| `debrief` | Score objectives PASS/PARTIAL/FAIL, route failures |
| `extract` | Same as debrief (end of mission) |
| `handoff` | Structured JSON for another session or human handoff |
| `escalate` | Escalation protocol with evidence |
| `TOTAL DEMOCRACY` | All squads, max priority |
| `scope check` | What's in vs out of scope right now |
| `debt` | List tracked technical debt |
| `abort` | Stop, report, roll back if safe |

</div>

---

## Tactical Signals

The assistant leads with a situation marker, then evidence. You can use them too.

```
🟢 GREEN   clear / go
🟡 YELLOW  caution / needs attention
🔴 RED     blocked / failing
🎯         scope locked
📍 MARK    look here: path or line
⬆️ STEP UP escalate
✅ CLEAR   done / verified
o7          acknowledged
```

Full signal grid: [protocols/tactical-signals.md](protocols/tactical-signals.md)

---

## What's in the Repo

```
promptdivers/
├── Banner.png                     ← repo banner (README hero)
├── install.sh / install.ps1       ← start here (Bash / PowerShell)
├── FIRST_MISSION.md               ← new to IDE assistants? read this first
├── README.md / README-ES.md       ← you are here · guía en español
├── AGENTS.md                      ← canonical project brief (dogfood)
├── CLAUDE.md                      ← Claude Code stub → points to AGENTS.md
├── QUICK_REFERENCE.md             ← one-page field cheat sheet
├── GALACTIC_WAR_MAP.md            ← dogfood terrain map (pack status)
├── PROJECT_LOG.md                 ← session log for this repo
├── VERSION / CHANGELOG.md         ← semver history
├── LICENSE / CONTRIBUTING.md / SECURITY.md
├── docs/                          ← operating model, model fleet, IDE setup
├── stratagems/                    ← 24 concrete invokable actions
├── squads/                        ← playbooks A–D
├── protocols/                     ← signals, escalation, debrief, more
├── skills/                        ← bundled skills (core + support)
├── missions/                      ← 8 guided tutorial missions (+ index)
├── scripts/                       ← health-check.sh and tooling
└── templates/                     ← project-log, galactic-war-map, intel-dossier
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). MIT License. **Security:** report vulnerabilities per [SECURITY.md](SECURITY.md) — private channel, not public issues.

---

<div align="center">

## Trademarks

*Helldivers 2* and related names are trademarks of their respective owners.  
Promptdivers is an independent fan-style metaphor for engineering workflow —  
not affiliated with, endorsed by, or sponsored by the game's publishers.

---

*Promptdivers — spreading managed democracy, one commit at a time.*

**FOR DEMOCRACY. 🫡**

</div>
