# Multi-agent setup — Promptdivers in any IDE

Promptdivers is tool-agnostic. The same doctrine loads through different files depending on the IDE. This guide tells you **what to copy where** for each environment.

---

## Two layers — understand this first

**Layer 1 — Project context** (per repo, in your project root)  
`AGENTS.md` + `CLAUDE.md` — the agent's contract with your specific project. Stack, permissions, critical paths. You edit this per project.

**Layer 2 — Skills** (global, installed once per IDE)  
`skills/promptdivers-*` — the playbooks that load on demand. Install them once and they're available in every project.

These two layers are **independent**. You can use the context without the skills, or the skills without the full context. But both together is where the system shines.

---

## Claude Code / Cowork

### Project context

Place `CLAUDE.md` at your project root. Claude Code reads it automatically on session start.

Option A — stub pattern (recommended, keeps one source of truth):
```bash
# Copy the stub from this pack — it tells Claude to load AGENTS.md
cp path/to/promptdivers/CLAUDE.md your-project/CLAUDE.md
cp path/to/promptdivers/AGENTS.md your-project/AGENTS.md
```

Option B — single file (simpler for small projects):
```bash
# Rename AGENTS.md → CLAUDE.md if you want one self-contained file
cp path/to/promptdivers/AGENTS.md your-project/CLAUDE.md
```

Personal defaults (applies to all your repos unless overridden):
```bash
cp path/to/promptdivers/AGENTS.md ~/.claude/CLAUDE.md
```

### Skills (install once, global)

```bash
mkdir -p ~/.claude/skills
cp -r path/to/promptdivers/skills/promptdivers-orchestrator ~/.claude/skills/
cp -r path/to/promptdivers/skills/promptdivers-pelican ~/.claude/skills/
cp -r path/to/promptdivers/skills/promptdivers-tactical-signals ~/.claude/skills/
```

After installing, the skills appear as commands in Claude Code and Cowork. Trigger them by name or use the keywords in each skill's description.

### Session log (optional but recommended)

```bash
cp path/to/promptdivers/templates/project-log.template.md your-project/PROJECT_LOG.md
```

Say `save` at the end of any session and the agent updates this file.

---

## Cursor

### Project context

Two options — thin rule or full file:

**Option A — `.cursor/rules/` (recommended)**  
Copy the bundled rule stub:
```bash
cp path/to/promptdivers/.cursor/rules/promptdivers-2.mdc your-project/.cursor/rules/
```
The rule tells Cursor to load `AGENTS.md` and the squads. Edit `AGENTS.md` for policy changes.

**Option B — full file**  
Copy `AGENTS.md` to your project root. Cursor will pick it up if you add it to `.cursor/rules/` with `alwaysApply: true`.

### Skills

**Global (all projects):**
```bash
mkdir -p ~/.cursor/skills
cp -r path/to/promptdivers/skills/promptdivers-orchestrator ~/.cursor/skills/
cp -r path/to/promptdivers/skills/promptdivers-pelican ~/.cursor/skills/
cp -r path/to/promptdivers/skills/promptdivers-tactical-signals ~/.cursor/skills/
```

**Project only:**
```bash
cp -r path/to/promptdivers/skills/promptdivers-orchestrator your-project/.cursor/skills/
# repeat for pelican and tactical-signals
```

---

## Windsurf

1. Copy `AGENTS.md` to your project root.
2. Create `.windsurf/rules/promptdivers.md` with this content:
   ```
   Read AGENTS.md at the project root before every task.
   Follow the squad doctrine in squads/ and the protocols in protocols/.
   Use QUICK_REFERENCE.md as your field cheat sheet.
   ```
3. Copy the skills to `~/.windsurf/skills/` if Windsurf supports a skills directory (check current docs — the format matches Cursor's `SKILL.md` convention).

---

## GitHub Copilot (VS Code)

1. Create `.github/copilot-instructions.md` in your repo:
   ```markdown
   This project uses Promptdivers agent doctrine.
   Read AGENTS.md at the project root before coding.
   Mission routing is in QUICK_REFERENCE.md.
   Squad playbooks are in squads/.
   ```
2. Copy `AGENTS.md` to your project root.
3. Skills are not natively supported by Copilot — paste the relevant squad section directly into `copilot-instructions.md` when needed.

---

## OpenCode

1. `AGENTS.md` at the project root is the primary file OpenCode looks for — no rename needed.
2. Copy `squads/` and `protocols/` alongside it if you want the full playbook available.

---

## Gemini CLI

1. Create `GEMINI.md` at your project root (confirm current filename in Google's Gemini CLI docs):
   ```markdown
   This project uses Promptdivers. Read AGENTS.md and README.md before starting.
   Squad playbooks are in squads/. Protocols are in protocols/.
   ```
2. Gemini has a large context window — you can inline more content from `AGENTS.md` than other IDEs.

---

## JetBrains AI / others

Same two-layer pattern:
- One **human-readable contract** (`AGENTS.md`) at the project root.
- One **IDE-specific stub** that says "read the contract + these squad files."

---

## Monorepos

Put `AGENTS.md` at the repo root with a monorepo map (which package owns what).  
Add package-local `AGENTS.md` files only when a subproject truly needs different doctrine; otherwise use relative paths in the root brief.

---

## Minimal drop-in set (any IDE)

| File | Purpose | Required |
|------|---------|----------|
| `AGENTS.md` | Full agent brief | Yes |
| `CLAUDE.md` (or IDE stub) | Auto-load hook | Yes for Claude Code |
| `QUICK_REFERENCE.md` | One-page cheat sheet | Recommended |
| `PROJECT_LOG.md` | Session continuity | Recommended |
| `squads/squad-*.md` | Mission playbooks | When using squads |
| Skills in IDE skills dir | On-demand routing | Recommended |

---

*Promptdivers — same democracy, any drop pod.*
