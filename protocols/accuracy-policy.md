# Accuracy policy — Helldivers metaphor (Promptdivers)

Promptdivers uses *Helldivers*-style language as a **metaphor layer**. This policy keeps that metaphor fun **without** turning into invented lore, invented mechanics, or evidence-free rules.

**Related:** `skills/promptdivers-ministry-of-truth/SKILL.md` · `AGENTS.md` · `protocols/pack-self-audit.md`

---

## Core rule

If a statement could be read as a factual claim about the game (mechanics, lore, numbers, unlock rules), **do not state it as fact** in this pack.

Instead, write it as:

- “In the **Helldivers-inspired metaphor** of this framework…” and then state the **Promptdivers doctrine** (the actual rule for agent work).

---

## Allowed (safe) uses

- Naming and vibe: squads, stratagems, “drop”, “extract”, “fronts”, “pings”.
- High-level analogies that do not depend on game truth:
  - “Pings before paragraphs” as a comms design principle.
  - “Friendly fire” as a coordination failure in multi-agent work.
- Trademark/attribution lines (see `README.md` / `README-ES.md`).

---

## Disallowed (unsafe) uses

- Any “this is how Helldivers works” claim that implies mechanics or canon:
  - cooldowns, damage, faction behavior, unlock progression, “always/never” rules framed as game truth
- Numbers presented as if authoritative (“X seconds”, “Y damage”, “Z tiers”) unless they’re explicitly marked as metaphor-only and not normative.

---

## Evidence discipline (pack-wide)

Promptdivers is evidence-first. Therefore:

- **Rules** must point to a **Promptdivers file** (protocol/squad/stratagem/skill), not to game “canon”.
- **Verification** claims require an audit trail:
  - path + brief summary, or
  - command/output excerpt, or
  - reproducible steps.

If the pack doesn’t contain the referenced thing, mark it **UNVERIFIED** and add a follow-up (or remove it).

---

## Rewrite pattern (recommended)

Before:

> “In Helldivers 2, X happens, so we do Y…”

After:

> “In the Helldivers-inspired metaphor of this framework, we treat X as a reminder to do Y. Promptdivers rule: [link to protocol / squad / stratagem].”

---

## Enforcement

- During pack edits: include this in self-audit (`protocols/pack-self-audit.md`).
- When drift is detected: load the “Ministry of Truth” skill and run a claim audit:
  - `skills/promptdivers-ministry-of-truth/SKILL.md`

---

*Promptdivers — fun tone, strict truth.*

