# Releasing — Promptdivers pack

This repository is a documentation and template pack. Releases are still important: they are how consumers know what doctrine and skills they are installing.

## Rules of thumb

- `VERSION` is the canonical version string.
- `CHANGELOG.md` follows Keep a Changelog: ship changes by **moving** them from `[Unreleased]` into a dated version section.
- Anything referenced in README/docs should exist in the repo (no “phantom” assets).

## Checklist (maintainers)

1. **Sanity / drift**
   - `VERSION` matches the README badge.
   - `CHANGELOG.md` has a new dated section for this release.
   - `CHANGELOG.md` `[Unreleased]` contains only placeholders (or truly upcoming items).

2. **Artifact existence (catch the common breakages)**
   - `Banner.png` exists (if referenced).
   - `.cursor/rules/promptdivers-2.mdc` exists (if referenced).
   - `PROJECT_LOG.md` and `GALACTIC_WAR_MAP.md` exist for dogfood (if this repo claims to dogfood).

3. **Health check**
   - Run `./scripts/health-check.sh .` and review any 🔴/🟡 items.

4. **Tagging**
   - Create a git tag `vX.Y.Z` matching `VERSION`.
   - Push tag to origin.

## Notes for contributors

See `CONTRIBUTING.md` for scope and conventions.

