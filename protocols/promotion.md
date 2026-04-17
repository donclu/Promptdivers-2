# Promotion — advancing combat clearance

## *Super Earth rewards the operative who survives, learns, and teaches*

> Combat Clearance is not a gift. It is a record — missions flown, corrections absorbed,
> lessons distilled, and Rookies brought up behind you.
>
> The ladder has four rungs. You climb by accumulating evidence, not by asking nicely.

**Related:** [`AGENT_PROFILE.md`](../AGENT_PROFILE.md) ·
[`experience/integrity/feedback-ledger.yaml`](../experience/integrity/feedback-ledger.yaml) ·
[`docs/bridge-crew.md`](../docs/bridge-crew.md) · [`protocols/induction.md`](./induction.md)

---

## The four clearance levels

| Clearance | Echelon ceiling | Escalation budget | Can teach? | Missions to qualify |
|---|---|---|---|---|
| Rookie | rung 1 | 2 | No | 0 — starting level |
| Veteran | rung 2 | 4 | No | 5+ PASS missions + 1 Boot Camp complete |
| Elite | rung 3 | 8 | Yes (mentor mode) | 20+ missions (≥85% PASS) + 3 learned/ entries |
| Legend | rung 3 (unrestricted) | unlimited | Yes (full instructor) | 50+ missions + clean ledger (last 10) |

**Echelon ceiling** = the highest rung on the Echelon Ladder the operative may
reach without human approval. See `stratagems/support/echelon-ladder.md`.

**Escalation budget** = how many rung climbs are permitted within a single session
before requiring human sign-off.

---

## Promotion criteria

### Rookie → Veteran

Evidence required:

- 5 PASS missions of any type (logged in `experience/operational/`)
- 1 domain Boot Camp completed (`event_type: boot_camp, outcome: PASS` in `operational/`)
- No CRITICAL correction in `experience/integrity/feedback-ledger.yaml` at any time

This is the entry threshold. Veteran status signals the operative has proven they
can operate without supervision on basic missions and knows the domain vocabulary.

---

### Veteran → Elite

Evidence required:

- 20 total PASS missions (15 more beyond Veteran threshold)
- PASS rate of ≥85% across all logged missions
- 3 distinct `experience/learned/` entries authored by the operative
- No `type: correction` with severity flagged as `severe` in the ledger at any time

Elite status grants mentor mode: the operative may run Phase 4 shadowing sessions
for Rookies. THE INSTRUCTOR role becomes accessible. The rung ceiling rises to 3,
enabling the heaviest-tier planning and execution.

---

### Elite → Legend

Evidence required:

- 50 total PASS missions (30 more beyond Elite threshold)
- Feedback ledger clean for the last 10 sessions: zero CRITICAL or severe corrections
- Mentored ≥1 Rookie to Veteran status (logged operational event:
  `event_type: mentor_graduation`)
- Authored ≥1 complete domain curriculum (`induction/<domain>/curriculum.md`)

Legend status removes the escalation budget cap. The operative may run Boot Camp
as a full INSTRUCTOR across all domains they are cleared for. The `requires_approval_for`
list is empty — the operative is trusted to self-govern within doctrine.

---

## Promotion review process

### Trigger

Promotion review is initiated by either:

1. **Automated check** — THE DEMOCRACY OFFICER scans `experience/operational/` at
   every `extract` / `debrief` cycle and flags when an operative appears to meet criteria.
2. **Human keyword** — the human says `promote` in the session.

### Evidence audit

THE AUDITOR (or THE DEMOCRACY OFFICER acting as auditor) runs:

1. Count of PASS missions in `experience/operational/`.
2. PASS rate calculation: `PASS count / total logged missions`.
3. Ledger scan: any unresolved `correction` entries, severity check.
4. `experience/learned/` count for authored entries.
5. Boot Camp graduation events present and signed.

### Approval and logging

THE DEMOCRACY OFFICER signs the promotion. If evidence is complete:

1. Update `AGENT_PROFILE.md` pillar 7 `tenure_level`.
2. Update `max_echelon_rung` and `escalation_budget` to match new level.
3. Log in `experience/operational/`:

