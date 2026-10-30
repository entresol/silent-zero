---
type: design
status: reviewed
sources: [nd-sel4-microkit-user-manual, 2022-wistoff-systematic-prevention-core, 2026-trustworthy-where-are-we, 2009-klein-sel4-formal-verification, 2018-klein-formally-verified-software, nd-sel4-verified-configurations, 2026-sel4-functional-correctness-proof, 2026-heiser-mcs-safety-os, 2026-trustworthy-guaranteeing-timeliness-mcs, nd-trustworthy-wcet-worst-case, 2026-sillitoe-resurrecting-sel4-wcet]
updated: 2026-10-29
---

# The kernel

In zOS the kernel is [[sel4]] with its mixed-criticality extensions. It isolates components, moves messages between them and hands out processor time, and it is the only code at its privilege level (paper, Section 3).

## What it must do

- **Isolate in space.** No component may read or write another's memory or gain authority it was not given.
- **Isolate in time.** An agent that loops or is hijacked must not take the control loop's processor time. See [[mixed-criticality]].
- **Bound its own execution time.** The control loops can keep a deadline only if the kernel beneath them has a bound on its own execution time. See [[wcet-analysis]].

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| Functional correctness of the C code | proven, for the verified configurations | refinement proof in Isabelle/HOL | [[2009-klein-sel4-formal-verification]], [[nd-sel4-verified-configurations]] |
| Functional correctness of the MCS kernel on RISC-V | proven, announced June 2026 (the announcement names neither the level nor 64-bit; RISC-V verified configurations are 64-bit and C-level, per [[nd-sel4-verified-configurations]]) | proof, announced | [[2026-sel4-functional-correctness-proof]] |
| MCS on 64-bit Arm | under way | none yet | [[2026-sel4-functional-correctness-proof]] |
| Integrity and confidentiality (no timing channels) | proven on AArch32, AArch64, RISC-V; not stated for MCS | proof | [[nd-sel4-verified-configurations]] |
| Binary correctness | listed for AArch32 only; other architectures not stated | proof | [[nd-sel4-verified-configurations]] |
| Verified kernel under Microkit on the Raspberry Pi 4 | none: the Pi 4B is verified only without MCS, and Microkit always uses MCS | our reading from two sources | [[nd-sel4-verified-configurations]], [[nd-sel4-microkit-user-manual]] |
| Kernel boot, IOMMU/SMMU | outside every verified configuration | assumed | [[nd-sel4-verified-configurations]] |
| Processor time as capability with enforced budgets | implemented in MCS | covered by the C-level refinement proof in our reading; no theorem on temporal isolation | [[2026-heiser-mcs-safety-os]], [[2026-sel4-functional-correctness-proof]] |
| Containment of a compromised component in the field | demonstrated under a white-box red-team attack, 2017 | test | [[2018-klein-formally-verified-software]] |
| Sound kernel WCET on 32-bit Arm before MCS | existed, archived | static analysis; loop bounds set by hand on ARM11, later proved by translation validation (processor not stated) | [[nd-trustworthy-wcet-worst-case]], [[2026-sillitoe-resurrecting-sel4-wcet]], [[2026-trustworthy-guaranteeing-timeliness-mcs]] |
| WCET of the MCS kernel on 64-bit RISC-V | runs, placeholder values | none yet: no bound | [[2026-sillitoe-resurrecting-sel4-wcet]] |
| Sound instruction latencies for CVA6 | expected Q1 2027 | to be proved against the design | [[2026-sillitoe-resurrecting-sel4-wcet]] |
| Schedulability framework for MCS | planned, September 2027 | none yet | [[2026-heiser-mcs-safety-os]] |
| Time protection against timing channels | implemented in research versions on Arm, x86, RISC-V; proof in progress | measurement on prototypes; no proof | [[2022-wistoff-systematic-prevention-core]], [[2026-trustworthy-where-are-we]] |

No current seL4 has a WCET bound on a 64-bit core. Budgets keep an agent from taking more than its share of time, but a deadline also needs the kernel's WCET and a schedulability analysis, and neither exists yet for MCS.

## How the paper uses these sources

