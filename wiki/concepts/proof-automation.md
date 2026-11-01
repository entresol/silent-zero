---
type: concept
status: reviewed
sources: [2024-lattuada-verus-practical-foundation, 2026-he-neuro-symbolic-proof, 2009-klein-sel4-formal-verification]
short: Machine-made proofs that a checker accepts
updated: 2026-11-01
---

# Proof automation

Generating the proofs of a formal verification by machine instead of by hand. A proof checker such as Isabelle accepts only correct proofs, so a model that proposes proof steps may be wrong as often as the time budget allows; only what the checker accepts counts ([[2026-he-neuro-symbolic-proof]], §1, §3).

## State, October 2026

- For seL4, a method that has a small fine-tuned model propose single proof steps, prunes with counterexample finders and searches a tree proves 77.6 per cent of the still-valid theorems in three evaluation splits of the FVEL benchmark, and about 20 per cent of those whose human proofs exceed ten lines ([[2026-he-neuro-symbolic-proof]]).
- The first seL4 proof took about 20 person-years, 11 of them specific to seL4 and much of the rest research, frameworks and tools ([[2009-klein-sel4-formal-verification]], §5.2); the automated proofs cover existing theorem statements, so they measure the cost of re-proving, not of specifying ([[2026-he-neuro-symbolic-proof]]; our reading).
- [[verus]] is a different kind of help: the verifier itself is built for fast SMT checking of Rust. Its authors report 3 to 61 times shorter verification times than other tools on list benchmarks, and a page table, an allocator and a log verified with proof-to-code ratios of 3.9 to 13.3 ([[2024-lattuada-verus-practical-foundation]]). Neither source is about the other: the models of [[2026-he-neuro-symbolic-proof]] work in Isabelle on seL4.
- AutoVerus, which the zOS paper cites for models that write Verus proofs, is not yet covered here.

## Open questions

- How much of a new proof, with new specifications and invariants, such methods can carry. See [[kernel]] and [[drivers]].
- Whether proof effort falls enough to verify a broker or a safety controller, the parts zOS wants proven next. See [[broker]], [[safety-path]].
