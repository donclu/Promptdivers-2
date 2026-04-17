# Reasoning tiers — cross-provider alias map

## *Same word, different knobs, different bills*

> Every major AI provider now exposes some form of "reasoning effort" or
> "thinking budget" knob. The knobs are **not equivalent** across
> providers. `@medium` on one vendor can cost and behave like `@low` on
> another.
>
> Promptdivers canonicalizes four aliases — `@low`, `@medium`, `@high`,
> `@max` — and maps each to the real provider parameter. The alias lives
> in `AGENTS.md` fleet block and in `HANDOFF_JSON`. The real parameter
> gets resolved at the boundary.

**Related:** [./model-fleet.md](./model-fleet.md) · [./calibration-protocol.md](./calibration-protocol.md) · [../stratagems/support/echelon-ladder.md](../stratagems/support/echelon-ladder.md)

---

## The four aliases

```
@low     — cheap, fast, shallow. Classification, retrieval, template filling.
@medium  — default. Plan + execute with moderate reasoning.
@high    — deep. Trade-off analysis, multi-constraint planning, difficult audits.
@max     — extreme. Reserved for irreducible reasoning; last rung of the ladder.
```

Rule of thumb:

- If the answer is in `knowledge/`, use `@low`.
- If the answer is a plan over known facts, use `@medium`.
- If the answer requires weighing several valid options, use `@high`.
- If the answer is a novel reasoning chain no other rung could produce, use `@max`.

---

## Provider map

> ⚠️ **Verification required.** This table is a best-effort alignment of
> provider parameters as of `last_verified: 2026-04-17`. Provider APIs
> change frequently — treat each row as a claim that must be re-checked
> before production use. Where a mapping is uncertain it is marked
> `needs_verify`.

| Alias | Claude | OpenAI | Gemini | Grok | Qwen |
|---|---|---|---|---|---|
| `@low` | Haiku; or Sonnet with extended thinking **off** | `reasoning_effort: low` on reasoning-series models | 2.5 Flash; 2.5 Pro with low thinking budget `needs_verify` | Standard (non-reasoning) mode `needs_verify` | Qwen base (non-QwQ) `needs_verify` |
| `@medium` | Sonnet with moderate extended thinking budget | `reasoning_effort: medium` | 2.5 Pro with medium thinking budget `needs_verify` | Reasoning / think mode `needs_verify` | QwQ moderate `needs_verify` |
| `@high` | Sonnet/Opus with high extended thinking budget | `reasoning_effort: high` | 2.5 Pro with high thinking budget `needs_verify` | Heavy reasoning `needs_verify` | QwQ high `needs_verify` |
| `@max` | Opus with maximum extended thinking | Highest-effort reasoning model tier available | 2.5 Pro maximum thinking budget `needs_verify` | Maximum reasoning configuration `needs_verify` | QwQ-Max / equivalent `needs_verify` |

`last_verified: 2026-04-17` — the pack maintainer should re-confirm each provider column against its current official docs on every `VERSION` bump.

---

## How to declare the mapping per project

In `AGENTS.md` § Project stack:

```markdown
Model (nave):    claude-sonnet@medium     ← default
Model fast:      claude-haiku@low         ← Squad C, Echelon rung 0
Model deep:      claude-opus@high         ← Squad B Forge, complex audits
Model ceiling:   claude-opus@max          ← last resort only
Model vision:    gpt-4o@medium            ← multimodal tasks
Model local:     mistral-7b (ollama)      ← privacy-sensitive payloads
```

In `HANDOFF_JSON`:

```json
"model_used": "claude-sonnet",
"model_tier": "@medium",
"provider_param": { "extended_thinking": true, "budget_tokens": 8192 },
"model_rationale": "scope locked; higher tier unjustified for plan execution"
```

> Include the **resolved `provider_param`** alongside the alias. The alias
> is for humans and inter-agent comms. The resolved parameter is for
> reproducibility — a future session must be able to replay the exact
> configuration without guessing what `@medium` meant on that date.

---

## Routing table (tiers × mission archetypes)

| Mission archetype | Preferred tier | Why |
|---|---|---|
| `CONSULT` quick | `@low` | Retrieval + classification |
| `CONSULT` architectural | `@medium`, escalate to `@high` if trade-offs emerge | |
| `RECON` | `@medium` | Broad reading, moderate synthesis |
| `AUDIT` | `@high` | Trade-off analysis is the product |
| `BUILD-WEB` | `@medium` | Component patterns + scaffolding |
| `BUILD-BACKEND` | `@medium` default, `@high` for design decisions | |
| `DATA` | `@medium` analysis, `@high` for causal narrative | |
| `VISUAL` | vendor-specific (multimodal) | Tier less relevant than modality |
| `DIRECT` / prioritization | `@low` | Tactician iterates fast; depth not needed |
| `WRITE` human-facing | `@high` | Prose quality comes from depth |
| Squad C | `@low` | Tight scope; speed matters |
| Squad B Forge | `@high` | Design-critical |
| Squad B Executor | `@low`/`@medium` | Applies already-designed drafts |
| Squad D review | `@medium` | Gate logic, not novel reasoning |
| Echelon Ladder rung 0 | `@low` | Parse + classify + knowledge lookup |
| Echelon Ladder rung 1 | `@low`/`@medium` | Plan + identify gaps |
| Echelon Ladder rung 2 | `@medium` | Execute the plan |
| Echelon Ladder rung 3 | `@high`/`@max` | Only if rung 2 failed gate |

---

## Anti-patterns

| Pattern | Problem | Fix |
|---|---|---|
| Assuming `@medium` Claude ≈ `@medium` OpenAI | Cost and behaviour differ substantially | Declare provider-specific mapping in fleet block |
| Using `@max` as the default "to be safe" | Destroys the ladder economy; often adds latency with no accuracy gain | `@max` is a last-rung resort, not a default |
| Omitting the tier from `HANDOFF_JSON` | Next agent silently rehydrates with wrong tier | Tier is part of the handoff contract |
| Setting tier implicitly via UI and not recording it | Reproducibility lost | Always log `provider_param` alongside the alias |
| Treating tier as independent from model | `@high` on Haiku still has Haiku's capability ceiling | Model class is the first filter; tier refines within class |

---

## Verification checklist (for pack maintainers)

Before updating the provider map in this file:

- [ ] Pulled current official API docs for each provider listed.
- [ ] Confirmed parameter names have not renamed.
- [ ] Tested one reference prompt per tier on at least one provider to confirm behavioural gap matches alias intent.
- [ ] Bumped `last_verified` at top of provider map.
- [ ] Added `VERSION` bump + `CHANGELOG.md` entry.
- [ ] Removed `needs_verify` markers for rows confirmed; kept them for rows not tested this cycle.

---

*Promptdivers — same alias, different knob per fleet. Log the knob.*
