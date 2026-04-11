# Automaton Assault — Offensive

## Code: `ATA`

> "They build their walls of scripts and cron jobs. We tear them down with proper automation."

---

## When to call

- An existing **script, pipeline, or automation** is brittle, undocumented, or failing.
- There's a **manual process** that should be automated.
- A deployment, build, or data pipeline needs to be **rebuilt or replaced**.
- Scraping, API integration, or scheduled tasks need to be set up or fixed.

---

## Inputs

1. **Target** — which automation/script/pipeline needs work.
2. **Current state** — what exists today? What breaks? What's manual?
3. **Desired state** — what should it do when we're done?
4. **Constraints** — schedule, dependencies, credentials, platform limitations.

---

## Steps

1. **Map the current automation:**
   ```markdown
   ## AUTOMATION INTEL
   Name: [script/pipeline name]
   Location: [path or service]
   Trigger: [cron / manual / webhook / CI event]
   Dependencies: [what it needs to run]
   Last known working: [date or "unknown"]
   Known issues: [what breaks and when]
   Documentation: [exists? where?]
   ```

2. **Classify the Automaton threat level:**
   - 🟢 **Functional but undocumented** — Fortify (FRT) to document, then leave it
   - 🟡 **Flaky / intermittent failures** — diagnose and fix (Squad C approach)
   - 🔴 **Broken / needs replacement** — design new automation (Squad B if complex)

3. **For fixes (🟡):**
   - Identify the failure mode
   - Fix the root cause (not just retry logic)
   - Add error handling and logging
   - Add monitoring / alerts if possible

4. **For replacements (🔴):**
   - Design the new automation from scratch
   - If it's a script: make it idempotent, logged, and with proper error handling
   - If it's a pipeline: define stages, dependencies, failure modes
   - If it's scraping/API: handle rate limits, retries, auth, data validation

5. **For new automation (manual → automated):**
   - Document the current manual process step by step
   - Identify which steps can be automated vs need human judgment
   - Build the automation in phases (one step at a time, test each)
   - Keep a manual fallback until the automation is proven

6. **Verify:**
   - Run the automation end to end
   - Test failure cases (what happens when input is bad? when deps are down?)
   - Document: how to run, how to debug, how to recover

7. **Log:** `Stratagem: ATA on [target]. Type: [fix/replace/new]. Result: [summary]`

---

## Outputs

- Working automation (script / pipeline / scheduled task)
- Documentation: what it does, how to run, how to debug
- Error handling and logging built in
- Optional: monitoring/alerting setup (pair with Guard Dog)

---

## Cooldown / limits

- No cooldown for fixes. For full replacements: treat as Squad B (batch approach).
- **Never hardcode credentials** in scripts. Use environment variables or secret managers.
- **Always test failure cases** — an automation that only works when everything is perfect is an Automaton in disguise.
- If the automation interacts with external systems (APIs, websites): **rate limit and be respectful**.

---

*"Automaton Assault — Super Earth builds automation that documents itself."*
