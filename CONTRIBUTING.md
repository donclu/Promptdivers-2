# Contributing to Promptdivers

## Scope

Changes should stay aligned with the pack’s goal: portable **framework** (doctrine: squads, protocols, docs, templates) plus optional **IDE skills**. Avoid unrelated refactors.

## Project brief files

- **Edit [`AGENTS.md`](AGENTS.md)** for the full operational brief (stack, permissions, workflow, keywords).
- **[`CLAUDE.md`](CLAUDE.md)** is intentionally a **stub** in this repo: it points Claude Code at `AGENTS.md`. Do not paste the full brief back into `CLAUDE.md` unless the project deliberately switches to the “single self-contained file” pattern (see [`docs/MULTI_AGENT_SETUP.md`](docs/MULTI_AGENT_SETUP.md)).

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/) where possible: `feat:`, `fix:`, `docs:`, `chore:`, etc.

## Documentation

New narrative docs go under [`docs/`](docs/). Update cross-references in `QUICK_REFERENCE.md` and `docs/agent-ecosystem-integration.md` when adding new files.

**Bilingual entry:** when you change onboarding or positioning in [`README.md`](README.md), update [`README-ES.md`](README-ES.md) in the same PR when practical.

## Versioning and operational log (maintainers)

This pack **dogfoods** Promptdivers on itself:

- After **significant** changes, update [`CHANGELOG.md`](CHANGELOG.md) and bump [`VERSION`](VERSION) when cutting a release.  
- Append a session to [`PROJECT_LOG.md`](PROJECT_LOG.md) and refresh the **HANDOFF_JSON** block so the next session (human or assistant) can resume.  
- To publish a release: follow the **Releasing** steps at the bottom of [`CHANGELOG.md`](CHANGELOG.md) (`git tag`, push tags).
- Release checklist: see [`RELEASING.md`](RELEASING.md).

## Public repository checklist (before pushing or going public)

- [ ] No secrets, tokens, or internal URLs in Markdown, scripts, or examples.  
- [ ] [`.gitignore`](.gitignore) covers local env files (`.env*`) and editor cruft; no personal `settings.json` committed unless intentional.  
- [ ] [`LICENSE`](LICENSE) copyright year and holder are correct for your org.  
- [ ] [`SECURITY.md`](SECURITY.md) points to your preferred private reporting path (GitHub Advisories or maintainer contact).  
- [ ] [`VERSION`](VERSION) / [`CHANGELOG.md`](CHANGELOG.md) match the release you intend to tag.  
- [ ] Run [`scripts/health-check.sh`](scripts/health-check.sh) on this repo root as a quick sanity pass.

---

*Promptdivers — FOR DEMOCRACY.*
