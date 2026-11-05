---
type: concept
status: reviewed
sources: [2024-lattuada-verus-practical-foundation, 2026-he-neuro-symbolic-proof, 2026-he-neuro-symbolic-proof-osdi, 2024-zhang-selene-pioneering-automated, 2009-klein-sel4-formal-verification, 2026-ahn-promise-proof-automation, 2025-yang-autoverus-automated-proof]
short: Machine-made proofs that a checker accepts
updated: 2026-11-05
---

# Proof automation

Generating the proofs of a formal verification by machine instead of by hand. A proof checker such as Isabelle accepts only correct proofs, so a model that proposes proof steps may be wrong as often as the time budget allows; only what the checker accepts counts ([[2026-he-neuro-symbolic-proof]], §1, §3).

## State, October 2026

- For seL4, a method that has a small fine-tuned model propose single proof steps, prunes with counterexample finders and searches a tree proves 77.6 per cent of the still-valid theorems in three evaluation splits of the FVEL benchmark, and about 20 per cent of those whose human proofs exceed ten lines ([[2026-he-neuro-symbolic-proof]]). The peer-reviewed OSDI version repeats these figures, reports an average saving of 79.8 per cent of proof-writing effort where the preprint said 71.1 ([[2026-he-neuro-symbolic-proof-osdi]]).
- Selene of 2024, which its authors call the first project-level benchmark from seL4's proofs, tested GPT-3.5-turbo and GPT-4 on 340 lemmas: GPT-4 proved 41.7 per cent of the easiest set on the first try and almost none of the hardest ([[2024-zhang-selene-pioneering-automated]]). Later work names it as the baseline it improves on.
- The first seL4 proof took about 20 person-years, 11 of them specific to seL4 and much of the rest research, frameworks and tools ([[2009-klein-sel4-formal-verification]], §5.2); the automated proofs cover existing theorem statements, so they measure the cost of re-proving, not of specifying ([[2026-he-neuro-symbolic-proof]]; our reading).
- [[verus]] is a different kind of help: the verifier itself is built for fast SMT checking of Rust. Its authors report 3 to 61 times shorter verification times than other tools on list benchmarks, and a page table, an allocator and a log verified with proof-to-code ratios of 3.9 to 13.3 ([[2024-lattuada-verus-practical-foundation]]). Neither source is about the other: the models of [[2026-he-neuro-symbolic-proof]] work in Isabelle on seL4.
- A second method, PROMISE, retrieves structurally similar proof fragments from existing Isabelle proofs to guide a beam search. On a benchmark of 223 theorems from seL4's l4v it reaches 55.7 per cent averaged over seven model settings, against 34.0 for Rango and 26.8 for Selene with five attempts; the authors re-implemented the baselines, and the benchmark and metric differ from the FVEL work above; our reading: the two percentages cannot be compared ([[2026-ahn-promise-proof-automation]], §4, §5).
- AutoVerus, a network of model agents that writes proofs for [[verus]], reports correct proofs for more than 90 per cent of 150 Rust proof tasks, more than half in under 30 seconds or three model calls. The wiki read only the abstract. The tasks come from code-generation and verification benchmarks; our reading: the rate cannot be compared with the seL4 figures above ([[2025-yang-autoverus-automated-proof]]).

## Open questions

- How much of a new proof, with new specifications and invariants, such methods can carry. See [[kernel]] and [[drivers]].
- Whether proof effort falls enough to verify a broker or a safety controller, the parts zOS wants proven next. See [[broker]], [[safety-path]].
