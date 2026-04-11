# Mission debrief — Pelican window

## *Extract, score, redeploy stratagems*

When a mission (session or phase) ends, **close the loop**: compare outcomes to the **brief**, record evidence, and route failures to **existing** squads and ecosystem skills—no parallel command system.

**Related:** [inter-agent-protocol.md](inter-agent-protocol.md) · [tactical-signals.md](tactical-signals.md) · [../QUICK_REFERENCE.md](../QUICK_REFERENCE.md) · [../templates/project-log.template.md](../templates/project-log.template.md)

---

## When to run

- Human says **`debrief`**, **`extract`**, or **`save`** after objectives were stated.
- End of a squad run, batch, or Operation Total Democracy slice.
- Before **`handoff`** when `objectives` were tracked for this stretch.

---

## 1. Mission brief (start of work)

Set **1–5 verifiable objectives**. Each item needs a **done criterion** a reviewer (human or agent) can check without guessing.

```text
OBJECTIVE: [short label]
  DONE WHEN: [observable condition — test passes, file exists, PR merged, human confirmed, etc.]
```

Also record: squad (A–D), `do_not_touch` paths, and link to `AGENTS.md` / stack if relevant.

If the human never formalized objectives, infer **at most 3** from chat and label them **INFERRED** so the debrief stays honest.

---

## 2. Per-objective score

For each objective:

| Result | Meaning |
|--------|---------|
| **PASS** | Done criterion met; evidence attached. |
| **PARTIAL** | Some progress; criterion not fully met; say what remains. |
| **FAIL** | Criterion not met; no acceptable workaround yet. |

**Evidence** (pick what fits): file path + summary, test output line, commit SHA, screenshot note, log excerpt.

---

## 3. Mission status (aggregate)

Align with risk / ping language in `QUICK_REFERENCE.md`:

| `mission_status` | Condition |
|------------------|-----------|
| **GREEN** | All objectives PASS. |
| **YELLOW** | At least one PARTIAL; none FAIL. |
| **RED** | One or more FAIL. |

Optional **score** (for gamified crews): `pass_count` / `objective_count` as a simple fraction—do not pretend precision without criteria.

---

## 4. Failure and PARTIAL → stratagem map

Use **existing** playbooks and skills. Pick the **primary** failure mode per objective.

| Failure mode | Redeploy |
|--------------|----------|
| Scope too large; needs design / many files | **ESCALATE** toward Squad B; load **sdd-workflow**; Forge ≠ Executor. |
| Unknown terrain; bad or missing brief | Squad A (THE SCOUT / THE AUTHENTIC); **agent-context** if `AGENTS.md` is wrong or missing. |
| Tooling / MCP / permissions | **mcp-best-practices**; update `AGENTS.md` permissions block. |
| Quality, security, release gate | **app-auditor**; Squad D (THE AUDITOR / THE SENTINEL). |
| Multi-session continuity | **structured-workflow**; refresh `PROJECT_LOG` + `HANDOFF_JSON`. |
| Stakeholder voice / readability | **onboarding-calibration** → **humanizer** (after calibration). |
| Pattern worth remembering | **agent-memory** `mem_save` (if configured) + SCRIBE note in log. |
| Production crisis or human orders max response | **operation-total-democracy.md** / escalation level 5. |

Emit a **one-line SITREP** per tactical-signals doctrine: marker + English evidence.

---

## 5. Output shape

1. **Table:** objective → PASS | PARTIAL | FAIL → evidence (short).  
2. **mission_status:** GREEN | YELLOW | RED.  
3. **Stratagem line:** if not GREEN, list next squad/skill per objective that failed or partial.  
4. **Sub-missions:** if secondary or tertiary missions surfaced during the run, list them in `missions_queued` inside `HANDOFF_JSON` before closing the handoff. Do **not** close objectives that belong to a sub-mission not yet started. Each queued item needs: `priority`, `squad`, `nave`, `objective`, `spawned_by`.  
5. **`save` / `handoff`:** merge into session notes and `HANDOFF_JSON` per [../templates/project-log.template.md](../templates/project-log.template.md).

---

## 6. Anti-patterns

- Scoring without criteria invented after the fact (“we basically won”).  
- FAIL with no evidence and no stratagem route.  
- Starting a **new** methodology instead of the map above.  
- Duplicating the full brief inside every debrief—**link** the session block or `objectives` in JSON.

---

*Promptdivers — the Pelican only lands when the board is honest.*
