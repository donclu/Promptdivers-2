# Autocannon — Offensive

## Code: `ACN`

> "Spray and clean. Every file touched gets formatted."

---

## When to call

- After a batch of edits, code style has drifted.
- Before a PR or commit, you want a **clean lint + format pass**.
- The project has a linter/formatter configured but files have violations.

---

## Inputs

1. **Scope** — which files or directories to clean (default: files touched in this session).
2. **Tools** — which linter/formatter the project uses (ESLint, Prettier, Black, Ruff, rustfmt, etc.).

---

## Steps

1. **Identify the project's lint/format tools** from config files (`package.json` scripts, `.eslintrc`, `pyproject.toml`, etc.).
2. **Run formatter** on the scoped files:
   ```
   npx prettier --write src/touched-files/**
   # or
   black src/touched_files/
   # or
   cargo fmt
   ```
3. **Run linter** and fix auto-fixable issues:
   ```
   npx eslint --fix src/touched-files/
   # or
   ruff check --fix src/
   ```
4. **Review remaining lint errors** — report any that can't be auto-fixed.
5. **Run tests** to ensure formatting didn't break anything.
6. **Log:** `Stratagem: ACN on [scope] — [N] files cleaned`.

---

## Outputs

- All scoped files formatted and lint-clean (or report of remaining manual fixes).
- Clean diff ready for commit.

---

## Cooldown / limits

- Can be called **anytime** — no cooldown.
- Does **not** change logic — only style. If a lint rule requires logic changes, flag it for the human.
- Pairs well with every other stratagem — call Autocannon as a cleanup pass after any offensive/defensive action.

---

*"Autocannon — managed democracy means managed code style."*
