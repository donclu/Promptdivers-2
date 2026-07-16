# Mind control protocol — Illuminate inside threat

> "The most dangerous enemy is the one wearing your uniform."

---

## What is mind control

In the *Helldivers*-inspired fiction of this framework, “mind control” is a metaphor: a squadmate appears friendly but acts for the enemy. In agent work, **mind control** happens when:

- The agent produces output that **looks correct** but is **logically wrong** — confident hallucination.
- Generated code **compiles and passes tests** but does the **wrong thing** (silent logic errors).
- Docs or explanations **contradict the codebase** while sounding authoritative.
- Tests pass because they **mock too aggressively**, not because the code is correct.
- The agent **confidently answers** a question with fabricated information.

This is the core **Illuminate threat** — the danger isn't obvious breakage (that's Terminids), it's **plausible-looking wrongness**.

---

## Detection signals

### High suspicion triggers

| Indicator | Why it's suspicious |
|-----------|-------------------|
| Agent says "this will work" without testing | Confidence without evidence |
| Code works on first try for a complex problem | Possible oversimplification |
| Tests all pass but cover only happy path | Mocking may be hiding real failures |
| Explanation doesn't match what the code does | Hallucinated understanding |
| Agent invents an API/method/flag that doesn't exist | Confabulation |
| "I've verified" without showing the verification | Unsubstantiated claim |

### Low suspicion (probably fine)

| Indicator | Why it's likely OK |
|-----------|-------------------|
| Agent shows the test output | Evidence-backed |
| Code matches an existing pattern in the repo | Pattern following, not inventing |
| Agent says "I'm not sure about X" | Honesty = not mind-controlled |
| Change is small and obvious | Low complexity = low hallucination risk |

---

## Verification tiers

Not all output needs the same level of scrutiny. Match verification to risk:

### Tier 1 — Trust but verify (low risk)
- Small, obvious changes
- Pattern-following code
- **Check:** Quick read of the diff. Does it look right?

### Tier 2 — Verify then trust (medium risk)
- New logic, complex conditions, math
- API integrations, auth flows, data transformations
- **Check:** Run the code. Check edge cases. Read assertions in tests carefully — are they testing the right thing?

### Tier 3 — Independent verification (high risk)
- Security-critical code (auth, crypto, permissions)
- Financial calculations, data integrity
- Claims about external systems or APIs
- **Check:** Second agent or human reviews. Source check (does that API actually exist? does that flag actually work?). Consider **THE AUDITOR** mandatory.

---

## Response protocol

### When you suspect mind control

1. **`📍 MARK — Possible mind control`** — flag the suspicious output.
2. **Do not use the output** until verified.
3. **Verify against reality:**
   - Does the code actually compile and run? (Don't trust "it should work")
   - Do the tests actually test what they claim? Read the assertions.
   - Does the explanation match the code? Compare line by line.
   - Does the cited API/method/flag actually exist? Check the docs.
4. **If confirmed false:**
   ```
   🚨 ALERT — Mind control confirmed
   - Output: [what was wrong]
   - Reality: [what's actually true]
   - Affected: [files/decisions that used the bad output]
   - Rollback: [what needs to be reverted]
   ```
5. **Log the incident** — mind control incidents are Illuminate intelligence:
   ```markdown
   ### Illuminate incident: mind control
   - Symptom: [what looked right but wasn't]
   - Root cause: [hallucination / outdated training / bad assumption]
   - Impact: [what was affected]
   - Detection: [how it was caught]
   ```

---

## Prevention rules

1. **Evidence over assertion.** Never accept "it works" without seeing the test output.
2. **Run the code.** If the agent says "this function returns X," call the function.
3. **Check external claims.** If the agent cites a specific API, library version, or documentation, verify it.
4. **Auditor on high-risk work.** THE AUDITOR exists for this reason.
5. **Label uncertainty.** Agents should say "I believe" or "I'm not certain" rather than stating uncertain things as fact.
6. **Two-agent rule for security.** Security-critical code should never be written and reviewed by the same agent/session.

---

## This is not "AI bad"

Mind control is a **risk pattern**, not a verdict. The same agent that hallucinates an API can also write perfectly correct code in the next message. The protocol isn't about distrust — it's about **proportional verification**, exactly like the Illuminate threat in the game: real, manageable, and best handled with awareness rather than paranoia.

---

*Promptdivers — verify before you trust, even your own squad.*
