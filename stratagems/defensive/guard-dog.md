# Guard Dog — Defensive

## Code: `GDG`

> "It follows you around and barks at regressions. Good boy."

---

## When to call

- The project has **no CI/CD** or the existing pipeline doesn't catch regressions.
- You just added tests (Shield Generator) and want them to run **automatically** on every push/PR.
- A recurring bug keeps coming back — automated guard needed.

---

## Inputs

1. **CI platform** — GitHub Actions, GitLab CI, CircleCI, etc. (default: GitHub Actions).
2. **Test command** — what runs the tests (`npm test`, `pytest`, `cargo test`, etc.).
3. **Trigger** — push to main, PR, or both.

---

## Steps

1. **Check for existing CI config** — `.github/workflows/`, `.gitlab-ci.yml`, etc.
2. **If none exists**, create a basic CI workflow:
   ```yaml
   # .github/workflows/guard-dog.yml
   name: Guard Dog — Regression Check
   on: [push, pull_request]
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - uses: actions/setup-node@v4  # adapt to stack
           with:
             node-version: '20'
         - run: npm ci
         - run: npm test
   ```
3. **If CI exists**, add or verify the test step is present and runs on the right triggers.
4. **Add lint step** if the project has a linter configured.
5. **Test the workflow** locally if possible (`act` for GitHub Actions).
6. **Log:** `Stratagem: GDG — CI guard [created/updated] at [path]`.

---

## Outputs

- CI workflow file created or updated.
- Tests run on every push/PR automatically.
- `✅ CLEAR` when verified.

---

## Cooldown / limits

- One-time setup per project (or per significant change to test infrastructure).
- Human must **approve** the workflow file before first commit.
- If the project needs a complex multi-stage pipeline, escalate to Squad B.

---

*"Guard Dog — it never sleeps, it never forgets, it serves democracy."*
