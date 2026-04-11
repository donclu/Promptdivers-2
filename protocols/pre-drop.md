# Pre-drop check — planet state before deployment

## *Read the map before you drop. Every time.*

> In Helldivers you check the galactic war map before selecting your planet: enemy density,
> active operations, liberated sectors. In Promptdivers you do the same before picking a squad
> and a ship.

**When to run:** at the start of any session; before filling `NEXT_MISSION.md`; whenever the
human says `status` or `debrief` and no planet state is in context.

**Related:** [`templates/galactic-war-map.template.md`](../templates/galactic-war-map.template.md) ·
[`templates/next-mission.template.md`](../templates/next-mission.template.md) ·
[`docs/model-fleet.md`](../docs/model-fleet.md) ·
[`QUICK_REFERENCE.md`](../QUICK_REFERENCE.md)

---

## Step-by-step

### 1. Locate the planet state

Priority order:

1. `GALACTIC_WAR_MAP.md` in the project root (copy of the template, kept current).
2. `PROJECT_LOG.md` — last session block and threat index.
3. `AGENTS.md` — "Known issues / technical debt" section.
4. If none exists: run **Squad D → THE SENTINEL** health check, or ask the human for a quick
   verbal SITREP.

---

### 2. Read and classify the terrain

From whichever source you found, extract:

| Field | What to look for |
|-------|-----------------|
| **Sectors** | Which paths/modules are LIBERATED · CONTESTED · ENEMY HELD · UNEXPLORED |
| **Active fronts** | Terminids (bugs/defects) · Automatons (brittle scripts/CI) · Illuminate (ungoverned AI) |
| **Threat level** | LOW / MEDIUM / HIGH / CRITICAL — take the highest active threat |
| **Campaign score** | % liberation (nice to have; skip if time-constrained) |
| **Progression level** | Cadet → Helldiver → Skull Admiral → Super Earth Hero |

---

### 3. Derive squad recommendation

| Planet state | Recommended squad |
|--------------|-------------------|
| Unexplored terrain / no `AGENTS.md` | **Squad A** — map first |
| Wide Automaton or multi-file debt | **Squad B** — artillery |
| Spotted Terminid bug, 1–5 files | **Squad C** — surgical |
| Pre-deploy / PR / monitoring | **Squad D** — defense |
| Multiple CRITICAL fronts simultaneously | **Operation Total Democracy** |

---

### 4. Derive nave (ship class) recommendation

| Mission type + context | Recommended class |
|------------------------|-------------------|
| Deep reasoning, large repo, AUDIT, WRITE | **Class A** |
| Fast iteration, Squad C surgical, quick CONSULT | **Class B** |
| Sensitive data, air-gapped, offline | **Class C (local)** |
| Vision tasks (images, diagrams, UI screenshots) | **Class A multimodal** (gpt-4o, gemini) |

Cross-check against `AGENTS.md` `Model (nave)` declaration — use the project default unless
mission requirements justify a different class.

---

### 5. Output: Planet status block

Write 3–6 lines to fill the `## Planet status` section of `NEXT_MISSION.md`:

```markdown
## Planet status (pre-drop check)

- **Active fronts:** [Terminids / Automatons / Illuminate — list only active ones]
- **Hottest sector:** [path, module, or "general repo"]
- **Threat level:** LOW | MEDIUM | HIGH | CRITICAL
- **Source:** GALACTIC_WAR_MAP.md | PROJECT_LOG.md | AGENTS.md | verbal SITREP
- **Recommended squad:** A | B | C | D — because: [one line]
- **Recommended nave:** CLASS A | B | C — because: [one line]
```

If no project-level planet state exists yet, note it and recommend running Squad A or Squad D
to establish baseline before the mission.

---

## Anti-patterns

| Anti-pattern | Fix |
|--------------|-----|
| Jumping straight to "what do you want me to do?" without terrain check | Run pre-drop first; 30 seconds of context saves 10 minutes of misalignment |
| Treating all missions as Squad B (heavy artillery) | Match squad to planet state; not every bug needs a full artillery mission |
| Using Class A model for a quick CONSULT | Class B frigates exist for a reason — save Class A depth for when it matters |
| No `GALACTIC_WAR_MAP.md` in the project | Copy `templates/galactic-war-map.template.md` and fill it in after first Squad D pass |
| Skipping pre-drop mid-session when scope changes | Re-run whenever a new front opens during a mission |

---

## If no planet state is available

```text
[THE AUTHENTIC] → [HUMAN] | REQUEST |
  No GALACTIC_WAR_MAP.md or PROJECT_LOG.md found.
  To establish planet state, either:
    a) Run Squad D → THE SENTINEL for a quick health scan, OR
    b) Give me a 2-line verbal SITREP: main problem + affected area.
  Without it I'll assume UNEXPLORED terrain and route to Squad A.
```

---

*Promptdivers — check the map, drop with purpose. FOR DEMOCRACY.*
