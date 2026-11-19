# Verus

> Verifier for Rust code with SMT solving; case studies, no kernel; AutoVerus writes proofs for it.

System · LLM reviewed · updated 2026-11-04 · 2 sources · https://silentzero.ooo/wiki/systems/verus.html

A verifier for Rust. The programmer writes specifications and proofs in Rust beside the code, and an SMT solver checks them; Rust's ownership types carry the memory reasoning ([Verus, a practical foundation for systems verification](https://silentzero.ooo/wiki/sources/2024-lattuada-verus-practical-foundation.html.md)).

## State, October 2026

The SOSP 2024 paper reports case studies: a page table, an allocator, a persistent log and ports of two earlier verified systems, 6.1K lines of code with 31K of proof. It says other groups used Verus for cluster-management controllers, a verified microkernel, a confidential-VM security module and to verify LLM-produced code ([Verus, a practical foundation for systems verification](https://silentzero.ooo/wiki/sources/2024-lattuada-verus-practical-foundation.html.md)). The wiki has no source on newer Verus releases.

## Licence and code

The paper says Verus, its artifact and its case studies are open source ([Verus, a practical foundation for systems verification](https://silentzero.ooo/wiki/sources/2024-lattuada-verus-practical-foundation.html.md), §1); the wiki's source does not name the licence.

## Related

[Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md) for models that write proofs for tools like this one. AutoVerus, which writes Verus proofs, is described in [AutoVerus](https://silentzero.ooo/wiki/sources/2025-yang-autoverus-automated-proof.html.md). [Memory-safe code](https://silentzero.ooo/wiki/concepts/memory-safe-code.html.md) for the wider case for Rust.

## Open questions

- Whether Verus can carry seL4-sized components, such as the broker or a safety controller. See [The broker](https://silentzero.ooo/wiki/design/broker.html.md), [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md).

## Sources

- [AutoVerus](https://silentzero.ooo/wiki/sources/2025-yang-autoverus-automated-proof.html.md)
- [Verus, a practical foundation for systems verification](https://silentzero.ooo/wiki/sources/2024-lattuada-verus-practical-foundation.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Memory-safe code](https://silentzero.ooo/wiki/concepts/memory-safe-code.html.md)
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [Rust in Android](https://silentzero.ooo/wiki/sources/2025-vander-rust-android-move.html.md)
