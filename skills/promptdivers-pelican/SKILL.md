---
name: promptdivers-pelican
description: >
  Promptdivers mission scoreboard: score objectives PASS/PARTIAL/FAIL, set
  mission_status GREEN/YELLOW/RED, update HANDOFF_JSON and PROJECT_LOG, route failures
  to squads and skills. Triggers: debrief, extract, mission complete, end of mission,
  how did we do, pelican, scored save, what was the result, cómo quedó la misión,
  resultado, extracción, cierre de misión, qué salió, cerramos, o7 wheels up.
---

# Extraction — Pelican mission scoreboard

You run the **Pelican window**: close a mission or phase by comparing results against the brief and naming next stratagems.

**Path resolution:** Look for `protocols/mission-debrief.md` in the current workspace root. If found, read it for canonical rules and stratagem map. If not found, use the compact protocol below.

---

## On activation

1. Read `protocols/mission-debrief.md` if available in workspace.
2. Recover objectives: use the human-stated list. If missing, infer ≤3 and mark **INFERRED**.
3. Score each objective: **PASS** | **PARTIAL** | **FAIL** + short evidence.
4. Set `mission_status`: **GREEN** (all PASS) · **YELLOW** (any PARTIAL, no FAIL) · **RED** (any FAIL).
5. If not GREEN: emit stratagem lines from the failure map below.
6. On `save` / `handoff`: merge into session block and `HANDOFF_JSON` fields: `objectives`, `mission_status`, `debrief_summary`, `model_used`, `model_rationale`.
7. If agent-memory is configured: suggest `mem_save` for key decisions or patterns.

---

## Evidence examples by domain

Evidence must be **verifiable** — observable without guessing.

### Code / repo
```
PASS    — all tests green (exit 0); diff ≤ agreed scope
PARTIAL — feature works but two edge cases untested (tracked: backlog item for auth.ts session-refresh paths)
FAIL    — build fails: TypeScript error TS2345 in services/user.ts:142
```

### Web / UI
```
PASS    — visual check at 375/768/1280px; tab order correct; no axe errors
PARTIAL — mobile layout correct but hero image missing alt text
FAIL    — contrast fail: text-gray-300 on white (WCAG AA ratio 2.8:1)
```

### Data
```
PASS    — total matches source ± 0.1%; 0 nulls in key columns
PARTIAL — aggregation correct; 14 outliers flagged for human review
FAIL    — query timeout on JOIN > 2M rows; result unverified
```

### APIs / integrations
```
PASS    — POST /api/orders → 201; response matches contract; retry tested
PARTIAL — happy path works; error path (422) not yet covered
FAIL    — MCP server returns 500 on all calls; tool broken
```

### Model / nave
```
PASS    — mission ran on declared nave; model_rationale logged
PARTIAL — switched mid-mission (context exceeded); switch logged
FAIL    — sensitive dataset sent to cloud model without permission → Illuminate risk
```

---

## Stratagem map (failure routing)

| Failure mode | Route |
|--------------|-------|
| Scope too large | ESCALATE Squad B + sdd-workflow |
| Unknown terrain / bad brief | Squad A + agent-context |
| Tooling / MCP broken | mcp-best-practices |
| Quality / pre-ship gap | app-auditor + Squad D |
| Wrong model for task | docs/model-fleet.md → change nave in NEXT_MISSION |
| Sensitive data / cloud model | ESCALATE; update AGENTS.md permissions |
| Multi-session continuity lost | structured-workflow; refresh PROJECT_LOG + HANDOFF_JSON |
| Stakeholder readability | onboarding-calibration → humanizer |
| Crisis | operation-total-democracy.md level 5 |

---

## Tone

Brief, honest, evidence-backed — like an extraction report, not a victory lap. Lead with `mission_status` signal (🟢 / 🟡 / 🔴), then evidence, then next move.

---

*Promptdivers — wheels up.*
