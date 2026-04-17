# Echelon Ladder — Support

## Code: `ELD`

> "Climb the rungs only as far as the mission demands. Every rung you skip, you pay for at the top."

---

## When to call

- You need to execute a task where a **low-tier model might be enough**, but you are not sure in advance.
- You want to **extract the maximum reasoning** out of low/medium tiers before committing @high or @max.
- You have a **calibrated** project (see [`../../docs/calibration-protocol.md`](../../docs/calibration-protocol.md)) — the ladder needs `knowledge/` and `experience/` primed to produce savings.
- You want the cost profile of a ladder, not of a single heavy-model call.

Do **not** call:

- For single-turn trivial lookups (go straight `@low`, no ladder).
- For Squad D pass-through reviews where judgment is the product.
- During TOTAL DEMOCRACY — emergency protocol supersedes cost optimization.
- On a fresh project with no calibration — the ladder has nothing to retrieve against.

---

## Inputs

1. **Task** — what the mission wants done.
2. **Success criteria** — how a gate will know the rung's output is acceptable.
3. **Max rung allowed** — from `AGENT_PROFILE.md` pillar 7 (operating limits).
4. **Escalation budget** — how many climbs allowed in this session.
5. **Available fleet** — resolved per [`../../docs/reasoning-tiers.md`](../../docs/reasoning-tiers.md).

---

## The four rungs

```
RUNG 0  —  CLASSIFY & LOOKUP           (@low)
RUNG 1  —  PLAN & GAP-DETECT           (@low or @medium)
RUNG 2  —  EXECUTE                     (@medium)
RUNG 3  —  DEEP REASON / FINAL WORD    (@high or @max)
```

Between each rung sits a **gate**. The gate is deterministic wherever possible (schema validation, checklist of booleans, presence of required keys). Only if the deterministic gate is undecidable does a light model act as arbiter.

---

## Rung 0 — Classify & lookup

**Model tier:** `@low`.
**Role:** THE SCOUT.

1. Parse the task. Extract:
   - Domain (one of the declared `knowledge/<domain>.yaml` names).
   - Mission archetype (CONSULT / RECON / BUILD / DATA / ...).
   - Explicit variables or parameters mentioned in the task.
2. Query `knowledge/` for facts matching the extracted domain + variables.
3. Query `experience/learned/` for rules whose `applies_when` matches.
4. Emit **Rung-0 Report**:

```yaml
rung: 0
task_summary: "<one line>"
domain: <knowledge/ domain or null>
archetype: <CONSULT | RECON | ...>
extracted_variables: { ... }
facts_found:
  - key: <key>
    value: <value>
    source: <from knowledge/>
    confidence: <from knowledge/>
rules_applicable:
  - path: experience/learned/<file>.md
    rule: "<one-line rule>"
answer_possibly_complete: true | false
missing_to_answer: [ ... ]     # if not complete
```

### Gate 0 → 1

**PASS criteria** (terminal — do not climb):

- `answer_possibly_complete: true` AND
- All facts used have `confidence: high` AND
- No `experience/integrity/` `boundary` entries forbid the planned action.

If PASS: THE SCOUT produces the final answer citing `knowledge/` keys. Log as `echelon_rung_final: 0` in the operational event.

**FAIL criteria:** `answer_possibly_complete: false` OR any fact is `confidence: low` OR the task requires action (not just answer). Climb to Rung 1.

---

## Rung 1 — Plan & gap-detect

**Model tier:** `@low` or `@medium` per routing table in `reasoning-tiers.md`.
**Role:** THE ARCHITECT (light mode).

1. Take the Rung-0 Report as input.
2. Produce a **plan** broken into concrete phases.
3. Identify **gaps** — missing facts, missing skills, missing permissions.
4. Produce a **checklist** the next rung must satisfy.
5. Emit **Rung-1 Report**:

```yaml
rung: 1
plan:
  - phase: 1
    action: "<what>"
    stratagem: <code or null>
    model_tier: "@<alias>"
  - phase: 2
    ...
gaps:
  - "<missing fact/skill/permission>"
checklist:
  - "<testable boolean>"
  - ...
risk_flags: [ ... ]
```

### Gate 1 → 2

**PASS criteria:**

- Plan covers all phases to reach success criteria.
- No critical gap unresolved (gaps either filled by INTEL REQUEST or marked acceptable).
- Checklist is **testable** — no vague items.
- Risk flags acceptable per `AGENT_PROFILE.md` limits.

