---
type: concept
status: reviewed
sources: [2026-he-neuro-symbolic-proof, 2009-klein-sel4-formal-verification]
short: Machine-made proofs that a checker accepts
updated: 2026-10-31
---

# Proof automation

Generating the proofs of a formal verification by machine instead of by hand. A proof checker such as Isabelle accepts only correct proofs, so a model that proposes proof steps may be wrong as often as the time budget allows; only what the checker accepts counts ([[2026-he-neuro-symbolic-proof]], §1, §3).

## State, October 2026

- For seL4, a method that has a small fine-tuned model propose single proof steps, prunes with counterexample finders and searches a tree proves 77.6 per cent of the still-valid theorems in three evaluation splits of the FVEL benchmark, and about 20 per cent of those whose human proofs exceed ten lines ([[2026-he-neuro-symbolic-proof]]).
- The first seL4 proof took about 20 person-years, 11 of them specific to seL4 and much of the rest research, frameworks and tools ([[2009-klein-sel4-formal-verification]], §5.2); the automated proofs cover existing theorem statements, so they measure the cost of re-proving, not of specifying ([[2026-he-neuro-symbolic-proof]]; our reading).
- Verus and AutoVerus, which the zOS paper also cites for cheaper proofs, are not yet covered here.

## Open questions

- How much of a new proof, with new specifications and invariants, such methods can carry. See [[kernel]] and [[drivers]].
- Whether proof effort falls enough to verify a broker or a safety controller, the parts zOS wants proven next. See [[broker]], [[safety-path]].
