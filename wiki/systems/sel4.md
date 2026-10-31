---
type: system
status: reviewed
sources: [2009-klein-sel4-formal-verification, 2018-klein-formally-verified-software, nd-sel4-verified-configurations, 2026-sel4-functional-correctness-proof, 2026-heiser-mcs-safety-os, 2026-trustworthy-guaranteeing-timeliness-mcs, nd-trustworthy-wcet-worst-case, 2026-sillitoe-resurrecting-sel4-wcet, 2026-sel4-release-17]
updated: 2026-10-31
---

# seL4

A microkernel of the L4 family whose C implementation has a machine-checked proof of [[functional-correctness]], first completed in 2009 for ARMv6 ([[2009-klein-sel4-formal-verification]]). It provides a minimal set of mechanisms: threads, capabilities, virtual address spaces, IPC, notifications and interrupt delivery ([[2018-klein-formally-verified-software]], §3.1). Drivers run in user mode, except the kernel's timer ([[2009-klein-sel4-formal-verification]], §3.3, §3.4). Its proofs are in Isabelle/HOL in the `seL4/l4v` repository ([[nd-sel4-verified-configurations]]).

## Proofs, October 2026

| Property | Where | Source |
| --- | --- | --- |
| Functional correctness at C level | AArch32, AArch64, RISC-V, x86-64, in the verified configurations; fast path covered on Arm only | [[nd-sel4-verified-configurations]] |
| Integrity and confidentiality (storage channels, not timing) | AArch32, AArch64, RISC-V; not stated for MCS | [[nd-sel4-verified-configurations]]; [[2018-klein-formally-verified-software]], §3.2 |
| Binary correctness | listed for AArch32 | [[nd-sel4-verified-configurations]] |
| Functional correctness of the MCS configuration | RISC-V, announced 29 June 2026; port to 64-bit Arm under DARPA's PROVERS programme | [[2026-sel4-functional-correctness-proof]] |
| Platforms with the C-level proof | since release 17.0.0 (30 October 2026), by the release notes' own words, "all 64-bit platforms seL4 support"; they list eight RISC-V platforms and fifteen AArch64 ones. The MCS proof on RISC-V covers `hifive` (HiFive Unleashed) only | [[2026-sel4-release-17]] |
| Kernel boot, IOMMU and SMMU, debug interfaces | not covered by any verified configuration | [[nd-sel4-verified-configurations]] |
| Multicore | verification in progress | [[2026-heiser-mcs-safety-os]] |

The documentation page's RISC-V section still called the MCS verification ongoing on 23 October 2026 ([[nd-sel4-verified-configurations]]).

## Size and cost

8,700 lines of C and 600 of assembler in 2009 ([[2009-klein-sel4-formal-verification]]); about 10,000 lines of C later ([[2018-klein-formally-verified-software]], §3; [[nd-trustworthy-wcet-worst-case]]); just over 11,000 lines in the 64-bit RISC-V build analysed in 2026 ([[2026-sillitoe-resurrecting-sel4-wcet]], §3). The first proof took about 20 person-years, 11 of them seL4-specific ([[2009-klein-sel4-formal-verification]], §5.2); all seL4-specific proofs to 2018 add up to 18 ([[2018-klein-formally-verified-software]], sidebar).

## Time

- **MCS** makes processor time a capability with budget and period. See [[mixed-criticality]].
- **WCET.** A sound analysis existed for 32-bit Arm before MCS and was archived when Arm stopped publishing instruction latencies ([[nd-trustworthy-wcet-worst-case]], [[2026-trustworthy-guaranteeing-timeliness-mcs]]). In the words of Sillitoe et al., seL4 thereby "lost any hard real-time guarantees" (§1). Since 2026 the analysis runs again on 64-bit RISC-V for the MCS configuration, still with placeholder values ([[2026-sillitoe-resurrecting-sel4-wcet]]). See [[wcet-analysis]].

## In use

Under DARPA's HACMS programme, seL4 carried the mission computer of Boeing's Unmanned Little Bird, which stayed safe under a mid-flight cyberattack in 2017 ([[2018-klein-formally-verified-software]]).

## Performance

Round-trip IPC on Intel Skylake: 986 cycles, against 2,717 for Fiasco.OC and 8,157 for Zircon, from Mi et al. 2019 as cited in [[2026-heiser-mcs-safety-os]].

## Not yet in the wiki

CAmkES, the roadmap, the multicore proof. See also [[time-protection]]; systems built on seL4: [[microkit]], [[lionsos]].
