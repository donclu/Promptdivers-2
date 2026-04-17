# Skill registry — what the operative can call and when

## *The Quartermaster's manifest. Know your loadout before the drop.*

> Every skill in the pack has a cost, a purpose, and a minimum clearance.
> Loading a skill above your tenure without authorization is friendly fire.
> Not loading the right skill when you need it is a mission kill.
>
> This file is the single source of truth for skill × role × tenure relationships.
> **THE QUARTERMASTER** owns this file. Update it when skills are added or deprecated.

**Related:** [./bridge-crew.md](./bridge-crew.md) · [./agent-job-families.md](./agent-job-families.md) ·
[../AGENT_PROFILE.md](../AGENT_PROFILE.md) · [../protocols/promotion.md](../protocols/promotion.md)

---

## How to read this registry

| Column | Meaning |
|---|---|
| **Skill** | Skill name / code (matches `skills/<name>/SKILL.md`) |
| **Mission tags** | Archetypes where this skill is most useful |
| **Minimum clearance** | Rookie / Veteran / Elite / Legend — do not invoke below this level without `AUTHORIZE SENIOR` |
| **Default tier** | `@low` / `@medium` / `@high` — the reasoning tier the skill works best at |
| **JF fit** | Job families that most commonly need this skill |
| **Notes** | When NOT to invoke |

---

## Core skills (ship with the pack)

| Skill | Mission tags | Min clearance | Default tier | JF fit | Notes |
|---|---|---|---|---|---|
| **promptdivers-orchestrator** | ALL | Rookie | `@low` | JF-6 (ORCHESTRATOR) | Entry point — load first |
| **promptdivers-pelican** | debrief, extract, save | Rookie | `@low` | ALL | Load at session close only |
| **promptdivers-stratagem-terminal** | any — stratagem selection | Rookie | `@low` | ALL | Route before improvising |
| **promptdivers-orbital-control** | RNF, parallel ops, multi-agent | Veteran | `@medium` | JF-6 | Do not invoke for solo work |
| **promptdivers-ministry-of-truth** | RECON, AUDIT, DATA, WRITE | Rookie | `@medium` | JF-2, JF-5 | Always load alongside research or audit |
| **promptdivers-tactical-signals** | ALL — comms | Rookie | `@low` | ALL | Not a mission skill; comms protocol only |

---

## Ecosystem skills (extend the pack)

| Skill | Mission tags | Min clearance | Default tier | JF fit | Notes |
|---|---|---|---|---|---|
| **structured-workflow** | BUILD, DATA, DIRECT, AUDIT | Rookie | `@medium` | JF-1, JF-3 | Use for multi-phase work; do not load for single-turn queries |
| **sdd-workflow** | BUILD-BACKEND, Squad B | Veteran | `@high` | JF-1 | Requires SPEC + DESIGN phase first |
| **ui-design-expert** | BUILD-WEB, VISUAL, LAUNCH-WEB | Rookie | `@medium` | JF-1 (frontend), JF-4 | Load before any UI generation |
| **app-auditor** | AUDIT, pre-ship, QA | Veteran | `@high` | JF-1, JF-2, JF-3 | Heavy — do not invoke for routine code review |
| **humanizer** | WRITE, LAUNCH-WEB, stakeholder | Veteran | `@high` | JF-4 | Run calibration first; voice without calibration = drift |
| **github-style-learner** | BUILD (any), PR review | Veteran | `@medium` | JF-1 | Load before first commit in a repo |
| **skill-creator** | meta — creating new skills | Elite | `@high` | JF-6, JF-1 | Requires senior; output must pass Ministry of Truth |
| **consolidate-memory** | extract, end-of-sprint, promotion | Veteran | `@medium` | ALL | Run at each promotion; mandatory at exit interview |
| **mcp-best-practices** | Automaton front, CI/CD, integrations | Veteran | `@medium` | JF-3 | Load when touching MCP server config |
| **docx** | WRITE, reports | Rookie | `@low` | JF-4 | Output only — not a planning skill |
| **pptx** | WRITE, presentations | Rookie | `@low` | JF-4 | Output only |
| **pdf** | DATA, RECON, WRITE | Rookie | `@low` | JF-2, JF-4 | Extraction only; do not use for reasoning |
| **xlsx** | DATA, finance, analysis | Rookie | `@medium` | JF-2 | Load for any spreadsheet-primary task |
| **humanizer** | see above | — | — | — | duplicate entry for grep convenience |

---

## Echelon Ladder skill requirements by rung

The Echelon Ladder (`stratagems/support/echelon-ladder.md`) does not load additional skills by default. Skills are invoked within a rung only if the mission archetype requires them.

| Rung | Role | Typical skills invoked |
|---|---|---|
| 0 — Classify & lookup | THE SCOUT | None (reads knowledge/ directly) |
| 1 — Plan & gap-detect | THE ARCHITECT (light) | `promptdivers-ministry-of-truth` if research gap |
| 2 — Execute | THE FORGE / THE EXECUTOR | Archetype-specific (see above table) |
| 3 — Deep reason | THE FORGE (senior) / THE AUDITOR | `app-auditor` for audit; `sdd-workflow` for design |

---

## Skills by job family (loading priority)

### JF-1 — CODE FIRST
```
Priority 1: structured-workflow, github-style-learner
Priority 2: sdd-workflow (Squad B only)
Priority 3: app-auditor (pre-ship)
On demand:  skill-creator (Elite+)
```

### JF-2 — ANALYSIS FIRST
```
Priority 1: promptdivers-ministry-of-truth (always)
Priority 2: structured-workflow
Priority 3: humanizer (reports — calibrate first)
On demand:  app-auditor, xlsx, pdf
```

### JF-3 — OPS FIRST
```
Priority 1: structured-workflow
Priority 2: mcp-best-practices
Priority 3: app-auditor
On demand:  github-style-learner (before touching automation scripts)
```

### JF-4 — WRITING FIRST
```
Priority 1: humanizer (after calibration)
Priority 2: docx / pptx / pdf (output format)
Priority 3: promptdivers-ministry-of-truth (fact-check before publish)
```

### JF-5 — RESEARCH FIRST
```
Priority 1: promptdivers-ministry-of-truth (always, mandatory)
Priority 2: structured-workflow (research phases)
Priority 3: humanizer (final deliverable prose)
```

### JF-6 — ORCHESTRATOR FIRST
```
Priority 1: promptdivers-orchestrator (self — entry point)
Priority 2: promptdivers-orbital-control (parallel missions)
Priority 3: promptdivers-stratagem-terminal (routing decisions)
On demand:  promptdivers-pelican (close-out)
```

---

## Skills requiring human authorization

These skills produce output with material real-world effects. THE DEMOCRACY OFFICER
must confirm human authorization before invocation unless the project `AGENTS.md`
pre-authorizes them.

| Skill | Reason | Authorization method |
|---|---|---|
| Any skill touching deploy / push | Irreversible external action | Explicit human keyword per session |
| **skill-creator** | Produces new doctrine | Elite clearance + DEMOCRACY OFFICER ledger entry |

---

## Registry maintenance

THE QUARTERMASTER updates this file when:
- A new skill is installed in `skills/`
- A skill is deprecated or renamed
- Minimum clearance for a skill changes after empirical evidence
- A new job family is added to `docs/agent-job-families.md`

Anti-pattern: removing skills from the registry without marking them
`status: deprecated` first. Deprecated skills stay in the registry for one full
`VERSION` cycle, then are removed.

---

*Promptdivers — know your loadout. The wrong skill at the wrong rung costs more than no skill.*
