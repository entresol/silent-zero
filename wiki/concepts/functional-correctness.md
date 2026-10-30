---
type: concept
status: reviewed
sources: [2009-klein-sel4-formal-verification, 2018-klein-formally-verified-software, nd-sel4-verified-configurations, 2026-sel4-functional-correctness-proof]
updated: 2026-10-29
---

# Functional correctness

A program is functionally correct when every behaviour of its implementation is allowed by its specification. For [[sel4]] it is proved as refinement: the C code refines an abstract specification, so every property proved as a Hoare triple about the specification also holds for the code ([[2009-klein-sel4-formal-verification]], §2.3).

## What it gives and what it does not

- It rules out whole classes of bugs at once. For seL4 the proof implies that the kernel never crashes, never dereferences a null or misaligned pointer and that every system call terminates, under the proof's assumptions ([[2009-klein-sel4-formal-verification]], §4.5).
- It says nothing about whether the specification is what a user wants. The authors grant this point to "a cynic" and answer that the specification is simpler and more abstract than the code ([[2009-klein-sel4-formal-verification]], §4.5).
- It holds only under its assumptions: compiler, assembly, hardware, and for seL4 the boot code and cache and TLB maintenance ([[2009-klein-sel4-formal-verification]], §4.4, §4.5). Binary verification later removed the compiler from this list for ARMv7 ([[2018-klein-formally-verified-software]], §3.2).
- It is the base for security proofs. Properties proved as Hoare triples about the abstract specification carry over to the code through refinement, though "not all security properties can be" stated that way ([[2009-klein-sel4-formal-verification]], §2.3). Integrity and intransitive non-interference have been proved for seL4 ([[2018-klein-formally-verified-software]], §3.2); how confidentiality reaches the code is not explained in the wiki's sources.

## State for seL4, October 2026

Proved at C level for AArch32, AArch64, RISC-V and x86-64 in their verified configurations; at binary level for AArch32 ([[nd-sel4-verified-configurations]]). For the MCS configuration, proved on RISC-V, announced June 2026 ([[2026-sel4-functional-correctness-proof]]).

## Open questions

- How much of a zOS system beyond the kernel can be brought to this standard, and which parts stay tested or assumed. See [[kernel]].
