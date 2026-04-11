# Hellpod — Support

## Code: `HPD`

> "Drop in hot. File ready on landing."

---

## When to call

- You need to **create a new file** that follows an existing pattern in the project.
- Bootstrapping a new component, route, test file, or module from convention.
- The project has clear patterns and you need to replicate them, not invent.

---

## Inputs

1. **Template source** — an existing file that exemplifies the pattern.
2. **New file path** — where the new file should land.
3. **Customization** — what's different (name, behavior, dependencies).

---

## Steps

1. **Identify the pattern file** — the best existing example of what you're creating.
2. **Read it** and extract the pattern: structure, imports, naming convention, export style.
3. **Create the new file** following the exact same pattern:
   - Same import style
   - Same naming convention
   - Same structure/ordering
   - Same test setup if creating a test file
4. **Customize** only the parts that must differ (function names, logic, types).
5. **Register** the new file if needed (add to index, router, module registry, etc.).
6. **Verify** — does it compile/import? Quick sanity check.
7. **Log:** `Stratagem: HPD — created [path] from pattern [template-path]`.

---

## Outputs

- New file matching project conventions.
- Any registration/index updates needed.
- File ready for content development.

---

## Cooldown / limits

- No cooldown — use for every new file.
- The value is in **matching patterns, not inventing them**. If there's no clear pattern to follow, ask the human first.
- If creating more than 5 files, this is Squad B territory — use batching.

---

*"Hellpod — every new file drops the democratic way."*
