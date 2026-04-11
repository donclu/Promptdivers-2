# Tutorial Mission 08 — Propaganda Drop (Campaign Web / Landing)

## Mission type: LAUNCH-WEB (BUILD-WEB + WRITE + VISUAL hybrid)

> *"Super Earth does not whisper. It broadcasts — clear HTML, honest claims, and a CTA worth clicking."*

---

## Scenario

You need a **small public web surface**: a landing page, a manifesto-style microsite, an open-source project splash, or a tongue-in-cheek **“propaganda”** page (still truthful — no fabricated metrics). The mission walks you from **strategy → copy → layout → implementation → deploy**, using Promptdivers stratagems and ecosystem skills.

**Difficulty:** ⭐⭐⭐ Medium–hard (many moving parts — run in **phases**)  
**Time:** ~45–60 minutes  
**Stratagems used:** Eagle Visuals (EVS), Hellpod (HPD), Fortify (FRT), Eagle Report (ERP), Eagle Rearm (ERM)  
**Skills (recommended):** **ui-design-expert** (Phase 0 before any UI code), **humanizer** (after [onboarding-calibration.md](../docs/onboarding-calibration.md)), **structured-workflow** (if the site grows beyond one page)

---

## Why structured paste-prompts help the model

The blocks below are **deliberate scaffolding**, not bureaucracy.

| Mechanism | Effect on reasoning |
|-----------|---------------------|
| **Numbered deliverables** | Reduces skipped steps (e.g. jumping to CSS before audience). |
| **Separated phases** | BUILD-WEB + WRITE stay distinct: message first, pixels second. |
| **Explicit “done when”** | You can debrief with PASS/PARTIAL/FAIL like any other mission. |
| **Constraints (“forbidden claims”)** | Lowers hallucinated statistics and fake testimonials. |

You are teaching the assistant to **chain abstractions**: brief → information architecture → visual language → code → verification → ship.

---

## Pre-drop checklist

- [ ] You know **who** the page is for (one primary audience).
- [ ] You know **one primary CTA** (sign up, star repo, read docs, join Discord, etc.).
- [ ] You have a **hosting target** in mind (GitHub Pages, Netlify, Vercel, static bucket — pick one).
- [ ] Optional: brand colors, logo path, or “must match existing site” constraint in `AGENTS.md`.

---

## Phase 0 — Planet check (do not skip)

Paste:

```text
Pre-drop check (protocols/pre-drop.md):

1. Read GALACTIC_WAR_MAP.md or PROJECT_LOG.md if this repo has them.
2. List: active fronts (Terminids / Automatons / Illuminate) that touch *this* web work
   (e.g. Terminids = broken links; Automatons = hand-rolled deploy scripts; Illuminate = unreviewed AI copy on a public page).
3. Recommend squad + nave for *this* phase only (LAUNCH-WEB is usually Squad B mindset with Forge ≠ Executor).

Reply with:
- Hottest sector (path or “greenfield”)
- Threat level
- Recommended nave class (A/B/C) and one-line rationale
```

**Expected result:** A short planet-status block you can paste into `NEXT_MISSION.md` under **Planet status**.

---

## Phase 1 — Campaign brief (strategy, not pixels)

Paste:

```text
🎯 ON TARGET — LAUNCH-WEB Phase 1: strategy only. No HTML yet.

Produce a **Campaign brief** with these sections:

1. **Audience** — one paragraph: who lands here, what they already believe, what they fear.
2. **Objective** — one sentence: what success looks like (measurable if possible: clicks, stars, signups).
3. **Core message** — one sentence value prop + one sentence “why now”.
4. **Proof plan** — bullet list: what evidence we *actually* have (quotes, numbers, screenshots, logos). Mark each as REAL or PLACEHOLDER.
5. **Forbidden claims** — list things we must NOT say (unverified metrics, fake quotes, trademark violations).
6. **Tone** — pick 3 adjectives (e.g. earnest, dry, cinematic). Calibrate AI-likeness per docs/onboarding-calibration.md if using humanizer later.

End with: “Ready for Phase 2: copy architecture.”
```

**Expected result:** A document you can treat as the **source of truth** for all copy and layout decisions.

---

## Phase 2 — Copy architecture (headlines before components)

Paste:

```text
🚀 GO — Phase 2: copy architecture only. Still no HTML.

Using the Campaign brief, produce:

1. **Page title** + **meta description** (≤160 chars).
2. **Above-the-fold block**: H1, subhead, primary CTA label, secondary CTA (optional).
3. **Section outline** (order matters): for each section — H2, 2–4 bullets of substance, optional CTA.
4. **Footer**: legal/minimal links, copyright line, “not affiliated” if parody/satire branding.
5. **Accessibility pass on copy**: avoid idioms that break i18n if audience is global; flag any jargon.

If any proof was PLACEHOLDER in Phase 1, either remove the claim or label it clearly as “Example only” in the outline.

End with: “Ready for Phase 3: visual language.”
```

**Expected result:** IA + copy deck. **humanizer** pass optional after calibration if stakeholders read this.

---

