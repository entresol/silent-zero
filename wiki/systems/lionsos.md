---
type: system
status: reviewed
sources: [2025-heiser-fast-secure-adaptable, 2026-trustworthy-lionsos, 2026-heiser-mcs-safety-os, 2022-parker-sel4-device-driver, 2026-tyler-smt-based-deductive]
glossary: LionsOS
updated: 2026-11-01
---

# LionsOS

An operating system from composable components on [[sel4]] and [[microkit]], from the Trustworthy Systems group at UNSW Sydney ([[2026-trustworthy-lionsos]]), aimed at embedded, IoT and cyber-physical uses ([[2026-heiser-mcs-safety-os]]). It is static: it loads no components at run time, but can swap a component for one of the same type ([[2026-trustworthy-lionsos]]).

## State, October 2026

Version 0.4.0, "undergoing active research and development". Base device classes (network, block, serial, I²C) are expected to be mostly stable ([[2026-trustworthy-lionsos]]). A Pancake version of a LionsOS Ethernet driver and the queue library are verified with SMT-based proofs; whether LionsOS ships that version is not stated ([[2026-tyler-smt-based-deductive]]). Verification of the other drivers and components is under way ([[2026-trustworthy-lionsos]]).

## Design

- Single-purpose components; a driver only translates between its device and a device-class interface ([[2026-trustworthy-lionsos]], [[2026-tyler-smt-based-deductive]]).
- Lock-free, bounded, single-producer, single-consumer queues in shared memory, zero copy, signalled by notifications ([[2022-parker-sel4-device-driver]], [[2026-heiser-mcs-safety-os]]).
- Virtualisers multiplex devices and translate addresses; copiers separate clients where needed ([[2026-trustworthy-lionsos]], [[2026-heiser-mcs-safety-os]]).
- Unmodified Linux drivers can run in a virtual machine as a driver VM ([[2026-heiser-mcs-safety-os]]).
- Small code: in a point-of-sale demonstrator the trusted components average about 210 lines ([[2026-heiser-mcs-safety-os]]); the design paper counts about 3.1 kSLOC of trusted code there ([[2025-heiser-fast-secure-adaptable]], §6.2.1).
- Measured against Linux: on a 1 Gb/s Arm board one core carries the full gigabit with a third to spare where Linux plateaus at about 500 Mb/s, with round-trip times three to ten times lower. Free IPC would change little, by the authors' simulation. The numbers are throughput, load and round-trip times, not bounds ([[2025-heiser-fast-secure-adaptable]], §6.3).

The device driver framework behind this design, sDDF, was first presented in 2022 ([[2022-parker-sel4-device-driver]]).

## Licence and code

Not yet covered by the wiki's sources.

## Open questions

- What the run-time swap of components permits, and who may trigger it. See [[static-system]].
- Worst-case latency: the design paper reports none ([[2025-heiser-fast-secure-adaptable]]).
