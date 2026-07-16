# Eagle 500kg — Eagle

## Code: `E5K`

> "Confirmed dead? Then it dies properly."

---

## When to call

- A file, module, or feature is **confirmed dead** — unused, unreferenced, deprecated.
- You have **evidence** it's safe to remove (no imports, no tests reference it, no config points to it).
- Cleaning up after a migration or refactor.

---

## Inputs

1. **Target** — exact file(s) or directory to delete.
2. **Evidence** — how you know it's dead (grep shows no references, deprecation notice, human confirmed).

---

## Steps

1. **Search for all references** to the target:
   ```
   grep -rn "target-name" src/ --include="*.{ts,js,py,go}"
   grep -rn "target-file" .  # check configs, docs, etc.
   ```
2. **Check version control** — when was it last meaningfully changed?
3. **Verify no dynamic references** — string interpolation, dynamic imports, reflection.
4. **Present evidence to human:**
   ```
   📍 MARK — Confirmed dead: [path]
   - Last modified: [date]
   - References found: 0
   - Dynamic import risk: [none / low / check X]
   Requesting permission to delete.
   ```
5. **Wait for `🚀 GO`** from human.
6. **Delete** the file(s).
7. **Clean up orphaned imports** in any file that used to reference the target.
8. **Run tests** — if anything breaks, the target wasn't dead. Revert immediately.
9. **Log:** `Stratagem: E5K — deleted [path]. Evidence: [summary]`.

---

## Outputs

- Dead code/files removed.
- No orphaned references remaining.
- Tests still pass.

---

## Cooldown / limits

- **Always get human confirmation** before deleting. No exceptions.
- If the deletion cascade affects >5 files of cleanup, upgrade to Eagle Airstrike.
- `git` makes this reversible, but still — **evidence first, delete second**.

---

*"Eagle 500kg — clean kills only."*
