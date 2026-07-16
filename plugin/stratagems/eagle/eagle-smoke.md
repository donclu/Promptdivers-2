# Eagle Smoke Strike — Eagle

## Code: `ESS`

> "Pop smoke. Create cover before the assault."

---

## When to call

- You're about to make **risky changes** and want a safety net.
- Before any offensive or orbital stratagem that could break things.
- The human wants to be able to **revert cleanly** if the plan goes wrong.

---

## Inputs

1. **Branch name** — descriptive, following project conventions (e.g., `fix/auth-rewrite`, `feat/new-api`).
2. **Base branch** — where to branch from (usually `main` or `develop`).

---

## Steps

1. **Check current git status:**
   ```bash
   git status
   git stash list
   ```
2. **If there are uncommitted changes**, ask human: stash, commit, or proceed dirty?
3. **Create the branch:**
   ```bash
   git checkout -b <branch-name>
   ```
4. **Confirm:**
   ```
   ✅ CLEAR — Smoke deployed. Working on branch: <branch-name>
   Safe to operate. Main branch untouched.
   ```
5. **Log:** `Stratagem: ESS — branch [name] created from [base]`.

---

## Outputs

- New feature/fix branch created.
- Main branch protected from risky changes.
- Clean revert path: `git checkout main && git branch -D <branch>`.

---

## Cooldown / limits

- Promptdivers safety rule: call **before** any orbital stratagem. Orbital without smoke is reckless.
- One branch per mission focus. Don't create 5 branches in one session.
- Human must approve branch name.

---

*"Eagle Smoke Strike — cover first, charge second."*
