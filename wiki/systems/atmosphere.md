---
type: system
status: reviewed
sources: [2025-chen-atmosphere-practical-verified, nd-mars-research-atmosphere, 2024-lattuada-verus-practical-foundation]
short: Microkernel in Rust, verified with Verus
updated: 2026-11-21
---

# Atmosphere

A microkernel written in Rust and verified with [[verus]] at the University of Utah, presented at SOSP 2025. It proves functional correctness, refinement of a high-level specification, and a noninterference property for one configuration of containers ([[2025-chen-atmosphere-practical-verified]]).

## State, October 2025 to November 2026

- The SOSP 2025 paper reports 6K lines of executable code and 20.1K lines of proof code, under 2.5 person-years, verification in under 20 seconds, and a proof-to-code ratio of 3.32:1. The project page gives 7.5:1 and does not explain the difference ([[2025-chen-atmosphere-practical-verified]], [[nd-mars-research-atmosphere]]).
- It runs on multi-CPU hardware under a big lock. Authority is by a tree of containers; revoking resources means terminating the container ([[2025-chen-atmosphere-practical-verified]]).
- The wiki's sources show no later release, and the pages read link no repository. The Verus paper's "verified microkernel (7.5 to 1)" may be an earlier state of it (our reading, [[2024-lattuada-verus-practical-foundation]]).

## Licence and code

The paper carries a Creative Commons Attribution 4.0 licence; the sources read name no licence for the kernel and link no repository.

## Related

[[sel4]], [[verus]], [[kernel]], [[proof-automation]], [[mixed-criticality]].

## Open questions

- Whether any real-time property, such as a bound on the time a system call can block, can be stated and proved for a kernel under a big lock; the paper says long-running calls can block others and leak timing.
- Whether the design can carry budgets as capabilities and revocation by derivation, which zOS takes from seL4 MCS; Atmosphere's authors chose against fine-grained revocation, and its paper describes no time budgets.
- Which of its figures to use for proof effort: the paper's 3.32:1 or the project page's 7.5:1.
