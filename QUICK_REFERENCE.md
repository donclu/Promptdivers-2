# Promptdivers — quick reference

## *Everything you need in the field*

---

## Three fronts (classify the fight)

```text
TERMINIDS   → bugs, regressions, flaky tests, prod defects
AUTOMATONS  → brittle classic automation (scripts, pipelines, “magic” jobs)
ILLUMINATE  → ungoverned AI: no brief, no review, leaks, shadow agents

WINNING     → gain ground for Super Earth: solutions + governed AI/automation = trailer-grade “managed democracy” and a happier crew (less firefighting, more life)
```

Details: `docs/factions-and-objectives.md`.

---

## Four guarantees (hard rules)

1. **Token efficiency**: minimum sufficient context. Prefer pointers/paths over pasting playbooks. Use `TOKEN_BUDGET`.
2. **Context questions**: if the goal/scope is unclear, ask 1–3 questions before acting.
3. **Limits notice**: if you hit a reasoning/tooling ceiling, say so early and route to RNF/SOS/ESCALATE with evidence.
4. **No hallucinations**: never invent facts, numbers, APIs, or “Helldivers canon”. If data is used, it must be auditable (path + method).

Optional brief flags:
`COMMS_MODE: STANDARD | RADIO` (see `protocols/radio-comms.md`)
`TOKEN_BUDGET: LOW | MED | HIGH`
`PARALLELISM: OFF | 2_AGENTS | 3_AGENTS`

Pack maintenance:
`protocols/pack-self-audit.md` (dogfood checklist before releases / big doc moves)

---

## Mission debrief (Pelican window)

End a phase or session with a **scored** close-out when objectives were set (or infer ≤3 and label INFERRED).

1. Each objective → **PASS** / **PARTIAL** / **FAIL** + evidence.  
2. **`mission_status`:** GREEN (all PASS) · YELLOW (PARTIAL only) · RED (any FAIL).  
3. If not GREEN → route to the **stratagem map** (Squad B, `sdd-workflow`, `mcp-best-practices`, Squad A, `app-auditor`, etc.) — see `protocols/mission-debrief.md`.  
4. Persist in `PROJECT_LOG` + optional `HANDOFF_JSON` fields (`objectives`, `mission_status`, `debrief_summary`).

Bundled skill: `skills/promptdivers-pelican/SKILL.md` (triggers: `debrief`, `extract`, mission complete).

---

## Mission archetypes (superskill router)

| Tag | Use for |
|-----|---------|
| **CONSULT** | Advice, no repo |
| **RECON** | Read-only codebase map |
| **AUDIT** | Pre-ship / app-auditor / `/explain` |
| **BUILD-WEB** | UI — load ui-design-expert early |
| **BUILD-BACKEND** | APIs, services — SDD + Squad B |
| **DATA** | Analysis, pipelines |
| **VISUAL** | Images + optional ui art-direction |
| **DIRECT** | Priorities, NEXT_MISSION, handoffs |
| **WRITE** | Human-facing prose — calibration → humanizer |
| **LAUNCH-WEB** | Campaign landing / microsite / splash — brief → copy → design Phase 0 → static ship → deploy |

Full map: `docs/super-earth-operating-model.md` · Calibration: `docs/onboarding-calibration.md`.  
Tutorial index: `missions/README.md` (copy-paste missions that scaffold model reasoning).

---

## Mission tree

```text
STEP 0 — Planet check (pre-drop):
  → Read GALACTIC_WAR_MAP.md (or PROJECT_LOG.md / AGENTS.md debt section)
  → Identify active fronts + hottest sector + threat level
  → Derive squad + nave recommendation
  → Fill "Planet status" block in NEXT_MISSION  (see protocols/pre-drop.md)
  → If no planet state exists: Squad A first, or ask for verbal SITREP

No AGENTS.md / no project brief?
  → Squad A (Advance) — Map the terrain first

>10 files or heavy refactor / migration?
  → Squad B (Artillery) — Prefer Squad A first if terrain is unknown

Bug or feature in ~1–5 files?
  → Squad C (Surgical) — One shot, one objective

QA, PR review, monitoring, pre-deploy?
  → Squad D (Defense) — Continuous loop

Production crisis or human says TOTAL DEMOCRACY?
  → Operation Total Democracy — All squads
```

---

## Solo vs help (token economy)

Use the lightest call that unblocks progress:

```text
SOLO (stay in-thread)  → clear next step, ≤5 files, no major unknowns
RNF Reinforce          → needs parallelism (draft vs apply, or explore vs execute)
SOS SOS Beacon         → blocked and need a human decision, access, or missing info
ESCALATE               → high-risk / policy / security / scope contract change
```

Rule of thumb: **blocked = SOS**, **wide but clear = RNF**, **dangerous = ESCALATE**.

