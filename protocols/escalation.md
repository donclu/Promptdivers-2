# Escalation protocol

> Super Earth does not refuse reinforcements out of pride.  
> Super Earth refuses **avoidable** chaos.

---

## Levels

```text
LEVEL 1 — Squad C (Surgical) working alone
           ↓ scope too large or risk too high
LEVEL 2 — Squad C + Defense auditor pass
           ↓ confirmed not fixable as a small patch
LEVEL 3 — Squad B (Artillery) full sequence
           ↓ design or terrain stale
LEVEL 4 — Squad A re-brief (THE AUTHENTIC + recon)
           ↓ crisis spans systems or humans declare max op
LEVEL 5 — OPERATION TOTAL DEMOCRACY
```

---

## Triggers (guide, not law)

### C → Level 2

- Root cause touches **more than ~5 files** (project-tune this threshold in `AGENTS.md`).
- Public API contract must change.
- Validator finds regression outside agreed scope.
- Security or PII involved.

### SOS vs RNF vs ESCALATE (fast choice)

Use the smallest call that restores progress and governance:

- **SOS** when you are **blocked** on a *human-only* decision: access, permissions, business intent, scope contract, or “we need you to pick A vs B”.
- **RNF (Reinforce)** when you are blocked by **parallel capacity**: the work is wide but can be split into owned paths with a clear sync point.
- **ESCALATE (levels)** when the task becomes **high-risk** (security/data loss), crosses contracts, or cannot be safely completed with the current squad level.

### Level 2 → Level 3 (activate B)

- Defense auditor: “not surgical.”
- Multiple failing tests from one underlying issue.
- DB schema / migration involved.
- Surgical fix created a **larger** problem.

### Multi-front guidance (same planet)

When multiple fronts are active on the same planet:

- **Slice by front** (Terminids vs Automatons vs Illuminate) only when each slice can own files with minimal overlap.
- Otherwise keep one mission active and queue the rest in `missions_queued` (do not context-switch mid-flight).

### Level 3 → Level 4

- `DESIGN.md` / `SPEC.md` no longer matches the repo.
- Hidden debt blocks the plan.
- `AGENTS.md` dangerously stale (wrong stack or rules).

### Level 5 — TOTAL DEMOCRACY

- Active production incident hurting users.
- Data loss or corruption risk.
- Critical security exposure.
- Cascading failures (fix X breaks Y, fix Y breaks Z).
- Human explicitly orders **TOTAL DEMOCRACY**.

---

## ESCALATE report template

```markdown
## ESCALATE REPORT
From: [CODENAME]
Squad: [A/B/C/D]
Time: [ISO or human-readable]
Suggested level: [2–5]

### Situation
[What we were doing]

### Problem
[What went wrong or does not fit]

### Evidence
[Logs, errors, paths, test names]

### Impact
[Users, data, security, timeline]

### Recommendation
[Next squad + first concrete step]

### Severity
LOW | MEDIUM | HIGH | CRITICAL
```

---

## After escalation

- Human picks the squad and **narrows scope** again.
- Update `PROJECT_LOG.md` with the decision.
- Do not continue the old plan under a new severity without explicit OK.

---

*Promptdivers — escalate early enough to avoid democracy by accident.*
