# Induction — Boot Camp graduation protocol

## *You don't earn a drop clearance by reading about drops*

> Boot Camp is not a reading list. It is a series of live drills — each one
> designed to prove the operative can operate under fire in the domain, not
> just recite its glossary.
>
> Passing all four training phases is the only path to **Cleared to Drop** status.
> There are no shortcuts past Layers 1–3. Not for any model. Not under any circumstance.

**Related:** `induction/<domain>/curriculum.md` · `induction/<domain>/quiz.yaml` ·
[`protocols/promotion.md`](./promotion.md) · [`docs/bridge-crew.md`](../docs/bridge-crew.md) ·
[`AGENT_PROFILE.md`](../AGENT_PROFILE.md)

---

## Who runs Boot Camp

**THE INSTRUCTOR** owns the Boot Camp from first drill to graduation signal.
The INSTRUCTOR must hold Elite or Legend clearance — a Rookie or Veteran cannot run
induction for another operative. If no eligible INSTRUCTOR is available, route to human
with an INTEL REQUEST.

**THE DEMOCRACY OFFICER** gates promotion after Boot Camp is complete.
THE INSTRUCTOR certifies the operative passed the drills; THE DEMOCRACY OFFICER
confirms the ledger is clean before advancing `tenure_level` in `AGENT_PROFILE.md`.

---

## The four training phases

```
Phase 1 — VOCABULARY     : Glossary fluency. Know the language before you fly.
Phase 2 — FACTS          : Domain facts with citations. Know the terrain.
Phase 3 — RULES          : Planning drill. Know the rules of engagement.
Phase 4 — SHADOWING      : Live-fire simulation. Predict before you execute.
```

---

## Phase 1 — Vocabulary

**Source material:** `induction/<domain>/glossary.yaml`

The operative answers a glossary quiz drawn from the domain's `quiz.yaml`.
Every answer must include the source citation (file path + field name) from `knowledge/`
or `induction/<domain>/`.

**Pass gate:** ≥80% correct answers, all correct answers citing source.

---

## Phase 2 — Facts

**Source material:** `knowledge/<domain>.yaml` + any `induction/<domain>/facts.yaml`

The operative executes 5 distinct fact lookups in the domain's knowledge files and
reports findings in structured form: `fact`, `source_file`, `source_field`, `retrieved_at`.

**Pass gate:** All 5 lookups complete, every entry citing `knowledge/` correctly.
A lookup that produces "not found" counts as pass if the operative correctly identifies
the gap and emits an INTEL REQUEST for it.

---

## Phase 3 — Rules

**Source material:** `induction/<domain>/curriculum.md` §rules-of-engagement

The operative completes a planning drill: given a mission scenario, produce the
correct Echelon Ladder rung plan (start rung, escalation path, stop condition).
Evaluated against the answer key in `induction/<domain>/quiz.yaml`.

**Pass gate:** The planned structure matches the correct answer ±1 rung.
An off-by-two or higher counts as fail.

---

## Phase 4 — Shadowing

**Source material:** `experience/operational/` — entries tagged `training_value: high`
in the active domain (minimum 3 entries; THE INSTRUCTOR selects them).

The operative reads each tagged operational event, makes a prediction before seeing
the recorded outcome, then compares. Predictions are recorded in the drill log.

**Pass gate:** ≥2 out of 3 shadowing predictions broadly correct (correct squad route,
correct rung, or correct correction type — any two of these three axes counts).

---

## Failure handling

### First fail — retry

Re-do the failed phase drill once. No penalty; no escalation.
THE INSTRUCTOR notes the retry in the session log.

### Second fail — gap analysis

Escalate to THE INSTRUCTOR for a structured gap analysis:
- Which concept or fact caused both failures?
- Is it a knowledge gap (missing from `knowledge/`) or a doctrine gap (missing from curriculum)?
- THE INSTRUCTOR emits a corrective note; the operative gets one more attempt.

### Third fail — curriculum may need updating

