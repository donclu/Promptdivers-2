# Why low-rung planning saves heavy-rung cost

## The rule

Always run Echelon Ladder rungs 0 and 1 (low-tier planning + gap detection) **before** committing any @high or @max model to a task — even when the task "obviously" needs a heavy model.

## Why

A heavy model asked to plan + execute in one shot re-derives the plan every turn. A low-tier plan, written once and validated against a gate, becomes a **contract** that the heavy model consumes cheaply. Observed in `operational/2026-04-17-squad-b-orb-001-hot-zone.yaml`: the @medium Forge never climbed to @high because the @low Scout had already partitioned the work.

The deeper principle: heavy-tier reasoning is expensive because it is **generative** per call. Low-tier reasoning is cheap because it is largely **retrieval + classification**. The Echelon Ladder moves retrieval down and generation up, so the heavy model is only asked to do the irreducibly generative part.

## How to apply

Triggers:

- Any mission tagged `BUILD-BACKEND`, `BUILD-WEB`, Squad B, or Squad C with >2 files.
- Any `CONSULT` where the human has given a long brief — a @low rung should first extract the question shape before any @medium+ answer.

Do **not** apply:

- Single-turn `CONSULT` that is unambiguously a lookup (answer is in `knowledge/`).
- Squad D pass-through reviews where the judgment is the whole point.
- Emergency / TOTAL DEMOCRACY — the ladder is a cost optimization, not a crisis protocol.

## Evidence

- `experience/operational/2026-04-17-squad-b-orb-001-hot-zone.yaml`
- `stratagems/support/echelon-ladder.md` §gating-rules
- General pattern: see `docs/prompt-economics.md` for the pack's prior articulation of token economy.

## Caveat

The rule assumes the low-tier rungs have **knowledge/** facts to retrieve against. A project that has not run calibration (see `docs/calibration-protocol.md`) cannot expect the ladder to produce savings on the first missions — the knowledge store has to be primed first.
