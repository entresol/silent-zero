---
type: design
status: reviewed
sources: [2025-heiser-fast-secure-adaptable, 2022-parker-sel4-device-driver, 2026-tyler-smt-based-deductive, 2026-trustworthy-lionsos, 2026-heiser-mcs-safety-os, nd-sel4-microkit-user-manual, nd-sel4-verified-configurations, 2009-klein-sel4-formal-verification, 2019-markettos-thunderclap-exploring-vulnerabilities, 2024-trail-leftoverlocals-listening-llm]
updated: 2026-11-03
---

# Drivers

In zOS drivers run in user mode, each with access only to its own device. Legacy drivers, above all for graphics and AI accelerators, run in a Linux virtual machine on the agent's side. Where a device can write to memory directly and the IOMMU configuration is not proven, the driver joins the trusted base as *assumed* (paper, Section 3).

## What it must do

- Keep a faulty or hostile driver from reaching beyond its device and its queues.
- On the motion path, be correct, because a wrong command to a motor is a safety failure.
- Keep devices that write to memory directly within bounds.

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| Drivers as user-level programs, except the kernel's timer | since the first seL4 | design | [[2009-klein-sel4-formal-verification]] |
| sDDF: single-threaded drivers, lock-free queues, the driver never touching the data | in use in LionsOS | design, benchmarks on slides | [[2022-parker-sel4-device-driver]], [[2026-trustworthy-lionsos]] |
| Performance comparable to or better than Linux | measured for networking and SD storage on Arm and x86, plotted figures, no worst case | measurement, by the system's authors | [[2025-heiser-fast-secure-adaptable]], [[2022-parker-sel4-device-driver]], [[2026-heiser-mcs-safety-os]] |
| A Pancake version of a LionsOS Ethernet driver, and the queue library, follow the device and OS protocols, move buffers correctly and meet a completion condition | proven, 2026 | SMT-based proof; trusted: the transpiler, the Viper backend and solver, a hand-written weak-memory encoding, a device model taken from the manual; the OS side is assumed to keep its queue contracts | [[2026-tyler-smt-based-deductive]] |
| Other LionsOS drivers verified | under way | none yet | [[2026-trustworthy-lionsos]] |
| Unmodified Linux drivers in a driver VM | available in LionsOS; drivers shown: GPU framebuffer, Ethernet, SD block, sound on one Arm board; a few weeks per device class | design and use | [[2025-heiser-fast-secure-adaptable]], [[2026-heiser-mcs-safety-os]] |
| Each driver sees only its own device | a configuration choice in Microkit; only interrupts are exclusive to one PD | design | [[nd-sel4-microkit-user-manual]] |
| IOMMU/SMMU covered by the kernel proof | no verified configuration covers it | assumed | [[nd-sel4-verified-configurations]] |
| An enabled IOMMU keeps a malicious device out of kernel memory | not so in general: attacks worked on macOS, FreeBSD and Linux with the IOMMU on; Windows mostly did not use it (2019, Intel and AMD hardware) | tests on nine machines | [[2019-markettos-thunderclap-exploring-vulnerabilities]] |

## The paper and its sources

- Section 3's "each with access only to its own device registers (Parker 2022)": the slides support user-mode drivers with fewer privileges, not this wording. Our reading: [[microkit]] lets the system description give each driver only its own registers, but does not enforce that, except for interrupts.
- Section 6 says devices that write to memory directly "have defeated IOMMU protection in Linux, macOS and FreeBSD" (Markettos et al. 2019). [[2019-markettos-thunderclap-exploring-vulnerabilities]] confirms it, with two qualifications: on Linux and FreeBSD the authors had to switch the IOMMU on, and Windows was open too, because it mostly did not use the IOMMU. The tests ran on Intel and AMD machines in 2019; the Arm SMMU was not tested. See [[iommu]].
- Section 5 and In brief on the verified Ethernet driver: confirmed by [[2026-tyler-smt-based-deductive]], with the trusted parts listed above. Whether LionsOS ships the verified Pancake driver is not stated.
- The driver VM is cited to Heiser et al. 2025 ([[2025-heiser-fast-secure-adaptable]]), which shows a framebuffer, Ethernet, SD and sound driver in VMs. The paper's "above all graphics and AI accelerators" goes beyond that list: no accelerator appears there.

- Section 6 says GPUs "have leaked memory between processes" with one flaw exposing about 181 MB per query (Trail of Bits 2024). [[2024-trail-leftoverlocals-listening-llm]] confirms it for AMD, Apple and Qualcomm GPUs from the authors' tests, and for some Imagination GPUs on Google's confirmation, as of January 2024; the 181 MB was measured on an AMD Radeon RX 7900 XT with a 7B model in llama.cpp. Our reading: the leak occurs inside the GPU, which the source does not relate to IOMMUs, so a driver VM that passes a GPU through would inherit whatever isolation the GPU itself gives.

## Open

- No verified driver for a bus to motor controllers (serial, CAN, I²C) exists in the sources, though drivers on the motion path are where correctness matters most.
- The verified driver's device model is translated from the manual by hand; specifications from the device's Verilog are work in progress ([[2026-tyler-smt-based-deductive]], §3.3.1).
- Microkit describes IO address spaces backed by an IOMMU or SMMU in general terms, and states the mapping explicitly only for x86 ([[nd-sel4-microkit-user-manual]]); no verified kernel configuration covers the IOMMU. Whether the pib's Raspberry Pi has an IOMMU at all is not answered by a source in the wiki.
- Which Thunderclap attack classes reach a system whose drivers run in user mode with page-aligned buffers is not answered by any source in the wiki; our reading is in [[2019-markettos-thunderclap-exploring-vulnerabilities]].