- Section 3 cites the seL4 roadmap (seL4 Foundation n.d.-b) for "Its C-level verification is complete for RISC-V"; the primary source is now in the wiki, [[2026-sel4-functional-correctness-proof]], which could be cited directly.
- Section 4 cites [[2026-heiser-mcs-safety-os]] for "Provable schedulability for MCS remains ongoing research". Confirmed: the slides give September 2027 for the schedulability framework.
- Section 2.3 cites [[2009-klein-sel4-formal-verification]] for the cost of the first proof ("roughly 25 person-years", a repeat "under ten"). The source gives about 22 in total and estimates 8 for a repeat; the paper also cites a project page not yet in the wiki.
- Section 3 cites [[nd-sel4-verified-configurations]] for boot and IOMMU lying outside the proof, and the roadmap for AArch64 in the third quarter of 2027. The first is confirmed; the roadmap is not yet in the wiki.
- Section 4 cites [[2018-klein-formally-verified-software]] for HACMS. The full text confirms the paper's account.
- Sections 3 and 4 cite [[2026-heiser-mcs-safety-os]] for time as a protected resource. The slides confirm it.
- Section 4 says closing timing side channels needs a hardware instruction that exists only as prototypes, citing [[2022-wistoff-systematic-prevention-core]]. Confirmed for on-core state; [[2026-trustworthy-where-are-we]] shows the proof of time protection for seL4 still in progress.

## Open

- Which 32-bit cores the old analysis covered. Section 4 of the paper says seL4's sound WCET analysis existed "only for the ARM11 processor", following [[nd-trustworthy-wcet-worst-case]]. The sources conflict. The archived page names ARM11; [[2026-sillitoe-resurrecting-sel4-wcet]] (§1) says the *first* analysis, Blackham et al. 2011, was on Armv7; the current project page [[2026-trustworthy-guaranteeing-timeliness-mcs]] and the slides [[2026-heiser-mcs-safety-os]] say Armv6 and Armv7. The ARM1136 is an Armv6 core ([[2009-klein-sel4-formal-verification]], §5.1). All agree the work covered 32-bit Arm before MCS, and the archived page adds that on ARM11 the loop bounds were set by hand. Our reading: "only for ARM11" is narrower than three sources and "sound and complete" is stronger than the archived page for that core; "32-bit Arm, before MCS" is safe. Blackham et al. 2011 and Sewell et al. 2016, not yet covered here, would settle it.
- What Arm's latencies change. Section 4 of the paper says Arm stopped publishing latencies "for its out-of-order cores" and concludes that only an open RISC-V core puts a proof of timing within reach. [[2026-sillitoe-resurrecting-sel4-wcet]] (footnote 1) says Arm stopped for its in-order cores as well and has resumed for them, and plans the analysis on an in-order Armv8 core. Our reading: the paper's conclusion still holds for latencies *proved* against the hardware design, since Arm's would rest on vendor documentation and stay *assumed*; only the wording "for its out-of-order cores" is narrower than the source.
- **Kernel loops without a static bound.** Capability lookups, message cancellation and the MCS scheduling queues walk structures sized at run time, and system design has to bound them ([[2026-sillitoe-resurrecting-sel4-wcet]], §5.1). The project plans WCET per kernel operation, so that a system that never destroys objects after boot gets a lower bound ([[2026-trustworthy-guaranteeing-timeliness-mcs]]). Our reading: a static system fixes object counts and rights at build time, which should help with both. It is open whether that yields the bounds the analysis needs.
- The sources say nothing about whether the integrity and confidentiality proofs have been carried to the MCS configuration. Since Microkit always uses MCS, every Microkit-based zOS lacks them for now, and the [[broker]] relies on integrity.
- The MCS proof is a functional-correctness proof. No source states a theorem that budgets keep one component from taking another's processor time; for zOS's claim that an agent cannot starve the control loop, that is *implemented*, not *proven*.
- **The broker's time.** In MCS a passive server runs on its client's budget ([[2026-heiser-mcs-safety-os]]). Whether the zOS broker should be such a server is a design question for the [[static-system]].

## Not yet in the wiki

The roadmap, the multicore proof. See also [[time-protection]] and, for the layer above, [[static-system]].
