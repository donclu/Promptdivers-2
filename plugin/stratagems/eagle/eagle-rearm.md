# Eagle Rearm — Eagle

## Code: `ERM`

> "Session cleanup. Reload for the next drop."

---

## When to call

- A session has gone long and the agent's context is cluttered.
- You want to **close cleanly** and set up the next session perfectly.
- The mission shifted significantly and you need a fresh start with proper handoff.

---

## Inputs

1. **Trigger** — end of session, mission pivot, or context overload.

---

## Steps

1. **Run Pelican debrief** — score objectives if any were set:
   - Each objective → PASS / PARTIAL / FAIL + evidence
   - Set `mission_status`: GREEN / YELLOW / RED
2. **Update `PROJECT_LOG.md`** with session summary:
   - What was done
   - Decisions made
   - DEBT discovered
3. **Produce `HANDOFF_JSON`** with all fields:
   ```json
   {
     "schema": "promptdivers-handoff/v1",
     "updated": "[timestamp]",
     "mission_last": "[A/B/C/D]",
     "objective": "[one line]",
     "mission_status": "[GREEN/YELLOW/RED]",
     "open_tasks": [],
     "debt": [],
     "next_recommended": {
       "squad": "[X]",
       "nave": "[model]",
       "reason": "[why]"
     }
   }
   ```
4. **Signal:**
   ```
   ✅ CLEAR — Eagle Rearm complete. SESSION CLOSED.
   Next: [recommendation]
   ```
5. **Log:** `Stratagem: ERM — session closed. Status: [GREEN/YELLOW/RED]`.

---

## Outputs

- PROJECT_LOG updated with session entry.
- HANDOFF_JSON refreshed.
- Clean handoff for next session or agent.

---

## Cooldown / limits

- Call **once per session** at the end.
- If the human says `save` or `debrief`, this stratagem fires automatically.
- Do not skip the debrief — an unlogged session is lost territory.

---

*"Eagle Rearm — a clean extraction is a successful mission."*
