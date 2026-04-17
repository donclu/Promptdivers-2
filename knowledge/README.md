# knowledge/ — the operative's intel vault

## *Facts with source, not vibes*

> This directory stores what the agent **knows** about the project domain, in a shape that even a low-reasoning model can read without thinking.
> It is not prose. It is a tiny, auditable fact store — every entry has a source, a date, and a confidence level.

**Related:** [../AGENT_PROFILE.md](../AGENT_PROFILE.md) · [../protocols/accuracy-policy.md](../protocols/accuracy-policy.md) · [../docs/calibration-protocol.md](../docs/calibration-protocol.md)

---

## Why a fact store instead of a doc

A prose document makes a **@medium** model re-read and re-reason every turn. A structured fact store lets a **@low** model do a lookup. That gap is where the Echelon Ladder economy lives.

```
Prose doc:   "The Bile Titan fleet was ~47 units last quarter."  →  model re-interprets each read
YAML fact:   Q_bile_titans@2026Q1 = 47 (source: ..., confidence: high)  →  deterministic lookup
```

---

## Layout

```
knowledge/
├── README.md                       ← this file (schema + rules)
├── _schema-sample.yaml             ← optional: machine-readable schema if you add one
└── <domain-name>.yaml              ← one file per domain — keep domains narrow
```

**Domain naming:** `kebab-case`, scoped narrowly. Prefer `terminids-front-ops.yaml` over `war.yaml`.

---

## Schema

Every domain file uses three sections: `static`, `dynamic`, `derived`.

```yaml
domain:           <kebab-case name>
updated:          <YYYY-MM-DD>
source_authority: <who the agent defers to for this domain>
expiry_policy:    <when to re-verify — see calibration-protocol §expiry>

static:           # facts that do not change over time
  - key:        <snake_case_identifier>
    value:      <literal — bool, string, number, or list>
    source:     <URL | document path | interview id>
    confidence: high | medium | low
    note:       <optional — one line>

dynamic:          # facts with temporal scope
  - key:        <snake_case_identifier>
    scope:      { year: YYYY, month: MM, region: <name> }   # any subset
    value:      <literal>
    unit:       <if numeric>
    source:     <required>
    confidence: high | medium | low
    observed:   <YYYY-MM-DD when the value was observed>

derived:          # computed from static + dynamic — never typed by human
  - key:        <snake_case_identifier>
    expression: "<symbolic expression referencing keys above>"
    computed_by: validator | echelon-rung-N | human
    last_computed: <YYYY-MM-DD>
```

### Field rules

| Rule | Why |
|---|---|
| `source` is **required** on every static + dynamic | Accuracy policy — no ungoverned facts |
| `confidence` is **required** — no "unknown" allowed | Forces the agent to commit to a signal |
| `expiry_policy` at top of file | Stale facts become lies; calibration sets cadence |
| `derived` never has a `value` field | Values are computed, not declared |
| Dates in ISO `YYYY-MM-DD` | Machine-readable, no ambiguity |

---

## How the agent uses it

1. **Read-only lookup first.** Before reasoning, THE SCOUT or any operative consults `knowledge/<domain>.yaml`. If the answer is there, cite the key and source. No further reasoning needed.
2. **Gap detection.** If a needed fact is absent or expired, emit `INTEL REQUEST` — either ask the human or escalate to a higher Echelon rung that can fetch it.
3. **Never overwrite silently.** Updates append a new dated record. Old values stay visible so experience keeps them.
4. **Derived ≠ declared.** If a number can be computed from other keys, it belongs in `derived`, not `dynamic`.

---

## Anti-patterns

| Pattern | Fix |
|---|---|
| One giant `knowledge.yaml` with every fact in the project | Split by domain; one file per mission frontier |
| Facts without `source` | Reject the write. No source → no fact. |
| Prose explanations in `static` | Move to `experience/learned/` — it's a lesson, not a fact |
| Updating a value in place | Add a new dated record; preserve history |
| Using this for volatile state (e.g. "current PR open") | Volatile state belongs in `PROJECT_LOG.md` handoff, not here |

---

## Example

See [terminids-front-ops.yaml](terminids-front-ops.yaml) for a worked example adapted to the Promptdivers metaphor (Terminids = bugs/defects in consumer repos).

---

*Promptdivers — know what you know, cite where you got it.*
