# PROJECT_LOG — Promptdivers

Running log for this repository. New sessions append **below** the active-constraints block (chronological order).

---

## Active constraints

- Current release target: **3.3.0** (see `VERSION` and `CHANGELOG.md`)
- Branch / environment: default / pre-release
- Anything fragile: keep `AGENTS.md` and `CHANGELOG.md` aligned on semver; tag in git when releasing

---

## Session: 2026-04-10 — Branding: Promptdivers + Banner.png in READMEs

### Summary

- Renamed product references from **Promptdivers 2** → **Promptdivers** across the pack (53 files); left **Helldivers 2** and path `.cursor/rules/promptdivers-2.mdc` unchanged.
- Added [`Banner.png`](Banner.png) to **README.md**, **README-ES.md**, and **FIRST_MISSION.md**; documented in README repo tree. **v3.3.0**.

### Files / areas

- Bulk prose: `LICENSE`, `CHANGELOG.md`, `AGENTS.md`, `QUICK_REFERENCE.md`, docs, protocols, squads, missions, skills, templates, scripts, `.cursor/rules/promptdivers-2.mdc`, etc.
- `README.md`, `README-ES.md`, `FIRST_MISSION.md`, `VERSION`, `CHANGELOG.md`, `PROJECT_LOG.md`

---

## Session: 2026-04-10 — Tutorial 08 LAUNCH-WEB + missions index

### Summary

- Added **`missions/tutorial-08-propaganda-web.md`** (campaign landing / propaganda-style web → deploy) with phased paste-briefs and a short “why structure helps reasoning” table.
- Added **`missions/README.md`** tutorial index. New archetype **LAUNCH-WEB** wired into super-earth model, QUICK_REFERENCE, agent-ecosystem-integration, SKILLS_AND_EXTENSIONS, orchestrator skill, README/AGENTS/README-ES. **v3.2.0**.

### Files / areas

- `missions/tutorial-08-propaganda-web.md`, `missions/README.md`, `docs/super-earth-operating-model.md`, `QUICK_REFERENCE.md`, `docs/agent-ecosystem-integration.md`, `docs/SKILLS_AND_EXTENSIONS.md`, `skills/promptdivers-orchestrator/SKILL.md`, `README.md`, `README-ES.md`, `AGENTS.md`, `VERSION`, `CHANGELOG.md`, `PROJECT_LOG.md`

---

## Session: 2026-04-10 — Public GitHub hygiene + professional shell/docs polish

### Summary

- Added **`SECURITY.md`**, **`.editorconfig`**, expanded **`.gitignore`** (IDE cruft, scratch/local dirs, backups).
- Hardened **`install.sh`**: `set -euo pipefail`, `--project` validation, `install_skills` locals, here-doc help, safer unknown-arg handling.
- **`CONTRIBUTING.md`**: public repository checklist. **README** / **README-ES** / **AGENTS.md** link or index security + tree updates.
- **Pelican** skill: cleaner PARTIAL evidence example. **v3.1.1**.

### Files / areas

- `SECURITY.md`, `.editorconfig`, `.gitignore`, `install.sh`, `CONTRIBUTING.md`, `README.md`, `README-ES.md`, `AGENTS.md`, `skills/promptdivers-pelican/SKILL.md`, `VERSION`, `CHANGELOG.md`, `PROJECT_LOG.md`

---

## Session: 2026-04-10 — Pre-drop planet check + mission hierarchy + audit fixes

### Summary

