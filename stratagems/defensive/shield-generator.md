# Shield Generator — Defensive

## Code: `SHG`

> "Territory without tests is territory you'll lose tomorrow."

---

## When to call

- Code was just written or modified but has **no test coverage**.
- A module is critical but **untested** — identified by Scout or Sentinel.
- After a Squad C fix, to prevent the same bug from returning.

---

## Inputs

1. **Target** — file or module to cover.
2. **Test framework** — what the project uses (Jest, Vitest, pytest, Go test, etc.).
3. **Priority behaviors** — which functions/paths are most critical to test first.

---

## Steps

1. **Read the target** end to end. Identify exports, public API, edge cases.
2. **Check existing tests** — are there any? What's already covered?
3. **Write tests for the happy path** first — the main expected behavior.
4. **Write edge case tests** — null inputs, empty arrays, auth failures, boundary values.
5. **Write error path tests** — what happens when things go wrong?
6. **Run the test suite.** All new tests must pass.
7. **Check coverage** if the project has a coverage tool:
   ```
   npx jest --coverage --collectCoverageFrom="src/target/**"
   ```
8. **Log:** `Stratagem: SHG on [path] — [N] tests added, coverage [X]% → [Y]%`.

---

## Outputs

- Test file(s) created following project conventions.
- All new tests passing.
- Coverage delta reported.

---

## Cooldown / limits

- No cooldown — call as often as needed.
- Should be called **after every offensive stratagem** as a follow-up.
- If the module is too complex for quick test coverage, log as DEBT and recommend Squad B.

---

*"Shield Generator — what you test, you keep."*
