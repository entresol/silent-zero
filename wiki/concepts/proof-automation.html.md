# Proof automation

> Machines proposing proof steps, Isabelle checking them; 77.6 % of a seL4 benchmark sample; Verus as a faster verifier. PROMISE as a second method; AutoVerus for Rust.

Concept · LLM reviewed · updated 2026-11-04 · 5 sources · https://silentzero.ooo/wiki/concepts/proof-automation.html

Generating the proofs of a formal verification by machine instead of by hand. A proof checker such as Isabelle accepts only correct proofs, so a model that proposes proof steps may be wrong as often as the time budget allows; only what the checker accepts counts ([Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md), §1, §3).

## State, October 2026

- For seL4, a method that has a small fine-tuned model propose single proof steps, prunes with counterexample finders and searches a tree proves 77.6 per cent of the still-valid theorems in three evaluation splits of the FVEL benchmark, and about 20 per cent of those whose human proofs exceed ten lines ([Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md)).
- The first seL4 proof took about 20 person-years, 11 of them specific to seL4 and much of the rest research, frameworks and tools ([seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md), §5.2); the automated proofs cover existing theorem statements, so they measure the cost of re-proving, not of specifying ([Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md); our reading).
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md) is a different kind of help: the verifier itself is built for fast SMT checking of Rust. Its authors report 3 to 61 times shorter verification times than other tools on list benchmarks, and a page table, an allocator and a log verified with proof-to-code ratios of 3.9 to 13.3 ([Verus, a practical foundation for systems verification](https://silentzero.ooo/wiki/sources/2024-lattuada-verus-practical-foundation.html.md)). Neither source is about the other: the models of [Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md) work in Isabelle on seL4.
- A second method, PROMISE, retrieves structurally similar proof fragments from existing Isabelle proofs to guide a beam search. On a benchmark of 223 theorems from seL4's l4v it reaches 55.7 per cent averaged over seven model settings, against 34.0 for Rango and 26.8 for Selene with five attempts; the authors re-implemented the baselines, and the benchmark and metric differ from the FVEL work above; our reading: the two percentages cannot be compared ([PROMISE](https://silentzero.ooo/wiki/sources/2026-ahn-promise-proof-automation.html.md), §4, §5).
- AutoVerus, a network of model agents that writes proofs for [Verus](https://silentzero.ooo/wiki/systems/verus.html.md), reports correct proofs for more than 90 per cent of 150 Rust proof tasks, more than half in under 30 seconds or three model calls. The wiki read only the abstract. The tasks come from code-generation and verification benchmarks; our reading: the rate cannot be compared with the seL4 figures above ([AutoVerus](https://silentzero.ooo/wiki/sources/2025-yang-autoverus-automated-proof.html.md)).

## Open questions

- How much of a new proof, with new specifications and invariants, such methods can carry. See [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md) and [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md).
- Whether proof effort falls enough to verify a broker or a safety controller, the parts Silent Zero wants proven next. See [The broker](https://silentzero.ooo/wiki/design/broker.html.md), [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md).

## Sources

- [AutoVerus](https://silentzero.ooo/wiki/sources/2025-yang-autoverus-automated-proof.html.md)
- [Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md)
- [PROMISE](https://silentzero.ooo/wiki/sources/2026-ahn-promise-proof-automation.html.md)
- [seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md)
- [Verus, a practical foundation for systems verification](https://silentzero.ooo/wiki/sources/2024-lattuada-verus-practical-foundation.html.md)

## Related pages

- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md)
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Memory-safe code](https://silentzero.ooo/wiki/concepts/memory-safe-code.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md)
