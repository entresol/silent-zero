# seL4

> The verified microkernel Silent Zero builds on: proofs per architecture and platform, cost, MCS, timing, HACMS; what its foundation says about certification.

System · LLM reviewed · updated 2026-11-21 · 17 sources · https://silentzero.ooo/wiki/systems/sel4.html

A microkernel of the L4 family whose C implementation has a machine-checked proof of [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md), first completed in 2009 for ARMv6 ([seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md)). It provides a minimal set of mechanisms: threads, capabilities, virtual address spaces, IPC, notifications and interrupt delivery ([Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md), §3.1). Drivers run in user mode, except the kernel's timer ([seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md), §3.3, §3.4). Its proofs are in Isabelle/HOL in the `seL4/l4v` repository ([seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)).

## Proofs, October 2026

| Property | Where | Source |
| --- | --- | --- |
| Functional correctness at C level | AArch32, AArch64, RISC-V, x86-64, in the verified configurations; fast path covered on Arm only | [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) |
| Integrity and confidentiality (storage channels, not timing) | AArch32, AArch64, RISC-V; not stated for MCS | [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md); [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md), §3.2; on AArch64 also the seL4 news item of 24 August 2026, which says the confidentiality proof is finished there and security isolation complete under listed assumptions; `CAVEATS.md` of 17.0.0 says "in progress" for AArch64 with hypervisor extensions, see [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md) ([security proofs complete on AArch64](https://silentzero.ooo/wiki/sources/2026-proofcraft-sel4-security-proofs.html.md), [release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md)) |
| Binary correctness | listed for AArch32 | [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) |
| Functional correctness of the MCS configuration | RISC-V, announced 29 June 2026; port to 64-bit Arm under DARPA's PROVERS programme | [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md) |
| Platforms with the C-level proof | since release 17.0.0 (30 October 2026), by the release notes' own words, "all 64-bit platforms seL4 support"; they list eight RISC-V platforms and fifteen AArch64 ones. The MCS proof on RISC-V covers `hifive` (HiFive Unleashed) only | [release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md) |
| Kernel boot, [IOMMU](https://silentzero.ooo/wiki/concepts/iommu.html.md) and SMMU, debug interfaces | not covered by any verified configuration | [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) |
| Multicore | verification in progress; the verified scope is single-core, with a multikernel configuration under way | [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md); [seL4 for reliability](https://silentzero.ooo/wiki/sources/2026-heiser-sel4-operating-systems.html.md) (article dated April to June 2026); slides of September 2026 compare SMP and multikernel by benchmark and state no proof status ([Trustworthy Systems R&D update](https://silentzero.ooo/wiki/sources/2026-heiser-trustworthy-systems-update.html.md)) |

An overview by Heiser (published 30 April, current version 26 June 2026) says the MCS time mechanisms were then outside the proofs, with verification expected in 2027; its version date is three days before the announcement of 29 June 2026 above ([seL4 for reliability](https://silentzero.ooo/wiki/sources/2026-heiser-sel4-operating-systems.html.md)). The documentation page's RISC-V section still called the MCS verification ongoing on 23 October 2026 ([seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)).

The verification of Microkit's main handler loop by Paturel et al. assumes Hoare triples about seL4 system calls that have not been proved; proving them, including blocking Recv, is ongoing at UNSW ([two interfaces for seL4 kernel verification](https://silentzero.ooo/wiki/sources/2026-sison-two-interfaces-sel4.html.md), §2). See [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md).

## Size and cost

8,700 lines of C and 600 of assembler in 2009 ([seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md)); about 10,000 lines of C later ([Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md), §3; [WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)); just over 11,000 lines in the 64-bit RISC-V build analysed in 2026 ([Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md), §3). The first proof took about 20 person-years, 11 of them seL4-specific ([seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md), §5.2); all seL4-specific proofs to 2018 add up to 18 ([Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md), sidebar). The group's project page gives about 25 person-years for design, documentation, implementation and verification together, a repeat under ten, about 200,000 lines of Isabelle proof script for the 2009 kernel and about 500,000 lines of proof files by 2015. It counts 160 bugs found in the C code, 144 of them during verification, and says the assembler and the boot code, 1,200 lines, are unverified ([Trustworthy Systems n.d.: Proof Statistics](https://silentzero.ooo/wiki/sources/nd-trustworthy-proof-statistics.html.md)). In 2026 a method with a small language model and Isabelle as checker re-proved 77.6 per cent of the still-valid theorems in three evaluation splits of the FVEL benchmark, drawn from seL4's proofs ([Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md)). Heiser's 2026 overview gives 11 person-years, 200,000 lines of proof script and 8,500 lines of C for the first proof, citing Klein et al. 2014; its count of C lines differs from the two above, and it says the proof base is now well over a million lines ([seL4 for reliability](https://silentzero.ooo/wiki/sources/2026-heiser-sel4-operating-systems.html.md)). See [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md).

## Time

- **MCS** makes processor time a capability with budget and period. See [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md).
- **WCET.** A sound analysis existed for 32-bit Arm before MCS and was archived when Arm stopped publishing instruction latencies ([WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md), [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)). In the words of Sillitoe et al., seL4 thereby "lost any hard real-time guarantees" (§1). Since 2026 the analysis runs again on 64-bit RISC-V for the MCS configuration, still with placeholder values ([Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md)). See [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md).

## Certification

The seL4 Foundation argues that the proofs go beyond what Common Criteria EAL 7 and the automotive standard ISO 26262 (ASIL-D) require, and that they fit evidence objectives of DO-178C Level A. Its page names no certificate and no certified product, does not mention IEC 61508, and says that, to its knowledge, Isabelle/HOL has not yet been qualified for a DO-178C certification ([seL4 Foundation: seL4 proofs and certification](https://silentzero.ooo/wiki/sources/nd-sel4-proofs-certification.html.md)). See [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md).

## In use

Under DARPA's HACMS programme, seL4 carried the mission computer of Boeing's Unmanned Little Bird, which stayed safe under a mid-flight cyberattack in 2017 ([Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)). A 2026 talk abstract describes a project for Army ground vehicles that is building ROS 2 on seL4 as a separation kernel; it reports proofs of concept for two configurations, and the security services are planned ([ARSENAL](https://silentzero.ooo/wiki/sources/2026-lide-arsenal-assured-robotics.html.md)).

## Performance

Round-trip IPC on Intel Skylake: 986 cycles, against 2,717 for Fiasco.OC and 8,157 for Zircon, from Mi et al. 2019 as cited in [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md).

## Not yet in the wiki

CAmkES, the multicore proof. The roadmap is in [seL4 Foundation: Development roadmap](https://silentzero.ooo/wiki/sources/nd-sel4-sel4-roadmap.html.md). See also [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md); systems built on seL4: [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md), [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md), [KataOS](https://silentzero.ooo/wiki/systems/kataos.html.md), [Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md).

## Sources

- [Announcing KataOS and Sparrow](https://silentzero.ooo/wiki/sources/2022-google-announcing-kataos-sparrow.html.md)
- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)
- [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)
- [Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md)
- [release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md)
- [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md)
- [security proofs complete on AArch64](https://silentzero.ooo/wiki/sources/2026-proofcraft-sel4-security-proofs.html.md)
- [seL4 for reliability](https://silentzero.ooo/wiki/sources/2026-heiser-sel4-operating-systems.html.md)
- [seL4 Foundation: seL4 proofs and certification](https://silentzero.ooo/wiki/sources/nd-sel4-proofs-certification.html.md)
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)
- [seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md)
- [Trustworthy Systems n.d.: Proof Statistics](https://silentzero.ooo/wiki/sources/nd-trustworthy-proof-statistics.html.md)
- [Trustworthy Systems R&D update](https://silentzero.ooo/wiki/sources/2026-heiser-trustworthy-systems-update.html.md)
- [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)
- [two interfaces for seL4 kernel verification](https://silentzero.ooo/wiki/sources/2026-sison-two-interfaces-sel4.html.md)
- [WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)

## Related pages

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md)
- [IOMMU](https://silentzero.ooo/wiki/concepts/iommu.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md)
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md)
- [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md)
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md)
- [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md)
- [Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md)
- [KataOS](https://silentzero.ooo/wiki/systems/kataos.html.md)
- [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md)
- [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md)
- [NVIDIA Halos for Robotics](https://silentzero.ooo/wiki/systems/nvidia-halos.html.md)
- [PikeOS](https://silentzero.ooo/wiki/systems/pikeos.html.md)
- [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md)
- [agentOS, an operating system for agents on seL4](https://silentzero.ooo/wiki/sources/2026-hubbard-agentos-operating-system.html.md)
- [Anthropic 2026a: Project Glasswing, securing critical software for the AI era](https://silentzero.ooo/wiki/sources/2026-anthropic-project-glasswing-securing.html.md)
- [ARSENAL](https://silentzero.ooo/wiki/sources/2026-lide-arsenal-assured-robotics.html.md)
- [AutoRocq](https://silentzero.ooo/wiki/sources/2025-tu-agentic-verification-software.html.md)
- [Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md)
- [Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md)
- [OSVBench](https://silentzero.ooo/wiki/sources/2025-li-osvbench-benchmarking-llms.html.md)
- [Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md)
- [seL4 Foundation: Development roadmap](https://silentzero.ooo/wiki/sources/nd-sel4-sel4-roadmap.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md)
- [Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md)
- [Verifying Device Drivers with Pancake](https://silentzero.ooo/wiki/sources/2025-zhao-verifying-device-drivers.html.md)
