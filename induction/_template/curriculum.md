# Curriculum — [DOMAIN NAME]

> Copy this file to `induction/<your-domain>/curriculum.md` and fill in the bracketed fields.
> Delete this header block when the curriculum is finalized.

**Domain:** [kebab-case name, must match a `knowledge/<domain>.yaml`]
**Job families:** [JF-N, ...] — which operatives this is for
**Created:** [YYYY-MM-DD]
**Author / THE INSTRUCTOR:** [role or session id]
**Status:** draft | active | superseded

---

## Audience

[One paragraph: what kind of operative, what they already know, what they do NOT know yet.]

---

## Sources of truth

[List the canonical sources for this domain. These become the `source_authority` in `knowledge/<domain>.yaml`.]

1. [Primary source — URL or file path]
2. [Secondary source]
3. [Tertiary / fallback]

---

## Layer 1 — Vocabulary (target: 20-30 min)

**Goal:** operative can read a domain document without stopping to look up terms.

### What to read
- `induction/[domain]/glossary.yaml` — all entries
- [Optional: one short reference doc, max 2 pages]

### Drills
- `induction/[domain]/exercises/01-vocabulary-drill.md`

### Gate
- `induction/[domain]/quiz.yaml` — Layer 1 section
- **Pass criteria:** ≥ 80% correct answers, sources cited

---

## Layer 2 — Foundational facts (target: 30-40 min)

**Goal:** operative can look up domain facts from `knowledge/` and cite them accurately.

### What to read
- `knowledge/[domain].yaml` — full file
- [Optional: one external reference that backs the most important dynamic facts]

### Drills
- `induction/[domain]/exercises/02-fact-lookup-drill.md`

### Gate
- `induction/[domain]/quiz.yaml` — Layer 2 section
- **Pass criteria:** 5 facts retrieved correctly with source citation

---

## Layer 3 — Rules and patterns (target: 40-60 min)

**Goal:** operative knows WHY the key decisions in this domain are made the way they are.

### What to read
- `experience/learned/` — entries with `applies_when` including this domain
- [Any design docs, ADRs, or known-decision files specific to this project]

### Drills
- `induction/[domain]/exercises/03-planning-drill.md`

### Gate
- `induction/[domain]/quiz.yaml` — Layer 3 section
- **Pass criteria:** given a scenario, produce a plan that matches the expected structure

---

## Layer 4 — Shadowing (variable duration)

**Goal:** operative has "seen" the domain in action and can predict decisions correctly.

### What to study
Tag at least 3 entries in `experience/operational/` with `training_value: high` for this domain.
The operative reads each in this order:
1. Read the input + context only. Pause.
2. Predict: what would the plan be? What rung would it reach?
3. Read the actual outcome. Compare.
4. If delta is significant, add a note to `experience/learned/`.

### Gate
- No formal quiz. THE INSTRUCTOR reviews the delta notes.
- **Pass criteria:** ≥ 2 out of 3 predictions were broadly correct (structure, not exact wording).

---

## Known gaps

[List things the curriculum does NOT cover. Be honest — gaps known up front are safer than gaps discovered in production.]

- [Gap 1]
- [Gap 2]

---

## Anti-patterns for this domain

[3-5 common mistakes specific to this domain. Each should reference a `learned/` entry if one exists.]

| Anti-pattern | Why it fails | Source |
|---|---|---|
| [Pattern] | [Failure mode] | [experience/learned/...] |

---

## Graduation criteria

An operative is **inducted** in this domain when:
- Layers 1-3 quizzes: all passed.
- Layer 4: at least attempted (even if predictions were off — the delta log matters more).
- THE INSTRUCTOR (or THE DEMOCRACY OFFICER) signs off.
- Tenure level advances by one step if this was the first domain for that operative.
