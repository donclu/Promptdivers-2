# Roles and field operatives — what to call them

Promptdivers does **not** ship separate executable “AI agents” (no extra binaries or accounts). It ships **named roles**—**field operatives** with **codenames**—that **you** (or the model) **adopt** in a session by pasting the activation block from a squad file.

## What to call them

| Term | Meaning |
|------|--------|
| **Field operative** / **role** | A pattern of behavior: scope, permissions, and output shape for one stretch of work. |
| **Codename** | The in-fiction label (`THE AUTHENTIC`, `THE FORGE`, …) used in comms and prompts. |
| **Squad** | A mission bundle (A–D) that sequences several roles. |
| **Session** | Usually one chat/thread; you can switch roles over time in the same session. |

So you can say: *“Run as **THE SCOUT** for this pass”* or *“Squad C: **THE MARKSMAN** turn.”*  
Avoid implying there are twelve separate products—there are **twelve named hats** the same assistant wears when you load the matching prompt.

## When it *is* multiple agents

- **Two chats / two sessions:** e.g. one as **THE FORGE** (drafts only), another as **THE EXECUTOR** (apply only)—required discipline for **Squad B**.  
- **Subagents / tasks:** Some IDEs let you spawn a sub-run; treat each as a session with one codename.  
- **Humans:** You are still **Super Earth High Command**; operatives report to you.

## Codename roster (canonical)

| Codename | Typical squad(s) | One-line job | Activation prompts in |
|----------|------------------|--------------|-------------------------|
| **THE AUTHENTIC** | A, B, C | Context, scope, `AGENTS.md`, briefings | `squad-a-advance.md`, `squad-b-artillery.md`, `squad-c-surgical.md` |
| **THE SCOUT** | A | Read-only recon, `INTEL_REPORT` | `squad-a-advance.md` |
| **THE ARCHITECT** | A | SPEC / DESIGN / TASKS | `squad-a-advance.md` |
| **THE SENTINEL** | A, D | Risk scan, pre-flight | `squad-a-advance.md`, `squad-d-defense.md` |
| **THE FORGE** | B | Drafts, design batches | `squad-b-artillery.md` |
| **THE EXECUTOR** | B | Apply drafts, integrate | `squad-b-artillery.md` |
| **THE AUDITOR** | B, D | Tests, diff, PR gate | `squad-b-artillery.md`, `squad-d-defense.md` |
| **THE MARKSMAN** | C | Diagnose, minimal fix | `squad-c-surgical.md` |
| **THE VALIDATOR** | C | Scope-only verification | `squad-c-surgical.md` |
| **THE SCRIBE** | D | Logs, changelog, brief updates | `squad-d-defense.md` |
| **THE TACTICIAN** | D | Backlog, `NEXT_MISSION` | `squad-d-defense.md` |

**Default anchor role** for any project brief: **THE AUTHENTIC** (see [`AGENTS.md`](../AGENTS.md)).

## Strategem four (high level)

For quick planning, the four slots are often summarized as:

1. **THE AUTHENTIC** — context  
2. **THE FORGE** — design/draft  
3. **THE EXECUTOR** — apply  
4. **THE AUDITOR** — verify  

Specialist names above are **refinements** for squads A–D.

---

*Promptdivers — one democracy, many helmets.*
