# Reinforce protocol

> "Helldiver down? Drop another one. The mission continues."

---

## What is reinforcement

In Helldivers, when a teammate dies, you **call in a reinforcement** — a new pod drops from orbit. In agent work, **reinforcement** means:

- Spawning a **second agent session** to work in parallel with the first.
- Bringing in a **different model/nave** for a task the current one can't handle.
- **Splitting work** between agents with different strengths.
- Replacing a **stuck or corrupted** session with a fresh one.

---

## When to reinforce

| Situation | Reinforcement type |
|-----------|-------------------|
| Scope too wide for one agent | Split: each agent owns different files |
| Need different skills (backend + frontend) | Specialist: each agent has a different skill focus |
| Current session context is polluted | Replace: fresh agent with clean handoff |
| Speed: parallel work would finish faster | Parallel: independent modules in separate sessions |
| Model limitation: current nave can't do vision/code/prose | Swap: different model for specific phase |

---

## Protocol

### Step 1 — Decide the split

Before calling reinforcement, define:

```markdown
## REINFORCE PLAN
- Primary agent: [CODENAME] working on [scope]
- Reinforcement agent: will work on [scope]
- Overlap zone: [files BOTH might need — requires coordination]
- DO NOT TOUCH: [files reserved for each agent exclusively]
- Sync point: [when both report back]
```

### Step 2 — Produce reinforcement briefing

The primary agent creates a handoff for the reinforcement:

```markdown
## REINFORCEMENT BRIEFING
For: [incoming agent/session]

### Mission context
- Read: AGENTS.md (stack, permissions, constraints)
- Read: PROJECT_LOG.md (latest handoff)
- Current state: [summary of where things are]

### Your assignment
- Objective: [specific goal]
- Files in your scope: [list]
- DO NOT TOUCH: [primary agent's files]
- Tests to run: [commands]

### Coordination
- Primary agent is working on: [their scope]
- Report when: [sync condition]
- Conflicts: contact primary before editing [overlap zones]
```

### Step 3 — Execute in parallel

- Both agents work independently on their assigned scope.
- If either encounters a scope conflict → `⏸️ HOLD` + notify.
- Periodic `📋 SITREP` from both.

### Step 4 — Merge and verify

- Primary agent reviews reinforcement agent's work.
- Check for conflicts in overlap zones.
- Run full test suite.
- Unified `PROJECT_LOG` update.

---

## Signals

```text
🔄 REINFORCE — requesting parallel agent for [reason]
📋 SITREP — [PRIMARY/REINFORCEMENT] — progress: [summary]
✅ CLEAR — both scopes complete, merging
🔴 RED — conflict detected in [file] — coordinating
```

---

## Anti-patterns

- Reinforcing without a **clear split** — two agents with vague scope = friendly fire guaranteed.
- Not defining **DO NOT TOUCH** zones — see `protocols/friendly-fire.md`.
- Assuming reinforcement agents have **the same context** — they don't. Always send a briefing.
- Using reinforcement when the problem is **unclear scope** — that's Squad A, not more agents.

---

*Promptdivers — more boots on the ground, same managed democracy.*
