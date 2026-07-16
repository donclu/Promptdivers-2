# experience/ — the operative's service record

## *What a veteran carries that a fresh recruit does not*

> An agent without experience repeats mistakes it has already seen.
> This directory is the difference between "ran the mission once" and "learned what the mission costs".

**Related:** [../AGENT_PROFILE.md](../AGENT_PROFILE.md) · [../knowledge/README.md](../knowledge/README.md) · [../protocols/mission-debrief.md](../protocols/mission-debrief.md)

---

## Why four subdomains

A human expert carries four kinds of memory about their job. The agent needs the same partition or every `save` becomes a dumping ground.

```
experience/
├── operational/     ← MISSIONS executed — what ran, what the outcome was
├── learned/         ← LESSONS distilled — WHY things work or fail (prose)
├── integrity/       ← FEEDBACK LEDGER — corrections + confirmations from the human
└── quality/         ← AUDITS conducted — findings, cost, recurrence
```

| Subdomain | Human analog | Primary format | Who writes it |
|---|---|---|---|
| `operational/` | A work log / CV bullets | YAML events | THE SCRIBE at `save`/`extract` |
| `learned/` | "Why we do X this way" notes | Prose `.md` + optional `.yaml` sidecar | THE SCRIBE or THE ARCHITECT on insight |
| `integrity/` | Personal code + boss corrections | YAML ledger | THE DEMOCRACY OFFICER on correction/confirmation |
| `quality/` | Audit findings / inspection reports | YAML audit records | THE AUDITOR at debrief |

**Why both prose AND code (YAML):**

- **Prose** carries the *reasoning* a future agent needs to judge edge cases. It lives in `learned/`.
- **YAML** carries the *facts and events* a low-tier model can query without reading. It lives in the other three.
- `learned/` may also ship a `.yaml` sidecar that extracts the rule + applicability for fast lookup, while the `.md` stays for depth.

---

## File naming

```
operational/YYYY-MM-DD-<mission-id>-<slug>.yaml
learned/<topic>.md                       ← optional <topic>.yaml sidecar
integrity/feedback-ledger.yaml           ← single append-only file
quality/YYYY-Qx-audit-<slug>.yaml
```

---

## Event schema — `operational/`

```yaml
event_type: mission
mission_id: <e.g. PFC-014 or Squad-B-ORB-003>
date: YYYY-MM-DD
squad: A | B | C | D | mixed
stratagems_used: [<code>, ...]
model_used: <family>
model_tier: "@low" | "@medium" | "@high" | "@max"
echelon_rung_final: 0 | 1 | 2 | 3
outcome: PASS | PARTIAL | FAIL
objectives:
  - id: obj-1
    text: "..."
    result: PASS | PARTIAL | FAIL
cost:
  tokens_in: <int>
  tokens_out: <int>
  usd_estimate: <float or null>
observations: "<one paragraph — what was surprising, what is worth remembering>"
follow_up: []     # pointer to learned/ entries if this mission produced a lesson
```

## Lesson schema — `learned/`

The `.md` file is prose: audience is the next agent, not a machine. Structure:

```markdown
# <Topic>

## The rule
<one line, imperative — "Do X" or "Never Y">

## Why
<the incident or observation that produced the rule>

## How to apply
<when this kicks in — which squad, which mission type>

## Evidence
- operational/YYYY-MM-DD-...yaml
- quality/... (if audit-derived)
- external source if any
```

Optional sidecar `.yaml` for fast machine lookup:

```yaml
topic: <slug>
rule: "<one-line imperative>"
applies_when: [<squad | stratagem | mission_type>]
confidence: high | medium | low
source_events: [operational/..., quality/...]
```

## Ledger schema — `integrity/`

One append-only file. Each entry is either a `correction` or a `confirmation`.

```yaml
entries:
  - date: YYYY-MM-DD
    type: correction | confirmation | boundary
    rule: "<imperative>"
    why: "<reason the human gave>"
    how_to_apply: "<when/where this kicks in>"
    source_turn: "<session id or git sha if logged>"
```

`correction` = human said "no, not that". `confirmation` = human said "yes, that was right" on a non-obvious call. `boundary` = human refused an action — record what and why.

## Audit schema — `quality/`

```yaml
audit_id: <slug>
date: YYYY-MM-DD
auditor: THE AUDITOR | external
scope: "<what was audited>"
findings:
  - id: F-001
    severity: LOW | MEDIUM | HIGH | CRITICAL
    category: terminid | automaton | illuminate    # per AGENTS.md fronts
    text: "..."
    resolution: open | fixed | deferred
    follow_up_mission: <operational/... if one was launched>
recurrence_check:
  - prior_audit: <quality/...>
    recurring_finding_ids: []
```

---

## How the agent uses experience during a mission

1. **Before acting** on a new task, THE SCOUT scans:
   - `operational/` for missions with same `squad` + `stratagems_used`
   - `learned/` for rules tagged with matching `applies_when`
   - `integrity/` for any `correction` or `boundary` that would forbid the planned action
2. **During the mission**, if a lesson applies, cite the `learned/` file path in the session — do not re-derive the rule.
3. **At `save` / `extract`**, THE SCRIBE writes one `operational/` event. THE DEMOCRACY OFFICER decides if any new `integrity/` entry is needed. THE AUDITOR writes `quality/` on debrief.

---

## Consolidation

Experience grows. Without pruning it becomes noise.

- Run the **consolidate-memory** skill at extraction time (see [../protocols/mission-debrief.md](../protocols/mission-debrief.md)).
- Merge duplicate `learned/` entries. Prefer one strong rule over three weak restatements.
- Archive `operational/` events older than 6 months to `experience/_archive/` unless referenced by an active `learned/` entry.
- Never delete `integrity/` entries — they are the contract with the human. Mark superseded entries with `status: superseded_by: <id>`.

---

## Anti-patterns

| Pattern | Fix |
|---|---|
| Writing lessons directly in `PROJECT_LOG.md` | `PROJECT_LOG.md` is session log; durable lessons live here |
| Copying entire diffs into `operational/` events | Event references the commit sha; do not duplicate content |
| Dropping `integrity/` entries when "no longer needed" | They accumulate meaning over time; mark superseded, never delete |
| Tagging every mission as a "lesson" | A lesson requires a WHY; without it, it's just a mission entry |
| Allowing low-confidence lessons to influence scope | Confidence matters: `low` confidence lessons are hints, not rules |

---

*Promptdivers — a veteran operative is a library, not a chatbot.*
