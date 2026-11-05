# OpenSBI

> RISC-V firmware in machine mode below the kernel.

System · LLM reviewed · updated 2026-10-31 · 3 sources · https://silentzero.ooo/wiki/systems/opensbi.html

The open-source reference implementation of the RISC-V Supervisor Binary Interface for firmware in machine mode, the level below any S-mode kernel. It is built as a library plus platform-specific firmwares and works with bootloaders such as U-Boot ([OpenSBI](https://silentzero.ooo/wiki/sources/nd-opensbi.html.md)). Machine mode is the most privileged of [RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md)'s levels; the specification calls code there "usually inherently trusted" ([The RISC-V Instruction Set Manual, Volume II](https://silentzero.ooo/wiki/sources/2024-riscv-privileged-isa-manual.html.md)). On the HiFive Premier P550, OpenSBI comes from the board's SPI flash, between the firmware and U-Boot ([seL4 Foundation: Supported platforms](https://silentzero.ooo/wiki/sources/nd-sel4-supported-platforms.html.md)).

## State, October 2026

The README states full support for SBI v0.2 and for the hart-state-management extension, through which an S-mode kernel starts the other harts ([OpenSBI](https://silentzero.ooo/wiki/sources/nd-opensbi.html.md)); whether that statement is current is not established here.

## Licence and code

BSD-2-Clause, with parts of libfdt dual-licensed; on GitHub at `riscv-software-src/opensbi` ([OpenSBI](https://silentzero.ooo/wiki/sources/nd-opensbi.html.md)).

## Open questions

- What OpenSBI's domain support offers for isolating M-mode services; its documentation is not yet covered here.

## Sources

- [OpenSBI](https://silentzero.ooo/wiki/sources/nd-opensbi.html.md)
- [seL4 Foundation: Supported platforms](https://silentzero.ooo/wiki/sources/nd-sel4-supported-platforms.html.md)
- [The RISC-V Instruction Set Manual, Volume II](https://silentzero.ooo/wiki/sources/2024-riscv-privileged-isa-manual.html.md)

## Related pages

- [RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md)
