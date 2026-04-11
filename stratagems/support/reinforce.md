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

## Steps

1. **Produce a HANDOFF block** for the reinforcement agent:
   ```markdown
   ## REINFORCE REQUEST
   From: [CODENAME]
   Time: [timestamp]

   ### Context for reinforcement
   - AGENTS.md: [path]
   - Current mission: [description]
   - Your assignment: [specific scope]
   - DO NOT TOUCH: [files the primary agent is working on]

   ### Coordination
   - Primary agent is working on: [files/modules]
   - You are working on: [files/modules]
   - Sync point: [when both should report back]
   ```
2. **Human opens a new session** with the reinforcement briefing.
3. **Both agents report** via tactical signals when reaching the sync point.
4. **Primary agent merges** results or flags conflicts.
5. **Log:** `Stratagem: RNF — reinforcement called for [reason]. Split: [description]`.

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

---

*"Reinforce — democracy is a team sport."*
