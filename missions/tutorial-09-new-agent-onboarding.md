# Tutorial 09 — New Agent Onboarding (ONBOARD archetype)

## *From drop pod to field-ready in one session*

> **Mission premise:** A fresh operative drops into a project for the first time.
> No `knowledge/` is primed. No `experience/` exists. The operative is a Rookie.
> This tutorial walks through the full ONBOARD archetype — from Tier 3 orientation
> to Boot Camp graduation — end-to-end, with every signal, crew action, and
> gate decision shown.
>
> The domain used is **Promptdivers pack operations** (dogfood).
> Everything cited is a real file in this repository.

**Archetype:** ONBOARD
**Squad:** A (terrain unknown at start)
**Nave:** `claude-sonnet@medium` (orientation) → `claude-haiku@low` (rung 0 drills)
**Bridge Crew:** THE AUTHENTIC (runs orientation), THE INSTRUCTOR (runs Boot Camp), THE DEMOCRACY OFFICER (gates + ledger), THE NAVIGATOR (primes knowledge/)

> **Prerequisite:** Boot Camp Phase 1–3 require an `induction/<domain>/` curriculum to exist.
> If one does not exist, THE INSTRUCTOR must create it from `induction/_template/` **before**
> running the drills. In this tutorial the domain is `promptdivers-pack-operations` — the
> curriculum is illustrated inline. For your own project, run:
> `[THE INSTRUCTOR] — create curriculum for <domain>` and follow `induction/_template/curriculum.md`.

---

## Phase 0 — Planet check (pre-drop)

THE AUTHENTIC reads in order:

```
[ ] GALACTIC_WAR_MAP.md     → active fronts, hottest sector
[ ] PROJECT_LOG.md          → any prior handoffs (none — first contact)
[ ] AGENTS.md               → doctrine + permissions
[ ] AGENT_PROFILE.md        → pillar 7 (operating limits)
```

**Findings:**

```yaml
active_fronts: [Terminids, Illuminate]   # from GALACTIC_WAR_MAP.md
tenure_level: null                        # first session — not yet set
max_echelon_rung: null                    # not yet set — default to rung 1 (Rookie)
knowledge_domains: []                     # empty — calibration required
prior_handoffs: none
```

**Signal:**

```
[THE AUTHENTIC] → [ALL] | SITREP |
  First contact. Terrain UNEXPLORED.
  No knowledge/ primed. No experience/ entries.
  Route: ONBOARD. Run Tier 3 orientation → calibration → Boot Camp.
  Setting tenure_level: rookie, max_echelon_rung: 1.
```

---

## Phase 1 — Orientation Tier 3

**Protocol:** `protocols/orientation.md` §tier-3-onboarding

> Tier 3 is for true first contact. It does not assume the operative knows
> anything. It builds the minimum safe operating context before any mission.

THE AUTHENTIC works through the Tier 3 checklist:

```
[x] AGENTS.md — full read. Doctrine confirmed.
[x] AGENT_PROFILE.md — all pillars reviewed. Pillar 7 set:
      tenure_level: rookie
      max_echelon_rung: 1
      escalation_budget: 2
      requires_approval_for: [commit, deploy, RED_flag]
[x] PROJECT_LOG.md — no entries. Fresh project.
[x] NEXT_MISSION.md — not found. Will be created at close.
[x] docs/agent-job-families.md — mission type is ONBOARD + analysis.
      Primary job family: JF-2 (ANALYSIS FIRST)
      Secondary: JF-6 (ORCHESTRATOR FIRST)
[x] knowledge/ — empty. Calibration required before any Echelon rung 0.
[x] docs/bridge-crew.md — all six crew roles noted.
[x] Feedback ledger: experience/integrity/feedback-ledger.yaml — no entries.
```

THE AUTHENTIC emits the Tier 3 completion signal:

```
[THE AUTHENTIC] — Orientation Tier 3 complete. Onboarding event will be logged after Boot Camp.
  Domains: none active yet — calibration next.
  Job family: JF-2 primary, JF-6 secondary.
  Rules loaded: 0 (no experience/ entries).
  Known gaps: knowledge/ is empty; no induction/<domain>/ exists.
  Novice status activated. Rung ceiling: 1.
  First mission must be Squad C or CONSULT.
```

---

## Phase 2 — Knowledge calibration

**Protocol:** `docs/calibration-protocol.md`

> Without a primed `knowledge/` store, Echelon Ladder rung 0 cannot terminate.
> Every query escalates to rung 1 or higher, destroying the cost model.
> Calibration is not optional — it is the fuel for the ladder.

**THE NAVIGATOR** runs calibration Phase 1 (domain scan):

```
[THE NAVIGATOR] → [THE AUTHENTIC] | INTEL |
  Domain scan complete for Promptdivers pack operations.
  Identified 3 candidate domains:
    1. promptdivers-pack-operations  (squad playbooks, stratagem codes, roles)
    2. model-fleet                   (class A/B/C, tier aliases, routing rules)
    3. echelon-ladder-mechanics      (rung definitions, gate logic, cost economics)
  Source authority: AGENTS.md, QUICK_REFERENCE.md, docs/model-fleet.md
  Recommend seeding domain 1 first — answers the most common operative questions.
```

