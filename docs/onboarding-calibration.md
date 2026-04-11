# Onboarding calibration — question round

Use at the **start** of a multi-step engagement or when the deliverable type is unclear.  
Pairs with **structured-workflow** (Fase 1) and optionally **humanizer** for anything a human reads.

**Token rule:** Ask only what you do not already know from context. Cap at **one round** of follow-ups unless the human wants more.

---

## Core questions (from structured workflow — adapt wording)

1. **Outcome:** What does “done” look like? (Concrete end state.)  
2. **Scope:** What is explicitly **in** and **out**?  
3. **Stack / tools:** Languages, frameworks, formats, or “no code, advice only.”

---

## Human-facing output — add these two (humanizer bridge)

If the work produces **text other humans read** (README, `/explain`, emails, posts, docs, UI copy, audit summaries for stakeholders):

### 1. AI-likeness (how “default assistant” should it sound?)

Ask in plain language, map to a simple scale:

| Level | Meaning |
|-------|---------|
| **High** | Clear, structured, “assistant polish” — fine for internal specs |
| **Mid** | Professional but not obviously templated |
| **Low** | Human cadence; vary rhythm; avoid IA connectors — load **humanizer** |

Example prompt to the human:  
*“Should this read like a polished AI report (fine for tech), like a normal professional doc, or more personal / less ‘chatbot’?”*

### 2. Creativity

| Level | Meaning |
|-------|---------|
| **Low** | Single safe path, minimal alternatives |
| **Mid** | 2–3 options where it matters |
| **High** | Brainstorming, metaphors, multiple directions — still within scope lock |

Example:  
*“Do you want one straight recommendation, a few options with tradeoffs, or a wider creative pass?”*

---

## After answers

- If **low AI-likeness** or **high creativity** on prose → load **humanizer** skill and apply its Style Profile / termometer when delivering.  
- If **technical-only** (code, diffs, logs) → skip humanizer unless they ask for “friendlier” text later.

---

## Optional quick tags (tactical)

Human can reply with tags to skip the chat:

```text
VOICE: ai | pro | human
CREATIVE: low | mid | high
```

---

*Promptdivers — calibrate once, spread democracy with the right voice.*