- Added **`protocols/pre-drop.md`** — full pre-drop protocol: read `GALACTIC_WAR_MAP.md` → active fronts + hottest sector → derive squad + nave recommendation.
- Updated **`templates/next-mission.template.md`** with "Planet status" pre-drop section and "Mission queue" (Primary / Secondary / Tertiary).
- Extended **`HANDOFF_JSON`** to schema v2: `planet_status` object + `missions_queued[]` (priority, squad, nave, objective, spawned_by). `next_recommended` preserved for compat.
- **`protocols/mission-debrief.md`** step 5: now includes `missions_queued` guidance before handoff.
- **`QUICK_REFERENCE.md`**: Step 0 planet check in mission tree; Mission queue section; INTEL_REPORT vs Intel Dossier note; stratagems cross-link; ESS wording fix.
- **`skills/promptdivers-orchestrator/SKILL.md`**: Step 0 pre-drop in "On activation" + inline mission tree.
- **Bug fixes**: broken `README.md` links in `docs/agent-ecosystem-integration.md` + `docs/super-earth-operating-model.md` → `../README.md`. `install.sh --help` now reflects real `--project` behavior. ESS wording unified to "feature/safety branch" in both QUICK_REFERENCE and stratagems/README.
- **Terminology**: `model_preferred` unified to `Model (nave)` across `docs/model-fleet.md`, `docs/super-earth-operating-model.md`, `docs/agent-ecosystem-integration.md`, `templates/next-mission.template.md`.
- **Doc cleanup**: AGENTS.md clarifies GALACTIC_WAR_MAP as template; README.md URL placeholder fixed; stratagems ↔ QUICK_REFERENCE cross-links added.
- **README.md + README-ES.md**: loop description updated to mention pre-drop check and mission queue. **v3.1.0**.

### Decisions

- Pre-drop protocol reads GALACTIC_WAR_MAP.md first (fallback: PROJECT_LOG.md → AGENTS.md debt → verbal SITREP). If nothing exists: assume UNEXPLORED → Squad A.
- HANDOFF_JSON schema bumped to v2; v1 consumers can ignore new fields safely.
- `missions_queued` is the canonical mission queue; `next_recommended` kept for backward compat = first queued item.

### Files / areas

- `protocols/pre-drop.md` (new)
- `templates/next-mission.template.md`, `templates/project-log.template.md`
- `protocols/mission-debrief.md`
- `QUICK_REFERENCE.md`, `stratagems/README.md`
- `skills/promptdivers-orchestrator/SKILL.md`
- `docs/agent-ecosystem-integration.md`, `docs/super-earth-operating-model.md`, `docs/model-fleet.md`
- `install.sh`, `AGENTS.md`, `README.md`, `README-ES.md`
- `VERSION`, `CHANGELOG.md`, `PROJECT_LOG.md`

### HANDOFF_JSON

```json
{
  "schema": "promptdivers-handoff/v2",
  "updated": "2026-04-10T00:00:00Z",
  "mission_last": "C",
  "squad_files_used": [],
  "model_used": "claude-sonnet",
  "model_rationale": "deep multi-file doc edits + new protocol authoring",
  "planet_status": {
    "active_fronts": ["Automatons"],
    "hottest_sector": "templates/ + protocols/ (orphaned GALACTIC_WAR_MAP, no pre-drop wiring)",
    "threat_level": "LOW"
  },
  "objective": "Audit fixes + pre-drop planet check protocol + mission hierarchy",
  "objectives": [
    {"id": "1", "label": "Bugs fixed", "done_when": "broken links + install.sh --help + ESS wording corrected", "result": "PASS", "evidence": "docs/agent-ecosystem-integration.md:7, super-earth-operating-model.md:7, install.sh:34, QUICK_REFERENCE ESS line"},
    {"id": "2", "label": "model_preferred unified", "done_when": "no remaining model_preferred in user-facing docs", "result": "PASS", "evidence": "model-fleet.md, super-earth-operating-model.md, agent-ecosystem-integration.md, next-mission.template.md"},
    {"id": "3", "label": "Doc cleanup", "done_when": "GALACTIC_WAR_MAP clarified, INTEL_REPORT vs Dossier note, cross-links, URL placeholder", "result": "PASS", "evidence": "AGENTS.md, QUICK_REFERENCE.md, stratagems/README.md, README.md"},
    {"id": "4", "label": "Pre-drop protocol", "done_when": "protocols/pre-drop.md created + wired into NEXT_MISSION + QUICK_REFERENCE + orchestrator", "result": "PASS", "evidence": "protocols/pre-drop.md (new), templates/next-mission.template.md, QUICK_REFERENCE.md, skills/promptdivers-orchestrator/SKILL.md"},
    {"id": "5", "label": "Mission hierarchy", "done_when": "Primary/Secondary/Tertiary in NEXT_MISSION + missions_queued in HANDOFF_JSON + debrief note + QUICK_REFERENCE queue section", "result": "PASS", "evidence": "templates/next-mission.template.md, templates/project-log.template.md, protocols/mission-debrief.md, QUICK_REFERENCE.md"},
    {"id": "6", "label": "READMEs + version bump", "done_when": "README.md + README-ES.md loop updated, VERSION=3.1.0, CHANGELOG entry", "result": "PASS", "evidence": "README.md, README-ES.md, VERSION, CHANGELOG.md"}
  ],
  "mission_status": "GREEN",
  "debrief_summary": "All 6 objectives PASS. Pack is now at v3.1.0 with pre-drop planet check + mission hierarchy fully wired.",
  "open_tasks": [],
  "debt": [],
  "missions_queued": [
    {"priority": "primary", "squad": "D", "nave": "AUTO", "objective": "Validate install.sh --project with the new next-mission.template.md to confirm pre-drop section copies correctly", "spawned_by": null}
  ],
  "next_recommended": {
    "squad": "D",
    "nave": "gpt-4o-mini",
    "reason": "quick validation pass; Class B is sufficient"
  }
}
```

