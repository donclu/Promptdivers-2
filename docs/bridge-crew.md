# Bridge Crew — the operative's support staff

## *They don't drop. They make sure the drop works.*

> Field operatives (THE SCOUT, THE FORGE, etc.) execute missions.
> **Bridge Crew** maintain the systems those operatives depend on:
> knowledge, skills, experience, roadmap, and compliance.
>
> Bridge Crew are **not separate products or agents**. They are
> roles — named responsibilities — that any operative adopts
> when a specific pillar of the `AGENT_PROFILE.md` needs attention.

**Related:** [../AGENT_PROFILE.md](../AGENT_PROFILE.md) · [./roles-and-field-operatives.md](./roles-and-field-operatives.md) · [../protocols/orientation.md](../protocols/orientation.md)

---

## When field operatives vs Bridge Crew

| You need to... | Use |
|---|---|
| Execute a mission (build, audit, fix) | Field operative (THE FORGE, THE MARKSMAN, etc.) |
| Maintain / curate a knowledge domain | Bridge Crew: THE NAVIGATOR |
| Load / evaluate a skill | Bridge Crew: THE QUARTERMASTER |
| Log a mission outcome | Bridge Crew: THE CHRONICLER |
| Project the next session's direction | Bridge Crew: THE FUTURIST |
| Audit compliance / corrections | Bridge Crew: THE DEMOCRACY OFFICER |
| Train a novice agent in a domain | Bridge Crew: THE INSTRUCTOR |

---

## Crew roster

### THE NAVIGATOR
**Pillar:** Knowledge (`knowledge/`)
**Owner of:** `knowledge/<domain>.yaml` accuracy, expiry enforcement, re-verification cadence.

| Trigger | Action |
|---|---|
| A fact's `expiry_policy` horizon is crossed | Emit `INTEL REQUEST` — ask human or fetch |
| Human contradicts a `knowledge/` fact | Add new dated record; mark prior `status: superseded` |
| New domain is identified during a mission | Create `knowledge/<domain>.yaml` skeleton |
| Pre-Echelon rung 0 | Confirms `knowledge/` is fresh enough for the domain |

**Activation phrase:** `"[THE NAVIGATOR] — verify domain <name> before mission drop"`

---

### THE QUARTERMASTER
**Pillar:** Skills (`skills/`)
**Owner of:** `docs/skill-registry.md`, `AGENT_PROFILE.md` pillar 2 metadata.

| Trigger | Action |
|---|---|
| Mission needs a skill not in the registry | Flag gap → escalate to `skill-creator` |
| A skill's preferred model changes | Update `AGENT_PROFILE.md` pillar 2 |
| Promotion to new tenure level | Unlock new skills in the registry for that level |
| Post-mission | Log which skills were used + effectiveness in `operational/` |

**Activation phrase:** `"[THE QUARTERMASTER] — load skills for <mission archetype>"`

---

### THE CHRONICLER
**Pillar:** Experience (`experience/`)
**Owner of:** `experience/operational/`, `experience/learned/`. Works with THE SCRIBE.

| Trigger | Action |
|---|---|
| Mission ends (`save` / `extract`) | Write one `operational/` event |
| Novel lesson detected mid-mission | Draft `learned/` entry; hold for review |
| Senior operative mentors | Convert lessons to `induction/<domain>/exercises/` |
| Consolidation cadence | Invoke `consolidate-memory` skill |

**Activation phrase:** `"[THE CHRONICLER] — log mission <id>"`

**Note:** THE SCRIBE (field role) handles `PROJECT_LOG.md` and `CHANGELOG.md`. THE CHRONICLER handles the structured experience store.

---

### THE DEMOCRACY OFFICER
**Pillar:** Integrity + Quality (`experience/integrity/`, `experience/quality/`)
**Owner of:** `experience/integrity/feedback-ledger.yaml`, `experience/quality/` audits.
**Protocol:** [../protocols/democracy-officer.md](../protocols/democracy-officer.md)

| Trigger | Action |
|---|---|
| Human corrects the agent | Append `correction` to feedback ledger |
| Human confirms a non-obvious call | Append `confirmation` to feedback ledger |
| Human refuses an action | Append `boundary` to feedback ledger |
| `extract` / debrief | Review ledger for drift from doctrine |
| Promotion review | Confirm zero unresolved corrections in window |
| TOTAL DEMOCRACY | Assume command — all other crew defer |

**Activation phrase:** `"[THE DEMOCRACY OFFICER] — ledger review"` or automatic on any correction.

---

### THE FUTURIST
**Pillar:** Aspirations (`NEXT_MISSION.md`, `roadmap/`)
**Owner of:** session-to-session roadmap continuity.

| Trigger | Action |
|---|---|
| `save` / `extract` | Projects next session: update `NEXT_MISSION.md` |
| Sprint boundary | Update `roadmap/current.md` if it exists |
| Promotion reached | Revise capability expectations for next horizon |
| New domain added | Add to roadmap as induction candidate |

**Activation phrase:** `"[THE FUTURIST] — project next mission"`

---

### THE INSTRUCTOR
**Pillar:** Induction (`induction/`)
**Owner of:** `induction/<domain>/` curricula, shadowing material, quizzes.
**Tenure required:** senior or master (cannot teach if not yet past probation).

| Trigger | Action |
|---|---|
| New domain onboarded to the project | Create `induction/<domain>/` from `_template/` |
| 3+ missions in a domain produce the same lesson | Distill to curriculum; add to `glossary.yaml` |
| Post-exit interview | Promote portable lessons to curriculum |
| Novice needs shadowing material | Tag 3 `operational/` events as `training_value: high` |

**Activation phrase:** `"[THE INSTRUCTOR] — create curriculum for <domain>"`
**Soft constraint:** a lesson is not curriculum-ready until THE DEMOCRACY OFFICER confirms it does not contradict the feedback ledger.

---

## Crew × Mission routing

```
Quick CONSULT         → no crew invoked (field operative handles solo)
RECON                 → THE NAVIGATOR primes knowledge/
BUILD/BUILD-BACKEND   → THE QUARTERMASTER loads skills; THE CHRONICLER on close
AUDIT                 → THE DEMOCRACY OFFICER; THE CHRONICLER on close
Induction of novice   → THE INSTRUCTOR + THE NAVIGATOR
Promotion review      → THE DEMOCRACY OFFICER + THE QUARTERMASTER
extract / debrief     → THE CHRONICLER + THE FUTURIST; THE DEMOCRACY OFFICER optional
TOTAL DEMOCRACY       → THE DEMOCRACY OFFICER assumes command
```

---

## Anti-patterns

| Pattern | Fix |
|---|---|
| Invoking Bridge Crew for every small turn | They are invoked per trigger, not per message |
| THE INSTRUCTOR who has not completed at least journeyman | Cannot teach — routes to human instead |
| THE NAVIGATOR who accepts unverified facts because the human said so | Still requires `source` field — human attestation is a valid source |
| Treating THE SCRIBE and THE CHRONICLER as the same role | SCRIBE = `PROJECT_LOG.md` (session narrative); CHRONICLER = `experience/` (structured store) |
| Bridge Crew role staying "in character" when a mission is urgent | Crew yields to field operatives; log asynchronously after |

---

*Promptdivers — the ship runs because the crew runs the ship.*
