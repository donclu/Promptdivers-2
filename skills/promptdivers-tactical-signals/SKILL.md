---
name: promptdivers-tactical-signals
description: >
  Promptdivers signal grid: ping-first communication for mixed-language teams and
  AI agents. Covers all domains — code, UI, data, APIs, model switches. Triggers:
  o7, GREEN, RED, HOLD, GO, MARK, ALERT, tactical signals, pings, señales, semáforo,
  qué significa ese emoji, cómo señalizar, status rápido, ping, situación, señal.
---

# Signal grid — tactical pings across all theaters

**Path resolution:** Look for `protocols/tactical-signals.md` in the current workspace root. If found, read it for the full signal table and examples. If not found, use the compact grid below.

---

## Core doctrine

1. **Lead with one signal marker**, then English detail + path or evidence.
2. Short signals travel farther than long prose — especially across languages.
3. Formal `PROJECT_LOG` entries stay prose; signals are for chat and session flow.
4. `o7` = acknowledged; use when accepting an order or handoff.

---

## Signal grid

| Signal | Meaning |
|--------|---------|
| 🟢 GREEN | Clear / go / all good |
| 🟡 YELLOW | Caution / flaky / needs attention |
| 🔴 RED | Blocked / failing / tests down |
| 🚨 ALERT | Critical — prod / security / data risk |
| 🎯 ON TARGET | Scope locked to this |
| 📍 MARK | Look here: path, line, or finding |
| ⏸️ HOLD | Pause — waiting on something |
| 🚀 GO | Authorized — proceed |
| ✅ CLEAR | Done / pass / verified |
| ❌ NO GO | Reject / do not proceed |
| ⬆️ STEP UP | Escalate to higher squad |
| 📋 SITREP | Status snapshot |
| o7 | Acknowledged |

---

## Signal examples by domain

**Format: marker + one-line English + path or metric**

### Code / repo
```
🟢 GREEN — tests pass, CI green (exit 0), ready to merge
🔴 RED — build failed: src/auth/login.ts:42 TypeScript error TS2345
🎯 ON TARGET — scope locked to: src/components/Button.tsx
📍 MARK — root cause at: services/user.ts:187
⬆️ STEP UP — exceeds ~5 files → ESCALATE to Squad B
```

### Web / UI
```
🟡 YELLOW — layout regression on mobile <360px: components/Card.tsx
🔴 RED — a11y: 3 inputs missing labels (axe report attached)
📍 MARK — contrast fail: text-gray-400 on white in HeroSection
✅ CLEAR — visual check passed at 375, 768, 1280px
```

### Data
```
📍 MARK — dataset: data/sales-q1.csv, 12k rows, 3 nulls in revenue column
🟡 YELLOW — outlier: row 4423 revenue = -$98k, flagging for review
🔴 RED — query failed: timeout on JOIN across 2M rows
✅ CLEAR — aggregation verified: $4.2M ± 0.1% vs source
```

### APIs / integrations
```
📍 MARK — POST /api/orders → 422 Unprocessable: missing field "sku"
🔴 RED — MCP connection failed: server returns 500 → load mcp-best-practices
🟡 YELLOW — rate limit hit (429), adding retry with backoff
✅ CLEAR — endpoint tested: 200, response matches contract
```

### Model / nave switches
```
📋 SITREP — switching nave: claude-sonnet → gemini-pro (repo > 200k tokens)
⏸️ HOLD — model does not support MCP tools; routing to local mistral
✅ CLEAR — nave switch logged in HANDOFF_JSON model_rationale
🚨 ALERT — sensitive data sent to cloud model — verify AGENTS.md permissions
```

---

*Promptdivers — o7*
