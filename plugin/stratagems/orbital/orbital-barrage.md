# Orbital Barrage — Orbital

## Code: `ORB`

> "When precision won't do, you level the grid square."

---

## When to call

- A **major dependency**, framework, or architectural pattern needs to change across the entire codebase.
- Examples: React → Vue, Express → Fastify, REST → GraphQL, JavaScript → TypeScript, Python 2 → 3.
- The change is **too large for Eagle** (>4 files) and needs **Squad B discipline**.

---

## Inputs

1. **Migration** — what is changing (from → to).
2. **Blast radius** — estimated number of files affected.
3. **Spec** — SPEC.md or DESIGN.md describing the target state.
4. **Rollback plan** — how to undo if it fails.

---

## Steps

1. **Prerequisite check:**
   - [ ] Squad A completed? (terrain mapped?)
   - [ ] SPEC.md / DESIGN.md exist?
   - [ ] Eagle Smoke Strike deployed? (feature branch created?)
   - [ ] Human approved the migration plan?
2. **THE FORGE** — Draft batches of 3–5 files:
   ```
   BATCH 1 — [name] — dependencies/foundation
     Files: [list]
     Risk: [LOW/MEDIUM/HIGH]
   BATCH 2 — [name] — core logic
     Files: [list]
     Depends on: BATCH 1
   ...
   ```
3. **THE EXECUTOR** — Apply batches in order. Test after each batch.
4. **THE AUDITOR** — Review each batch: scope, tests, rollback.
5. **Between batches:**
   - `📋 SITREP` — progress report
   - If problems: `⏸️ HOLD` + assess
6. **After all batches:**
   - Full test suite
   - Integration check
   - Debrief (Pelican)
7. **Log:** `Stratagem: ORB — migration [from→to]. Batches: [N]. Status: [GREEN/YELLOW/RED]`.

---

## Outputs

- Complete migration across all affected files.
- All tests passing post-migration.
- Detailed batch-by-batch log in PROJECT_LOG.
- HANDOFF_JSON with migration status.

---

## Cooldown / limits

- **One major migration per mission.** Do not stack orbital barrages.
- Always requires **Eagle Smoke Strike** first (safety branch).
- Always requires **Squad B** — THE FORGE ≠ THE EXECUTOR.
- Human must approve the batch plan before execution begins.
- If a batch fails, do **not** proceed to the next — fix or abort.

---

*"Orbital Barrage — sometimes you have to rebuild to liberate."*
