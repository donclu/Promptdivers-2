# GALACTIC WAR MAP — [project name]

## *Managed democracy status across all sectors*

> Update this file periodically with Squad D (THE SENTINEL) or the Democracy Officer protocol.

---

## Territory status

| Sector (module) | Status | Last op | Squad | Threats | Test coverage | Docs |
|-----------------|--------|---------|-------|---------|--------------|------|
| `src/api/` | 🟢 LIBERATED | Squad C, YYYY-MM-DD | C | None | 87% | ✅ |
| `src/auth/` | 🟡 CONTESTED | Squad B, YYYY-MM-DD | B | DEBT-001: session refresh | 42% | 🟡 |
| `src/legacy/` | 🔴 ENEMY HELD | Never | — | Terminids: 14 bugs | 0% | ❌ |
| `src/utils/` | 🟢 LIBERATED | Squad C, YYYY-MM-DD | C | None | 91% | ✅ |
| `tests/` | 🟡 CONTESTED | Squad D, YYYY-MM-DD | D | Flaky: 3 intermittent | — | 🟡 |

### Status legend

| Status | Meaning |
|--------|---------|
| 🟢 **LIBERATED** | Tests pass, docs current, no known threats |
| 🟡 **CONTESTED** | Working but has known issues or missing coverage |
| 🔴 **ENEMY HELD** | Untouched, untested, undocumented, or actively broken |
| ⚫ **UNEXPLORED** | Never been mapped by Squad A |

---

## Campaign score

```
Liberation Progress: ██████████░░░░░░ 63%
Sectors liberated:   4 / 8
Sectors contested:   2 / 8
Enemy held:          2 / 8

Missions completed:  12
  PASS:              9 (75%)
  PARTIAL:           2 (17%)
  FAIL:              1 (8%)

Super Earth Approval: 🟡 MODERATE
```

---

## Threat index

| Front | Active threats | Severity |
|-------|---------------|----------|
| **Terminids** (bugs) | 14 open bugs, 3 flaky tests | MEDIUM |
| **Automatons** (brittle automation) | CI has 1 undocumented job, 2 manual deploy steps | LOW |
| **Illuminate** (ungoverned AI) | Agent sessions not always debriefed; last 2 sessions have no HANDOFF_JSON | HIGH |

---

## Progression level

| Level | Criteria | Status |
|-------|----------|--------|
| 💀 **Cadet** | AGENTS.md exists, first Squad A completed | ✅ |
| ⚔️ **Helldiver** | All squads used at least once, PROJECT_LOG active | 🟡 |
| 🏅 **Skull Admiral** | Debrief scoring active, stratagems used, galactic map maintained | ❌ |
| 🌟 **Super Earth Hero** | CI/CD integrated, multi-agent ops, zero Illuminate violations | ❌ |

---

## How to update this file

1. Run `Squad D → THE SENTINEL` for a health check.
2. Or run the **Democracy Officer** protocol (`protocols/democracy-officer.md`).
3. Update sectors based on: test coverage, open bugs, doc status, last mission.
4. Recalculate liberation progress: `liberated / total × 100`.
5. Update threat index from PROJECT_LOG DEBT items and open issues.

---

*Promptdivers — know your terrain, hold your ground. FOR DEMOCRACY.*
