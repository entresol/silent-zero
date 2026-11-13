---
type: source
id: 2026-heiser-sel4-operating-systems
status: reviewed
read: full
kind: survey
sources: [2026-heiser-sel4-operating-systems]
updated: 2026-11-13
---

# Heiser 2026: seL4 for reliability

Gernot Heiser (UNSW Sydney). "seL4: Operating Systems With the Reliability of Mathematics". IEEE Reliability Magazine 3(2), pp. 55–62, June 2026 (published online 30 April 2026), [doi:10.1109/MRL.2026.3680074](https://doi.org/10.1109/MRL.2026.3680074); [abstract and PDF at Trustworthy Systems](https://trustworthy.systems/publications/papers/Heiser_26.abstract). Open access under CC BY 4.0. Read in full, text only; the figures were not read beyond their captions.

## What it shows

An overview by its author, a UNSW professor, of what seL4's proofs cover and what they do not, written for reliability engineers. The article gives no new measurements. Its statements, by section:

- **Proof scope.** The core is functional correctness of the C code. It assumes the small amount of assembly, the boot code and a correct understanding of the hardware. Proofs of confidentiality, integrity and availability compose with it. A translation-validation toolchain takes the compiler out of the trusted base and links to the formal Arm and RISC-V ISA specifications ("seL4 microkernel").
- **What the verification does not cover, as of writing.** It applies to a single-core configuration; a multikernel configuration is in progress. Timing channels cannot be excluded, because the ISA abstracts over timing; work on this is in progress. The Arm64 confidentiality proof "is expected to be completed mid-year". The mechanisms for controlling the time resource (MCS) are not yet verified, with verification "expected to be completed in 2027" (sections "seL4 microkernel", "Memory management", and the closing section).
- **WCET.** seL4 had a sound and complete analysis, made for Armv6 and stale because Arm stopped publishing instruction latencies, and the group has "recently re-established" it for open-source 64-bit RISC-V cores. The article calls seL4 the only protected-mode kernel known to have such an analysis.
- **Cost.** The initial functional-correctness proof took 11 person-years, not counting reusable frameworks, and 200,000 lines of proof script for 8,500 lines of C; the proof base is now well over a million lines. Proof effort grows quadratically with specification size, so the kernel is kept small (about 10–12 kSLOC).
- **Capabilities and memory.** No ambient authority, hence no confused deputy of the access-list kind; the kernel hands all free memory to an initial task and needs no heap, so the kernel cannot run out of memory, and a client cannot use up memory to attack another part of the system (the article says this for memory only, time being treated separately); capabilities are revocable. A VMM is outside the trusted base.
- **LionsOS.** A static system composed from small components. An i.MX8 Ethernet driver has 569 lines against 4,775 for the Linux driver and was written by a second-year student. Unmodified Linux drivers run in VMs with a large trusted base, behind an IOMMU. Most components of the point-of-sale reference design have fewer than 500 lines; initial explorations, by the author's account, show that verifying such small components with automated tools is feasible, given that seL4 enforces the interfaces. Verification of LionsOS "is expected to be completed in 2027", under the PISTIs-V project; the same programme funds the multikernel verification.
- **Deployment.** The article names the 2021 DARPA drone challenge, NIO cars from 2024 and an aircraft-ground voice system, and says that seL4 is hard to use without a framework.

## How

A feature article. Claims are the author's, with references to the group's papers; there is no experiment or method section.

## Limits

What the article says itself: the proofs depend on their assumptions and on correct hardware, and it names Rowhammer and physical manipulation as outside them. A careful reader adds: the statements on proof status carry the article's dates (published online 30 April, current version 26 June 2026) and have dated. The wiki has newer sources for two of them, noted below. The deployment claims and the LionsOS figures are the author's own, from the author's own group.

## Against the wiki

- [[sel4]]: confirms the single-core scope and the boot code as a proof assumption; it does not say that the IOMMU lies outside the proofs, which the wiki takes from [[nd-sel4-verified-configurations]]. Extends it with a second primary source on the MCS proof status. The article's "MCS unverified, expected 2027" has a version date three days before the announcement of 29 June 2026 that the MCS configuration has a functional-correctness proof on RISC-V ([[2026-sel4-functional-correctness-proof]]); the article's date of current version is 26 June. Our reading: the article was probably finished before that announcement, so the two do not conflict; it does not say so.
- [[sel4]], [[kernel]]: the AArch64 confidentiality proof "expected mid-year" matches the news item of 24 August 2026 reporting it finished ([[2026-proofcraft-sel4-security-proofs]]).
- Cost of the first proof: this article gives 11 person-years, 200,000 lines of proof script and 8,500 lines of C. The wiki holds 8,700 lines of C and 600 of assembler ([[2009-klein-sel4-formal-verification]]) and the project page's 7,500 verified lines ([[nd-trustworthy-proof-statistics]]). The article cites Klein et al. 2014 for its figure and does not say how it counts. The 11 person-years match the seL4-specific share named in [[2009-klein-sel4-formal-verification]].
- [[lionsos]]: extends it with the driver size comparison and the 2027 verification target. The Linux-driver-in-VM point matches [[2026-heiser-mcs-safety-os]].
- [[wcet-analysis]]: says the analysis was "recently re-established" for open-source 64-bit RISC-V cores, with no detail. The paper and [[2026-sillitoe-resurrecting-sel4-wcet]] describe it as still using placeholder latencies; the article does not contradict that, and adds no bound.

## For zOS

[[kernel]]: no row changes state. The article supports, as a second primary statement, that single-core is the verified scope and that the MCS time mechanisms were outside the proof when it was written. It also gives a 2027 target for the LionsOS verification, which bears on [[drivers]] and [[static-system]]. Nothing in it contradicts this wiki.
