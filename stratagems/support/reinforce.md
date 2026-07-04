# Reinforce — Support

## Code: `RNF`

> "Helldiver down! Calling reinforcements!"

---

## When to call

- The current task is **too broad** for a single agent session but doesn't warrant full Squad B.
- You need a **parallel agent** working on a different aspect of the same problem.
- Different **skill sets** are needed simultaneously (e.g., one agent on backend, another on frontend).

---

## Inputs

1. **Reason** — why reinforcement is needed (scope, skills, speed).
2. **Split** — how to divide the work between agents.
3. **Shared state** — what both agents need to know (AGENTS.md, relevant files, constraints).
4. **Conflict zones** — files that **both** agents might touch (these need coordination).

---

## Canonical protocol

This stratagem is an **action card**. The canonical procedure lives in:

- `protocols/reinforce.md`

Use that protocol for the full split/briefing/merge steps and anti-patterns.

---

## Outputs

- Reinforcement briefing document.
- Clear scope split with no overlap in "hot" files.
- Sync point defined.

---

## Cooldown / limits

- Max **2 parallel agents** unless the human is experienced with multi-agent coordination.
- Always define **DO NOT TOUCH** zones — two agents editing the same file = Friendly Fire.
- If the split is unclear, this is actually a Squad B job — escalate instead.

## Claude Code mechanism

RNF with 2 agents = two `Agent` tool calls issued together (each can carry its own `model`); this needs no special opt-in. If the split needs more than 2 agents, staged phases, or per-agent `effort` control, that's `PRD` territory and requires the `Workflow` tool, which is gated — see [`docs/claude-code-model-execution.md`](../../docs/claude-code-model-execution.md).

---

*"Reinforce — democracy is a team sport."*
