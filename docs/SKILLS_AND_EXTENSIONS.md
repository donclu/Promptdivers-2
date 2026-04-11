# Skills and extensions — Promptdivers

**If you read only one integration doc, read [agent-ecosystem-integration.md](agent-ecosystem-integration.md).** Broad mission types (CONSULT, RECON, BUILD-WEB, LAUNCH-WEB, etc.) live in [super-earth-operating-model.md](super-earth-operating-model.md). Step-by-step tutorial missions (copy-paste briefs that scaffold reasoning): [missions/README.md](../missions/README.md).

This pack is **plain Markdown** so any model can use it. **Cursor Skills**, **Claude Code skills**, and similar systems are **optional accelerators**: they teach the IDE *when* to load *which* playbook.

**Doc index / reading order:** [../README.md](../README.md)  
**Calibration (voice + creativity):** [onboarding-calibration.md](onboarding-calibration.md)

---

## What you already have (external ecosystem)

These are **not** part of this repo but pair well with Promptdivers:

| Skill / doc | Use with Promptdivers |
|-------------|------------------------|
| **Agent orchestrator** | Generic router; merge with [agent-ecosystem-integration.md](agent-ecosystem-integration.md) + **`promptdivers-orchestrator`** (superskill) |
| **Agent context** | `AGENTS.md` / project rules — THE AUTHENTIC |
| **Agent memory** | Sessions, `mem_save`, Engram — with THE SCRIBE / `PROJECT_LOG` |
| **GitHub style learner** | PR / house style — THE AUDITOR |
| **Structured workflow** | Logs, handoffs, scope lock, phases, racimo — backbone for any long mission |
| **SDD / spec-driven** | Large features — feeds Squad B |
| **MCP best practices** | Tools and permissions in `AGENTS.md` |
| **App auditor** | Pre-ship audit, `/explain`, IA detection — Squad D + ESCALATE on critical |
| **UI design expert** | All UI/UX; run **Phase 0** before building; Squads B/C |
| **Humanizer** | Stakeholder prose; **after** [onboarding-calibration.md](onboarding-calibration.md) asks **AI-likeness** + **creativity** |

Promptdivers adds **squads A–D**, **tactical signals**, **three fronts**, **escalation**, and the **superskill router** so one doctrine covers consult → code → data → images → direction.

### Humanizer (required calibration)

For README, `/explain`, exec summaries, posts, or “friendly” audit text:

1. Ask **how AI-like** the voice should sound (polished assistant ↔ human cadence).  
2. Ask **how much creativity** (single path ↔ options ↔ brainstorm).  
3. Load **humanizer** and deliver; optional **termómetro** per that skill.

See [onboarding-calibration.md](onboarding-calibration.md).

---

## Bundled copy-ready skills (in this repo)

| Skill | Path |
|-------|------|
| **promptdivers-orchestrator** | [`skills/promptdivers-orchestrator/SKILL.md`](../skills/promptdivers-orchestrator/SKILL.md) |
| **promptdivers-tactical-signals** | [`skills/promptdivers-tactical-signals/SKILL.md`](../skills/promptdivers-tactical-signals/SKILL.md) |
| **promptdivers-pelican** | [`skills/promptdivers-pelican/SKILL.md`](../skills/promptdivers-pelican/SKILL.md) |

Copy each folder into your user skills directory (e.g. Cursor: `~/.cursor/skills/<skill-name>/`, Claude Code: `~/.claude/skills/<skill-name>/`) **or** into your project.

All three bundled skills carry **multi-domain capability libraries** (web/UI, data, images, APIs, tooling) and model/nave routing embedded inside them.

- **promptdivers-orchestrator** — **Stratagem: Field Command**: consult, recon, audit, web, backend, data, visuals, direction, writing + model/nave routing (fleet: Class A/B/C — Claude, GPT, Gemini, local) + built-in capability library (web/UI, data, images, APIs, verification); **max two heavy skills per phase**.
- **promptdivers-tactical-signals** — **Signal grid**: pings + domain-specific signal examples (code, UI, data, images, APIs, model switches); lead with marker, English detail + path/metric.
- **promptdivers-pelican** — **Extraction / scoreboard**: score objectives PASS/PARTIAL/FAIL with cross-domain evidence (code tests, visual checks, data metrics, API responses, model rationale); `mission_status` GREEN/YELLOW/RED; stratagem routing on failure; `model_used` + `model_rationale` in `HANDOFF_JSON`.

---

## Gaps worth filling (recommended extra skills)

These are thin wrappers or specs beyond the bundled orchestrator.

### 2. `promptdivers-squad-a` … `promptdivers-squad-d` (or one `promptdivers-squads` skill)

**Triggers:** match squad names and mission types.

**Job:**

- `view` / read the matching `squads/squad-*.md` in this pack (or the consuming project’s copy).

**Why:** Keeps the main agent context small until a mission is chosen.

**Alternative:** One skill with four sections if your tool dislikes many small skills.

---

### 3. `promptdivers-handoff`

**Triggers:** “handoff,” “save state,” “next agent,” “resume tomorrow.”

**Job:**

- Emit JSON or structured markdown matching `templates/project-log.template.md` handoff section.
- List open files, decisions, DEBT items, and next mission.

**Why:** Consistent continuity across Claude / Cursor / Copilot sessions.

**Note:** **Scored mission close-out** is covered by [`protocols/mission-debrief.md`](../protocols/mission-debrief.md) and bundled **`promptdivers-pelican`**; a thin `promptdivers-handoff` can still focus on bare continuity without duplicating the debrief protocol body.

---

### 4. `promptdivers-escalation`

**Triggers:** “escalate,” “too big,” “production down,” “TOTAL DEMOCRACY.”

**Job:**

- Load `protocols/escalation.md` + `protocols/operation-total-democracy.md`.
- Require evidence blocks for `ESCALATE`.

---

### 5. Agent Orchestrator (your existing skill)

Keep **Agent Orchestrator** as the **generic** router. Use **promptdivers-orchestrator** when the session is mission/squad/tactical-heavy, or merge the decision trees manually using [agent-ecosystem-integration.md](agent-ecosystem-integration.md).

---

## Claude Code vs Cursor vs Copilot

| Concern | Claude Code | Cursor | Copilot / others |
|--------|-------------|--------|-------------------|
| Default project file | `CLAUDE.md` | Rules + optional skills | `copilot-instructions.md` or editor docs |
| Lazy loading | Skills / subagents per vendor docs | Skills (`SKILL.md`) | Usually single instruction file; split by linking paths |
| Best fit for Promptdivers | Mirror `AGENTS.md` → `CLAUDE.md` | Rule stub + optional skills | Short stub pointing at `AGENTS.md` |

**Recommendation:** Treat **`AGENTS.md` as canonical**; every other surface is a **pointer** plus tool-specific permissions.

---

## Anti-patterns

- Duplicating full squad markdown inside a skill—**link or `view` the file** in the consuming project instead.
- Putting **secrets or repo-specific paths** inside a global skill—keep those in **project** `AGENTS.md` only.

---

## Contributing skills back

If you publish `promptdivers-*` skills to a repo or marketplace, add a **Compatibility** line:

- Tested with: Cursor `SKILL.md` format / Claude Code / …
- Requires: project has `AGENTS.md` + `squads/` (or paths configured in skill frontmatter).

---

*Promptdivers — extend the stratagem grid, do not duplicate the constitution.*
