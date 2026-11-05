# The kernel

> SeL4 with MCS as the Silent Zero kernel: proven (C-level correctness; MCS functional correctness on RISC-V), not stated for MCS (integrity, confidentiality), tested (HACMS), assumed (boot, IOMMU); no WCET bound on any 64-bit core yet; the roadmap dates MCS on AArch64 to Q3 2027.

Design · LLM reviewed · updated 2026-11-05 · 15 sources · https://silentzero.ooo/wiki/design/kernel.html

In Silent Zero the kernel is [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md) with its mixed-criticality extensions. It isolates components, moves messages between them and hands out processor time, and it is the only code at its privilege level (paper, Section 3).

## What it must do

- **Isolate in space.** No component may read or write another's memory or gain authority it was not given.
- **Isolate in time.** An agent that loops or is hijacked must not take the control loop's processor time. See [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md).
- **Bound its own execution time.** The control loops can keep a deadline only if the kernel beneath them has a bound on its own execution time. See [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md).

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| Functional correctness of the C code | proven, for the verified configurations | refinement proof in Isabelle/HOL | [seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md), [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) |
| Functional correctness of the MCS kernel on RISC-V | proven, announced June 2026 (the announcement names neither the level nor 64-bit; RISC-V verified configurations are 64-bit and C-level, per [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)) | proof, announced | [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md) |
| Platforms of the MCS proof on RISC-V | `hifive` (HiFive Unleashed, no longer sold) only; the proof without MCS covers further RISC-V boards, among them the HiFive Premier P550, since release 17.0.0 | release notes | [release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md), [SiFive and the HiFive boards](https://silentzero.ooo/wiki/systems/sifive-hifive.html.md) |
| MCS on 64-bit Arm | under way; the roadmap plans C-level verification for the third quarter of 2027 | plan, none yet | [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md), [seL4 Foundation: Development roadmap](https://silentzero.ooo/wiki/sources/nd-sel4-sel4-roadmap.html.md) |
| Multikernel configuration for multi-core systems | verification scheduled to complete in the third quarter of 2028 | plan | [seL4 Foundation: Development roadmap](https://silentzero.ooo/wiki/sources/nd-sel4-sel4-roadmap.html.md) |
| Integrity and confidentiality (no timing channels) | proven on AArch32, AArch64, RISC-V; not stated for MCS | proof; on AArch64 a news item of 24 August 2026 also announces the confidentiality proof | [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md), [security proofs complete on AArch64](https://silentzero.ooo/wiki/sources/2026-proofcraft-sel4-security-proofs.html.md) |
| Binary correctness | listed for AArch32 only; other architectures not stated | proof | [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) |
| Verified kernel under Microkit on the Raspberry Pi 4 | none: the Pi 4B is verified only without MCS, and Microkit always uses MCS | our reading from two sources | [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md), [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md) |
| Kernel boot, IOMMU/SMMU | outside every verified configuration | assumed | [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) |
| Processor time as capability with enforced budgets | implemented in MCS | covered by the C-level refinement proof in our reading; no theorem on temporal isolation | [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md), [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md) |
| Containment of a compromised component in the field | demonstrated under a white-box red-team attack, 2017 | test | [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md) |
| Sound kernel WCET on 32-bit Arm before MCS | existed, archived | static analysis; loop bounds set by hand on ARM11, later proved by translation validation (processor not stated) | [WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md), [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md), [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md) |
| WCET of the MCS kernel on 64-bit RISC-V | runs, placeholder values | none yet: no bound | [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md) |
| Sound instruction latencies for CVA6 | expected Q1 2027 | to be proved against the design | [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md) |
| Schedulability framework for MCS | planned, September 2027 | none yet | [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md) |
| Time protection against timing channels | implemented in research versions on Arm, x86, RISC-V; proof in progress | measurement on prototypes; no proof | [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md), [Where are we with Time Protection?](https://silentzero.ooo/wiki/sources/2026-trustworthy-where-are-we.html.md) |

No current seL4 has a WCET bound on a 64-bit core. Budgets keep an agent from taking more than its share of time, but a deadline also needs the kernel's WCET and a schedulability analysis, and neither exists yet for MCS.

## How the paper uses these sources

- Section 3 cites the seL4 roadmap (seL4 Foundation n.d.-b) for "Its C-level verification is complete for RISC-V"; the primary source is now in the wiki, [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md), which could be cited directly.
- Section 4 cites [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md) for "Provable schedulability for MCS remains ongoing research". Confirmed: the slides give September 2027 for the schedulability framework.
- Section 2.3 cites [seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md) for the cost of the first proof ("roughly 25 person-years", a repeat "under ten"). The source gives about 22 in total and estimates 8 for a repeat; the project page the paper also cites gives about 25 and a repeat under ten ([Trustworthy Systems n.d.: Proof Statistics](https://silentzero.ooo/wiki/sources/nd-trustworthy-proof-statistics.html.md)). Confirmed against that page, which counts documentation in its total. The same sentence says the proof "covered about 8,700 lines of C"; the page says 7,500 of 8,700 lines were verified.
- Section 3 cites [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) for boot and IOMMU lying outside the proof, and the roadmap for AArch64 in the third quarter of 2027. Both are confirmed: [seL4 Foundation: Development roadmap](https://silentzero.ooo/wiki/sources/nd-sel4-sel4-roadmap.html.md) says "C verification completed for RISC-V, to complete for AArch64 Q3/27" for the MCS extensions.
- Section 4 cites [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md) for HACMS. The full text confirms the paper's account.
- Sections 3 and 4 cite [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md) for time as a protected resource. The slides confirm it.
- Section 4 says closing timing side channels needs a hardware instruction that exists only as prototypes, citing [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md). Confirmed for on-core state; [Where are we with Time Protection?](https://silentzero.ooo/wiki/sources/2026-trustworthy-where-are-we.html.md) shows the proof of time protection for seL4 still in progress.

## Open

- Which 32-bit cores the old analysis covered. Section 4 of the paper says seL4's sound WCET analysis existed "only for the ARM11 processor", following [WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md). The sources conflict. The archived page names ARM11; [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md) (§1) says the *first* analysis, Blackham et al. 2011, was on Armv7; the current project page [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md) and the slides [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md) say Armv6 and Armv7. The ARM1136 is an Armv6 core ([seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md), §5.1). All agree the work covered 32-bit Arm before MCS, and the archived page adds that on ARM11 the loop bounds were set by hand. Our reading: "only for ARM11" is narrower than three sources and "sound and complete" is stronger than the archived page for that core; "32-bit Arm, before MCS" is safe. Blackham et al. 2011 and Sewell et al. 2016, not yet covered here, would settle it.
- What Arm's latencies change. Section 4 of the paper says Arm stopped publishing latencies "for its out-of-order cores" and concludes that only an open RISC-V core puts a proof of timing within reach. [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md) (footnote 1) says Arm stopped for its in-order cores as well and has resumed for them, and plans the analysis on an in-order Armv8 core. Our reading: the paper's conclusion still holds for latencies *proved* against the hardware design, since Arm's would rest on vendor documentation and stay *assumed*; only the wording "for its out-of-order cores" is narrower than the source.
- **Kernel loops without a static bound.** Capability lookups, message cancellation and the MCS scheduling queues walk structures sized at run time, and system design has to bound them ([Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md), §5.1). The project plans WCET per kernel operation, so that a system that never destroys objects after boot gets a lower bound ([Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)). Our reading: a static system fixes object counts and rights at build time, which should help with both. It is open whether that yields the bounds the analysis needs.
- The sources say nothing about whether the integrity and confidentiality proofs have been carried to the MCS configuration. Since Microkit always uses MCS, every Microkit-based Silent Zero lacks them for now, and the [The broker](https://silentzero.ooo/wiki/design/broker.html.md) relies on integrity.
- The MCS proof is a functional-correctness proof. No source states a theorem that budgets keep one component from taking another's processor time; for Silent Zero's claim that an agent cannot starve the control loop, that is *implemented*, not *proven*.
- **The broker's time.** In MCS a passive server runs on its client's budget ([MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)). Whether the Silent Zero broker should be such a server is a design question for the [The static system](https://silentzero.ooo/wiki/design/static-system.html.md).

## Not yet in the wiki

The multicore proof itself. See also [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md) and, for the layer above, [The static system](https://silentzero.ooo/wiki/design/static-system.html.md).

## Sources

- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)
- [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)
- [release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md)
- [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md)
- [security proofs complete on AArch64](https://silentzero.ooo/wiki/sources/2026-proofcraft-sel4-security-proofs.html.md)
- [seL4 Foundation: Development roadmap](https://silentzero.ooo/wiki/sources/nd-sel4-sel4-roadmap.html.md)
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md)
- [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md)
- [Trustworthy Systems n.d.: Proof Statistics](https://silentzero.ooo/wiki/sources/nd-trustworthy-proof-statistics.html.md)
- [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)
- [WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)
- [Where are we with Time Protection?](https://silentzero.ooo/wiki/sources/2026-trustworthy-where-are-we.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [The static system](https://silentzero.ooo/wiki/design/static-system.html.md)
- [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md)
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md)
- [Raspberry Pi](https://silentzero.ooo/wiki/systems/raspberry-pi.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [SiFive and the HiFive boards](https://silentzero.ooo/wiki/systems/sifive-hifive.html.md)
- [Anthropic 2026a: Project Glasswing, securing critical software for the AI era](https://silentzero.ooo/wiki/sources/2026-anthropic-project-glasswing-securing.html.md)
- [Instruction Sets Should Be Free](https://silentzero.ooo/wiki/sources/2014-asanovic-instruction-sets-free.html.md)
- [seL4 on PC99 (x86-64)](https://silentzero.ooo/wiki/sources/nd-sel4-x64-platform.html.md)
- [SiFive: HiFive Unleashed](https://silentzero.ooo/wiki/sources/nd-sifive-hifive-unleashed.html.md)
- [The RISC-V Instruction Set Manual, Volume I](https://silentzero.ooo/wiki/sources/2024-riscv-unprivileged-isa-manual.html.md)
- [Verus, a practical foundation for systems verification](https://silentzero.ooo/wiki/sources/2024-lattuada-verus-practical-foundation.html.md)