Optional paste into your brief: `TOKEN_BUDGET: LOW | MED | HIGH`  
Interpretation: LOW = minimal text + proof only; MED = balanced; HIGH = thorough exploration + richer reports.

Optional paste into your brief: `PARALLELISM: OFF | 2_AGENTS | 3_AGENTS`  
Interpretation: OFF = solo only; 2/3 = allow RNF splits with explicit ownership + sync points. Use `PRD` (Parallel Drop) when the planet has multiple active missions/fronts.

---

## Stratagem loadout (pick what fits your mission)

Full codex: [`stratagems/README.md`](stratagems/README.md). Invoke by name in chat.

```text
⚔️ OFFENSIVE — attack problems directly
  OPS  Orbital Precision Strike  — rewrite one critical file from spec
  EAS  Eagle Airstrike           — coordinated change across 2–4 files
  RGN  Railgun                   — eliminate an unnecessary dependency
  ACN  Autocannon                — automated lint + format pass
  DSK  Data Strike               — data analysis, cleaning, pipeline work
  ATA  Automaton Assault         — fix/replace/build automation and scripts

🛡️ DEFENSIVE — protect liberated territory
  SHG  Shield Generator          — add tests for uncovered code
  GDG  Guard Dog                 — set up CI/CD regression guard
  TSL  Tesla Tower               — install pre-commit hooks
  FRT  Fortify                   — document a module with docstrings

📦 SUPPORT — logistics and coordination
  RNF  Reinforce                 — request parallel agent session
  RSP  Resupply                  — refresh context (re-read AGENTS.md + logs)
  SOS  SOS Beacon                — structured escalation to human
  PRD  Parallel Drop             — coordinate multi-mission planet work (ownership + RNF)
  HPD  Hellpod                   — bootstrap file from project pattern
  IDR  Intel Dossier             — structured research and intelligence gathering
  PFG  Prompt Forge              — design, test, and iterate AI prompts

🦅 EAGLE — fast strikes (reusable)
  E5K  Eagle 500kg               — delete confirmed dead code
  ESS  Eagle Smoke Strike        — create feature/safety branch before risky edits
  ERM  Eagle Rearm               — clean session close with debrief + handoff
  ERP  Eagle Report              — produce formal reports and deliverables
  EVS  Eagle Visuals             — generate diagrams, mockups, charts, visuals

☄️ ORBITAL — heavy strikes (require Squad B)
  ORB  Orbital Barrage           — major framework/dependency migration
  ORL  Orbital Laser             — full module/feature removal
  OEM  Orbital EMS               — scope freeze until review
```

---

## Roles — first line to paste

```text
THE AUTHENTIC   — Load AGENTS.md + log. Define scope. Brief the next role.
THE SCOUT       — Read-only recon. No edits. Emit INTEL report.
THE ARCHITECT   — SPEC + DESIGN + TASKS. Surface tradeoffs on big choices.
THE SENTINEL    — Pre-flight risks and edge cases.

THE FORGE       — Produce drafts (e.g. /drafts). Match repo patterns. Do not “just apply everywhere.”
THE EXECUTOR    — Apply drafts in order. One focused step at a time.
THE AUDITOR     — Tests + diff + scope. APPROVE or ESCALATE.
THE VALIDATOR   — “Only the agreed files?” Yes → CONFIRM. No → ESCALATE.

THE MARKSMAN    — Diagnose → root cause → minimal fix → test. Single-threaded.
THE SCRIBE      — PROJECT_LOG + changelog + brief updates to AGENTS.md when stack shifts.
THE TACTICIAN   — Prioritized backlog + NEXT_MISSION recommendation.
```

---

## Human keywords

```text
status            → SITREP / checkpoint
save              → Log + handoff (+ memory if configured); if objectives were tracked, include debrief per protocols/mission-debrief.md
debrief           → Run Pelican window: score objectives, mission_status, stratagem routing; then log/handoff
extract           → Same as debrief (mission end / RTB)
handoff           → Structured handoff for another agent
escalate          → Escalation ladder
TOTAL DEMOCRACY   → Level 5 — all squads
scope check       → In-scope vs out-of-scope
debt              → List DEBT-xxx
abort             → Stop + rollback if safe
```

---

## Tactical pings (signals first)

**Idea:** same as Helldivers—**pings beat paragraphs** for mixed-language crews; English stays canonical in files.

| Lead | Meaning |
|------|---------|
| 🟢 GREEN | Clear / go |
| 🟡 YELLOW | Caution / flaky |
| 🔴 RED | Blocked / tests fail |
| 🚨 ALERT | Critical / prod / security |
| 🎯 ON TARGET | Scope locked |
| 📍 MARK | Look: path or line |
| ⏸️ HOLD | Pause |
| 🚀 GO | Authorized |
| ✅ CLEAR | Done / pass |
| ❌ NO GO | Reject |
| ⬆️ STEP UP | Escalate |
| 📋 SITREP | Status snapshot |
| o7 | Acknowledged |

