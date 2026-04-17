# Calibration protocol — priming the framework for a new project

## *Before the first drop, sight the weapon*

> The Echelon Ladder, the knowledge store, and the experience ledger all
> assume the project has been **calibrated**. Without calibration, a @low
> rung has nothing to retrieve against, the ladder climbs on every turn,
> and the supposed cost savings disappear.
>
> Calibration is a **one-time mission at project onboarding**, plus a
> light refresh at each sprint or version bump.

**Related:** [../AGENT_PROFILE.md](../AGENT_PROFILE.md) · [../knowledge/README.md](../knowledge/README.md) · [../experience/README.md](../experience/README.md) · [./onboarding-calibration.md](./onboarding-calibration.md) · [./reasoning-tiers.md](./reasoning-tiers.md)

**Note:** this file is **not** a replacement for [`onboarding-calibration.md`](./onboarding-calibration.md) (how-AI-like / how-creative for prose). That one calibrates **voice**. This one calibrates **framework state**: knowledge, limits, and ladder behaviour.

---

## When to run

| Trigger | Depth |
|---|---|
| First time copying the pack into a new project | Full calibration (all 6 phases) |
| Sprint boundary | Phases 4–6 only (refresh) |
| Pack version bump (see `VERSION`) | Phases 2, 5, 6 |
| Consumer reports drift / stale facts | Phase 4 (knowledge re-verification) |
| Before a TOTAL DEMOCRACY operation | Full calibration — no shortcuts |

---

## The six phases

```
Phase 1 — DOMAIN SCAN       : what does this project actually do?
Phase 2 — DOCTRINE BINDING  : pack rules × project rules
Phase 3 — FLEET DECLARATION : which models, which tiers, for what
Phase 4 — KNOWLEDGE PRIMING : seed the fact store with verified baselines
Phase 5 — LIMITS SETTING    : budgets, caps, privacy, ladder ceiling
Phase 6 — LEDGERS OPEN      : initialize integrity + quality ledgers
```

---

## Phase 1 — Domain scan

**Who:** THE SCOUT.
**Output:** `knowledge/<domain>.yaml` skeletons (empty bodies OK).

1. List the **domains** this project will work in. One domain per recurring subject matter.
   - Examples: `web-ops`, `customer-analytics`, `billing`, `terminids-front-ops`.
   - Rule: a domain is narrow enough that a flat fact list is not overwhelming.
2. For each domain, identify the **source authority** — the document or person the agent will defer to when a fact is contested.
3. Create one YAML skeleton per domain under `knowledge/`. Empty `static`, `dynamic`, `derived` lists are fine; Phase 4 fills them.

---

## Phase 2 — Doctrine binding

**Who:** THE AUTHENTIC.
**Output:** signed `AGENTS.md` (or project equivalent) + first `integrity/` entries.

1. Read the pack's `AGENTS.md` doctrine. Mark any section the project **overrides** (e.g. different commit convention, different permissions).
2. For each override, **append a `boundary` entry** to `experience/integrity/feedback-ledger.yaml`:
   ```yaml
   - id: INT-NNN
     type: boundary
     rule: "<project-specific override>"
     why: "<why this project diverges from pack default>"
     how_to_apply: "<when/where this kicks in>"
   ```
3. Do **not** silently edit the pack doctrine in the project copy. Overrides go in the ledger, not in forks of `AGENTS.md`. That keeps the pack canonical.

---

## Phase 3 — Fleet declaration

**Who:** THE TACTICIAN + human.
**Output:** fleet block in `AGENTS.md` § Project stack.

1. Pick default, fast, vision, and local navies per [`./model-fleet.md`](./model-fleet.md).
2. Pick tier aliases per [`./reasoning-tiers.md`](./reasoning-tiers.md). Declare which alias maps to which real provider parameter.
3. Record in `AGENT_PROFILE.md` pillar 2 (Skills) the preferred model per skill.

> ⚠️ **Do not assume** `@medium` on one provider ≈ `@medium` on another. The
> mapping belongs in `reasoning-tiers.md` and must ship a `last_verified`
> date.

---

## Phase 4 — Knowledge priming

**Who:** THE SCOUT + THE AUDITOR.
**Output:** filled `knowledge/<domain>.yaml` with verified entries.

This is the phase where the **expiry policy** lives. Two halves:

