---
type: system
status: reviewed
sources: [2025-heiser-fast-secure-adaptable, 2026-trustworthy-lionsos, 2026-heiser-mcs-safety-os, 2022-parker-sel4-device-driver, 2026-tyler-smt-based-deductive, 2026-heiser-sel4-operating-systems, 2026-heiser-trustworthy-systems-update]
glossary: LionsOS
updated: 2026-11-14
---

# LionsOS

An operating system from composable components on [[sel4]] and [[microkit]], from the Trustworthy Systems group at UNSW Sydney ([[2026-trustworthy-lionsos]]), aimed at embedded, IoT and cyber-physical uses ([[2026-heiser-mcs-safety-os]]). It is static: it loads no components at run time, but can swap a component for one of the same type ([[2026-trustworthy-lionsos]]).

## State, October 2026

Version 0.4.0, "undergoing active research and development". Base device classes (network, block, serial, I²C) are expected to be mostly stable ([[2026-trustworthy-lionsos]]). A Pancake version of a LionsOS Ethernet driver and the queue library are verified with SMT-based proofs; whether LionsOS ships that version is not stated ([[2026-tyler-smt-based-deductive]]). Verification of the other drivers and components is under way ([[2026-trustworthy-lionsos]]); Heiser expects the verification of LionsOS to be completed in 2027 and says initial explorations show verifying small components, mostly under 500 lines in the reference design, to be feasible ([[2026-heiser-sel4-operating-systems]]).

Slides of September 2026 add a community firewall project, released in November 2025, a virtual network switch, and sDDF support for ACPI and PCIe ([[2026-heiser-trustworthy-systems-update]], slides 5 to 8). The same slides say that [[microkit]] can now start, stop and upgrade protection domains at run time, used by the Carrels project; whether LionsOS uses this is not stated, and the static description above is from the project page.

## Design

- Single-purpose components; a driver only translates between its device and a device-class interface ([[2026-trustworthy-lionsos]], [[2026-tyler-smt-based-deductive]]).
- Lock-free, bounded, single-producer, single-consumer queues in shared memory, zero copy, signalled by notifications ([[2022-parker-sel4-device-driver]], [[2026-heiser-mcs-safety-os]]).
- Virtualisers multiplex devices and translate addresses; copiers separate clients where needed ([[2026-trustworthy-lionsos]], [[2026-heiser-mcs-safety-os]]).
- Unmodified Linux drivers can run in a virtual machine as a driver VM ([[2026-heiser-mcs-safety-os]]).
- Driver size: an i.MX8 Ethernet driver of 569 lines, against 4,775 for the Linux driver, written by a second-year student, according to Heiser's overview; unmodified Linux drivers run in a VM with a large trusted base behind an IOMMU ([[2026-heiser-sel4-operating-systems]]).
- Small code: in a point-of-sale demonstrator the trusted components average about 210 lines ([[2026-heiser-mcs-safety-os]]); the design paper counts about 3.1 kSLOC of trusted code there ([[2025-heiser-fast-secure-adaptable]], §6.2.1).
- Measured against Linux: on a 1 Gb/s Arm board one core carries the full gigabit with a third to spare where Linux plateaus at about 500 Mb/s, with round-trip times three to ten times lower. Free IPC would change little, by the authors' simulation. The numbers are throughput, load and round-trip times, not bounds ([[2025-heiser-fast-secure-adaptable]], §6.3).

The device driver framework behind this design, sDDF, was first presented in 2022 ([[2022-parker-sel4-device-driver]]).

## Licence and code

Not yet covered by the wiki's sources.

## Open questions

- What the run-time swap of components permits, and who may trigger it. See [[static-system]].
- Worst-case latency: the design paper reports none ([[2025-heiser-fast-secure-adaptable]]).