---

## Session: 2026-04-10 — README: framework + skills; README-ES

### Summary

- Reframed **README.md**: product is the **framework** (doctrine + skills); IDE assistant is the runtime. Clarified three bundled skills are sufficient; optional skills remain in SKILLS_AND_EXTENSIONS only.
- Added **README-ES.md** (Spanish entry point, links to English canonical docs).
- **install.sh** and **FIRST_MISSION.md** wording aligned. **v3.0.1**.

### Files / areas

- `README.md`, `README-ES.md`, `install.sh`, `FIRST_MISSION.md`, `VERSION`, `CHANGELOG.md`

---

## Session: 2026-04-10 — Dogfood: pack uses its own doctrine

### Summary

- **Promptdivers applied to itself:** `AGENTS.md` now describes this documentation pack (not a generic app template).  
- Added operational memory (`PROJECT_LOG.md`), `CHANGELOG.md`, and `VERSION` for semver visibility.  
- Maintainers should update this log and CHANGELOG on significant doc or structure changes.

### Decisions

- Single source of policy: **`AGENTS.md`**; **`CLAUDE.md`** remains a stub pointing here.  
- **No** `package.json` required for the pack; tooling may be added later with explicit maintainer approval.

### Files / areas

- `AGENTS.md` — specialized stack, map, permissions for Markdown pack  
- `PROJECT_LOG.md` — created (this file)  
- `CHANGELOG.md`, `VERSION` — versioning surface  

### DEBT

- (none)

### Follow-ups

- [ ] Maintainer: `git tag -a v2.0.0 -m "Promptdivers initial release"` when ready, then push tags  
- [ ] Optional: link-check pass across `docs/` and `README.md` (Squad D style)

---

## Session: 2026-04-10 — Model fleet (naves) + multi-domain skills

### Summary

- New `docs/model-fleet.md`: ship manifest for AI models (Class A/B/C — Claude, GPT, Gemini, local); mission routing; `model_preferred` declaration; Illuminate risk rules.
- Templates updated: `next-mission` (Nave field), `project-log` HANDOFF_JSON (`model_used`, `model_rationale`, `next_recommended.nave`).
- `AGENTS.md`, `QUICK_REFERENCE.md`, `super-earth-operating-model.md` (nave column), `docs/agent-ecosystem-integration.md`, `docs/README.md`, `README.md` all updated.
- Three bundled skills refactored to multi-domain: orchestrator (capability library + fleet), tactical-signals (cross-domain pings), pelican (cross-domain evidence). Removed four standalone web skills from `.cursor/skills/`.
- **v2.3.0**.