```
[THE INSTRUCTOR] → [HUMAN] | INTEL REQUEST |
  Operative has failed Phase <N> three times on domain <domain>.
  Possible curriculum gap. Please review:
    - induction/<domain>/quiz.yaml — are the questions unambiguous?
    - induction/<domain>/curriculum.md — is the relevant concept covered?
  Recommend holding promotion until curriculum is updated.
```

This is not a demotion event. The operative remains at current `tenure_level`.
The gap is logged in `experience/quality/`.

---

## Graduation ceremony

When all four phases are passed:

**Step 1 — THE INSTRUCTOR emits the clearance signal:**

```
[THE INSTRUCTOR] → [OPERATIVE] | CONFIRM |
  Boot Camp complete. Cleared to drop on <domain>.
  Phases 1–4: PASS. Drills on record.
  Advance to promotion check if tenure criteria are met.
```

**Step 2 — THE DEMOCRACY OFFICER logs the confirmation:**

Append to `experience/integrity/feedback-ledger.yaml`:

```yaml
- id: INT-NNN
  date: <today>
  type: confirmation
  rule: "Boot Camp completed for domain <domain>"
  why: "All four training phases passed. Operative cleared to drop."
  source_turn: "induction — <domain> Boot Camp graduation"
  status: active
```

**Step 3 — THE CHRONICLER creates the operational event:**

```yaml
# experience/operational/<date>-boot-camp-<domain>.yaml
event_type: boot_camp
domain: <domain>
outcome: PASS
phases_passed: [1, 2, 3, 4]
instructor: THE INSTRUCTOR
democracy_officer_signed: true
date: <today>
```

**Step 4 — AGENT_PROFILE.md update:**

THE DEMOCRACY OFFICER advances `tenure_level` in pillar 7 by one step
(Rookie → Veteran, if promotion criteria are also met — see `protocols/promotion.md`).
If promotion criteria are NOT yet met, Boot Camp completion is recorded but
`tenure_level` does not advance until the mission count and ledger conditions are clear.

---

## Phase shortcuts

| Condition | Permitted shortcut | Who signs off |
|---|---|---|
| `@high` or `@max` model with documented prior exposure to the domain | May skip Phase 4 (Shadowing) | THE INSTRUCTOR confirms in writing |
| Cross-domain transfer from an already-inducted domain | May not skip any phase — starts at Phase 1 in the new domain | No exceptions |
| Existing `experience/learned/` entries in the domain | Do NOT substitute for passing the quiz | Non-negotiable |
| Phase 1–3 | No shortcut under any condition | Absolute rule |

The @high / @max shortcut for Phase 4 exists because shadowing predicts behavior
under novel conditions — a model with documented domain exposure has already
demonstrated that exposure. Phase 1–3 establish the shared vocabulary and citation
discipline that every operative and every crew member depends on.

---

## Cross-domain induction

An operative who is Cleared to Drop on Domain A and begins Domain B:

- Starts at Phase 1 in Domain B. No carry-over of phase completions.
- `tenure_level` does NOT reset. A Veteran who picks up a new domain remains Veteran
  while completing Domain B Boot Camp.
- Domain B Boot Camp completion is a separate event in `experience/operational/`.
- Echelon rung caps apply per the operative's current `tenure_level`, not per domain.

---

## Anti-patterns

| Pattern | Fix |
|---|---|
| Skipping the quiz because "the operative has read the glossary" | Reading is not drilling. Run the quiz. |
| Running Boot Camp without an eligible INSTRUCTOR | Route to human if no Elite/Legend is available |
| Logging Boot Camp complete before Phase 4 | THE DEMOCRACY OFFICER will not sign incomplete drills |
| Treating a retry as a demotion signal | Retries are normal. Three fails are a curriculum signal, not a condemnation. |
| Running cross-domain Boot Camp starting at Phase 3 | Domain B starts at Phase 1. Always. |

---

*Promptdivers — you earn the drop by surviving the Boot Camp. FOR DEMOCRACY.*
