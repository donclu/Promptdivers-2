# Agent job families — what kind of Helldiver are you?

## *Not every operative drops with the same loadout*

> Before induction starts, the project must declare which **job family**
> the agent belongs to. The family determines: default reasoning tier,
> which skills to pre-load, which Bridge Crew to activate first,
> and which `induction/<domain>/` modules are relevant.
>
> A job family is not a rigid box — operatives can cross families —
> but it is the **default loadout** for calibration.

**Related:** [./bridge-crew.md](./bridge-crew.md) · [./model-fleet.md](./model-fleet.md) · [./reasoning-tiers.md](./reasoning-tiers.md) · [../protocols/orientation.md](../protocols/orientation.md)

---

## The six families

---

### JF-1 — CODE FIRST
*"Boots on the ground. Lines shipped."*

| Attribute | Value |
|---|---|
| **Primary missions** | BUILD-BACKEND, BUILD-WEB, Squad B, Squad C surgical |
| **Default tier** | `@medium` (Forge), `@low` (Executor) |
| **Pre-load skills** | `sdd-workflow`, `structured-workflow`, `github-style-learner`, `skill-creator` |
| **Bridge Crew priority** | THE QUARTERMASTER (skills) → THE CHRONICLER (ops log) |
| **Induction focus** | Codebase structure, conventions, key modules, test patterns |
| **Echelon ceiling during probation** | rung 1 |
| **Typical tenure path** | novice → journeyman in ~8-12 missions |

**Induction domains to seed first:**
- `induction/<repo-name>/` — repo structure + conventions
- `induction/squad-b-ops/` — if the project uses Squad B heavily

---

### JF-2 — ANALYSIS FIRST
*"The mission is to know, not to build."*

| Attribute | Value |
|---|---|
| **Primary missions** | DATA, RECON, CONSULT-deep, AUDIT |
| **Default tier** | `@high` (analysis); `@low` for retrieval |
| **Pre-load skills** | `structured-workflow`, `app-auditor`, `humanizer` (for reports) |
| **Bridge Crew priority** | THE NAVIGATOR (knowledge freshness) → THE DEMOCRACY OFFICER (fact integrity) |
| **Induction focus** | Domain facts, source authority, measurement conventions, known gaps |
| **Echelon ceiling during probation** | rung 2 (analysis needs more depth earlier) |
| **Typical tenure path** | novice → journeyman in ~5-8 missions |

**Induction domains to seed first:**
- `induction/<data-domain>/` with heavy `glossary.yaml` and measurement schema
- `knowledge/<domain>.yaml` must be primed before first live mission

---

### JF-3 — OPS FIRST
*"Pipelines, deploys, and everything that should not break."*

| Attribute | Value |
|---|---|
| **Primary missions** | Automaton front (CI/CD, scripts, pipelines), Squad B migrations, Squad D defense |
| **Default tier** | `@medium`; `@low` for monitoring loops |
| **Pre-load skills** | `structured-workflow`, `mcp-best-practices`, `app-auditor` |
| **Bridge Crew priority** | THE NAVIGATOR (infra state) → THE CHRONICLER (ops events) |
| **Induction focus** | Pipeline topology, deploy targets, secrets management, rollback policy |
| **Echelon ceiling during probation** | rung 1 — ops mistakes are expensive |
| **Typical tenure path** | novice → journeyman in ~10-15 missions (conservative — high blast radius) |

**Induction domains to seed first:**
- `induction/automaton-front/` — CI/CD patterns and anti-patterns
- `knowledge/<infra-domain>/` — topology + key contracts

---

### JF-4 — WRITING FIRST
*"Words are the stratagem."*

