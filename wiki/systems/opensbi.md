---
type: system
status: reviewed
sources: [nd-opensbi, 2024-riscv-privileged-isa-manual, nd-sel4-supported-platforms]
updated: 2026-10-31
---

# OpenSBI

The open-source reference implementation of the RISC-V Supervisor Binary Interface for firmware in machine mode, the level below any S-mode kernel. It is built as a library plus platform-specific firmwares and works with bootloaders such as U-Boot ([[nd-opensbi]]). Machine mode is the most privileged of [[risc-v]]'s levels; the specification calls code there "usually inherently trusted" ([[2024-riscv-privileged-isa-manual]]). On the HiFive Premier P550, OpenSBI comes from the board's SPI flash, between the firmware and U-Boot ([[nd-sel4-supported-platforms]]).

## State, October 2026

The README states full support for SBI v0.2 and for the hart-state-management extension, through which an S-mode kernel starts the other harts ([[nd-opensbi]]); whether that statement is current is not established here.

## Licence and code

BSD-2-Clause, with parts of libfdt dual-licensed; on GitHub at `riscv-software-src/opensbi` ([[nd-opensbi]]).

## Open questions

- What OpenSBI's domain support offers for isolating M-mode services; its documentation is not yet covered here.
