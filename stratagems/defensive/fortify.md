# Fortify — Defensive

## Code: `FRT`

> "A module without docs is a position without sandbags."

---

## When to call

- A module or file has **no documentation** — no JSDoc, no docstrings, no README.
- Code is hard to understand without reading every line.
- A new team member (or agent) would be lost without inline context.
- After a refactor, docs are stale or missing.

---

## Inputs

1. **Target** — file, directory, or module to document.
2. **Doc style** — JSDoc, TSDoc, Python docstrings, Go doc comments, or a module-level README.
3. **Audience** — developers on the team, public API consumers, or future agents.

---

## Steps

1. **Read the target** end to end. Understand what it does.
2. **Identify public API** — exports, classes, functions, types that others consume.
3. **Write doc comments** for each public symbol:
   - One-line summary
   - Parameters with types and descriptions
   - Return value
   - Throws / errors
   - Example usage (if non-obvious)
4. **Add module-level doc** — a comment or README at the top explaining the module's purpose and how it fits in the system.
5. **Mark internal/private** symbols appropriately — `@internal`, `_prefix`, `#private`.
6. **Verify** — run doc generation if the project uses one (TypeDoc, Sphinx, GoDoc).
7. **Log:** `Stratagem: FRT on [path] — [N] symbols documented`.

---

## Outputs

- Doc comments on all public API symbols.
- Module-level overview.
- Optional: generated docs (HTML/JSON).

---

## Cooldown / limits

- No cooldown — call on every module that needs it.
- Do **not** document internal implementation details unless the human asks — focus on contract, not guts.
- Pairs with **Eagle Airstrike** (document after refactoring) and **Shield Generator** (test + doc = fortified position).

---

*"Fortify — documented territory is held territory."*
