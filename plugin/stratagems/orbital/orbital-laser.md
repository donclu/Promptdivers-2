# Orbital Laser — Orbital

## Code: `ORL`

> "Not a scalpel. Not a bomb. A continuous beam that erases everything in the path."

---

## When to call

- An entire **module, feature, or subsystem** needs to be **completely removed** from the codebase.
- This isn't dead code cleanup (Eagle 500kg) — it's systematic removal of something that was active.
- Examples: removing a deprecated API version, deleting a feature that's being replaced, eliminating an experimental branch that didn't work out.

---

## Inputs

1. **Target** — what is being removed (module name, feature area, API version).
2. **Reason** — why it's being removed (deprecated, replaced, failed experiment).
3. **Replacement** — what replaces it (if anything).
4. **Consumers** — who/what depends on the target (internal callers, external users, config references).

---

## Steps

1. **Map the target completely:**
   - All files in the module/feature
   - All imports/references from outside the module
   - All config/env references
   - All documentation references
   - All test files
2. **Categorize references:**
   - **Internal** — can be updated in this operation
   - **External** — require separate communication/migration (APIs, packages)
3. **Create removal plan** (batch if >10 files):
   ```
   Phase 1: Update/remove external references (docs, config)
   Phase 2: Redirect internal callers to replacement
   Phase 3: Delete the target module files
   Phase 4: Delete orphaned test files
   Phase 5: Clean up imports, types, index files
   ```
4. **Execute phases in order.** Test after each.
5. **Final verification:**
   - `grep -rn "target-name" .` → 0 results
   - Full test suite passes
   - Build succeeds
6. **Log:** `Stratagem: ORL — removed [target]. Files deleted: [N]. Refs cleaned: [N]`.

---

## Outputs

- Target completely removed: files, references, config, docs, tests.
- No orphaned imports or references remaining.
- Build and tests clean.

---

## Cooldown / limits

- **One removal per mission.** This is a major operation.
- Requires **Eagle Smoke Strike** first (safety branch).
- Human must **approve the removal plan** before execution.
- If external consumers exist, the human must handle communication — the agent handles code.

---

*"Orbital Laser — total removal, total liberation."*
