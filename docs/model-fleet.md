# Model fleet — ship manifest

## *Every stratagem needs the right drop pod*

> Super Earth does not send a light scout ship for an orbital bombardment mission.  
> Neither should you send a 4-billion-parameter local model to architect a multi-service migration.

This document is the **fleet registry**: what each model family can do, when to use it, and how to declare it in your project so agents and humans make consistent decisions.

**Related:** [MULTI_AGENT_SETUP.md](MULTI_AGENT_SETUP.md) · [super-earth-operating-model.md](super-earth-operating-model.md) · [../QUICK_REFERENCE.md](../QUICK_REFERENCE.md)

---

## Model-selection principle

The **same mission** can run on different models. The right choice depends on:

1. **Task complexity** — context span, multi-step reasoning, code quality.  
2. **Modality** — does the task involve images, audio, or documents?  
3. **Speed / cost** — fast feedback loop vs. deep work.  
4. **Privacy / locality** — can the payload leave the machine?  
5. **Tool access** — does the IDE/platform support this model with Skills, MCP, agents?

**Declare in `AGENTS.md` stack block:**

```markdown
Model (nave):   claude-sonnet        ← default (YAML key: model_preferred)
Model fallback: fast-local           ← used when offline or cost-constrained
```

---

## Fleet registry

### Class A — Heavy cruisers (deep reasoning, large context)

| Ship (model family) | Strengths | Weak spots | Best missions |
|---------------------|-----------|------------|---------------|
| **Claude Sonnet / Opus** | Long context, strong reasoning, code, docs, nuance; follows complex briefs | Slower; cost on large volumes | RECON, BUILD-BACKEND, AUDIT, multi-file refactor (Squad B), WRITE |
| **GPT-4o** | Broad capability, strong function-calling, vision (images + docs) | Can drift on very long instructions | BUILD-WEB, DATA, VISUAL, multi-tool agent pipelines |
| **Gemini 1.5 / 2.x Pro** | Very long context (1M+ tokens), native multimodal (video, audio, docs) | Less established for pure code | AUDIT of entire repos, DATA on large datasets, VISUAL with video |
| **Grok-3 / xAI** | Real-time web data, quick iterative answers | Variable reliability on deep reasoning | CONSULT, RECON with live data, DIRECT |

### Class B — Frigates (fast, efficient, good for iteration)

| Ship | Strengths | Best for |
|------|-----------|---------|
| **Claude Haiku / Sonnet-mini** | Very fast, low cost, good for structured tasks | Squad C surgical fixes, quick CONSULT, first-pass recon, ping-first loops |
| **GPT-4o-mini** | Cheap, fast, still capable | First-pass audits, structured extraction, short iteration loops |
| **Gemini Flash** | Speed + multimodal at low cost | Quick image checks, structured data extraction, rapid SITREP generation |

### Class C — Local ships (offline, private, specialized)

| Ship | Strengths | Limits | Best for |
|------|-----------|--------|---------|
| **Mistral / Mixtral (local)** | Privacy, offline, fast on CPU/GPU | Smaller context, less capable at complex reasoning | Sensitive data, air-gapped repos, local automation |
| **Llama 3.x / Qwen (local)** | Open weights, customizable | Depends on local hardware | Domain-specific fine-tunes, on-prem enterprise |
| **Phi-4 / Gemma (local)** | Very fast, small footprint | Limited context, simpler reasoning | Embedded tooling, CI bots, local lint/format agents |
| **Code-specific (Codestral, DeepSeek-Coder)** | High code precision | Not general purpose | Pure code generation, completions, Squad B Forge work |

---

## Mission → model routing (quick chart)

| Mission archetype | Preferred class | Notes |
|-------------------|-----------------|-------|
| **CONSULT** | A or B | B if quick; A if architectural |
| **RECON** | A | Needs broad context reading |
| **AUDIT** | A (long context) | Gemini Pro on full-repo if 1M tokens needed |
| **BUILD-WEB** | A or B | GPT-4o for vision/component; Sonnet for complex components |
| **BUILD-BACKEND** | A | Claude/GPT-4o for reasoning + SDD |
| **DATA** | A or Gemini | Gemini for doc/spreadsheet ingestion; Claude for analysis narrative |
| **VISUAL** | A multimodal | GPT-4o vision or Gemini for image analysis; any for generation prompts |
| **DIRECT** | B (fast) | THE TACTICIAN needs quick iteration, not depth |
| **WRITE** | A | Claude preferred for nuanced prose; humanizer still applies |
| **Squad C (surgical)** | B | Speed matters; scope is tight |
| **Squad B (artillery)** | A for Forge; B for Executor | Forge needs depth; Executor needs iteration |
| **Squad D (defense / PR)** | B | Fast review loops |

---

## Declaring the fleet in your project

### In `AGENTS.md` (stack block)

```markdown
## Project stack

...
Model (nave): claude-sonnet        ← default for this project
Model fallback: gpt-4o-mini        ← when cost/speed constraint applies
Model vision: gpt-4o or gemini     ← for image / multimodal tasks
Model local: mistral-7b (ollama)   ← for private/offline tasks
```

### In `NEXT_MISSION.md` / template

Add:
```markdown
- **Nave (model):** claude-sonnet | gpt-4o-mini | gemini-pro | local | AUTO
- **Why this ship:** [one line — cost, context, multimodal, privacy]
```

### In `HANDOFF_JSON`

```json
"model_used": "claude-sonnet",
"model_rationale": "long context needed for full repo recon"
```

---

## Swapping ships mid-mission

You can switch models between phases without breaking doctrine:

1. **Phase closes** (debrief / Pelican).  
2. Next `NEXT_MISSION` declares new model.  
3. `HANDOFF_JSON` records the switch and rationale.

If the model switch is forced by a tool limitation (e.g., MCP not available in that host), log it as a **CONSTRAINT** in the session block.

---

## Illuminate risk: ungoverned model selection

Using a model without declaring it → silent context loss on handoff, billing surprises, privacy violations. Follow the Illuminate front:

- **Always declare** `model_used` in HANDOFF_JSON when it matters.  
- **Never** route sensitive data to a cloud model without explicit permission in `AGENTS.md` permissions block.  
- **Log** forced model changes as decisions, not silent edits.

---

## Anti-patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| Always using the heaviest model | Cost and latency; kills iteration speed | Match class to mission phase |
| Switching models silently | Breaks handoff; next agent assumes wrong context | Log in session block + HANDOFF_JSON |
| Assuming all models support MCP/tools | Many local and some cloud models do not | Check capabilities before assigning tool-heavy roles |
| Using a code-only model for WRITE | Poor prose quality | Route WRITE to A-class general model + humanizer |
| Using cloud model for classified data | Privacy / compliance breach | Always C-class local for sensitive payloads |

---

*Promptdivers — the right ship for the right drop zone. FOR DEMOCRACY.*
