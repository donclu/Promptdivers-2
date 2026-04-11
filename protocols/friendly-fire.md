# Friendly fire protocol

> "Super Earth regrets every lost Helldiver — especially the ones hit by their own squad."

---

## What is friendly fire

In Helldivers, you can (and will) hit your squadmates. In agent work, **friendly fire** happens when:

- An agent **reverts or overwrites** changes another agent just made.
- Two agents edit the **same file** without coordination, causing merge conflicts.
- A "fix" in one area **breaks** something that was just confirmed working by another role.
- An Autocannon (lint/format) reformats a file that THE FORGE is still drafting.

This is **not** a defect in the code — it's a coordination failure between agents or roles.

---

## Detection signals

| Signal | Situation |
|--------|-----------|
| `🔴 RED — Friendly fire: [file] was modified by both [ROLE_A] and [ROLE_B]` | Direct conflict |
| `🟡 YELLOW — Regression: [test] was PASS after BATCH 1, now FAIL after BATCH 2` | Indirect hit |
| `⬆️ STEP UP — My fix in [file] broke [other_file] that AUDITOR just approved` | Collateral |

---

## Prevention rules

1. **DO NOT TOUCH lists are mandatory.** Every role activation includes files that others own.
2. **One writer per file at a time.** If two roles need the same file, sequence them — never parallel.
3. **Squad B batches respect boundaries.** Each batch owns its files exclusively.
4. **Autocannon runs after, not during.** Don't format files while someone is still editing them.
5. **Reinforce protocol** (see `stratagems/support/reinforce.md`) requires defining conflict zones upfront.

---

## When it happens anyway

### Step 1 — CEASEFIRE

```
⏸️ HOLD — Friendly fire detected.
File: [path]
Conflict: [ROLE_A] edited lines [X-Y], [ROLE_B] edited lines [Z-W]
Stopping all edits until resolved.
```

### Step 2 — Assess damage

- What was the **last known good state** of the file?
- Which edit is correct? (Check against SPEC, DESIGN, or TASKS.)
- Are tests passing? If yes, the conflict may be cosmetic.

### Step 3 — Resolve

| Scenario | Resolution |
|----------|------------|
| Both edits are valid but conflict | Merge manually — take the best of both |
| One edit is wrong | Revert the wrong edit; keep the correct one |
| Both edits are wrong | Revert to last AUDITOR-approved state |
| Unclear which is right | `⏸️ HOLD` + `SOS Beacon` to human |

### Step 4 — Log and prevent recurrence

```markdown
### Friendly fire incident
- File: [path]
- Agents: [ROLE_A] vs [ROLE_B]
- Cause: [missing DO_NOT_TOUCH / parallel editing / sequential dependency]
- Resolution: [what was done]
- Prevention: [what changes to avoid next time]
```

---

## Anti-patterns

- "Just rewrite the whole file" after a friendly fire — this usually causes **more** damage.
- Blaming the model for coordination that the **brief** should have prevented.
- Not logging the incident — unlogged friendly fire is Illuminate territory.

---

*Promptdivers — watch your fire, Helldiver.*
