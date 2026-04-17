# induction/ — domain curricula and training material

## *Learn the battlefield before you fight on it*

> A fresh operative reads AGENTS.md and understands the doctrine.
> But doctrine is not domain knowledge.
> Doctrine tells you HOW to work. Domain knowledge tells you WHAT you are working on.
>
> This directory holds the **curricula** that close that gap — fast.

**Related:** [../AGENT_PROFILE.md](../AGENT_PROFILE.md) · [../protocols/orientation.md](../protocols/orientation.md) · [../protocols/induction.md](../protocols/induction.md) · [../docs/bridge-crew.md](../docs/bridge-crew.md)

---

## Structure

```
induction/
├── README.md                         ← this file
├── _template/                        ← copy this to start a new domain
│   ├── curriculum.md                 ← 4-layer learning plan
│   ├── glossary.yaml                 ← terms, definitions, synonyms
│   ├── exercises/
│   │   ├── 01-vocabulary-drill.md    ← Layer 1 drills
│   │   ├── 02-fact-lookup-drill.md   ← Layer 2 drills
│   │   └── 03-planning-drill.md      ← Layer 3 drills
│   └── quiz.yaml                     ← pass/fail gate between layers
└── <domain>/                         ← one folder per domain
    └── (same structure as _template)
```

---

## The four layers of induction

| Layer | Name | Goal | Duration (agent-time) | Gate |
|---|---|---|---|---|
| 1 | **Vocabulary** | Agent can speak the domain language | 20-30 min | Glossary quiz pass rate ≥ 80% |
| 2 | **Foundational facts** | Agent reads `knowledge/<domain>.yaml` without confusion | 30-40 min | Fact-lookup drill: 5 questions, cite sources |
| 3 | **Rules and patterns** | Agent knows the "why" behind key decisions | 40-60 min | Planning drill: given a scenario, produce correct plan |
| 4 | **Shadowing** | Agent studies 3 past missions as if replaying them | Variable | Predict-and-compare exercise, delta logged |

**Layer 4 is optional** for `@medium`+ models with high confidence on Layers 1-3. Always required for novice operatives and new domains.

---

## How to create a domain curriculum

1. Copy `_template/` to `<your-domain>/`.
2. Fill `curriculum.md` — who the audience is, what sources to read, in what order.
3. Fill `glossary.yaml` — at least 10 terms before the first mission drops.
4. Fill `quiz.yaml` with at least 5 questions per layer.
5. Tag 3 entries in `experience/operational/` as `training_value: high` for Layer 4.
6. THE INSTRUCTOR signs off → curriculum is active.

**Shortcut for new projects:** run calibration first (Phase 4), then generate the glossary from `knowledge/<domain>.yaml` static entries. One hour of work, not a day.

---

## When to use vs skip

| Situation | Use induction? |
|---|---|
| First session on a domain this project has never touched | Yes — all 4 layers |
| Returning operative, same domain, new session | No — Orientation Tier 1 only |
| Returning operative, new sub-domain added since last session | Yes — Layer 1-2 only |
| Cross-family mission (JF-1 doing JF-4 work) | Yes — Layer 1 of target family |
| Emergency / TOTAL DEMOCRACY | Skip — Orientation Tier 0 only |

---

## Quality signal

A curriculum is **good** when:
- A novice operative, after completing it, passes a real mission in the domain at rung ≤ 2.
- A fresh `@low` model can answer domain glossary questions by lookup, without reasoning.

A curriculum is **bad** when:
- It is just a list of links to external docs.
- It has no drills or quiz.
- The glossary has fewer than 10 entries.
- No shadowing material is tagged (operational/ has no `training_value: high` events).

---

*Promptdivers — know the terrain. Then move.*
