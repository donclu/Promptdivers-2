# Tactical signals — Helldivers-style field comms

## *Pings before paragraphs*

In the Helldivers-inspired **metaphor** of this framework, squads coordinate with short pings: emotes, single words, and shared markers. Everyone understands **“reinforce here”** faster than a speech.

Promptdivers uses the same idea for **humans ↔ agents ↔ subagents**:

- **Signals first** — one line (often with an emoji) states situation + intent.  
- **English remains canonical** for anything that lives in the repo (`AGENTS.md`, `PROJECT_LOG`, commits, specs).  
- **Long form is “voice chat”** — use when nuance, negotiation, or teaching is needed (like opening mic for a callout).

This keeps sessions readable for mixed-language teams and reduces tokens when the signal already constrains the answer.

---

## Doctrine

1. **Mark the situation before explaining** — agent (or human) opens with a signal line.  
2. **Same signal = same meaning everywhere** — do not invent one-off emoji slang per session; use the tables below.  
3. **Repo artifacts stay precise** — after the ping, still write paths, errors, and decisions in clear English in logs.  
4. **Ambiguity → one clarifying question** — if a ping is unclear, ask once; do not guess.  
5. **TOTAL DEMOCRACY** and other **keywords** are verbal stratagems — they override casual tone.

---

## Situation markers (lead line)

Use at the **start** of a message or SITREP.

| Signal | Meaning | Typical next step |
|--------|---------|-------------------|
| 🟢 **GREEN** | Clear / healthy / on track | Continue plan |
| 🟡 **YELLOW** | Caution / debt / flaky but moving | Note + optional scope trim |
| 🔴 **RED** | Blocked or failing tests / build | Stop batch; diagnose |
| 🚨 **ALERT** | Production, security, data loss risk | Escalate; see `escalation.md` |
| 🎯 **ON TARGET** | Scope understood; objective locked | Execute agreed files only |
| 📍 **MARK** | “Look here” — pointer to file:line or path | Open/read that location |
| ⏸️ **HOLD** | Pause; do not apply more changes | Wait for human or SITREP |
| 🚀 **GO** | Authorization to proceed on agreed scope | Execute |
| 🔧 **WORKING** | Fix or implementation in progress | Short update soon |
| ✅ **CLEAR** | Done / approved / tests pass | Log + next step |
| ❌ **NO GO** | Rejected / unsafe / wrong approach | Explain in one line + evidence |
| ⬆️ **STEP UP** | Needs heavier squad or human decision | Emit `ESCALATE` with evidence |
| 📋 **SITREP** | Status snapshot | Bullet facts only |
| 🧭 **LOST** | Missing context; cannot proceed safely | Ask 1 question or read `AGENTS.md` |

---

## Emotes / compact reactions (optional)

Same role as in-game quick emotes: **acknowledgement** without a paragraph.

| Emote | Use |
|-------|-----|
| **o7** | Acknowledged / will comply |
| **o7 o7** | Relayed to next role / handoff noted |
| **GLHF** | Session start (good luck) — optional, keep rare |
| **F** | Failed attempt / tests red — follow with 🔴 or evidence line |
| **W** | Win — small victory (e.g. tests green on one batch) |

Do not overuse meme density in formal logs; **PROJECT_LOG** should stay professional even if chat uses emotes.

---

## Map signals to protocol types

| Signal (lead) | Maps to `TYPE` |
|---------------|----------------|
| 📋 SITREP / 🟢🟡🔴🚨 states | `SITREP` |
| 📍 MARK + facts | `INTEL` |
| 🚀 GO + task | `REQUEST` |
| ✅ CLEAR / ❌ NO GO | `CONFIRM` |
| ⬆️ STEP UP / 🚨 ALERT | `ESCALATE` |
| ⏸️ HOLD / abort keyword | `ABORT` |

Full grammar: [inter-agent-protocol.md](inter-agent-protocol.md).

---

## One-line examples (human → agent)

```text
🟢 GREEN — continue TASKS.md item 3
🔴 RED — npm test fails on auth.test.ts (paste trace below)
📍 MARK — src/api/users.ts:88 — wrong guard
⏸️ HOLD — do not merge; checking legal
🚀 GO — Squad C, files listed in last message
⬆️ STEP UP — touches 12 files now, need Squad B
```

---

## One-line examples (agent → human)

```text
o7 🎯 ON TARGET — will edit only routes/login.ts and lib/session.ts
📋 SITREP — 🟡 YELLOW — 2 tests flaky, not related to this change
✅ CLEAR — batch 1 applied, typecheck clean
⬆️ STEP UP | ESCALATE — schema drift; see migration error in log
```

---

## When to skip signals

- **Legal, compliance, or security review** — full sentences on record.  
- **First-time onboarding** — explain once; then adopt signals.  
- **Public GitHub issues / customer-facing text** — no emoji protocol unless the project already uses it.

---

## Why this matches the game (metaphor)

| In Helldivers (metaphor) | In Promptdivers |
|---------------|-----------------|
| Ping wheel / short comms | Situation markers + keywords |
| Voice for complex callouts | Long-form chat or doc when needed |
| Shared objective on HUD | `AGENTS.md` + `QUICK_REFERENCE.md` |
| Reinforce / stratagem words | `escalate`, `TOTAL DEMOCRACY`, squad names |

Different human languages in the room **still share** the same ping meanings—same here: **English docs + universal signals**.

---

*Promptdivers — FOR DEMOCRACY. o7*
