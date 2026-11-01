---
type: system
status: reviewed
sources: [2024-lattuada-verus-practical-foundation]
short: Verifier for Rust code, SMT-based
updated: 2026-11-01
---

# Verus

A verifier for Rust. The programmer writes specifications and proofs in Rust beside the code, and an SMT solver checks them; Rust's ownership types carry the memory reasoning ([[2024-lattuada-verus-practical-foundation]]).

## State, October 2026

The SOSP 2024 paper reports case studies: a page table, an allocator, a persistent log and ports of two earlier verified systems, 6.1K lines of code with 31K of proof. It says other groups used Verus for cluster-management controllers, a verified microkernel, a confidential-VM security module and to verify LLM-produced code ([[2024-lattuada-verus-practical-foundation]]). The wiki has no source on newer Verus releases.

## Licence and code

The paper says Verus, its artifact and its case studies are open source ([[2024-lattuada-verus-practical-foundation]], §1); the wiki's source does not name the licence.

## Related

[[proof-automation]] for models that write proofs for tools like this one.

## Open questions

- Whether Verus can carry seL4-sized components, such as the broker or a safety controller. See [[broker]], [[safety-path]].
