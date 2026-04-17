# Changelog

All notable changes to **Promptdivers** (this documentation pack) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `protocols/pack-self-audit.md` — dogfooding checklist for pack consistency (sources-of-truth, links, flags, onboarding).
- `protocols/accuracy-policy.md` — metaphor vs canon accuracy policy (DEBT-001).
- `templates/mission-brief.template.md` — copy/paste mission brief template (flags + objectives + evidence).

## [3.4.0] — 2026-04-17

### Added — Echelon Framework (agent lifecycle + budget reasoning)

**Core framework files:**
- `AGENT_PROFILE.md` — 8-point service record index (Knowledge / Skills / Experience / Aspirations / Doctrine / Feedback Ledger / Operating Limits / Network).
- `ORIENTATION.md` — pre-drop briefing for new operatives (root-level, consumer-facing).
- `stratagems/support/echelon-ladder.md` (`ELD`) — 4-rung reasoning ladder (@low→@max) with JSON-contract gates and cost economics.
- `docs/reasoning-tiers.md` — `@low/@medium/@high/@max` alias map across Claude, OpenAI, Gemini, Grok, Qwen.
- `docs/calibration-protocol.md` — 6-phase project priming procedure (domain scan → knowledge seed → expiry policy).
- `docs/bridge-crew.md` — 6 support roles (THE NAVIGATOR, THE QUARTERMASTER, THE CHRONICLER, THE FUTURIST, THE DEMOCRACY OFFICER, THE INSTRUCTOR) with triggers and activation phrases.
- `docs/agent-job-families.md` — 6 operative archetypes (JF-1 to JF-6) with default tiers, pre-load skills, induction domains, and tenure paths.
- `docs/skill-registry.md` — canonical skill × job-family × tenure matrix (THE QUARTERMASTER's manifest).
- `protocols/orientation.md` — first-hour protocol with 4 tiers (Emergency / Standard / Full / Onboarding) and keyword triggers.
- `protocols/induction.md` — Boot Camp graduation protocol: 4 training phases (Vocabulary / Facts / Rules / Shadowing), gates, failure handling, graduation ceremony.
- `protocols/promotion.md` — clearance ladder (Rookie / Veteran / Elite / Legend), promotion criteria, demotion triggers, `AUTHORIZE SENIOR` escape hatch.

**Knowledge & experience store:**
- `knowledge/README.md` — schema for structured fact store (static / dynamic / derived, source, confidence, expiry).
- `knowledge/terminids-front-ops.yaml` — example knowledge domain (Terminids front, pack-canonical metahpor).
- `experience/README.md` — 4-domain experience structure (operational / learned / integrity / quality).
- `experience/operational/`, `experience/learned/`, `experience/integrity/`, `experience/quality/` — scaffolded with example entries.

**Induction system:**
- `induction/README.md` — how to use the curriculum system.
- `induction/_template/` — reusable domain template: `curriculum.md`, `glossary.yaml`, `quiz.yaml`, 3 exercises.

**Tutorials:**
- `missions/tutorial-09-new-agent-onboarding.md` — ONBOARD archetype end-to-end: Tier 3 orientation → calibration → Boot Camp graduation → session close.
- `missions/tutorial-10-echelon-experiment.md` (`EXP-001`) — empirical demonstration: @low+framework vs @medium+no-framework on 3 tasks.

### Changed

- `QUICK_REFERENCE.md` — added `ELD` and `ORT` to stratagem table; added `ONBOARD` mission archetype; added `@low/@medium/@high/@max` tier aliases to fleet section; added THE INSTRUCTOR + Bridge Crew callout to roles; added 8 lifecycle keywords (`orient`, `onboard`, `induct`, `calibrate`, `promote`, `boot camp`, `shadow`, `AUTHORIZE SENIOR`).
- `AGENTS.md` — fleet template updated to `@tier` notation (e.g. `claude-sonnet@medium`); added `Model deep` and `Model ceiling` lines; added cross-reference to `docs/reasoning-tiers.md`.

### Changed

- `QUICK_REFERENCE.md` — links to the pack self-audit checklist.
- `missions/README.md` and `FIRST_MISSION.md` — onboarding now points to the mission brief template.
- `stratagems/support/reinforce.md` — converted to an action card pointing to canonical `protocols/reinforce.md`.
- `protocols/friendly-fire.md` — points to canonical `protocols/reinforce.md`.
- `protocols/tactical-signals.md` — tightened wording to keep Helldivers references explicitly metaphor-only.

## [3.3.1] — 2026-04-14

### Added

- **`install.ps1`** — PowerShell installer for Windows (and `pwsh` elsewhere); mirrors `install.sh` (`-Project`, `-Cursor`, `-Claude`, `-Help` / `--project`, etc.). Documented in `README.md`, `README-ES.md`, and `docs/MULTI_AGENT_SETUP.md`.
- **Dogfood files:** `PROJECT_LOG.md` and `GALACTIC_WAR_MAP.md` now ship in the pack root for self-audit continuity.
- **Cursor rule:** `.cursor/rules/promptdivers-2.mdc` restored to the repository.

### Changed

- **Lore safety:** rephrased “in Helldivers…” lines to explicitly mark them as framework metaphor; any “rules” are now expressed as Promptdivers doctrine.
- **`scripts/health-check.sh`** — fixed `set -euo pipefail` early-exit when `mission_status` was absent; updated banner to “Promptdivers”.
- **`README.md`** — repo tree now reflects current tutorial count (8 + index).

## [3.3.0] — 2026-04-10

### Changed

- **Product name:** **Promptdivers** everywhere (dropped the “2” suffix in prose, footers, LICENSE, and installer strings). File path `.cursor/rules/promptdivers-2.mdc` is unchanged as a stable IDE hook.
- **README.md**, **README-ES.md**, and **FIRST_MISSION.md** — hero image [`Banner.png`](Banner.png) in the summary; repo tree lists `Banner.png`.

## [3.2.0] — 2026-04-10

### Added

- **`missions/tutorial-08-propaganda-web.md`** — LAUNCH-WEB tutorial: campaign / landing / “propaganda” microsite from strategy → copy → ui-design-expert Phase 0 → build → verify → deploy; includes explicit note on why structured paste-briefs improve model reasoning.
- **`missions/README.md`** — index of all tutorial missions + quick-pick table.
- **LAUNCH-WEB** mission archetype in `docs/super-earth-operating-model.md`, `QUICK_REFERENCE.md`, `docs/agent-ecosystem-integration.md`, `docs/SKILLS_AND_EXTENSIONS.md`, and `skills/promptdivers-orchestrator/SKILL.md`.

### Changed

- `README.md` repo tree — tutorial 08 + `missions/README.md`.
- `AGENTS.md` critical map — `missions/README.md` entry.
- `README-ES.md` — key docs table links to `missions/README.md`.

## [3.1.1] — 2026-04-10

### Added

- `SECURITY.md` — vulnerability reporting policy for public repositories.
- `.editorconfig` — shared UTF-8 / LF / trailing-whitespace defaults for Markdown and shell.

### Changed

- `install.sh` — `set -euo pipefail`, validated `--project` argument, `local` variables in `install_skills`, here-doc `--help`, unknown flags warn instead of silent skip; `cp -R` for portability.
- `.gitignore` — `.idea/`, `.vscode/*` (with optional `!.vscode/extensions.json`), backups, `scratch/`, `local/`.
- `CONTRIBUTING.md` — public repository checklist before pushing.
- `README.md` / `README-ES.md` — link to `SECURITY.md`.
- `AGENTS.md` — critical map lists `SECURITY.md`.
- `README.md` repo tree — `LICENSE` / `CONTRIBUTING` / `SECURITY`, `.editorconfig`, `protocols/pre-drop.md`.
- `skills/promptdivers-pelican/SKILL.md` — evidence example wording (professional backlog phrasing).

## [3.1.0] — 2026-04-10

### Added

- `protocols/pre-drop.md` — new pre-drop planet check protocol: read `GALACTIC_WAR_MAP.md` → identify active fronts + hottest sector → derive squad + nave recommendation before any mission.
- `templates/next-mission.template.md`: `## Planet status (pre-drop check)` section at top; `## Mission queue` with Primary / Secondary / Tertiary sub-blocks.
- `templates/project-log.template.md` `HANDOFF_JSON` v2: `planet_status` object + `missions_queued[]` array (priority, squad, nave, objective, spawned_by) + schema bump to `promptdivers-handoff/v2`.
- `QUICK_REFERENCE.md`: Step 0 planet check in mission tree; Mission queue section (primary/secondary/tertiary pattern); INTEL_REPORT vs Intel Dossier distinction; cross-link to `stratagems/README.md`.
- `stratagems/README.md`: cross-link back to `QUICK_REFERENCE.md`.

### Changed

- `skills/promptdivers-orchestrator/SKILL.md`: Step 0 pre-drop in "On activation"; planet check in inline mission tree.
- `docs/agent-ecosystem-integration.md`: fixed broken link `README.md` → `../README.md`; unified `model_preferred` → `Model (nave)`.
- `docs/super-earth-operating-model.md`: fixed broken link `README.md` → `../README.md`; unified `model_preferred` → `Model (nave)`.
- `docs/model-fleet.md`: replaced YAML `model_preferred` block with `Model (nave)` markdown label (YAML key noted as comment).
- `install.sh`: `--help` now accurately describes `--project` behavior (copies QUICK_REFERENCE.md + creates PROJECT_LOG.md from template).
- `QUICK_REFERENCE.md`: ESS wording → "feature/safety branch"; `GALACTIC_WAR_MAP.md` added to "Files every serious project should have".
- `stratagems/README.md`: ESS wording → "feature/safety branch".
- `AGENTS.md`: clarified `GALACTIC_WAR_MAP` as template in `templates/`.
- `README.md`: URL placeholder `your-org` → `<your-org>`; loop description updated to mention pre-drop check and mission queue.
- `README-ES.md`: loop description updated (pre-drop + mission queue).
- `protocols/mission-debrief.md`: step 5 output shape now includes sub-missions (`missions_queued`) guidance before handoff.
- `templates/next-mission.template.md`: precondition updated to `Model (nave)`.

## [3.0.1] — 2026-04-10

### Added

- `README-ES.md` — Spanish overview of the framework, three layers, skills adequacy, and links to canonical English docs.

### Changed

- `README.md` — Positioning: **framework + IDE skills** vs a single “agent product”; subtitle and onboarding text distinguish assistant (runtime) from pack (doctrine); human-keywords table and first-mission steps updated; link to README-ES.
- `install.sh` — Post-install message refers to skills + pack loading instead of “the agent loads doctrine.”
- `FIRST_MISSION.md` — Opening frames Promptdivers as framework + skills with assistant as executor.

## [3.0.0] — 2026-04-10

### Added

- **Stratagem Codex** — `stratagems/` directory with **24** concrete invokable actions organized by category:
  - **Offensive** (6): Orbital Precision Strike, Eagle Airstrike, Railgun, Autocannon, Data Strike, Automaton Assault
  - **Defensive** (4): Shield Generator, Guard Dog, Tesla Tower, Fortify
  - **Support** (6): Reinforce, Resupply, SOS Beacon, Hellpod, Intel Dossier, Prompt Forge
  - **Eagle** (5): Eagle 500kg, Eagle Smoke Strike, Eagle Rearm, Eagle Report, Eagle Visuals
  - **Orbital** (3): Orbital Barrage, Orbital Laser, Orbital EMS
- **7 tutorial missions** in `missions/` — guided step-by-step walkthroughs:
  - `tutorial-01-recon.md` — Squad A: map an unknown repo
  - `tutorial-02-bugfix.md` — Squad C: surgical bug fix with stratagem chaining
  - `tutorial-03-refactor.md` — Squad B: major refactor with FORGE/EXECUTOR split
  - `tutorial-04-audit.md` — Squad D: pre-release audit with Democracy Officer
  - `tutorial-05-total-democracy.md` — Crisis response: production incident protocol
  - `tutorial-06-data-analysis.md` — DATA archetype: data pipeline and analysis
  - `tutorial-07-research-prompt.md` — CONSULT+WRITE: research → prompt design workflow
- **`scripts/health-check.sh`** — Democracy health check script for any project
- **Intel Dossier template** — `templates/intel-dossier.template.md`: formal research deliverable format
- **4 new protocols:**
  - `protocols/friendly-fire.md` — agent conflict resolution (when agents overwrite each other's work)
  - `protocols/mind-control.md` — Illuminate inside threat: hallucination detection and verification tiers
  - `protocols/reinforce.md` — parallel agent coordination (spawning and syncing multiple agents)
  - `protocols/democracy-officer.md` — meta-audit: checking if the framework itself is being followed
- **Galactic War Map template** — `templates/galactic-war-map.template.md`: campaign dashboard showing territory status per module, liberation progress, threat index, and progression levels
- Stratagem loadout section in `QUICK_REFERENCE.md`
- Stratagem routing table in `skills/promptdivers-orchestrator/SKILL.md`
- Stratagem routing rule (step 7) in `.cursor/rules/promptdivers-2.mdc`

### Changed

- `AGENTS.md` critical project map updated with `stratagems/`, new protocols, `GALACTIC_WAR_MAP`
- `README.md` repo tree updated with all new directories and files
- `.cursor/rules/promptdivers-2.mdc` set to `alwaysApply: true` for pack dogfood

### Fixed

- `CONTRIBUTING.md` — removed dead reference to deleted `docs/README.md`
- `docs/SKILLS_AND_EXTENSIONS.md` — removed stale `.cursor/skills/` dogfood reference; removed tactical-signals from "gaps" (it's already bundled)
- `install.sh` — fixed bash negation bug (`!$VAR` → `[[ $VAR == false ]]`); added Windsurf IDE auto-detection

## [2.3.0] — 2026-04-10

### Added

- `docs/model-fleet.md` — ship manifest: AI model classes (A heavy / B frigate / C local), mission routing table, `model_preferred` declaration format, Illuminate risk rules for model selection
- Model/nave field in `templates/next-mission.template.md` and `HANDOFF_JSON` (`model_used`, `model_rationale`, `next_recommended.nave`)
- Fleet quick chart in `QUICK_REFERENCE.md` + golden rules 8–9 (log switches, no sensitive data to cloud without permission)
- Nave column in `docs/super-earth-operating-model.md` mission archetypes table
- Model stack block guidance in `AGENTS.md` + `docs/model-fleet.md` in critical project map
- Skills upgraded to multi-domain: `promptdivers-orchestrator` (capability library: web/UI, data, images, APIs, verification + fleet routing), `promptdivers-tactical-signals` (cross-domain ping examples), `promptdivers-pelican` (cross-domain evidence examples + model rationale in debrief)
- Removed standalone `.cursor/skills/{ux-ui,html-css,tailwind,web-tooling}/` (content embedded in orchestrator)

## [2.2.0] — 2026-04-10

### Added

- **`.cursor/skills/`** for Cursor: `promptdivers-orchestrator`, `promptdivers-tactical-signals`, `promptdivers-pelican`, plus **`ux-ui`**, **`html-css`**, **`tailwind`**, **`web-tooling`** (implementation + verification guidance)
- `skills/promptdivers-orchestrator/SKILL.md` — routes web UI work through optional project skills when present
- Docs: `README.md` tree, `docs/MULTI_AGENT_SETUP.md`, `docs/SKILLS_AND_EXTENSIONS.md`, `docs/agent-ecosystem-integration.md`

## [2.1.0] — 2026-04-10

### Added

- `protocols/mission-debrief.md` — Pelican window: verifiable objectives, PASS/PARTIAL/FAIL, `mission_status`, stratagem map to existing squads/skills
- `skills/promptdivers-pelican/SKILL.md` — optional Cursor skill for debrief / extract triggers
- `templates/project-log.template.md` — optional session debrief section; `HANDOFF_JSON` fields `objectives`, `mission_status`, `debrief_summary`
- Human keywords `debrief` and `extract`; cross-links in `QUICK_REFERENCE.md`, `AGENTS.md`, `README.md`, `docs/agent-ecosystem-integration.md`, `docs/SKILLS_AND_EXTENSIONS.md`, `docs/README.md`, orchestrator skill, `CLAUDE.md`, Copilot sample

## [2.0.0] — 2026-04-10

### Added

- English-first pack: `squads/`, `protocols/`, `docs/`, `templates/`, `skills/`
- `docs/super-earth-operating-model.md`, `docs/agent-ecosystem-integration.md`, tactical signals, factions
- `docs/roles-and-field-operatives.md` codename roster
- `CLAUDE.md` stub pointing at `AGENTS.md`; multi-IDE setup doc
- MIT `LICENSE`, `.gitignore`, `CONTRIBUTING.md`, trademark disclaimer in README
- **Dogfood:** this repo uses specialized `AGENTS.md`, `PROJECT_LOG.md`, `VERSION`, and this changelog

### Removed

- Legacy Spanish v1 drafts from the published tree (recover from git history if needed)

---

## Releasing (maintainer)

1. Update `CHANGELOG.md` (move items from `[Unreleased]` to a dated section).  
2. Set `VERSION` to the same semver.  
3. Append a session to `PROJECT_LOG.md` and refresh `HANDOFF_JSON`.  
4. Commit, then tag:  
   `git tag -a vX.Y.Z -m "Promptdivers vX.Y.Z"`  
5. Push commits and tags:  
   `git push && git push --tags`

After the GitHub repo URL is final, add compare/release links at the bottom of this file per Keep a Changelog.