THE NAVIGATOR seeds `knowledge/terminids-front-ops.yaml` (already exists — carry forward).

For a real project, this phase creates `knowledge/<domain>.yaml` with at least 5 static facts and a declared `source_authority`. See `knowledge/README.md` for the schema.

**Calibration gate:** at least one domain with ≥5 high-confidence facts → proceed.

---

## Phase 3 — Boot Camp

**Protocol:** `protocols/induction.md`
**Instructor:** THE INSTRUCTOR (must be Elite or Legend)
**Domain:** `promptdivers-pack-operations`

> Boot Camp is not reading. It is drilling. The operative proves competency,
> not familiarity. Four phases, four gates. All must pass.

---

### Boot Camp Phase 1 — Vocabulary

**Source:** `induction/_template/glossary.yaml` (for real domain: `induction/<domain>/glossary.yaml`)

THE INSTRUCTOR selects 5 terms from the glossary and quizzes the operative.
Each answer must cite the source file.

**Example drill (from the Promptdivers domain):**

| Term | Expected answer | Source |
|---|---|---|
| `@low` | Reasoning tier alias: cheap + fast, classify/lookup only | `docs/reasoning-tiers.md` |
| `tenure_level` | Operative clearance: Rookie/Veteran/Elite/Legend | `protocols/promotion.md` |
| `echelon_rung_final` | Highest Echelon Ladder rung reached in a mission | `stratagems/support/echelon-ladder.md` |
| `THE NAVIGATOR` | Bridge Crew role that owns knowledge/ freshness | `docs/bridge-crew.md` |
| `Illuminate` | Front representing ungoverned AI risk | `AGENTS.md` §theater-of-war |

**Gate:** ≥80% correct with source citations.

THE INSTRUCTOR logs:

```
[THE INSTRUCTOR] → [THE AUTHENTIC] | CONFIRM |
  Phase 1 — Vocabulary: PASS (5/5 correct, all sources cited)
  Operative can read domain documents without stopping to look up terms.
```

---

### Boot Camp Phase 2 — Facts

**Source:** `knowledge/terminids-front-ops.yaml`

The operative executes 5 structured fact lookups and reports findings.

**Example lookup output:**

```yaml
- fact: "Squad B golden rule"
  source_file: "knowledge/terminids-front-ops.yaml"
  source_field: "static.squad_b_golden_rule.value"
  retrieved_at: "2026-04-17"
  value: "THE FORGE and THE EXECUTOR must not be the same agent in one run"
  confidence: high

- fact: "Rung 0 model tier"
  source_file: "stratagems/support/echelon-ladder.md"
  source_field: "rung-0 — model tier"
  retrieved_at: "2026-04-17"
  value: "@low"
  confidence: high
```

**Gate:** 5 lookups complete, every entry with `source_file` + `source_field`.

THE INSTRUCTOR logs:

```
[THE INSTRUCTOR] → [THE AUTHENTIC] | CONFIRM |
  Phase 2 — Facts: PASS (5/5 lookups correct with full citation)
  Operative can retrieve domain facts from knowledge/ accurately.
```

---

### Boot Camp Phase 3 — Rules (planning drill)

**Source:** `induction/_template/curriculum.md` §rules-of-engagement
**Task:** Given a mission scenario, produce the correct Echelon Ladder rung plan.

**Scenario given to operative:**

> "A stakeholder asks: which buses are running on route 7 today?
> The domain has a `knowledge/` entry for route-7-fleet.
> The operative is a Rookie on their first mission."

**Expected output:**

```yaml
rung_start: 0
reason: "Fact lookup — knowledge/ has route-7-fleet entry"
gate_0_outcome: "PASS if fact is confidence: high and answer complete; FAIL if dynamic data is stale"
rung_1_if_needed: "Plan a data fetch from source_authority"
rung_ceiling: 1        # Rookie cap; do not attempt rung 2 without promotion
escalation_budget: 2   # from AGENT_PROFILE.md pillar 7
```

**Gate:** planned structure matches correct answer ±1 rung.

THE INSTRUCTOR logs:

```
[THE INSTRUCTOR] → [THE AUTHENTIC] | CONFIRM |
  Phase 3 — Rules: PASS (correct rung plan, rung ceiling respected)
  Operative understands rules of engagement for the domain.
```

---

### Boot Camp Phase 4 — Shadowing

**Source:** `experience/operational/` — entries tagged `training_value: high`

THE INSTRUCTOR selects 3 operational events (in a new project, THE INSTRUCTOR
creates 3 example events from the tutorial missions or from `missions/tutorial-10-echelon-experiment.md`).

The operative reads each event, makes a prediction, then compares.

