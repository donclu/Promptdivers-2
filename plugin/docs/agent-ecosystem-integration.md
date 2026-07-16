# Agent ecosystem integration — Promptdivers + your skills

This document is the **orchestration map**: it merges **Promptdivers** (missions, squads, protocols) with **Agent Orchestrator**-style routing plus your **deep skills** (UI, workflow, audit, humanizer, …).

**Mission archetypes** (CONSULT, RECON, AUDIT, BUILD-WEB, LAUNCH-WEB, DATA, VISUAL, DIRECT, WRITE): see [super-earth-operating-model.md](super-earth-operating-model.md). Guided drills: [missions/README.md](../missions/README.md).

Use this file when you are **not** sure which playbook to load first. **Full doc index:** [README.md](../README.md).

**Paths:** user skills live in different places (e.g. Cursor: `~/.cursor/skills/<name>/SKILL.md`). Adjust to your IDE.

**Economy:** Load **at most two heavy skills per phase**. Finish the phase, then load the next. “Heavy” ≈ full methodology (ui-design-expert, app-auditor, sdd-workflow). “Light” ≈ tactical (promptdivers-tactical-signals, short consult).

---

## Layer 0 — In-repo (always cite when using Promptdivers)

| Asset | Role |
|-------|------|
| `AGENTS.md` | Constitution (declares `Model (nave)` in stack block) |
| `QUICK_REFERENCE.md` | Squads + keywords + archetypes + fleet quick chart |
| `protocols/tactical-signals.md` | Pings / cross-language comms |
| `docs/factions-and-objectives.md` | Three fronts + “gain territory” |
| `docs/super-earth-operating-model.md` | **Full-spectrum** missions (consult → build → data → images) + nave column |
| `docs/model-fleet.md` | **Ship manifest**: AI model classes, mission routing, Illuminate risk |
| `docs/onboarding-calibration.md` | Question round + **humanizer** (AI-likeness + creativity) |
| `squads/squad-*.md` | Squad activation prompts |

---

## Decision tree (expanded)

```text
What is the human doing?
│
├── Promptdivers / squad / TOTAL DEMOCRACY / tactical pings
│   ├── tactical-signals.md + QUICK_REFERENCE.md + squad-*.md
│   └── ESCALATE → escalation.md + operation-total-democracy.md
│
├── Quick consult (no repo, advice only)
│   ├── structured-workflow: light Fase 1–2 OR 3–5 bullets if tiny
│   └── If output is user-facing prose → onboarding-calibration → humanizer
│
├── Repository recon / “what is this codebase?”
│   ├── Squad A THE SCOUT (read-only)
│   └── structured-workflow → PROJECT_LOG if multi-session
│
├── Pre-ship / full audit / explain to non-tech
│   ├── app-auditor (ingest README → domains → /explain)
│   └── Squad D; ESCALATE on CRITICAL; humanizer for /explain tone if calibrated
│
├── UI / UX / design system / “not AI slop”
│   ├── ui-design-expert (Phase 0 mandatory, then phases as needed)
│   ├── Optional project skills: **ux-ui**, **html-css**, **tailwind**, **web-tooling** (e.g. this pack: `.cursor/skills/`)
│   └── Squad B or C + Forge≠Executor on large UI refactors
│
├── Large feature / API / module
│   ├── sdd-workflow
│   ├── Squad A → B; structured-workflow for log + handoff
│   └── ui-design-expert when the feature is mostly interface
│
├── Small bugfix / tight change
│   └── Squad C; agent-memory mem_save at end if used
│
├── PR review / house style
│   ├── github-style-learner
│   └── Squad D auditor checklist
│
├── Data analysis / pipelines / notebooks
│   ├── Assume structured-workflow for plan + log if long
│   └── Verify numbers; TDD mental / checks per structured-workflow
│
├── Images / visual assets (not just UI code)
│   ├── Use IDE image tools if available
│   └── ui-design-expert for art direction tied to product (palette, layout)
│
├── Directing / prioritization / “what next for the team?”
│   ├── structured-workflow plan + NEXT_MISSION
│   └── Squad D THE TACTICIAN
│
├── User-facing writing (README, posts, emails, friendly audits)
│   ├── onboarding-calibration.md → voice + creativity
│   └── humanizer skill for delivery
│
├── First-time agent setup
│   ├── agent-context → AGENTS.md
│   ├── mcp-best-practices if MCPs
│   └── Squad A if no brief
│
├── Resume after break
│   ├── agent-memory if available
│   ├── structured-workflow → HANDOFF_JSON (check `objectives`, `mission_status`, `debrief_summary` if present)
│   └── Squad D Sentinel optional
│
├── Mission end / debrief / extract
│   ├── protocols/mission-debrief.md (+ optional promptdivers-pelican skill)
│   └── Then save / handoff with optional scored fields in PROJECT_LOG
│
├── MCP broken / new tool
│   └── mcp-best-practices
│
└── Lost context / new session
    ├── agent-memory recovery
    └── structured-workflow handoff
```

---

## Deep skill ↔ Promptdivers bridge

| Skill | Role | Bridge |
|-------|------|--------|
| **structured-workflow** | Log, handoff, scope lock, phases, racimo, TDD mental | THE SCRIBE; all multi-session work |
| **ui-design-expert** | Diagnose UI, tokens, a11y, platform patterns | Phase 0 before implementing; squads B/C |
| **app-auditor** | Context ingestion, severities, /explain, IA detection | Squad D; findings → DEBT + ESCALATE |
| **humanizer** | Voice, anti-IA connectors, style profile, termómetro | After calibration; stakeholder prose |
| **agent-context** | AGENTS.md quality | THE AUTHENTIC |
| **agent-memory** | Persistent memory | Session bookends with SCRIBE |
| **sdd-workflow** | SPEC/DESIGN/TASKS | Squad B fuel |
| **mcp-best-practices** | Safe tools | AGENTS.md permissions |
| **github-style-learner** | PR style | THE AUDITOR |
| **Agent orchestrator** | Generic router | Use **promptdivers-orchestrator** when missions + tactics matter |
| **promptdivers-pelican** (bundled) | Scored debrief, stratagem routing | `protocols/mission-debrief.md`; THE SCRIBE; keywords `debrief`, `extract` |

---

## Humanizer: when + how

- **When:** Deliverables that **people read** (not raw stack traces for engineers only—unless they ask for “human” summaries too).  
- **How:** Run [onboarding-calibration.md](onboarding-calibration.md): **AI-likeness** + **creativity**; then load **humanizer** `SKILL.md`.  
- **Pairing:** **app-auditor** `/explain` + humanizer = approachable audits. **Consult** + humanizer = advice that does not sound like a template.

---

## Recommended sequences (copy-paste mental model)

| Goal | Sequence |
|------|----------|
| “Quick question” | Answer directly; if scope creeps → structured-workflow plan |
| “Ship web feature” | agent-context → sdd-workflow → ui-design-expert → Squad B |
| “Is the app ready?” | app-auditor → (fixes) Squad C/B → re-audit slice |
| “Make README not cringe” | calibration → humanizer |
| “Analyze this repo” | Squad A Scout → INTEL_REPORT → optional auditor |
| “Data + deck for boss” | data work → calibration → humanizer for narrative |

---

## Still optional to author separately

| ID | Purpose |
|----|---------|
| `promptdivers-handoff` | HANDOFF_JSON helper |
| `promptdivers-squads` | Lazy-load one `squad-*.md` |

Bundled: `promptdivers-orchestrator`, `promptdivers-tactical-signals`, `promptdivers-pelican`.

---

*Promptdivers — one doctrine, many stratagems, finite tokens.*