**TERMINAL PASS** (do not climb): if the task was "produce a plan" and the plan is the deliverable, stop here. Log as `echelon_rung_final: 1`.

**FAIL criteria:** plan incomplete, gaps blocking, checklist untestable. Either recurse Rung 1 with added context or escalate to Rung 2 with a caveat.

---

## Rung 2 — Execute

**Model tier:** `@medium`.
**Role:** THE FORGE / THE EXECUTOR (per Squad B rule — not the same agent).

1. Consume the Rung-1 checklist as the contract.
2. Execute each phase in the plan.
3. Produce the deliverable.
4. Self-check against the checklist before handoff.
5. Emit **Rung-2 Report**:

```yaml
rung: 2
deliverable: "<path or content reference>"
checklist_results:
  - item: "<from rung 1>"
    pass: true | false
    evidence: "<pointer>"
failures: [ ... ]
```

### Gate 2 → 3

**PASS criteria:** every checklist item `pass: true`, no failures flagged, scope held.

**TERMINAL PASS** (most missions): log `echelon_rung_final: 2` and extract.

**FAIL criteria:** any checklist item failed, novel problem surfaced that requires reasoning outside the plan, audit surfaces concerns the @medium tier cannot adjudicate. Climb to Rung 3 — but only within the session's `escalation_budget`.

---

## Rung 3 — Deep reason / final word

**Model tier:** `@high` or `@max`.
**Role:** THE FORGE (senior) or THE AUDITOR for audit missions.

1. Consume the Rung-2 Report **plus** all prior rungs as context.
2. Focus exclusively on the failure(s) identified at Gate 2 → 3 — do **not** redo the plan.
3. Produce either:
   - A correction to Rung 2's deliverable, or
   - A recommendation to abort the mission (ESCALATE signal).
4. Emit **Rung-3 Report**:

```yaml
rung: 3
mode: correction | escalation
correction: "<if mode=correction, the targeted change>"
escalation_reason: "<if mode=escalation>"
new_learned_entries: [ ... ]     # what the session taught for experience/learned/
```

### Terminal PASS

Rung 3 has no gate above it. It either produces the correction (mission PASS at `echelon_rung_final: 3`) or emits ESCALATE (mission PARTIAL / FAIL).

---

## Cost economics — when the ladder wins

The ladder saves cost only when the **gate distribution** favors lower rungs. Target distribution on a calibrated project:

```
Rung 0 terminal:  30-50%
Rung 1 terminal:  15-25%
Rung 2 terminal:  30-50%
Rung 3 reached:   <15%
```

If over time `experience/operational/` shows `echelon_rung_final: 3` on more than ~15% of missions, the ladder is not saving cost — the knowledge store is under-primed, gates are too strict, or the project genuinely needs heavy reasoning and should default to `@high`. Re-run calibration Phase 4 and 5.

---

## Handoff fields the ladder adds

Every mission executed with `ELD` must log:

```json
"echelon": {
  "rungs_climbed": [0, 1, 2],
  "rung_final": 2,
  "gate_decisions": [
    { "gate": "0->1", "decision": "climb", "reason": "facts incomplete" },
    { "gate": "1->2", "decision": "climb", "reason": "terminal pass not applicable" },
    { "gate": "2->3", "decision": "stop",  "reason": "checklist pass" }
  ],
  "escalation_budget_remaining": 2
}
```

---

## Anti-patterns

| Pattern | Fix |
|---|---|
| Always climbing to Rung 3 "just in case" | Trust the gates; log every climb so the economy stays visible |
| Vague checklists at Rung 1 | A checklist item must be a testable boolean |
| Letting Rung 2 silently redo Rung 1's plan | Squad B rule: different operative. Rung 2 consumes, does not re-plan |
| Skipping Rung 0 on "obviously complex" tasks | Rung 0 is cheap; a surprising fact in `knowledge/` can collapse the plan |
| Treating `escalation_budget` as unlimited | The budget is the circuit breaker; without it, the ladder is just more turns |

---

## Cooldown / limits

- Respect `max_echelon_rung` from `AGENT_PROFILE.md` pillar 7.
- Respect `escalation_budget` per session.
- If both are hit before mission ends: emit ESCALATE to the human, do not silently stop.
- Always write one `experience/operational/` event per mission regardless of outcome.

---

*"Every rung climbed is a signal the rung below was not enough. Listen to the signal; do not drown it."*