### Files / areas

- `docs/model-fleet.md` (new), templates, AGENTS.md, QUICK_REFERENCE.md, super-earth-operating-model.md, docs/, skills/ + .cursor/skills/, VERSION, CHANGELOG.md

### Follow-ups

- [ ] Maintainer: `git tag -a v2.3.0 -m "Promptdivers v2.3.0"` when ready

---

## Session: 2026-04-10 — Cursor `.cursor/skills/` + web stack skills

### Summary

- Added **`.cursor/skills/`** with Promptdivers skills (orchestrator, tactical, pelican) and frontend helpers: **ux-ui**, **html-css**, **tailwind**, **web-tooling**.  
- Synced **`skills/promptdivers-orchestrator`** routing table; updated README, MULTI_AGENT_SETUP, SKILLS_AND_EXTENSIONS, agent-ecosystem-integration. **v2.2.0**.

### Files / areas

- `.cursor/skills/*/` — seven skill folders  
- `skills/promptdivers-orchestrator/SKILL.md`, docs as above, `VERSION`, `CHANGELOG.md`

### Follow-ups

- [ ] Consumer apps: copy `.cursor/skills/` subsets into their repos as needed

---

## Session: 2026-04-10 — Mission debrief protocol + Pelican skill

### Summary

- Added `protocols/mission-debrief.md` (objectives, PASS/PARTIAL/FAIL, `mission_status`, stratagem map).  
- Extended `templates/project-log.template.md` with optional debrief section and `HANDOFF_JSON` fields: `objectives[]`, `mission_status`, `debrief_summary`.  
- Added bundled skill `skills/promptdivers-pelican/SKILL.md`; cross-links in `QUICK_REFERENCE.md`, `AGENTS.md`, orchestrator, `docs/SKILLS_AND_EXTENSIONS.md`.

### Decisions

- **Pelican** = mission-end debrief + extraction metaphor; canonical rules live in the protocol, not only in the skill.  
- **`objective`** (singular) in handoff JSON remains for backward compatibility; `objectives[]` is optional for scored missions.

### Files / areas

- `protocols/mission-debrief.md`, `templates/project-log.template.md`, `skills/promptdivers-pelican/SKILL.md`  
- `QUICK_REFERENCE.md`, `AGENTS.md`, `skills/promptdivers-orchestrator/SKILL.md`, `docs/SKILLS_AND_EXTENSIONS.md`, `README.md` (tree if listed), `VERSION`, `CHANGELOG.md`

### DEBT

- (none)

### Follow-ups

- [ ] Maintainer: `git tag -a v2.1.0 -m "Promptdivers v2.1.0"` when ready, then push tags

### Mission debrief

| Objective | Result | Evidence |
|-----------|--------|----------|
| Publish mission debrief protocol | PASS | `protocols/mission-debrief.md` |
| Extend project log template + handoff JSON | PASS | `templates/project-log.template.md` |
| Ship Pelican skill + cross-links + semver note | PASS | this session + `skills/promptdivers-pelican/` |

**mission_status:** GREEN

**Next stratagems:** none for this slice.

---

## Session: 2026-04-10 — Repo cleanup + public release prep

### Summary

First real maintenance session on the pack. Goal: prepare Promptdivers for public release as an open repo serving both the AI community and Helldivers players.

**Changes made:**

- **Deleted** `.cursor/skills/` (duplicate of `skills/` — same content, two locations, one was dead weight)
- **Deleted** `docs/README.md` (redundant with root README), `AI-DIVERS.docx` (orphaned draft), `templates/copilot-instructions.sample.md` (removed from setup flow)
- **Rewrote** `README.md` — new "Quick Install" section covering Claude Code, Cursor, Windsurf per IDE; dual audience framing (AI community + Helldivers players); cleaner repo tree
- **Updated** all 3 bundled skills (`promptdivers-orchestrator`, `promptdivers-pelican`, `promptdivers-tactical-signals`) to work in Claude Code / Cowork, not only Cursor: added Spanish triggers, graceful path resolution when pack not in project root, compact inline fallback doctrine
- **Rewrote** `docs/MULTI_AGENT_SETUP.md` — full IDE-by-IDE install instructions with actual bash commands; two-layer architecture explained (project context vs global skills); monorepo section preserved

