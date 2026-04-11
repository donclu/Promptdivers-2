# Prompt economics

## *Every token is a stratagem point*

> Super Earth does not have infinite stratagem points.  
> Neither does your context window.

---

## Principles

### 1. Minimum sufficient context

**Rule:** Load only what the current mission needs.

```text
Wrong — Mission C (two files):
  “Here is the entire 800-file repo…”

Right — Mission C:
  “Relevant files: route.ts (excerpt) and validators.ts (excerpt).
   Stack from AGENTS.md. Problem: …”
```

| Mission | Minimum | Typical ceiling |
|---------|---------|-----------------|
| A | Base brief + goal + stack | + answers to a few clarifying questions |
| B | AGENTS.md + SPEC + TASKS | + current batch (3–5 files) |
| C | Target files | + AGENTS.md if rules are easy to violate |
| D | PROJECT_LOG header | + last few session entries |

---

### 2. Pay once for THE AUTHENTIC

THE AUTHENTIC builds **`AGENTS.md`** once per project (or per major era). Everyone else references it.

```text
Without a shared brief:
  Every session re-explains stack and rules → repeated tokens.

With AGENTS.md:
  “Follow AGENTS.md” → amortized cost.
```

---

### 3. Forge vs Executor (Squad B)

One agent that both invents and applies in a huge refactor tends to:

- Re-read noisy failure context
- Regenerate large blobs
- Entangle planning with half-broken state

**Split:**

- **Forge:** drafts, design, file boundaries.
- **Executor:** apply, run, fix integration—**smaller** context.

Estimated savings vary by repo; the win is **less entangled context**, not a magic percentage.

---

### 4. Batches of 3–5 files

Large refactors should move in **ordered batches** with explicit dependencies, not “all files at once.”

Reasons:

- Models lose thread on long file lists.
- Easier rollback and review.
- Clearer `ESCALATE` boundaries between batches.

---

### 5. PROJECT_LOG and handoff instead of re-explaining

After a long session, a structured **handoff** beats pasting the whole chat into a new thread.

---

## Checklist before sending a prompt

```text
☐ Mission type identified (A/B/C/D)
☐ Only relevant files attached or named
☐ AGENTS.md referenced instead of retyping stack
☐ For B: batch boundary explicit
☐ For C: “do not touch” list explicit
☐ If objectives were stated: end with debrief (`protocols/mission-debrief.md`) or keyword `debrief` / `extract`
```

---

*Promptdivers — spend tokens like ammunition: deliberately.*
