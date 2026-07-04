# AGENT_PROFILE.md — operative service record

> Copy from pack template. Index only — detail lives in referenced directories.
> Schema: see pack `AGENT_PROFILE.md` or vendored `.framework-promptdivers2/AGENT_PROFILE.md`.

**Related:** `AGENTS.md` · `knowledge/` · `experience/` · `protocols/promotion.md`

---

## Operating limits (pillar 7)

```yaml
token_budget_per_session:   # e.g. 150000
cost_cap_usd_per_session:   # e.g. 5.00
privacy_tier:               # pack-default | local-only | cloud-ok
tenure_level:               # rookie | veteran | elite | legend
max_echelon_rung:           # 0-3 per protocols/promotion.md
escalation_budget:          # rung climbs allowed per session
requires_approval_for:      # e.g. [commit, deploy, RED_flag]
```

## Pointers

```yaml
knowledge: knowledge/
experience: experience/
skills: skills/  # or global IDE skills path
doctrine: AGENTS.md
feedback_ledger: experience/integrity/feedback-ledger.yaml
next_mission: NEXT_MISSION.md
```

---

*Promptdivers — structured scaffolding beats raw model power.*