### Decisions

- **Canonical skills live in `skills/`** — `.cursor/skills/` was removed because it created drift. IDEs that need the files should copy from `skills/`.
- **Two-layer model is the public story**: project context (AGENTS.md) per repo + global skills per IDE. This is now explicit in README and MULTI_AGENT_SETUP.
- **Skills handle missing pack gracefully**: path resolution tries workspace root first, then falls back to inline doctrine. Avoids breaking the experience for users who install skills globally without the full pack in every project.
- **Dual audience**: README now opens for Helldivers players who don't know what an agent is. The metaphor is the entry point; the methodology is the payload.

### Files changed

- `README.md` — full rewrite
- `docs/MULTI_AGENT_SETUP.md` — full rewrite
- `skills/promptdivers-orchestrator/SKILL.md` — updated triggers, path resolution, inline fallback
- `skills/promptdivers-pelican/SKILL.md` — updated triggers (ES + EN), path resolution
- `skills/promptdivers-tactical-signals/SKILL.md` — updated triggers (ES + EN), path resolution
- Deleted: `.cursor/skills/`, `docs/README.md`, `AI-DIVERS.docx`, `templates/copilot-instructions.sample.md`

### DEBT

- [ ] README `.cursor/rules/promptdivers-2.mdc` reference — file still exists but `.cursor/skills/` is gone; verify the `.mdc` rule content doesn't point to removed paths
- [ ] Link audit across `docs/` (Squad D pass before v3.0.0)
- [ ] Consider adding a `promptdivers-handoff` and `promptdivers-squads` skill as suggested in `docs/SKILLS_AND_EXTENSIONS.md`

### Mission debrief

| Objective | Result | Evidence |
|-----------|--------|----------|
| Clean repo — remove redundant files | PASS | 4 items deleted |
| README suitable for public repo | PASS | New Quick Install + dual audience |
| Skills work in Claude Code / Cowork | PASS | Path resolution + Spanish triggers added |
| MULTI_AGENT_SETUP complete per IDE | PASS | Bash commands + two-layer model documented |

**mission_status:** 🟢 GREEN

---

## Session: 2026-04-10 — Public repo improvements (score 7→9)

### Summary

Second pass focused on closing the three gaps identified in the repo audit: install friction, missing onboarding for non-developers, and missing visual architecture.

**Changes made:**

- **Created `install.sh`** — auto-detects Claude Code and/or Cursor, installs all 3 skills globally in one command. Supports `--project <dir>` flag to bootstrap AGENTS.md + CLAUDE.md + PROJECT_LOG into a project simultaneously. Handles edge cases: existing files, missing IDE dirs, unknown IDE.
- **Rewrote README** — added ASCII architecture diagram showing the two-layer model visually, added "Your first mission — 5 minutes" section with real copy-paste walkthrough (scenario: unknown codebase, Squad A, status, debrief loop), added tactical signals summary, linked FIRST_MISSION.md.
- **Created `FIRST_MISSION.md`** — bridge document for Helldivers players who don't know what an AI agent is. Explains the three fronts as game metaphors, each squad as a mission type, and walks through a first drop step by step. Written in game propaganda tone, not technical documentation.

### Decisions

- `FIRST_MISSION.md` lives at the repo root (not in `docs/`) because it's the entry point for the non-technical audience, not a reference doc.
- `install.sh` uses `~/.claude` and `~/.cursor` presence for IDE detection — avoids requiring the user to know what IDE they have before running it.
- The "5 minutes" walkthrough in README uses a real scenario (inherited repo with no docs) because abstract examples don't convert.

### Files changed

- `install.sh` — new
- `FIRST_MISSION.md` — new
- `README.md` — added diagram, 5-min walkthrough, signal summary, FIRST_MISSION link, install.sh as primary entry point

