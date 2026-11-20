# LionsOS

> Static OS from small components on seL4 and Microkit; first driver verified; Summit 2026 talks on x86-64 VMs and driver specifications.

System · LLM reviewed · updated 2026-11-16 · 9 sources · https://silentzero.ooo/wiki/systems/lionsos.html

An operating system from composable components on [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md) and [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md), from the Trustworthy Systems group at UNSW Sydney ([Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md)), aimed at embedded, IoT and cyber-physical uses ([MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)). It is static: it loads no components at run time, but can swap a component for one of the same type ([Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md)).

## State, October 2026

Version 0.4.0, "undergoing active research and development". Base device classes (network, block, serial, I²C) are expected to be mostly stable ([Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md)). A Pancake version of a LionsOS Ethernet driver and the queue library are verified with SMT-based proofs; whether LionsOS ships that version is not stated ([SMT-based Deductive Verification of Device Drivers](https://silentzero.ooo/wiki/sources/2026-tyler-smt-based-deductive.html.md)). Verification of the other drivers and components is under way ([Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md)); Heiser expects the verification of LionsOS to be completed in 2027 and says initial explorations show verifying small components, mostly under 500 lines in the reference design, to be feasible ([seL4 for reliability](https://silentzero.ooo/wiki/sources/2026-heiser-sel4-operating-systems.html.md)).

Slides of September 2026 add a community firewall project, released in November 2025, a virtual network switch, and sDDF support for ACPI and PCIe ([Trustworthy Systems R&D update](https://silentzero.ooo/wiki/sources/2026-heiser-trustworthy-systems-update.html.md), slides 5 to 8). The same slides say that [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md) can now start, stop and upgrade protection domains at run time, used by the Carrels project; whether LionsOS uses this is not stated, and the static description above is from the project page.

Two more talks of the same summit: libvmm, the VMM library on Microkit, boots an unmodified Windows 11 and Linux guests on x86-64, through UEFI firmware, with sDDF drivers underneath ([Booting Windows on an x86-64 seL4-based VMM](https://silentzero.ooo/wiki/sources/2026-nguyen-booting-windows-x86-64.html.md)); and work on driver specifications taken from a device's Verilog, with a rely-guarantee style for device specifications and Pancake drivers, aims at end-to-end driver proofs and a system specification composed of client, virtualiser and driver specifications ([Formalising device protocols for sDDF driver verification](https://silentzero.ooo/wiki/sources/2026-murphy-formalising-device-protocols.html.md)). Neither talk mentions LionsOS by name, and neither says whether LionsOS ships the result.

## Design

- Single-purpose components; a driver only translates between its device and a device-class interface ([Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md), [SMT-based Deductive Verification of Device Drivers](https://silentzero.ooo/wiki/sources/2026-tyler-smt-based-deductive.html.md)).
- Lock-free, bounded, single-producer, single-consumer queues in shared memory, zero copy, signalled by notifications ([The seL4 Device Driver Framework](https://silentzero.ooo/wiki/sources/2022-parker-sel4-device-driver.html.md), [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)).
- Virtualisers multiplex devices and translate addresses; copiers separate clients where needed ([Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md), [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)).
- Unmodified Linux drivers can run in a virtual machine as a driver VM ([MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)).
- Driver size: an i.MX8 Ethernet driver of 569 lines, against 4,775 for the Linux driver, written by a second-year student, according to Heiser's overview; unmodified Linux drivers run in a VM with a large trusted base behind an IOMMU ([seL4 for reliability](https://silentzero.ooo/wiki/sources/2026-heiser-sel4-operating-systems.html.md)).
- Small code: in a point-of-sale demonstrator the trusted components average about 210 lines ([MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)); the design paper counts about 3.1 kSLOC of trusted code there ([Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md), §6.2.1).
- Measured against Linux: on a 1 Gb/s Arm board one core carries the full gigabit with a third to spare where Linux plateaus at about 500 Mb/s, with round-trip times three to ten times lower. Free IPC would change little, by the authors' simulation. The numbers are throughput, load and round-trip times, not bounds ([Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md), §6.3).

The device driver framework behind this design, sDDF, was first presented in 2022 ([The seL4 Device Driver Framework](https://silentzero.ooo/wiki/sources/2022-parker-sel4-device-driver.html.md)).

## Licence and code

Not yet covered by the wiki's sources.

## Open questions

- What the run-time swap of components permits, and who may trigger it. See [The static system](https://silentzero.ooo/wiki/design/static-system.html.md).
- Worst-case latency: the design paper reports none ([Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md)).

## Sources

- [Booting Windows on an x86-64 seL4-based VMM](https://silentzero.ooo/wiki/sources/2026-nguyen-booting-windows-x86-64.html.md)
- [Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md)
- [Formalising device protocols for sDDF driver verification](https://silentzero.ooo/wiki/sources/2026-murphy-formalising-device-protocols.html.md)
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)
- [seL4 for reliability](https://silentzero.ooo/wiki/sources/2026-heiser-sel4-operating-systems.html.md)
- [SMT-based Deductive Verification of Device Drivers](https://silentzero.ooo/wiki/sources/2026-tyler-smt-based-deductive.html.md)
- [The seL4 Device Driver Framework](https://silentzero.ooo/wiki/sources/2022-parker-sel4-device-driver.html.md)
- [Trustworthy Systems R&D update](https://silentzero.ooo/wiki/sources/2026-heiser-trustworthy-systems-update.html.md)
- [Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md)

## Related pages

- [The static system](https://silentzero.ooo/wiki/design/static-system.html.md)
- [IOMMU](https://silentzero.ooo/wiki/concepts/iommu.html.md)
- [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md)
- [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [agentOS, an operating system for agents on seL4](https://silentzero.ooo/wiki/sources/2026-hubbard-agentos-operating-system.html.md)
- [Microkit 2.4.0 release notes](https://silentzero.ooo/wiki/sources/2026-microkit-release-2-4-0.html.md)
- [seL4 Foundation: Development roadmap](https://silentzero.ooo/wiki/sources/nd-sel4-sel4-roadmap.html.md)
- [Verifying Device Drivers with Pancake](https://silentzero.ooo/wiki/sources/2025-zhao-verifying-device-drivers.html.md)
