# GitHub Copilot instructions (optional)

> Copy to `.github/copilot-instructions.md` in your project if you use Copilot.
> Promptdivers does not require this file — it is optional IDE integration.

## Project context

- Read `AGENTS.md` before suggesting changes.
- If `PROJECT_LOG.md` exists, respect the latest handoff and open tasks.
- Use `QUICK_REFERENCE.md` (or `.framework-promptdivers2/QUICK_REFERENCE.md`) for squad routing.

## Rules

- Do not invent APIs, paths, or game canon.
- Prefer minimal diffs; cite evidence for claims.
- On session end, suggest updating `PROJECT_LOG.md` if significant work was done.

## Promptdivers pack

If vendored: doctrine lives under `.framework-promptdivers2/`.
Run `./.framework-promptdivers2/install.sh --project .` to refresh from pack (when present).
