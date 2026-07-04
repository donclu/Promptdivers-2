# Claude Code — how "nave" and "echelon rung" become real tool calls

## *Declaring a ship in AGENTS.md does not launch it*

> ⚠️ **Verification required.** This document describes tool names and parameters
> observed in a live Claude Code session on `last_verified: 2026-07-04`. Harness
> tool schemas change across versions — re-check the current Claude Code docs
> before relying on exact parameter names for anything load-bearing.

**Related:** [`model-fleet.md`](model-fleet.md) · [`reasoning-tiers.md`](reasoning-tiers.md) · [`../squads/squad-b-artillery.md`](../squads/squad-b-artillery.md) · [`../stratagems/support/echelon-ladder.md`](../stratagems/support/echelon-ladder.md)

---

## The one thing to get right

**The main conversation thread runs on exactly one model until a human changes it.** An agent cannot silently swap its own underlying model mid-turn just because a mission calls for `claude-opus@high`. Declaring `Model (nave): claude-opus@high` in `AGENTS.md` is a **label for humans and for the two mechanisms below** — it is not, by itself, an instruction the running model can execute on itself.

Two things in Claude Code **do** cause a real model change, and one is human-only:

| Mechanism | Who triggers it | What it actually switches |
|---|---|---|
| `/model` command | Human, mid-session | The **main thread's** model, from that point forward |
| `Agent` tool (subagent) | The assistant, per call | The **subagent's** model — main thread is unaffected |
| `Workflow` tool (script) | The assistant, gated (see below) | Model **and** effort, per `agent()` call inside the script |

Everything in this pack that talks about "swapping ships mid-mission" resolves to one of these three rows. If a squad playbook or stratagem doesn't name one of them, it's still doctrine — not yet mechanism.

---

## Two independent axes, not one

Promptdivers already separates **nave** (model family: Sonnet/Opus/Haiku/...) from **echelon rung** (`@low`–`@max`, reasoning depth). That split maps cleanly onto Claude Code's own two parameters — but they live on **different tools**:

- The top-level `Agent` tool exposes **`model`** only (`sonnet` / `opus` / `haiku` / `fable`). No effort knob at this layer — a subagent spawned this way reasons at that model's default depth.
- A `Workflow` script's internal `agent()` calls expose **both** `model` and `effort` (`low` / `medium` / `high` / `xhigh` / `max`) per call, and per phase.

Practical consequence: if you need nave **and** rung control together (e.g. "Squad B Forge on Opus at `@high`, Executor on Sonnet at `@medium`"), you need the `Workflow` tool, not a bare `Agent` call — the plain `Agent` tool can pick Opus for you but can't also dial the rung.

```text
Alias        → Agent tool `model`   → Workflow `effort` (if rung control matters)
@low         → haiku                → low
@medium      → sonnet                → medium
@high        → sonnet or opus        → high
@max         → opus                  → max
```

---

## Mechanism 1 — subagent per call (`Agent` tool)

Use when a mission phase needs a **different model**, no rung control needed, and it's a single self-contained hand-off (not a multi-stage pipeline). This is available in every session, no opt-in required.

```text
Agent({
  description: "THE FORGE — draft Squad B batch 1",
  subagent_type: "general-purpose",
  model: "opus",
  prompt: "<batch scope, files, DO NOT TOUCH list, draft-only — see squad-b-artillery.md>"
})
```

A second, separate `Agent` call — different context, can be a different model — becomes THE EXECUTOR. That *is* the mechanical form of the Squad B golden rule ("Forge and Executor are never the same agent in one run"): two calls, not one agent role-playing two hats.

---

## Mechanism 2 — `Workflow` tool (model + effort per phase, gated)

Use for genuinely multi-stage or parallel missions where rung control matters: Echelon Ladder escalation, PRD (Parallel Drop), or a Squad B run with more than two roles.

**Gate — this is not free-fire.** The `Workflow` tool only fires when the human has explicitly opted into multi-agent orchestration: an "ultracode" signal, an explicit ask in the human's own words ("use a workflow", "fan out agents"), or **a skill/command whose own instructions tell the assistant to call it**. Promptdivers can satisfy that last condition on purpose: `promptdivers-orchestrator` (and the PRD / Squad B playbooks it routes to) may instruct "for this mission shape, invoke `Workflow`" — that's a legitimate trigger per the tool's own rules. Without one of these, defer to Mechanism 1 (plain parallel `Agent` calls) or ask the human.

Illustrative shape (not literal syntax — see current `Workflow` tool docs):

```text
phase('Forge')
const draft = await agent(FORGE_PROMPT, { model: 'opus', effort: 'high', phase: 'Forge' })
phase('Execute')
const applied = await agent(EXECUTE_PROMPT(draft), { model: 'sonnet', effort: 'medium', phase: 'Execute' })
```

---

## Mechanism 3 — `/model` (human-driven, main thread)

The human runs `/model` to change what the **main conversation** runs on. The assistant can — and should — *recommend* this ("esto conviene correrlo en Opus, ¿querés cambiar de modelo?") but cannot invoke it on itself. This is the right lever when the whole session, not just one subtask, needs a different tier (e.g. moving from quick CONSULT to a deep AUDIT with no subagents involved).

---

## Mapping Promptdivers constructs to a mechanism

| Construct | Mechanism | Note |
|---|---|---|
| Squad B — Forge ≠ Executor | Mechanism 1 (two `Agent` calls) or Mechanism 2 if rung differs too | See `squads/squad-b-artillery.md` |
| RNF (Reinforce) | Mechanism 1 — multiple `Agent` calls in one message | `stratagems/support/reinforce.md` |
| PRD (Parallel Drop) | Mechanism 2 (`Workflow` `parallel()`/`pipeline()`) if opted-in; otherwise multiple `Agent` calls | `stratagems/support/parallel-drop.md` |
| Echelon Ladder (rungs 0–3) | Mechanism 2 — one `agent()` call per rung, escalating `model`/`effort`; the **gate between rungs stays deterministic code**, not a model call, whenever possible | `stratagems/support/echelon-ladder.md` |
| "Whole session needs more depth" | Mechanism 3 (`/model`) | Not per-subtask — this is a session-wide change |

---

## What this does NOT change

- The main thread's model is still fixed until a human runs `/model`. No amount of doctrine in `AGENTS.md` self-executes.
- `Workflow` is still gated — Promptdivers cannot use it as a silent default just because a mission "feels" heavy. The gate exists to stop token-expensive fan-out from firing without consent, and that reasoning applies here too.
- None of this changes the golden rule "model switches must be logged" (`AGENTS.md`) — if anything it makes the log more literal: record which mechanism ran, not just the alias.

---

*Promptdivers — the ship manifest was always a promise. This is the delivery mechanism.*
