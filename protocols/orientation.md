# Orientation — the first-hour protocol

## *Read before you drop*

> An operative who starts acting before reading context is a conscript.
> An operative who reads the right files in the right order is a Helldiver.
>
> Orientation is **not induction** — it is the minimum required to not
> cause friendly fire on day one. Full domain mastery comes from induction
> (`induction/<domain>/`). Orientation only gets you safe to operate.

**Related:** [../ORIENTATION.md](../ORIENTATION.md) · [../AGENT_PROFILE.md](../AGENT_PROFILE.md) · [./induction.md](./induction.md) · [../docs/bridge-crew.md](../docs/bridge-crew.md)

---

## Who runs orientation

**THE AUTHENTIC** runs orientation at session start. Every session. Even if the operative has visited the project before — context windows do not persist, so re-orientation is not redundant, it is required.

The only exception: the session explicitly states a `PROJECT_LOG.md` handoff was loaded and the operative is resuming mid-mission (not starting fresh).

---

## The four tiers of orientation

```
Tier 0 — EMERGENCY      : 2 minutes. Minimum safe context only.
Tier 1 — STANDARD       : 5-10 minutes. Normal session start.
Tier 2 — FULL           : 15-20 minutes. New domain, first session on project.
Tier 3 — ONBOARDING     : 30-60 minutes. True first contact — no prior familiarity.
```

---

## Tier 0 — Emergency (2 min)

Used when: mid-crisis, production issue, TOTAL DEMOCRACY activated.

Read in this order — stop at first answer:

1. `PROJECT_LOG.md` — latest handoff block only.
2. `AGENTS.md` — permissions section only.
3. State assumptions out loud. Begin.

---

## Tier 1 — Standard (5-10 min)

Used when: returning to a known project for a regular session.

Read in this order:

- [ ] `AGENTS.md` — full (< 5 min, always worth re-reading)
- [ ] `AGENT_PROFILE.md` — pillar 7 (operating limits) + pillar 1 (which knowledge/ domains active)
- [ ] `PROJECT_LOG.md` — handoff block + last 3 entries
- [ ] `NEXT_MISSION.md` — what was scoped for this session
- [ ] Check `experience/integrity/feedback-ledger.yaml` — any `status: active` corrections

After reading, emit one line:
```
[THE AUTHENTIC] — Orientation Tier 1 complete. Active domains: <list>. 
Tenure: <level>. Rung ceiling: <N>. Ready.
```

---

## Tier 2 — Full (15-20 min)

Used when: first session on a project already calibrated but new to this operative.

Steps, in order:

- [ ] All of Tier 1 above.
- [ ] `docs/agent-job-families.md` — identify primary job family.
- [ ] `AGENT_PROFILE.md` — all pillars.
- [ ] `knowledge/<active-domain>.yaml` — for each domain in pillar 1.
- [ ] `experience/learned/` — scan file list; read any rule with `applies_when` matching planned mission.
- [ ] `induction/<domain>/glossary.yaml` — if it exists.
- [ ] `docs/bridge-crew.md` — which crew is relevant this session?

After reading, emit:
```
[THE AUTHENTIC] — Orientation Tier 2 complete.
Domains: <list>. Job family: <JF-N>. 
Rules loaded: <count>. Known gaps: <list>.
Ready for induction (if novice) or mission briefing.
```

---

## Tier 3 — Onboarding (30-60 min)

Used when: true first contact — the operative has never worked on this project
(or the project has never had an operative before — calibration has not run).

**Prerequisite:** calibration must run first if `knowledge/` is empty.
See [../docs/calibration-protocol.md](../docs/calibration-protocol.md).

Steps:

- [ ] Run Tier 2 checklist.
- [ ] Run calibration if `knowledge/` has no non-placeholder entries.
- [ ] Read `induction/<domain>/curriculum.md` for each active domain.
- [ ] Complete at least Layer 1 (vocabulary) and Layer 2 (foundational facts) of induction.
- [ ] Pass induction Layer 1 quiz before proceeding.
- [ ] Set `tenure_level: novice` in `AGENT_PROFILE.md` pillar 7.
- [ ] Set `max_echelon_rung` per job family probation limit.
- [ ] THE DEMOCRACY OFFICER logs the onboarding event in `experience/operational/`.

After reading, emit:
```
[THE AUTHENTIC] — Orientation Tier 3 complete. Onboarding event logged.
Novice status activated. Rung ceiling: <N>.
First mission must be Squad C or CONSULT.
```

---

## What orientation does NOT do

| Action | Where it belongs |
|---|---|
| Learn a domain deeply | `induction/<domain>/` + shadowing |
| Load all skills | THE QUARTERMASTER, triggered by the specific mission |
| Write anything | Nothing is written during orientation |
| Make decisions | Orientation is read-only |
| Re-derive policies | Policies exist in files; orientation reads them, never invents |

---

## Trigger keywords

If the human says any of the following, run the matching tier:

| Human says | Run tier |
|---|---|
| `status`, `resume`, `continue` | Tier 1 |
| `new session`, `brief me`, `orient` | Tier 2 |
| `onboard`, `first session`, `new project` | Tier 3 |
| `TOTAL DEMOCRACY`, crisis signal | Tier 0 |

---

## Anti-patterns

| Pattern | Fix |
|---|---|
| Skipping orientation because "the context is obvious" | Context windows lose state; re-read is never wasted |
| Running Tier 3 on every session | Tier 3 is onboarding only; use Tier 1 for regular sessions |
| Reading files not in the checklist "just in case" | Token economy; load on demand once mission is known |
| Acting before emitting the completion signal | Signal confirms the operative is ready; skip it = conscript mode |

---

*Promptdivers — read first, drop second.*