### DEBT

- [ ] `install.sh`: add Windows / PowerShell version (currently bash only)
- [ ] Consider a `promptdivers-squads` skill that bundles all four squads for users who don't have the pack in their project

### Mission debrief

| Objective | Result | Evidence |
|-----------|--------|----------|
| One-command install | PASS | install.sh created and executable |
| 5-min walkthrough in README | PASS | "Your first mission" section added |
| Visual architecture | PASS | ASCII two-layer diagram in README |
| Bridge for non-technical audience | PASS | FIRST_MISSION.md created |

**mission_status:** 🟢 GREEN

---


## Session: 2026-04-10 — Stratagem Codex + Protocols + Galactic War Map (v3.0.0)

### Summary

Major release transforming Promptdivers from abstract doctrine into a **concrete action system** aligned with Helldivers game mechanics. Created 18 stratagems in 5 categories, 4 new protocols (friendly-fire, mind-control, reinforce, democracy-officer), and a Galactic War Map template. Fixed 4 bugs in existing files.

### Decisions

- **Stratagems organized by game categories** (offensive/defensive/support/eagle/orbital) — matches the Helldivers mental model.
- **Each stratagem is self-contained** — loadable individually without the whole pack.
- **Orbital stratagems require Squad B** — heavy ordnance = higher clearance.
- **Mind control uses verification tiers** — proportional to risk, not paranoid.

### Files / areas

- `stratagems/` — entire new directory (19 files across 5 subdirectories)
- `protocols/` — 4 new files (friendly-fire, mind-control, reinforce, democracy-officer)
- `templates/galactic-war-map.template.md` — new campaign dashboard
- Updated: QUICK_REFERENCE, README, AGENTS.md, CHANGELOG, VERSION, CONTRIBUTING, SKILLS_AND_EXTENSIONS, .mdc rule, install.sh, orchestrator SKILL.md

### Mission debrief

| Objective | Result | Evidence |
|-----------|--------|----------|
| Fix known bugs (H1) | PASS | 4 files fixed |
| Stratagem Codex (H2) | PASS | 18 stratagems in `stratagems/` |
| Missing protocols (H4) | PASS | 4 new protocols |
| Galactic War Map (H3) | PASS | template created |
| Cross-reference updates | PASS | All indexes updated |

**mission_status:** 🟢 GREEN

---

## HANDOFF_JSON

```json
{
  "schema": "promptdivers-handoff/v1",
  "updated": "2026-04-10",
  "mission_last": "B",
  "squad_files_used": ["squads/squad-b-artillery.md"],
  "model_used": "claude-opus-4",
  "model_rationale": "Large multi-file creation requiring deep context across 25+ files",
  "objective": "v3.0.0: Stratagems, protocols, war map, fixes",
  "objectives": [
    {"id": "1", "label": "Bug fixes", "result": "PASS", "evidence": "CONTRIBUTING, SKILLS, .mdc, install.sh fixed"},
    {"id": "2", "label": "Stratagem Codex", "result": "PASS", "evidence": "18 stratagems in stratagems/"},
    {"id": "3", "label": "Protocols", "result": "PASS", "evidence": "4 new protocol files"},
    {"id": "4", "label": "Galactic War Map", "result": "PASS", "evidence": "template created"},
    {"id": "5", "label": "Cross-refs", "result": "PASS", "evidence": "All indexes updated"}
  ],
  "mission_status": "GREEN",
  "debrief_summary": "v3.0.0 shipped. Pack now has concrete game-like stratagem system.",
  "open_tasks": [
    "Full link audit (Squad D)",
    "Sample mission packs for v3.1.0",
    "i18n: Spanish/Portuguese",
    "Warbonds / progression system doc"
  ],
  "debt": [],
  "do_not_touch": [],
  "next_recommended": {
    "squad": "D",
    "nave": "claude-haiku",
    "reason": "Link audit + git tag v3.0.0 + push."
  }
}
```

---

*Promptdivers — memory is a weapon.*
