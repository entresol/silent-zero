---
type: concept
status: reviewed
sources: [2024-lattuada-verus-practical-foundation, 2026-he-neuro-symbolic-proof, 2009-klein-sel4-formal-verification, 2026-ahn-promise-proof-automation, 2025-yang-autoverus-automated-proof, 2026-rinard-testing-credible-compilation, 2026-liao-llvm-translation-validation]
short: Machine-made proofs that a checker accepts
updated: 2026-11-09
---

# Proof automation

Generating the proofs of a formal verification by machine instead of by hand. A proof checker such as Isabelle accepts only correct proofs, so a model that proposes proof steps may be wrong as often as the time budget allows; only what the checker accepts counts ([[2026-he-neuro-symbolic-proof]], §1, §3).

## State, October 2026

- For seL4, a method that has a small fine-tuned model propose single proof steps, prunes with counterexample finders and searches a tree proves 77.6 per cent of the still-valid theorems in three evaluation splits of the FVEL benchmark, and about 20 per cent of those whose human proofs exceed ten lines ([[2026-he-neuro-symbolic-proof]]).
- The first seL4 proof took about 20 person-years, 11 of them specific to seL4 and much of the rest research, frameworks and tools ([[2009-klein-sel4-formal-verification]], §5.2); the automated proofs cover existing theorem statements, so they measure the cost of re-proving, not of specifying ([[2026-he-neuro-symbolic-proof]]; our reading).
- [[verus]] is a different kind of help: the verifier itself is built for fast SMT checking of Rust. Its authors report 3 to 61 times shorter verification times than other tools on list benchmarks, and a page table, an allocator and a log verified with proof-to-code ratios of 3.9 to 13.3 ([[2024-lattuada-verus-practical-foundation]]). Neither source is about the other: the models of [[2026-he-neuro-symbolic-proof]] work in Isabelle on seL4.
- A second method, PROMISE, retrieves structurally similar proof fragments from existing Isabelle proofs to guide a beam search. On a benchmark of 223 theorems from seL4's l4v it reaches 55.7 per cent averaged over seven model settings, against 34.0 for Rango and 26.8 for Selene with five attempts; the authors re-implemented the baselines, and the benchmark and metric differ from the FVEL work above; our reading: the two percentages cannot be compared ([[2026-ahn-promise-proof-automation]], §4, §5).
- AutoVerus, a network of model agents that writes proofs for [[verus]], reports correct proofs for more than 90 per cent of 150 Rust proof tasks, more than half in under 30 seconds or three model calls. The wiki read only the abstract. The tasks come from code-generation and verification benchmarks; our reading: the rate cannot be compared with the seL4 figures above ([[2025-yang-autoverus-automated-proof]]).
- A different kind of evidence comes from a compiler. Rinard reports that a coding agent wrote a compiler for a small language with its Lean correctness proofs in 34 days under one supervisor, about 38,200 lines of Lean, roughly four lines of proof per line of code. Optimisations are not proved but checked by a verified certificate checker. The specifications and target model were not verified, and the agent at times, on its own, weakened theorems or left them unproved. One author reports one project, and it is not about seL4 ([[2026-rinard-testing-credible-compilation]], §1.1, §3, §3.2, §4.4, §5.1).
- Trivet (Liao and others, preprint of September 2026) applies the same split to compiler rewrites: a model completes proof holes in a Lean theorem, the Lean kernel checks the result, and 147 of 148 LLVM transformations are validated or refuted. The Lean formalisation covers integer instructions only, and proofs took minutes where Alive2 needs seconds on easy cases; the wiki read the paper in part ([[2026-liao-llvm-translation-validation]]).

## Open questions

- How much of a new proof, with new specifications and invariants, such methods can carry. See [[kernel]] and [[drivers]].
- Whether proof effort falls enough to verify a broker or a safety controller, the parts zOS wants proven next. See [[broker]], [[safety-path]].
