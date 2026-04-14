# GALACTIC WAR MAP — Promptdivers (pack)

## *Managed democracy status across all sectors*

> This is a **dogfood** map for the Promptdivers pack itself (docs + templates + scripts).
> Update periodically with Squad D (THE SENTINEL) or the Democracy Officer protocol.

---

## Territory status

| Sector (module) | Status | Last op | Squad | Threats | Test coverage | Docs |
|-----------------|--------|---------|-------|---------|--------------|------|
| `installers/` (`install.sh`, `install.ps1`) | 🟡 CONTESTED | Squad D, 2026-04-14 | D | Cross-platform edge cases | — | 🟡 |
| `skills/` | 🟢 LIBERATED | Squad D, 2026-04-14 | D | None known | — | ✅ |
| `docs/` | 🟡 CONTESTED | Squad D, 2026-04-14 | D | Link drift risk | — | 🟡 |
| `missions/` | ⚫ UNEXPLORED | Never | — | Unknown | — | — |
| `protocols/` | 🟢 LIBERATED | Squad D, 2026-04-14 | D | None known | — | ✅ |
| `stratagems/` | 🟢 LIBERATED | Squad D, 2026-04-14 | D | None known | — | ✅ |
| `templates/` | 🟡 CONTESTED | Squad D, 2026-04-14 | D | Needs dogfood verification | — | 🟡 |

### Status legend

| Status | Meaning |
|--------|---------|
| 🟢 **LIBERATED** | Docs current, no known threats |
| 🟡 **CONTESTED** | Working but has known issues or missing checks |
| 🔴 **ENEMY HELD** | Broken, undocumented, or high-risk |
| ⚫ **UNEXPLORED** | Never been mapped by Squad A |

---

## Campaign score

```
Liberation Progress: ██████░░░░░░░░░░ 38%
Sectors liberated:   4 / 7
Sectors contested:   3 / 7
Enemy held:          0 / 7

Missions completed:  1
  PASS:              0
  PARTIAL:           1
  FAIL:              0

Super Earth Approval: 🟡 MODERATE
```

---

## Threat index

| Front | Active threats | Severity |
|-------|---------------|----------|
| **Terminids** (bugs) | Minor doc typos, missing dogfood files | LOW |
| **Automatons** (brittle automation) | Windows install path historically brittle | MEDIUM |
| **Illuminate** (ungoverned AI) | Risk of “invented canon names” in metaphor text | MEDIUM |

---

## Progression level

| Level | Criteria | Status |
|-------|----------|--------|
| 💀 **Cadet** | AGENTS.md exists, first Squad A completed | ✅ |
| ⚔️ **Helldiver** | All squads used at least once, PROJECT_LOG active | 🟡 |
| 🏅 **Skull Admiral** | Debrief scoring active, stratagems used, galactic map maintained | 🟡 |
| 🌟 **Super Earth Hero** | CI/CD integrated, multi-agent ops, zero Illuminate violations | ❌ |

---

## How to update this file

1. Run `Squad D → THE SENTINEL` for a health check.
2. Or run the **Democracy Officer** protocol (`protocols/democracy-officer.md`).
3. Update sectors based on: link health, doc coherence, installer behavior, and release hygiene.
4. Recalculate liberation progress: `liberated / total × 100`.
5. Update threat index from `PROJECT_LOG.md` DEBT items and open issues.

---

*Promptdivers — know your terrain, hold your ground. FOR DEMOCRACY.*