| Attribute | Value |
|---|---|
| **Primary missions** | WRITE, LAUNCH-WEB propaganda, stakeholder comms, docs |
| **Default tier** | `@high` (prose quality demands depth) |
| **Pre-load skills** | `humanizer`, `onboarding-calibration.md` voice calibration, `docx`, `pptx` |
| **Bridge Crew priority** | THE FUTURIST (tone continuity) → THE DEMOCRACY OFFICER (brand compliance) |
| **Induction focus** | Voice guidelines, audience map, taboo words, past approved samples |
| **Echelon ceiling during probation** | rung 2 |
| **Typical tenure path** | novice → journeyman in ~6-10 missions |

**Induction domains to seed first:**
- `induction/voice-and-tone/` — samples + anti-examples
- `experience/integrity/` — any brand corrections from human

---

### JF-5 — RESEARCH FIRST
*"Find the truth before someone builds on a lie."*

| Attribute | Value |
|---|---|
| **Primary missions** | RECON-deep, Intel Dossier (IDR), CONSULT-architectural, pre-flight risk scan |
| **Default tier** | `@high` (novel synthesis); `@low` for source lookups |
| **Pre-load skills** | `promptdivers-ministry-of-truth` (critical — no hallucination), `structured-workflow` |
| **Bridge Crew priority** | THE NAVIGATOR + THE DEMOCRACY OFFICER (both mandatory) |
| **Induction focus** | Epistemics: what sources are trustworthy, how to cite, how to flag uncertainty |
| **Echelon ceiling during probation** | rung 2 |
| **Typical tenure path** | novice → journeyman in ~5-7 missions |

**Induction domains to seed first:**
- `induction/research-methods/` — source hierarchy, confidence levels, citation format
- `knowledge/<domain>/` must be fully sourced before research begins

---

### JF-6 — ORCHESTRATOR FIRST
*"Route the right operative to the right drop zone."*

| Attribute | Value |
|---|---|
| **Primary missions** | DIRECT, coordination, multi-agent fan-out, TOTAL DEMOCRACY |
| **Default tier** | `@low` / `@medium` — orchestrators iterate fast, not deep |
| **Pre-load skills** | `promptdivers-orchestrator`, `promptdivers-orbital-control`, `promptdivers-stratagem-terminal` |
| **Bridge Crew priority** | THE FUTURIST (next mission) → THE QUARTERMASTER (fleet state) |
| **Induction focus** | Squad playbooks A-D, stratagem codes, signal vocabulary, fleet manifest |
| **Echelon ceiling during probation** | rung 1 (orchestrators route, they don't deep-reason) |
| **Typical tenure path** | novice → journeyman in ~8-12 routing sessions |

**Induction domains to seed first:**
- `induction/promptdivers-operations/` — stratagem map + signal grid
- `knowledge/squad-ops.yaml` — active squads, current missions, known blockers

---

## Job family selection guide

```
Mostly writing code?                  → JF-1 (CODE FIRST)
Mostly analyzing data / making sense? → JF-2 (ANALYSIS FIRST)
Mostly keeping systems running?       → JF-3 (OPS FIRST)
Mostly producing documents/comms?     → JF-4 (WRITING FIRST)
Mostly researching / fact-finding?    → JF-5 (RESEARCH FIRST)
Mostly routing other agents?          → JF-6 (ORCHESTRATOR FIRST)
More than one?                        → Primary + secondary; primary sets probation limits
```

---

## Declaring the family in a project

Add to `AGENT_PROFILE.md` pillar 2:

```yaml
job_family:
  primary: JF-2      # ANALYSIS FIRST
  secondary: JF-5    # RESEARCH FIRST
  notes: "Finance analytics project — facts before features"
```

---

## Cross-family missions

When a mission pulls from two families, the **higher echelon ceiling** of the two applies. Example: a JF-1 operative on a WRITE mission (normally JF-4) may climb to rung 2 (JF-4 probation limit) rather than rung 1 (JF-1 probation limit) for that specific mission — but the Democracy Officer logs the cross-family use.

---

*Promptdivers — the loadout shapes the operative, but the mission tests the operative.*
