# Radio Comms — optional gamified ops layer

Promptdivers is evidence-first. **Radio Comms** is an optional *format layer* that makes the workflow feel like the game **without** changing the underlying governance.

## Opt-in

Paste into the mission brief (or `NEXT_MISSION.md`):

```text
COMMS_MODE: RADIO
```

If omitted: `COMMS_MODE: STANDARD`.

---

## Core rule (non-negotiable)

Radio lines must never replace evidence. For any claimed progress, include **one** of:

- a file path, or
- a command/result summary, or
- a concrete next step with an owner.

---

## Sequence (recommended)

### 1) Locate

```text
📋 SITREP — Planet Check initiated
Locating: Galaxy → Planet → PrimaryMission
Source: GALACTIC_WAR_MAP.md | PROJECT_LOG.md | AGENTS.md
```

### 2) Command

```text
🛰️ ORBITAL CONTROL — Ship online
Nave: CLASS A|B|C  |  TOKEN_BUDGET: LOW|MED|HIGH  |  PARALLELISM: OFF|2_AGENTS|3_AGENTS
```

### 3) Loadout

```text
📦 STRATAGEM TERMINAL — Loadout locked
Loadout: [PRD/RNF/SOS/IDR/DSK/ATA/...]
🎯 ON TARGET — Scope: [paths]
```

### 4) Drop + fight

```text
🚀 DROP — Deploying Promptdivers
Enemies(fronts): [Terminids|Automatons|Illuminate]
Objectives: [1–3 short labels]
```

During work, emit small updates:

```text
📍 MARK — finding at: [path]
📋 SITREP — progress: [one line] — blocker: [none|X]
⏸️ HOLD — overlap detected: [path] (re-splitting)
```

### 5) Reinforce / SOS

```text
🔄 RNF — reinforcement requested: [reason] — owns: [paths]
🆘 SOS — blocked on human decision: [question] — impact: [one line]
```

### 6) Extract (Pelican)

```text
✅ CLEAR — Calling Pelican-1 (debrief)
Primary: PASS|PARTIAL|FAIL — evidence: [path/test]
Secondaries: [list or none]
Stratagems used: [codes]
```

Optional: “stars” are derived from mission status (do not invent precision):

- GREEN → ★★★★★
- YELLOW → ★★★★☆
- RED → ★★☆☆☆

---

*Promptdivers — keep it fun, keep it auditable.*