## Phase 3 — Visual language (Phase 0 diagnostic)

Paste:

```text
📋 SITREP — Phase 3: visual language.

Load ui-design-expert **Phase 0** before writing CSS:

1. **Layout metaphor** — e.g. “single-column manifesto”, “split hero + proof grid”, “terminal aesthetic”.
2. **Type** — two font roles (display + body); system stack OK if specified.
3. **Color** — background, text, accent, link; contrast goal WCAG AA minimum for body text.
4. **Motion** — none / subtle / bold; respect prefers-reduced-motion.
5. **Anti-slop rules** — 3 things this page will *not* do (e.g. generic purple gradient, Inter-only, fake device frames).

Output: a **Design constraints** block (bullet list) the implementer must follow in Phase 4.
```

**Expected result:** Constraints that prevent generic “AI landing page” sameness.

---

## Phase 4 — Structure sketch (optional but cheap)

Paste:

```text
Call Eagle Visuals (EVS) — low-fidelity structure only:

Produce ONE of:
- ASCII wireframe of the page, OR
- Mermaid diagram of section flow, OR
- Bullet “component list” with rough priority (hero, social proof, FAQ, CTA repeat).

No brand assets required. Map each block to the H2s from Phase 2.
```

**Expected result:** A map from copy deck → layout regions.

---

## Phase 5 — Build the page(s)

Paste:

```text
🚀 GO — Phase 5: implementation.

Constraints:
- Match **Design constraints** (Phase 3) and **section outline** (Phase 2).
- Prefer static HTML + CSS in-repo unless the project already uses a framework — then match existing patterns.
- Call Hellpod (HPD): if a similar page exists, clone its structure; otherwise create `docs/` or `public/` paths per AGENTS.md.

Deliver:
1. File list created or modified
2. Responsive layout (mobile-first)
3. Semantic HTML (landmarks: header, main, footer; one h1)
4. Focus styles visible; buttons/links keyboard-accessible
5. No external tracking scripts unless human explicitly asked

If images are needed: use placeholders with explicit alt text or SVG icons with titles.

End with: “Ready for Phase 6: verification.”
```

**Expected result:** Working static page(s) in the repo.

---

## Phase 6 — Verification (mini audit)

Paste:

```text
🟡 YELLOW check — Phase 6: pre-deploy verification.

Run a lightweight pass (no need for full app-auditor unless this is high-stakes):

1. All links in copy resolve or are intentionally `#` with TODO in PROJECT_LOG
2. No PLACEHOLDER copy left on the public-facing surface unless marked “Example”
3. `forbidden claims` from Phase 1 — grep the HTML/MDX: none violated
4. Lighthouse-style sanity: images have dimensions or CSS aspect-ratio where needed
5. `prefers-reduced-motion` respected if animations exist

Output: table PASS/PARTIAL/FAIL per check with file:line evidence.
```

**Expected result:** Honest gate before you point DNS or enable Pages.

---

## Phase 7 — Deploy (pick your host)

Paste:

```text
🚀 GO — Phase 7: deploy.

Pick ONE path and document exact commands in PROJECT_LOG:

**A) GitHub Pages (docs/ or gh-pages branch)**  
- Build output directory  
- Actions workflow or branch setting  

**B) Netlify / Vercel**  
- Build command (if any) + publish directory  
- Env vars (none for static — confirm)

**C) Other static host**  
- Upload target + cache headers note if relevant

Deliver:
1. Public URL (or staging URL)
2. One paragraph “how to update the page next time” for THE SCRIBE
3. Call Fortify (FRT): add a short README section or `docs/deploy-landing.md` if missing
```

**Expected result:** Live URL + maintainer note.

---

## Phase 8 — Close out

Paste:

```text
Call Eagle Rearm (ERM):
- debrief this mission with objectives = phases 1–7 (use PASS/PARTIAL/FAIL)
- update HANDOFF_JSON: missions_queued if follow-ups exist (e.g. i18n, blog, analytics policy)
- optional Eagle Report (ERP): stakeholder summary of what shipped and what was explicitly *not* claimed
```

---

## Failure modes → stratagems

| Symptom | Next move |
|---------|-----------|
| Copy sounds like generic AI marketing | **humanizer** after calibration; tighten **Forbidden claims** |
| Layout is interchangeable with 1000 other landings | Re-run **ui-design-expert** Phase 0; add **Anti-slop rules** |
| Scope exploded to full product site | **ESCALATE** to Squad B + **sdd-workflow**; split into secondary missions |
| Deploy is a brittle one-off script | **Automaton Assault (ATA)** — document or replace with standard static hosting |

---

## Related docs

- [super-earth-operating-model.md](../docs/super-earth-operating-model.md) — **LAUNCH-WEB** archetype  
- [onboarding-calibration.md](../docs/onboarding-calibration.md) — voice before humanizer  
- [prompt-economics.md](../docs/prompt-economics.md) — why phased missions save tokens  
- `templates/next-mission.template.md` — log nave + mission queue for follow-on pages  

---

*Promptdivers — the message is the mission. FOR DEMOCRACY.*
