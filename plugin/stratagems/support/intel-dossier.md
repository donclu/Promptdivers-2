# Intel Dossier — Support

## Code: `IDR`

> "Intelligence wins wars. Guesswork loses planets."

---

## When to call

- You need to **research a topic** and produce a structured, reusable briefing.
- Before starting a new project, feature, or integration — you need to understand the landscape.
- Evaluating tools, frameworks, libraries, APIs, or vendors.
- Building a **knowledge base** for a team or stakeholder.
- Any situation where "I need to know about X before I act" applies.

---

## Inputs

1. **Research question** — what do you need to know? (Be specific.)
2. **Scope** — how deep? (Quick scan / thorough review / exhaustive analysis)
3. **Audience** — who reads this? (The agent / the team / leadership / public)
4. **Sources** — where to look (docs, web, codebase, data files, APIs, papers)

---

## Steps

1. **Define the intelligence requirement:**
   ```markdown
   ## INTEL REQUEST
   Question: [What do we need to know?]
   Scope: SCAN | REVIEW | DEEP ANALYSIS
   Audience: [who reads this]
   Sources: [where to look]
   Deadline: [when is this needed]
   ```

2. **Gather raw intelligence:**
   - Read documentation, source code, APIs, web resources
   - Extract facts, numbers, constraints, risks
   - Note **sources** for every claim — unsourced intel is Illuminate territory

3. **Analyze and structure:**
   - Group findings by theme or decision area
   - Identify options with tradeoffs
   - Flag risks, unknowns, and assumptions
   - Rate confidence: HIGH (verified) / MEDIUM (likely) / LOW (unconfirmed)

4. **Produce the dossier** using the template (`templates/intel-dossier.template.md`):
   - Executive summary (3 sentences max)
   - Key findings table
   - Options matrix (if evaluating alternatives)
   - Risks and unknowns
   - Recommendation
   - Sources

5. **Verify claims:**
   - Every factual claim should have a source
   - Mark unverified claims as `[UNVERIFIED]`
   - If using AI-generated summaries: apply Mind Control protocol on high-risk claims

6. **Log:** `Stratagem: IDR — Intel Dossier on [topic]. Confidence: [HIGH/MEDIUM/LOW]`

---

## Outputs

- Structured dossier document (Markdown)
- Sources list with links/paths
- Confidence rating
- Clear recommendation or options matrix

---

## Cooldown / limits

- No cooldown — use for any research task.
- **Time-box** deep analysis: set a limit before starting (30 min, 1 hour, etc.)
- If the research reveals scope larger than expected: `SOS Beacon` → ask human to narrow.
- For ongoing research (not one-shot): log in PROJECT_LOG and chain multiple sessions.

---

*"Intel Dossier — knowledge is Super Earth's greatest weapon."*
