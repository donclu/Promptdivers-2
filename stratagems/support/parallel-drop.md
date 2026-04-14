# Parallel Drop — Support

## Code: `PRD`

> "Same planet. Multiple missions. No friendly fire."

---

## When to call

- The planet has **multiple active fronts** (e.g. Terminids + Automatons + Illuminate) and one agent will thrash.
- The mission needs **distinct domains** (e.g. DB + backend + docs) with minimal overlap.
- You want to **economize tokens** by assigning each agent a narrow context window and ownership zone.

Do **not** call if the problem is unclear terrain (use Squad A) or if the work cannot be split without overlap (stay SOLO or escalate to Squad B planning).

---

## Inputs

1. **Parallelism budget**: `OFF` | `2_AGENTS` | `3_AGENTS`
2. **Split pattern** (pick one):
   - **Explore_vs_Execute**
   - **Docs_vs_Code**
   - **DB_vs_App**
   - **SecurityAudit_vs_Delivery**
   - **FrontSlices** (Terminids/Automatons/Illuminate)
3. **Ownership map**: per agent → owned paths + `DO_NOT_TOUCH`
4. **Sync points**: when to merge and what evidence is required

---

## Protocol

### Step 1 — Declare the planet and the mission queue

- Planet state: `GALACTIC_WAR_MAP.md` + latest `PROJECT_LOG.md` entry
- Mission queue: define **Primary** (now) and list secondary/tertiary (later).

### Step 2 — Pick the split pattern

Choose the smallest split that creates independence:

```text
Explore_vs_Execute         → Agent A explores + writes brief; Agent B applies changes.
Docs_vs_Code               → Agent A fixes docs/links; Agent B fixes scripts/code.
DB_vs_App                  → Agent A schema/migrations/queries; Agent B app layer/integration.
SecurityAudit_vs_Delivery  → Agent A threat scan + guardrails; Agent B delivery within guardrails.
FrontSlices                → A=Terminids (bugs), B=Automatons (automation), C=Illuminate (AI governance).
```

### Step 3 — Create the ownership map (no overlap by default)

```markdown
## PARALLEL DROP PLAN
- PARALLELISM: OFF | 2_AGENTS | 3_AGENTS
- TOKEN_BUDGET: LOW | MED | HIGH

### Agent A (CODENAME)
- Owns: [paths]
- DO NOT TOUCH: [paths owned by others]
- Deliverable: [what it returns]

### Agent B (CODENAME)
- Owns: [paths]
- DO NOT TOUCH: [paths owned by others]
- Deliverable: [what it returns]

### Agent C (optional)
- Owns: [paths]
- DO NOT TOUCH: [...]
- Deliverable: [...]

### Sync points
- Sync 1: [time/condition] → evidence required
- Sync 2: merge → tests/lints/docs checks
```

Default rule: **if overlap appears, stop and re-split** (`⏸️ HOLD`) before editing the same file.

### Step 4 — Run in parallel (RNF)

Use RNF to spawn the extra sessions (`protocols/reinforce.md`). Require periodic SITREPs:

```text
📋 SITREP — [AGENT] — progress: [1 line] — blockers: [none|X]
⏸️ HOLD — overlap detected in [path] — re-splitting
✅ CLEAR — deliverable ready: [path|summary]
```

### Step 5 — Merge and verify

- One agent (primary) merges results.
- Run verification appropriate to the planet: tests, scripts, link checks, and a mini debrief.
- Update `PROJECT_LOG.md` and the planet map if territory status changed.

---

## Outputs

- A completed mission slice (primary) plus updated mission queue.
- Evidence-backed deliverables per agent (paths, test output, or audit notes).
- Reduced token waste via narrow ownership contexts.

---

## Anti-patterns

- Parallelizing without ownership → guaranteed friendly fire (`protocols/friendly-fire.md`).
- Spawning 3 agents when 1 would do → token burn + coordination overhead.
- Treating “more agents” as a substitute for “better brief” → run Squad A instead.

---

*Promptdivers — drop together, govern together.*