Full doctrine + examples: `protocols/tactical-signals.md`.

---

## Inter-agent line format

```text
[CODENAME] → [RECIPIENT or ALL] | TYPE | Message

TYPE: SITREP | INTEL | REQUEST | CONFIRM | ESCALATE | ABORT
```

---

## Fleet (model selection — naves)

Match ship class to mission complexity. Full manifest: `docs/model-fleet.md`.

```text
CLASS A  (heavy cruisers) — deep reasoning, large context
  claude-sonnet/opus    RECON, BUILD-BACKEND, AUDIT, WRITE, Squad B Forge
  gpt-4o                BUILD-WEB, DATA, VISUAL (vision)
  gemini-pro/1.5        AUDIT full repos (1M ctx), DATA+docs, video/audio

CLASS B  (frigates) — fast iteration, low cost
  claude-haiku          Squad C, CONSULT quick, ping loops, Squad D review
  gpt-4o-mini           First-pass audit, structured extract
  gemini-flash          Rapid image check, fast SITREP

CLASS C  (local / private)
  mistral/llama/qwen    Sensitive data, offline, on-prem
  codestral/deepseek    Code-only Forge work
```

**Declare in `AGENTS.md` stack:**
```text
Model (nave):  <model>    ← default
Model fast:    <model>    ← Squad C + iteration
Model vision:  <model>    ← multimodal tasks
Model local:   <model>    ← private payloads
```

**In NEXT_MISSION + HANDOFF_JSON:** always record `nave` and a one-line `model_rationale` when the choice is non-obvious.

---

## Token cheatsheet

```text
Mission C: only the 2–3 files that matter.
Mission B: AGENTS.md + SPEC/TASKS + current batch (3–5 files), not the whole repo.
Mission A: brief + stack + goal; cap clarifying questions (e.g. 3) unless human wants more.
Reuse AGENTS.md instead of retyping the stack every session.
Split Forge vs Executor on B → large savings and fewer chained mistakes.
Use CLASS B model for iteration phases; upgrade to CLASS A only when depth is needed.
```

---

## Mission queue (primary / secondary / tertiary)

```text
Pattern: one question → one primary mission → work reveals sub-missions → debrief cycles.

PRIMARY    → the mission you drop into right now (squad + nave + objective).
SECONDARY  → missions that surface during the primary. Do NOT start them mid-primary.
             Add to missions_queued in HANDOFF_JSON with spawned_by: "primary".
TERTIARY   → follow-up tasks that depend on a secondary completing.
             Add with spawned_by: "secondary-N".

Rule: never silently expand scope. When new work appears → log it as secondary or tertiary
      → finish the primary first → debrief → check queue → deploy next.

In NEXT_MISSION.md → fill the "Mission queue" section as work unfolds.
In HANDOFF_JSON   → missions_queued[] carries the full queue to the next session.
```

---

## Risk levels

```text
LOW       — proceed; note for auditor
MEDIUM    — proceed carefully; auditor should see it
HIGH      — change plan before more edits
CRITICAL  — stop, redesign, escalate
```

---

## Escalation levels (short)

```text
1 — Squad C alone
2 — C + Defense auditor pass
3 — Full Squad B
4 — Squad A re-brief (context / design stale)
5 — TOTAL DEMOCRACY
```

---

## Golden rules

```text
1. On Squad B, Forge and Executor are never the same agent in one run.
2. Scout never mutates files—read only.
3. ESCALATE always includes evidence.
4. Without a project brief, do not pretend Squad B or C is “free solo”—do A first.
5. If scope grows during C → STOP → ESCALATE toward B.
6. End of session → update PROJECT_LOG (no exceptions).
7. No commit without human instruction unless they explicitly delegated that.
8. Model switches must be logged (session block + HANDOFF_JSON model_rationale).
9. Never route sensitive data to a cloud model without explicit AGENTS.md permission.
```

---

## Files every serious project should have

```text
AGENTS.md (or CLAUDE.md mirror)  — agent contract
PROJECT_LOG.md                    — running history + handoff
INTEL_REPORT.md                   — terrain map produced by Squad A (THE SCOUT); read-only output, not a deliverable
Intel Dossier (IDR stratagem)     — structured research deliverable; invoked on demand for deep investigation
SPEC.md / DESIGN.md / TASKS.md    — as needed for larger work
NEXT_MISSION.md                   — optional; Squad D / Tactician
GALACTIC_WAR_MAP.md               — optional; copy from templates/galactic-war-map.template.md
```

---

*Promptdivers — FOR DEMOCRACY.*
