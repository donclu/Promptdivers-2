# Prompt Forge — Support

## Code: `PFG`

> "The weapon is only as good as the blueprint. Forge the prompt, win the war."

---

## When to call

- You need to **design, write, or refine a prompt** for an AI system.
- Building prompts as deliverables: system prompts, user scripts, workflow templates, AGENTS.md sections.
- Testing and iterating on prompt effectiveness.
- Creating **prompt libraries** or **template packs** for a team or product.
- Debugging a prompt that isn't producing expected results.

---

## Inputs

1. **Purpose** — what should the prompt make the AI do?
2. **Target model** — which AI will run this prompt? (Claude, GPT, Gemini, local, unknown)
3. **Audience** — who will use the prompt? (developers, non-technical users, other agents)
4. **Constraints** — length limits, format requirements, tone, compliance needs.
5. **Success criteria** — how do you know the prompt is working?

---

## Steps

1. **Define the prompt specification:**
   ```markdown
   ## PROMPT SPEC
   Purpose: [What the prompt should achieve]
   Target model: [Which AI(s)]
   Format: [System prompt / user prompt / few-shot / chain-of-thought]
   Tone: [Technical / conversational / formal / Helldivers-themed]
   Length: [Short ≤500 chars / Medium ≤2000 / Long for system prompts]
   Success: [Observable outcome that proves it works]
   ```

2. **Research patterns:**
   - What prompting techniques fit? (CoT, few-shot, role-play, structured output)
   - Any existing prompts in the project to learn from?
   - Model-specific best practices (Claude prefers XML tags, GPT likes system messages)

3. **Draft the prompt:**
   - Clear role/identity statement
   - Specific task description with constraints
   - Input/output format specification
   - Edge cases and error handling instructions
   - Examples if using few-shot

4. **Test the prompt (at least 3 variations):**
   ```markdown
   ## TEST MATRIX
   | Test | Input | Expected Output | Actual Output | Pass? |
   |------|-------|-----------------|---------------|-------|
   | Happy path | [normal input] | [expected] | [actual] | ✅/❌ |
   | Edge case | [weird input] | [expected] | [actual] | ✅/❌ |
   | Adversarial | [tricky input] | [expected] | [actual] | ✅/❌ |
   ```

5. **Iterate based on failures:**
   - Identify why the prompt failed
   - Adjust: add constraints, examples, or clearer instructions
   - Re-test the failed cases
   - Document what didn't work (anti-patterns)

6. **Package the final prompt:**
   - Version it (v1, v2, etc.)
   - Document parameters and variables
   - Note model-specific adjustments
   - Include the test matrix as evidence

7. **Log:** `Stratagem: PFG — Prompt Forge for [purpose]. Version: [v]. Tests: [pass/total]`

---

## Outputs

- Final prompt text (versioned)
- Test matrix showing pass/fail across scenarios
- Documentation of parameters, variables, and model-specific notes
- Anti-patterns discovered during iteration

---

## Cooldown / limits

- No cooldown — use for every prompt design task.
- **Always test with at least 3 inputs** — a prompt that works on one example is not a prompt, it's a lucky guess.
- **Version your prompts.** Don't overwrite — keep v1, v2, v3.
- If the prompt is for production use (facing real users): **Mind Control protocol** — verify output quality with independent review.
- For prompt libraries: use Fortify (FRT) to document each prompt's purpose and parameters.

---

## Prompt design principles (Promptdivers doctrine)

1. **Specificity > cleverness.** Clear instructions beat elegant tricks.
2. **Constraints prevent drift.** Tell the AI what NOT to do, not just what to do.
3. **Examples > explanations.** Show, don't just tell.
4. **Test the edges.** If it only works on perfect input, it doesn't work.
5. **Document the failures.** What didn't work teaches more than what did.

---

*"Prompt Forge — every great Helldiver starts with a great stratagem blueprint."*
