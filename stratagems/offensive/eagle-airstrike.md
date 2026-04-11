# Eagle Airstrike — Offensive

## Code: `EAS`

> "Three files. One pass. In and out before the bugs know what hit them."

---

## When to call

- A fix or feature touches **2–4 files** that are closely related.
- Changes are **coordinated** — they must land together to make sense.
- Scope is clear and bounded — if it grows beyond 4 files, ESCALATE.

---

## Inputs

1. **File list** — exact paths (max 4).
2. **Change description** — what changes in each file and why.
3. **Order** — which file should change first (dependency order).

---

## Steps

1. **Read all target files** first. Understand the current state.
2. **Draft changes** for all files before applying any.
3. **Apply in dependency order** — upstream changes first.
4. **Run tests / typecheck** after the full set is applied.
5. **If any file breaks** — revert all, report, do not partial-apply.
6. **Log:** `Stratagem: EAS on [file1, file2, file3]`.

---

## Outputs

- All files updated in one coordinated pass.
- Summary of changes per file.
- Test results.

---

## Cooldown / limits

- **Max 4 files.** If the list grows, this is no longer an airstrike — it's a barrage. Upgrade to Orbital Barrage or Squad B.
- Can be called **multiple times** in a session (unlike orbital stratagems).
- Pairs well with **Shield Generator** (add tests after the strike).

---

*"Eagle Airstrike — coordinated, precise, democratic."*
