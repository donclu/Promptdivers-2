# Stratagem Codex — Promptdivers

## *Call it in. Hit the mark. Spread democracy.*

> In Helldivers, stratagems are **concrete actions** you call in on the battlefield — not abstract ideas. Promptdivers stratagems work the same way: each one is a **defined procedure** with a trigger, a scope, and a result.

**Quick field card:** [QUICK_REFERENCE.md](../QUICK_REFERENCE.md) (stratagem loadout section).

---

## How stratagems work

1. **Identify the need** — your mission hits a spot where a standard action applies.
2. **Call the stratagem** — tell the agent (or load the file yourself).
3. **Execute** — the stratagem has steps, inputs, and outputs.
4. **Log** — record in `PROJECT_LOG.md` which stratagems were used.

### Loadout

Like the game, you don't bring *every* stratagem to *every* mission. Pick what fits:

- **Squad C** missions: 1–2 stratagems (usually one offensive + one defensive).
- **Squad B** missions: 3–4 stratagems per batch.
- **Squad A** recon: mostly support stratagems.
- **Squad D** defense: defensive + support.
- **TOTAL DEMOCRACY**: everything available.

---

## Categories

### ⚔️ [Offensive](offensive/) — Attack problems directly

| Stratagem | Code | Use when |
|-----------|------|----------|
| [Orbital Precision Strike](offensive/orbital-precision-strike.md) | `OPS` | Surgical rewrite of one critical file |
| [Eagle Airstrike](offensive/eagle-airstrike.md) | `EAS` | Quick refactor across ~3 files |
| [Railgun](offensive/railgun.md) | `RGN` | Eliminate unnecessary dependency |
| [Autocannon](offensive/autocannon.md) | `ACN` | Automated lint + format pass |
| [Data Strike](offensive/data-strike.md) | `DSK` | Data analysis, cleaning, pipeline work |
| [Automaton Assault](offensive/automaton-assault.md) | `ATA` | Fix/replace/build automation and scripts |

### 🛡️ [Defensive](defensive/) — Protect liberated territory

| Stratagem | Code | Use when |
|-----------|------|----------|
| [Shield Generator](defensive/shield-generator.md) | `SHG` | Add tests for uncovered code |
| [Guard Dog](defensive/guard-dog.md) | `GDG` | Set up CI/CD regression guard |
| [Tesla Tower](defensive/tesla-tower.md) | `TSL` | Install pre-commit hooks |
| [Fortify](defensive/fortify.md) | `FRT` | Document a module with proper docstrings |

### 📦 [Support](support/) — Logistics and coordination

| Stratagem | Code | Use when |
|-----------|------|----------|
| [Reinforce](support/reinforce.md) | `RNF` | Request another agent/session in parallel |
| [Resupply](support/resupply.md) | `RSP` | Refresh context: re-read AGENTS.md + logs |
| [SOS Beacon](support/sos-beacon.md) | `SOS` | Escalate to human with structured evidence |
| [Hellpod](support/hellpod.md) | `HPD` | Bootstrap file from template/pattern |
| [Intel Dossier](support/intel-dossier.md) | `IDR` | Structured research and intelligence gathering |
| [Prompt Forge](support/prompt-forge.md) | `PFG` | Design, test, and iterate AI prompts |

### 🦅 [Eagle](eagle/) — Fast strikes with cooldown

| Stratagem | Code | Use when |
|-----------|------|----------|
| [Eagle 500kg](eagle/eagle-500kg.md) | `E5K` | Delete confirmed dead code/file |
| [Eagle Smoke Strike](eagle/eagle-smoke.md) | `ESS` | Create feature/safety branch before risky edits |
| [Eagle Rearm](eagle/eagle-rearm.md) | `ERM` | Reset session: debrief + clean handoff |
| [Eagle Report](eagle/eagle-report.md) | `ERP` | Produce formal reports and deliverables |
| [Eagle Visuals](eagle/eagle-visuals.md) | `EVS` | Generate diagrams, mockups, charts, visuals |

### ☄️ [Orbital](orbital/) — Heavy strikes requiring Squad B

| Stratagem | Code | Use when |
|-----------|------|----------|
| [Orbital Barrage](orbital/orbital-barrage.md) | `ORB` | Major framework/dependency migration |
| [Orbital Laser](orbital/orbital-laser.md) | `ORL` | Full module removal with cleanup |
| [Orbital EMS](orbital/orbital-ems.md) | `OEM` | Scope freeze: no changes until review |

---

## Invoking a stratagem

In chat, any of these work:

```text
"Call in Shield Generator on src/auth/"
"Stratagem: Railgun on lodash"
"Run Eagle 500kg on src/legacy/old-router.ts"
"SOS Beacon — I'm stuck on the migration"
```

The agent should:
1. Load the stratagem file.
2. Confirm scope with the human.
3. Execute the steps.
4. Log which stratagem was used in the session.

---

## Custom stratagems

Teams can add their own stratagems by creating new files in the appropriate category folder. Follow the template:

```markdown
# [Name] — [Category]

## Code: [3-letter code]

## When to call
[Trigger conditions]

## Inputs
[What the agent needs]

## Steps
[Numbered procedure]

## Outputs
[What gets produced]

## Cooldown / limits
[Any restrictions on reuse]
```

---

*Promptdivers — every problem has a stratagem. FOR DEMOCRACY.*
