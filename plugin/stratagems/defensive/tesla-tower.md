# Tesla Tower — Defensive

## Code: `TSL`

> "Anything that gets too close to the commit gets zapped."

---

## When to call

- Bad code keeps getting committed — style issues, lint errors, broken tests.
- The team needs a **local** quality gate before code even reaches CI.
- You want to enforce standards **at commit time**, not after push.

---

## Inputs

1. **Hook tool** — Husky, lefthook, pre-commit (Python), or raw git hooks.
2. **Checks to run** — lint, format, typecheck, test subset.
3. **Stack** — to pick the right tool.

---

## Steps

1. **Check for existing hooks** — `.husky/`, `.pre-commit-config.yaml`, `.git/hooks/`.
2. **Install hook runner** if missing:
   ```bash
   # Node projects
   npx husky init
   # Python projects
   pip install pre-commit && pre-commit install
   ```
3. **Configure pre-commit hook** to run:
   - Formatter on staged files (lint-staged + prettier, or black)
   - Linter on staged files
   - Optional: fast test subset
4. **Configure commit-msg hook** (optional) for conventional commits:
   ```bash
   npx commitlint --edit $1
   ```
5. **Test** by making a deliberately bad commit — verify it gets rejected.
6. **Log:** `Stratagem: TSL — pre-commit hooks installed: [list of checks]`.

---

## Outputs

- Pre-commit hooks configured and active.
- Bad commits rejected automatically.
- Documentation in README or CONTRIBUTING about the hooks.

---

## Cooldown / limits

- One-time setup plus occasional maintenance.
- **Do not** make hooks so slow they frustrate developers — keep under 10 seconds.
- If a hook catches something complex, log as DEBT — don't block the commit with a 5-minute test suite.

---

*"Tesla Tower — democracy starts at the commit."*
