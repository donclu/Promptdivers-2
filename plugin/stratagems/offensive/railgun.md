# Railgun — Offensive

## Code: `RGN`

> "One shot. One dependency. Gone."

---

## When to call

- A **dependency** (npm package, pip package, gem, etc.) should be **removed** — it's unused, redundant, a security risk, or replaceable with stdlib.
- You need to verify that nothing actually uses it before deleting.

---

## Inputs

1. **Target dependency** — name and current version.
2. **Reason** — why is it being removed (unused / vulnerability / replaced by X).

---

## Steps

1. **Search the entire codebase** for imports/requires of the dependency.
   ```
   grep -rn "import.*from.*<dep>" src/
   grep -rn "require.*<dep>" src/
   ```
2. **If found** — list every usage. Can each be replaced? If yes, proceed. If not, abort.
3. **Replace usages** with the alternative (stdlib, another dep, custom code).
4. **Remove from manifest** — `package.json`, `requirements.txt`, `Cargo.toml`, etc.
5. **Remove lockfile entry** — run `npm install` / `pip install` / equivalent to regenerate.
6. **Run tests.** If anything breaks, the dependency was not truly removable.
7. **Log:** `Stratagem: RGN — removed [dep] (reason: [X])`.

---

## Outputs

- Dependency removed from manifest and lockfile.
- All former usages replaced or confirmed absent.
- Test results.

---

## Cooldown / limits

- **One dependency per invocation.** Removing multiple deps is a Squad B job.
- Human must **confirm** the removal before step 4 (manifest change).
- If the dep has >10 import sites, consider Eagle Airstrike for the replacements first.

---

*"Railgun — no wasted dependencies in a democratic codebase."*
