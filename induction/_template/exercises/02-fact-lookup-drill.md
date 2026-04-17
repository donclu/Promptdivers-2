# Layer 2 — Fact lookup drill

## Domain: [DOMAIN NAME]

> This drill trains the habit of retrieving facts from `knowledge/` before reasoning.
> The rule: **look it up, then speak**. Never the reverse.

---

## Instructions

1. For each question, open `knowledge/[domain].yaml`.
2. Find the answer.
3. Write it down **with the exact key name and source** from the YAML.
4. Do not answer from memory — the point is the lookup habit.

---

## Questions

**Q1.** What is the current value of `[key_1]` for `[scope]`?
- Value: _______________
- Source key: _______________
- Confidence: _______________

**Q2.** What is the `source_authority` for this domain?
- Value: _______________

**Q3.** List all `static` facts in the domain and their confidence level.
- (table or list)

**Q4.** Is there a `derived` metric? If yes, what is its `expression`?
- Answer: _______________

**Q5.** When was the domain last `updated`? Is it within its `expiry_policy`?
- Last updated: _______________
- Expiry status: _______________

---

## Pass criteria

All 5 answers cite the correct key and source from `knowledge/[domain].yaml`. ✅
