# Functional correctness

> What seL4’s refinement proof gives, what it assumes, where it holds.

Concept · LLM reviewed · updated 2026-11-21 · 5 sources · https://silentzero.ooo/wiki/concepts/functional-correctness.html

A program is functionally correct when every behaviour of its implementation is allowed by its specification. For [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md) it is proved as refinement: the C code refines an abstract specification, so every property proved as a Hoare triple about the specification also holds for the code ([seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md), §2.3).

## What it gives and what it does not

- It rules out whole classes of bugs at once. For seL4 the proof implies that the kernel never crashes, never dereferences a null or misaligned pointer and that every system call terminates, under the proof's assumptions ([seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md), §4.5).
- It says nothing about whether the specification is what a user wants. The authors grant this point to "a cynic" and answer that the specification is simpler and more abstract than the code ([seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md), §4.5).
- It holds only under its assumptions: compiler, assembly, hardware, and for seL4 the boot code and cache and TLB maintenance ([seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md), §4.4, §4.5). Binary verification later removed the compiler from this list for ARMv7 ([Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md), §3.2).
- It is the base for security proofs. Properties proved as Hoare triples about the abstract specification carry over to the code through refinement, though "not all security properties can be" stated that way ([seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md), §2.3). Integrity and intransitive non-interference have been proved for seL4 ([Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md), §3.2); how confidentiality reaches the code is not explained in the wiki's sources.
- It has not been proved that seL4's abstract specification meets the Hoare triples that the English descriptions of system calls in the reference manual imply. The group works on it; Recv, including its blocking case with Signal, is the worked example, the work is to extend to more system calls, initially those the Microkit libraries use, and the proofs are described as almost complete for some motivating cases ([two interfaces for seL4 kernel verification](https://silentzero.ooo/wiki/sources/2026-sison-two-interfaces-sel4.html.md), §2).

## State for seL4, October 2026

Proved at C level for AArch32, AArch64, RISC-V and x86-64 in their verified configurations; at binary level for AArch32 ([seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)). For the MCS configuration, proved on RISC-V, announced June 2026 ([MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)).

## Open questions

- How much of a Silent Zero system beyond the kernel can be brought to this standard, and which parts stay tested or assumed. See [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md).

## Sources

- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)
- [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)
- [seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md)
- [two interfaces for seL4 kernel verification](https://silentzero.ooo/wiki/sources/2026-sison-two-interfaces-sel4.html.md)

## Related pages

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [limitations on formal verification for AI safety](https://silentzero.ooo/wiki/sources/2024-dickson-limitations-formal-verification.html.md)
- [Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md)
- [OSVBench](https://silentzero.ooo/wiki/sources/2025-li-osvbench-benchmarking-llms.html.md)
- [Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md)
- [seL4 Foundation: seL4 proofs and certification](https://silentzero.ooo/wiki/sources/nd-sel4-proofs-certification.html.md)
- [Trustworthy Systems n.d.: Proof Statistics](https://silentzero.ooo/wiki/sources/nd-trustworthy-proof-statistics.html.md)
- [Verifying Device Drivers with Pancake](https://silentzero.ooo/wiki/sources/2025-zhao-verifying-device-drivers.html.md)