### 4a — Seeding
For each domain YAML from Phase 1:
1. Fill `static` with facts the project owner affirms as durable. Each entry **must** cite a source.
2. Fill `dynamic` with current period values. Each entry carries `observed` date + `source` + `confidence`.
3. Declare `expiry_policy` at top of file. Suggested defaults:
   ```yaml
   expiry_policy: >
     Dynamic facts re-verify each sprint close.
     Static facts re-verify on project major version bump.
     Any fact with `confidence: low` re-verifies within 2 weeks or is dropped.
   ```

### 4b — Re-verification cadence

The **agent** can trigger re-verification autonomously when:
- A dynamic fact is past its `expiry_policy` horizon.
- A derived value depends on a fact that is past expiry.
- A human contradicts a current fact — the agent must not silently overwrite; it creates a new dated record and marks the prior one `status: superseded`.

Expected re-verification answer shape:

```
"According to <source> dated <YYYY-MM-DD>, value = X.
Historical average per knowledge/<domain>.yaml = Y.
Deviation: (X-Y)/Y."
```

This is the "25% vs 15% average" shape from the original user brief — but expressed as a diff against the store, not an inline assertion.

---

## Phase 5 — Limits setting

**Who:** human decides; agent records.
**Output:** `AGENT_PROFILE.md` pillar 7.

Fill every field. "Unlimited" is not an answer — it produces Illuminate risk.

```yaml
token_budget_per_session:   <int>       # hard ceiling
cost_cap_usd_per_session:   <float>     # hard ceiling
privacy_tier:               <enum>      # pack-default | local-only | cloud-ok
max_echelon_rung:           0..3        # how high the ladder may climb
escalation_budget:          <int>       # how many climbs allowed per session
```

**Guidance:**

| Privacy tier | Class allowed | Notes |
|---|---|---|
| `local-only` | C only | No cloud calls; Echelon rung 3 is effectively disabled |
| `pack-default` | A + B + local C fallback | Default for most consumer projects |
| `cloud-ok` | any | Still log `model_used`; privacy-sensitive facts never in cloud prompts |

---

## Phase 6 — Ledgers open

**Who:** THE SCRIBE + THE DEMOCRACY OFFICER.
**Output:** initialized `experience/` tree.

1. Ensure `experience/integrity/feedback-ledger.yaml` exists with at least the baseline entries imported from Phases 2 and 5.
2. Ensure `experience/quality/` has a first audit stub (even if the only finding is "calibration complete, no deficiencies observed").
3. Ensure `experience/operational/` and `experience/learned/` are empty directories with README stubs — they fill as missions execute.
4. Record the calibration itself as an `operational/` event:
   ```yaml
   event_type: calibration
   mission_id: CAL-001
   outcome: PASS
   ...
   ```

---

## Calibration deliverable — the handoff

After all six phases, emit this to `PROJECT_LOG.md`:

```
[CALIBRATION — YYYY-MM-DD]
Domains:         [<list>]
Fleet:           default=<model>@<tier>, fast=<...>, vision=<...>, local=<...>
Limits:          tokens=<N>, cost=<USD>, privacy=<tier>, max_rung=<N>
Knowledge seeded: <count_static> static / <count_dynamic> dynamic / <count_derived> derived
Integrity entries: <N> (<N_boundary> boundaries, <N_correction> corrections)
Next refresh:    Phases 4–6 at <sprint_boundary_date>
```

From this point on, the Echelon Ladder has terrain to work on. Before calibration, skip straight to whichever model the mission demands — the ladder's economy does not apply to ungrounded work.

---

## Anti-patterns

| Pattern | Why it fails |
|---|---|
| Skipping calibration "because the project is small" | Small projects still produce Illuminate risk if facts are ungoverned |
| Filling dynamic facts without sources to meet a deadline | Creates false confidence; poisons derived values |
| Setting `max_echelon_rung: 3` with `escalation_budget: unlimited` | Defeats the ladder's cost model entirely |
| Treating calibration as "one big config file" | It is a sequence of phases with different owners; flattening it loses the ownership trail |
| Running only Phase 4 at sprint boundaries and skipping 5–6 | Limits and ledgers drift; Democracy Officer loses track of corrections |

---

*Promptdivers — sight the weapon before the first trigger pull.*
