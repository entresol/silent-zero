---
type: system
status: reviewed
sources: [2024-lattuada-verus-practical-foundation, 2025-yang-autoverus-automated-proof, 2025-chen-atmosphere-practical-verified, nd-mars-research-atmosphere]
short: Verifier for Rust code, SMT-based
updated: 2026-11-21
---

# Verus

A verifier for Rust. The programmer writes specifications and proofs in Rust beside the code, and an SMT solver checks them; Rust's ownership types carry the memory reasoning ([[2024-lattuada-verus-practical-foundation]]).

## State, October 2026

The SOSP 2024 paper reports case studies: a page table, an allocator, a persistent log and ports of two earlier verified systems, 6.1K lines of code with 31K of proof. It says other groups used Verus for cluster-management controllers, a verified microkernel, a confidential-VM security module and to verify LLM-produced code ([[2024-lattuada-verus-practical-foundation]]). The SOSP 2025 paper on [[atmosphere]] is the wiki's source on a kernel built with it (the Verus paper lists a verified microkernel among other users): 6K lines of code, 20.1K lines of proof, under 2.5 person-years, verification in under 20 seconds ([[2025-chen-atmosphere-practical-verified]]). The wiki has no source on newer Verus releases.

## Licence and code

The paper says Verus, its artifact and its case studies are open source ([[2024-lattuada-verus-practical-foundation]], §1); the wiki's source does not name the licence.

## Related

[[proof-automation]] for models that write proofs for tools like this one. AutoVerus, which writes Verus proofs, is described in [[2025-yang-autoverus-automated-proof]]. [[memory-safe-code]] for the wider case for Rust.

## Open questions

- Whether Verus can carry seL4-sized components, such as the broker or a safety controller. [[atmosphere]] is a feature-rich microkernel verified with it, under a big lock, and its paper describes no time budgets. See [[broker]], [[safety-path]].
