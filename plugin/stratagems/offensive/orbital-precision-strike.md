# Orbital Precision Strike — Offensive

## Code: `OPS`

> "One file. One rewrite. Clean as a laser from orbit."

---

## When to call

- A **single file** is the root cause of a critical problem.
- The file needs a **complete rewrite**, not a patch — the current code is beyond surgical repair.
- You have **clear specs** for what the file should do (from SPEC.md, tests, or human description).

---

## Inputs

1. **Target file** — exact path.
2. **Specification** — what the rewritten file must do (behavior, API contract, tests it must pass).
3. **Constraint** — which interfaces/imports **must not change** (to avoid collateral damage).

---

## Steps

1. **Read** the target file end to end. Note all exports, imports, and callers.
2. **Catalog dependencies** — who imports from this file? List them.
3. **Write the replacement** from spec, matching the existing API surface.
4. **Diff check** — ensure no export was removed that a caller uses.
5. **Run tests** (if they exist). If tests break, the strike missed — revert and report.
6. **Log** the stratagem in session notes: `Stratagem: OPS on [path]`.

---

## Outputs

- Rewritten file passing all existing tests.
- Diff summary for auditor review.
- `📍 MARK` signal pointing at the rewritten file.

---

## Cooldown / limits

- **One file per invocation.** If you need to rewrite multiple files, use Eagle Airstrike or escalate to Squad B.
- Requires **THE MARKSMAN** or **THE FORGE** role. THE EXECUTOR should not call this without a draft.

---

*"Orbital Precision Strike — because sometimes the cleanest fix is a new file."*
