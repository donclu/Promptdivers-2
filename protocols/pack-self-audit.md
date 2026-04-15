# Pack self-audit — Promptdivers dogfooding checklist

## *Make the framework review itself*

This checklist is for maintaining **Promptdivers (the pack)** as a coherent, evidence-first framework.
It is also a template consumers can adapt to audit their own forks.

**Related:** [accuracy-policy.md](accuracy-policy.md) · [pre-drop.md](pre-drop.md) · [mission-debrief.md](mission-debrief.md) · [friendly-fire.md](friendly-fire.md) · [../QUICK_REFERENCE.md](../QUICK_REFERENCE.md)

---

## When to run

- Before a release (`VERSION` / `CHANGELOG.md` change)
- After adding or renaming any protocol / squad / stratagem / tutorial
- After expanding governance rules (permissions, “no hallucinations”, escalation)
- When a user reports confusion: “where is the source of truth for X?”

---

## 0) Declare audit scope

Write one line in `PROJECT_LOG.md`:

```text
Pack self-audit: scope=[docs|protocols|skills|templates|installers] reason=[release|drift|report|cleanup]
```

---

## 1) Source-of-truth map (no ambiguity allowed)

For each concept below, confirm **exactly one canonical home** and that other mentions are pointers:

| Concept | Canonical home should be | Also referenced from |
|--------|---------------------------|----------------------|
| Squad mission tree | `QUICK_REFERENCE.md` + `squads/` | `AGENTS.md` (map only) |
| Inter-agent message grammar | `protocols/inter-agent-protocol.md` | `QUICK_REFERENCE.md` |
| Tactical signals table | `protocols/tactical-signals.md` | `QUICK_REFERENCE.md` |
| Pre-drop planet check | `protocols/pre-drop.md` | tutorials + quick reference |
| Debrief / scoring | `protocols/mission-debrief.md` | `skills/promptdivers-pelican/SKILL.md` |
| Reinforcement (parallel sessions) | `protocols/reinforce.md` | `stratagems/support/reinforce.md` |
| Escalation ladder | `protocols/escalation.md` | quick reference |
| Friendly-fire prevention | `protocols/friendly-fire.md` | Squad B docs + PRD |
| Radio comms format | `protocols/radio-comms.md` | quick reference + orchestrator skills |
| Parallel Drop (PRD) | `stratagems/support/parallel-drop.md` | orbital-control skill |

If you find two “canonical” docs for the same concept, pick one, then convert the other into a thin pointer.

---

## 2) Link integrity (no broken references)

### Minimum checks (manual, fast)

- In every modified file, spot-check each “Related:” link is **relative** and points to an existing file.
- In `QUICK_REFERENCE.md`, ensure every referenced path exists.
- In `AGENTS.md`, ensure the “Critical project map” paths exist.

### Higher rigor (recommended before release)

- Run the pack health check script if present (see `scripts/`).
- If you add a new doc, ensure it is reachable from at least one index (README, quick reference, missions index, docs index).

---

## 3) Terminology + flags consistency (single spelling)

Confirm these tokens appear with the **same spelling** everywhere:

- `COMMS_MODE: STANDARD | RADIO` (see `protocols/radio-comms.md`)
- `TOKEN_BUDGET: LOW | MED | HIGH`
- `PARALLELISM: OFF | 2_AGENTS | 3_AGENTS`
- `mission_status: GREEN | YELLOW | RED` (debrief aggregate)
- `missions_queued` (handoff queue field name)

If a flag is documented, make sure it is defined in **one** place and referenced elsewhere.

---

## 4) Governance invariants (Illuminate controls)

Confirm the pack enforces these invariants by wording + cross-links:

- **No invented canon**: Helldivers language is explicitly metaphor, not asserted game mechanics.
- **No invented APIs/flags**: every mentioned file path / flag / command is present in the pack or marked UNVERIFIED.
- **Evidence-first**: “verified” claims include a path, output excerpt, or reproducible step.
- **Permissions**: “must confirm first / must never do” exists and is consistent (see `AGENTS.md`).

If any doc implies game mechanics as fact, rewrite it as metaphor + Promptdivers doctrine.

---

## 5) Onboarding health (first 10 minutes)

Verify there is one obvious start path:

- A newcomer can find: **what is Promptdivers**, **how to start**, **what to paste**, and **how to close the loop**.
- `FIRST_MISSION.md`, `missions/README.md`, and `QUICK_REFERENCE.md` do not contradict each other about the first steps.
- Tutorials reference current protocols/flags, not outdated ones.

---

## 6) Duplication hotspots (keep intentional overlap aligned)

Allowed duplication patterns:

- **Field summary** in `QUICK_REFERENCE.md` (short; points to canonical)
- **Action card** in `stratagems/` (inputs/outputs; points to canonical protocol)
- **Skill** in `skills/*/SKILL.md` (activation instructions; points to canonical protocol)

If a duplicated section is more than ~15–25 lines, prefer converting it into a pointer.

---

## 7) Close-out (log the result)

Record:

- What was changed (paths)
- Any renamed or re-homed canonical docs
- Any new flags added (should be rare)
- Whether `CHANGELOG.md` / `VERSION` needs updating

Then run a brief debrief if objectives were explicit (see `protocols/mission-debrief.md`).

---

*Promptdivers — if the framework can’t audit itself, it can’t govern others.*