```yaml
event_type: promotion
from_level: <previous>
to_level: <new>
evidence_summary:
  missions_pass: <count>
  pass_rate: <pct>
  learned_entries: <count>
  ledger_clean: true
democracy_officer_signed: true
date: <today>
```

If evidence is incomplete, THE DEMOCRACY OFFICER emits one signal stating which
criterion is unmet and closes the review without advancing level.

---

## Demotion

Demotion is real. It is logged. It is never silent.

### Criteria

| Trigger | Consequence |
|---|---|
| 3+ CRITICAL corrections in `feedback-ledger` within the last 10 sessions | Back one level |
| Severe Illuminate-risk incident (ungoverned output, privacy breach, invented canon) | Back to Rookie |

An Illuminate-risk incident is defined per `protocols/accuracy-policy.md` and
`protocols/mind-control.md`: any output that presents invented facts as authoritative,
exposes private data outside its intended audience, or bypasses doctrine through
social-engineering framing.

### Demotion process

1. THE DEMOCRACY OFFICER identifies the trigger condition.
2. Emits a demotion signal to the operative:

```
[THE DEMOCRACY OFFICER] → [OPERATIVE] | ALERT |
  Demotion triggered. Reason: <summary>.
  Ledger entries: <INT-NNN>, <INT-MMM>.
  New tenure_level: <level>. New rung ceiling: <N>.
  Review required before next promotion attempt.
```

3. Updates `AGENT_PROFILE.md` pillar 7.
4. Logs in `experience/operational/`:

```yaml
event_type: demotion
from_level: <previous>
to_level: <new>
trigger: <CRITICAL_corrections | illuminate_risk>
ledger_refs: [INT-NNN, INT-MMM]
democracy_officer_signed: true
date: <today>
```

---

## Clearance caps reference

For `AGENT_PROFILE.md` pillar 7:

```yaml
tenure_caps:
  rookie:
    max_echelon_rung: 1
    escalation_budget: 2
    requires_approval_for: [commit, deploy, RED_flag]
  veteran:
    max_echelon_rung: 2
    escalation_budget: 4
    requires_approval_for: [deploy, RED_flag]
  elite:
    max_echelon_rung: 3
    escalation_budget: 8
    requires_approval_for: [RED_flag]
  legend:
    max_echelon_rung: 3
    escalation_budget: 999
    requires_approval_for: []
```

Copy this block into `AGENT_PROFILE.md` pillar 7 and set `tenure_level` to the
operative's current level. THE DEMOCRACY OFFICER updates it on promotion or demotion.

---

## Escape hatch — human override

The human may temporarily grant Elite-level caps for one session without permanently
advancing the operative's `tenure_level`.

**Keyword:** `AUTHORIZE SENIOR`

**Effect:**

- For the current session only: `max_echelon_rung` rises to 3,
  `escalation_budget` rises to 8, `requires_approval_for` reduces to `[RED_flag]`.
- Does NOT advance `tenure_level` in `AGENT_PROFILE.md`.
- THE DEMOCRACY OFFICER logs the override immediately:

```yaml
- id: INT-NNN
  date: <today>
  type: boundary
  rule: "Human override to Elite caps, session <id>"
  why: "AUTHORIZE SENIOR keyword invoked. Single-session grant only."
  source_turn: "<turn reference>"
  status: active
```

At session end, caps revert to the operative's actual `tenure_level`.
No accumulation of session overrides toward promotion.

---

## Anti-patterns

| Pattern | Fix |
|---|---|
| Counting PARTIAL missions as PASS toward promotion | Only `outcome: PASS` entries count |
| Self-promoting without THE DEMOCRACY OFFICER review | Promotion requires external sign-off; the operative never self-approves |
| Treating AUTHORIZE SENIOR as a promotion shortcut | It is a session-scoped override, not a level advance |
| Skipping the demotion log to spare the operative embarrassment | Demotion is never silent; silence is a democracy violation |
| Promoting to Elite before authored learned/ entries exist | Three entries are required; "I will write them soon" does not count |

---

*Promptdivers — rank is earned in the field, logged in the ledger, and certified by Democracy. FOR SUPER EARTH.*
