---
type: source
id: 2026-sel4-functional-correctness-proof
status: reviewed
read: full
kind: report
sources: [2026-sel4-functional-correctness-proof]
updated: 2026-10-29
---

# seL4 Foundation 2026: MCS functional-correctness proof completed on RISC-V

A news item of the seL4 Foundation, dated 29 June 2026, read on its news page on 29 October 2026. [News page](https://sel4.systems/news/).

## What it shows

- Proofcraft has completed the proof of functional correctness for seL4 with the MCS configuration, on RISC-V.
- The item calls MCS the largest new seL4 feature, with wide-ranging changes to the kernel's implementation and API, and calls functional correctness the largest and most central proof in the seL4 verification stack.
- The proof will now be ported to 64-bit Arm, as part of DARPA's PROVERS programme.

## How

An announcement of three paragraphs. It names neither the configuration file, the proof's size nor a date for the Arm port.

## Limits

A careful reader adds:

- **Functional correctness only.** The item says nothing about integrity or confidentiality for MCS, and nothing about binary verification.
- **No date for AArch64.** The paper gives the third quarter of 2027 for AArch64 and cites the seL4 roadmap for it; that source is not yet in the wiki.
- [[nd-sel4-verified-configurations]] still called the MCS verification ongoing on 23 October 2026. This item is newer and more specific.
- [[2026-heiser-mcs-safety-os]], a talk from May 2026, gave "mid-'27" for the functional verification of seL4-MCS. It does not say for which architecture. The proof on RISC-V came a month after the talk.

## Against the wiki

- [[sel4]]: **confirms** what it said with Sillitoe et al. as an intermediate source; the wiki now cites the announcement itself.
- [[nd-sel4-verified-configurations]]: **replaces** its statement that the RISC-V MCS verification is ongoing.

## For zOS

- [[kernel]]: the paper says the MCS configuration on 64-bit RISC-V has a machine-checked proof of functional correctness (In brief, Section 3). This source confirms it. The paper's state for this claim stays *proven* for functional correctness. The item names neither the level of the proof nor 64-bit; that the RISC-V verified configurations are 64-bit and C-level comes from [[nd-sel4-verified-configurations]].
