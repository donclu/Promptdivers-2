# AGENT_PROFILE.md — the Helldiver's field dossier

## *What an operative carries in their drop pod*

> `AGENTS.md` is your **citizenship certificate** (doctrine, permissions, stack).
> `AGENT_PROFILE.md` is your **service record** (what you know, what you can do, what you've lived through, where you're going).
>
> Together they let a low-reasoning model perform like a higher-tier one — not by raw power, but by carrying structured scaffolding from past drops.

This file is an **index**, not a memory. Each point on the service record points to a directory or file where the real data lives. Keep the entries short; put detail in the referenced files.

**Related:** [AGENTS.md](AGENTS.md) · [docs/calibration-protocol.md](docs/calibration-protocol.md) · [docs/reasoning-tiers.md](docs/reasoning-tiers.md) · [stratagems/support/echelon-ladder.md](stratagems/support/echelon-ladder.md)

---

## The eight-point service record

```
1. KNOWLEDGE       → knowledge/          (facts with source, static + dynamic)
2. SKILLS          → skills/             (capabilities the agent can invoke)
3. EXPERIENCE      → experience/         (operational / learned / integrity / quality)
4. ASPIRATIONS     → NEXT_MISSION.md + roadmap/   (where we're going)
5. DOCTRINE        → AGENTS.md           (values, rules, permissions)
6. FEEDBACK LEDGER → experience/integrity/   (corrections + confirmations from human)
7. OPERATING LIMITS→ (this file, below)   (budget, cost, privacy, ceiling)
8. NETWORK         → handoffs/ + PROJECT_LOG.md   (collaborators, past handoffs)
```

Points 1–4 are what you **carry**. Point 5 is what you **obey**. Point 6 is what you **learn from correction**. Points 7–8 are the **boundaries and the radio**.

---

## 1. Knowledge
# [INTEL VAULT]

```yaml
pointer: knowledge/
schema: knowledge/README.md
domains: []            # fill per project — e.g. ["terminids-front", "web-ops"]
rag_index: null        # optional: path or URL to a RAG index over knowledge/
refresh_policy: "see docs/calibration-protocol.md §expiry"
```

Rule: **every fact has a source and a date**. No source → no fact. See `protocols/accuracy-policy.md`.

## 2. Skills
# [STRATAGEM LOADOUT]

```yaml
pointer: skills/
preferred_model:
  # fill per skill with tier alias from docs/reasoning-tiers.md
  # example (non-binding):
  prompt-forge:         "@medium"
  humanizer:            "@high"
  ui-design-expert:     "@medium + vision"
  echelon-ladder:       "mixed — each rung declares its own tier"
```

## 3. Experience
# [SERVICE RECORD]

```yaml
pointer: experience/
subdomains:
  operational: "missions executed — inputs, outcome, rung reached"
  learned:     "distilled lessons — WHY things work or fail"
  integrity:   "feedback ledger — corrections + confirmations from human"
  quality:     "audits conducted — findings, recurrence, recurrence cost"
format: "prose .md for reasoning; structured .yaml for queryable facts; both welcomed"
consolidation: "run `consolidate-memory` skill on extraction; see protocols/mission-debrief.md"
```

## 4. Aspirations
# [MISSION HORIZON]

```yaml
pointer: NEXT_MISSION.md + roadmap/
horizon:
  session:  "next 1-5 turns — NEXT_MISSION.md"
  sprint:   "next mission bundle — roadmap/current.md (optional)"
  project:  "long arc — roadmap/vision.md (optional)"
```

## 5. Doctrine
# [SUPER EARTH ORDERS]

```yaml
pointer: AGENTS.md
override: "CLAUDE.md is a stub — full briefing is AGENTS.md"
```

## 6. Feedback ledger
# [DEMOCRACY LEDGER]

```yaml
pointer: experience/integrity/feedback-ledger.yaml
captures:
  - corrections:    "human says 'no, not that' — record rule + why"
  - confirmations:  "human says 'yes that was right' — record non-obvious calls that worked"
  - abstentions:    "human chose to not do X — record boundaries"
audit_cadence: "every extract / debrief — Democracy Officer checks drift"
```

## 7. Operating limits
# [CLEARANCE CAPS]

```yaml
# — Session economics (set per project in calibration) —
token_budget_per_session:   # e.g. 150000 — adjust per project
cost_cap_usd_per_session:   # e.g. 5.00 — adjust per project
privacy_tier:               # "pack-default" | "local-only" | "cloud-ok"

# — Tenure state (set by THE DEMOCRACY OFFICER on promotion/demotion) —
tenure_level:               # rookie | veteran | elite | legend
max_echelon_rung:           # from tenure_caps below — hard ceiling for Echelon Ladder
escalation_budget:          # from tenure_caps below — rung climbs allowed per session
requires_approval_for:      # from tenure_caps below — actions requiring human sign-off

# — Clearance caps reference (copy the matching block from protocols/promotion.md) —
tenure_caps:
  rookie:
    max_echelon_rung: 1
    escalation_budget: 2
    requires_approval_for: [commit, deploy, RED_flag]
  veteran:
    max_echelon_rung: 2
    escalation_budget: 4
    requires_approval_for: [deploy, RED_flag]
  elite:
    max_echelon_rung: 3
    escalation_budget: 8
    requires_approval_for: [RED_flag]
  legend:
    max_echelon_rung: 3
    escalation_budget: 999
    requires_approval_for: []
```

Set `tenure_level` to the operative's current clearance and copy the matching caps into
the top fields. Full promotion criteria and demotion triggers: `protocols/promotion.md`.

## 8. Network
# [RADIO NET]

```yaml
pointer: PROJECT_LOG.md (handoffs section) + optional handoffs/
captures:
  - previous_agents:   "who worked on this before, what role, what they left"
  - delegations:       "sub-agent fan-outs — who got what, outcome"
  - open_escalations:  "unresolved ESCALATE signals awaiting reply"
```

---

## Pre-drop checklist

At session start, **THE AUTHENTIC** reads:

1. `AGENTS.md` (doctrine + permissions)
2. `AGENT_PROFILE.md` (this file — index only, follow pointers on demand)
3. Any `PROJECT_LOG.md` handoff
4. **Only the service record points needed for the current mission** — do not load everything

Token economy rule stays: **minimum sufficient context**. The profile is an index precisely so no single mission has to open all eight points.

---

*Promptdivers — an operative is not their model, but what they carry into the drop.*
