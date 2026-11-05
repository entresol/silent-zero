# MCS functional-correctness proof completed on RISC-V

> MCS functional correctness proved on RISC-V, June 2026; Arm next. report, full text.

Source · seL4 Foundation 2026 · LLM reviewed · updated 2026-10-29 · https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html

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
- **No date for AArch64.** The announcement gives none. The paper cites the seL4 roadmap for the third quarter of 2027, and [seL4 Foundation: Development roadmap](https://silentzero.ooo/wiki/sources/nd-sel4-sel4-roadmap.html.md) says so.
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) still called the MCS verification ongoing on 23 October 2026. This item is newer and more specific.
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md), a talk from May 2026, gave "mid-'27" for the functional verification of seL4-MCS. It does not say for which architecture. The proof on RISC-V came a month after the talk.

## Against the wiki

- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md): **confirms** what it said with Sillitoe et al. as an intermediate source; the wiki now cites the announcement itself.
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md): **replaces** its statement that the RISC-V MCS verification is ongoing.

## For Silent Zero

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md): the paper says the MCS configuration on 64-bit RISC-V has a machine-checked proof of functional correctness (In brief, Section 3). This source confirms it. The paper's state for this claim stays *proven* for functional correctness. The item names neither the level of the proof nor 64-bit; that the RISC-V verified configurations are 64-bit and C-level comes from [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md).

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)
- [security proofs complete on AArch64](https://silentzero.ooo/wiki/sources/2026-proofcraft-sel4-security-proofs.html.md)
- [seL4 Foundation: Development roadmap](https://silentzero.ooo/wiki/sources/nd-sel4-sel4-roadmap.html.md)
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)
