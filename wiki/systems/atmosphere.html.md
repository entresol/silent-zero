# Atmosphere

> Microkernel in Rust verified with Verus (SOSP 2025): functional correctness, one noninterference proof, 3.32 lines of proof per line of code; big lock; no time budgets described.

System · LLM reviewed · updated 2026-11-21 · 3 sources · https://silentzero.ooo/wiki/systems/atmosphere.html

A microkernel written in Rust and verified with [Verus](https://silentzero.ooo/wiki/systems/verus.html.md) at the University of Utah, presented at SOSP 2025. It proves functional correctness, refinement of a high-level specification, and a noninterference property for one configuration of containers ([Atmosphere, practical verified kernels with Rust and Verus](https://silentzero.ooo/wiki/sources/2025-chen-atmosphere-practical-verified.html.md)).

## State, October 2025 to November 2026

- The SOSP 2025 paper reports 6K lines of executable code and 20.1K lines of proof code, under 2.5 person-years, verification in under 20 seconds, and a proof-to-code ratio of 3.32:1. The project page gives 7.5:1 and does not explain the difference ([Atmosphere, practical verified kernels with Rust and Verus](https://silentzero.ooo/wiki/sources/2025-chen-atmosphere-practical-verified.html.md), [Mars Research Group: the Atmosphere project page](https://silentzero.ooo/wiki/sources/nd-mars-research-atmosphere.html.md)).
- It runs on multi-CPU hardware under a big lock. Authority is by a tree of containers; revoking resources means terminating the container ([Atmosphere, practical verified kernels with Rust and Verus](https://silentzero.ooo/wiki/sources/2025-chen-atmosphere-practical-verified.html.md)).
- The wiki's sources show no later release, and the pages read link no repository. The Verus paper's "verified microkernel (7.5 to 1)" may be an earlier state of it (our reading, [Verus, a practical foundation for systems verification](https://silentzero.ooo/wiki/sources/2024-lattuada-verus-practical-foundation.html.md)).

## Licence and code

The paper carries a Creative Commons Attribution 4.0 licence; the sources read name no licence for the kernel and link no repository.

## Related

[seL4](https://silentzero.ooo/wiki/systems/sel4.html.md), [Verus](https://silentzero.ooo/wiki/systems/verus.html.md), [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md), [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md), [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md).

## Open questions

- Whether any real-time property, such as a bound on the time a system call can block, can be stated and proved for a kernel under a big lock; the paper says long-running calls can block others and leak timing.
- Whether the design can carry budgets as capabilities and revocation by derivation, which Silent Zero takes from seL4 MCS; Atmosphere's authors chose against fine-grained revocation, and its paper describes no time budgets.
- Which of its figures to use for proof effort: the paper's 3.32:1 or the project page's 7.5:1.

## Sources

- [Atmosphere, practical verified kernels with Rust and Verus](https://silentzero.ooo/wiki/sources/2025-chen-atmosphere-practical-verified.html.md)
- [Mars Research Group: the Atmosphere project page](https://silentzero.ooo/wiki/sources/nd-mars-research-atmosphere.html.md)
- [Verus, a practical foundation for systems verification](https://silentzero.ooo/wiki/sources/2024-lattuada-verus-practical-foundation.html.md)

## Related pages

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md)