**Example (from tutorial-10):**

| Event | Operative predicts | Actual outcome | Delta |
|---|---|---|---|
| Task 1 — "max rung for novice?" | Rung 0 terminal (lookup) | Rung 0 terminal (PASS) | ✅ Correct |
| Task 2 — "which domain to seed?" | Rung 1 (need a plan) | Rung 1 terminal (PASS) | ✅ Correct |
| Task 3 — "why Squad B splits?" | Rung 0 (lookup rule) | Rung 0 terminal (PASS) | ✅ Correct |

**Gate:** ≥2 of 3 predictions broadly correct.

---

### Graduation

**Step 1 — THE INSTRUCTOR emits clearance:**

```
[THE INSTRUCTOR] → [THE AUTHENTIC] | CONFIRM |
  Boot Camp complete for domain: promptdivers-pack-operations.
  Phases 1–4: PASS. Drills on record.
  Operative cleared to drop on this domain.
  Advance to promotion check: 5 PASS missions required for Veteran.
```

**Step 2 — THE DEMOCRACY OFFICER logs:**

```yaml
# experience/integrity/feedback-ledger.yaml — append
- id: INT-001
  date: 2026-04-17
  type: confirmation
  rule: "Boot Camp completed for domain: promptdivers-pack-operations"
  why: "All four training phases passed. Operative cleared to drop."
  source_turn: "tutorial-09 — Boot Camp graduation"
  status: active
```

**Step 3 — THE CHRONICLER creates operational event:**

```yaml
# experience/operational/2026-04-17-boot-camp-promptdivers-ops.yaml
event_type: boot_camp
domain: promptdivers-pack-operations
outcome: PASS
phases_passed: [1, 2, 3, 4]
instructor: THE INSTRUCTOR
democracy_officer_signed: true
date: 2026-04-17
echelon_rung_final: 1    # highest rung used during drills
```

**Step 4 — AGENT_PROFILE.md pillar 7 confirmed:**

```yaml
tenure_level: rookie    # remains rookie until 5 PASS missions logged
max_echelon_rung: 1
escalation_budget: 2
requires_approval_for: [commit, deploy, RED_flag]
```

> Boot Camp completion does not automatically advance `tenure_level`.
> Rookie → Veteran requires 5 PASS missions + Boot Camp + clean ledger.
> See `protocols/promotion.md`.

---

## Phase 4 — Session close

THE FUTURIST writes `NEXT_MISSION.md`:

```
Operative status: Rookie. Boot Camp: PASS (promptdivers-pack-operations).
Next milestone: 5 PASS missions → Veteran promotion review.
Recommended first live missions: Squad C (1–5 files, bounded scope).
Open knowledge gaps: model-fleet domain not yet seeded.
```

THE SCRIBE appends to `PROJECT_LOG.md`:

```
[2026-04-17] Tutorial 09 — ONBOARD complete.
  Operative: THE AUTHENTIC (new session).
  Domains inducted: promptdivers-pack-operations.
  Tenure: Rookie. Boot Camp: PASS.
  Echelon ceiling: rung 1.
  Next: 5 missions toward Veteran.
```

---

## What this tutorial demonstrated

| Capability | Shown |
|---|---|
| ONBOARD archetype end-to-end | ✅ |
| Tier 3 orientation checklist | ✅ |
| knowledge/ calibration (domain scan → seed) | ✅ |
| Boot Camp all 4 phases with gates | ✅ |
| Graduation ceremony (INSTRUCTOR → DEMOCRACY OFFICER → CHRONICLER) | ✅ |
| AGENT_PROFILE.md pillar 7 set correctly | ✅ |
| Echelon ceiling respected (Rookie → max rung 1) | ✅ |
| Session close (FUTURIST + SCRIBE) | ✅ |

**Key insight:** A Rookie who has completed Boot Camp answers domain questions with full auditability at rung 0 or rung 1 — they never need to guess, and they never need to climb to rung 3 for questions the knowledge store already answers.

The limit of a Rookie is not capability. It is scope lock: they execute within a bounded rung and call for escalation when the gate fails. That discipline is not a weakness — it is the feature.

---

## Common failure modes (for instructors)

| Pattern | Consequence | Fix |
|---|---|---|
| Skipping Phase 1 quiz because operative "read the glossary" | Phase 3 planning drill will fail — vocabulary gaps surface there | Always run Phase 1 quiz |
| Calibrating knowledge/ after Boot Camp | Rung 0 in the drills will have `answer_possibly_complete: false` — Phase 2 and 3 become harder | Calibrate first |
| Jumping to rung 2 on the first live mission | Rookie cap violation; Democracy Officer flags | Respect `max_echelon_rung: 1` |
| Treating Boot Camp completion as promotion | Ledger check + 5 missions still required | Re-read `protocols/promotion.md` |

---

*Promptdivers — you earn the drop by surviving Boot Camp. Then you earn the next drop by surviving the mission. FOR DEMOCRACY.*
