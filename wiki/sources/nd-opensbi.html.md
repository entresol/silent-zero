# OpenSBI

> The SBI reference firmware for RISC-V machine mode. report, README.

Source · LLM reviewed · updated 2026-10-30 · https://silentzero.ooo/wiki/sources/nd-opensbi.html

The README of the OpenSBI repository, read on 30 October 2026. [Repository](https://github.com/riscv-software-src/opensbi). Only the README was read; the firmware and domain documentation it links to is not covered here.

## What it shows

- **What it is.** The RISC-V Supervisor Binary Interface (SBI) is the recommended interface between platform firmware in M-mode and a bootloader, hypervisor or operating system in S-mode or HS-mode, and between a hypervisor and its guests. OpenSBI is an open-source reference implementation for the first case.
- **Form.** A platform-independent library, `libsbi.a`, plus platform-specific libraries and example firmwares, which can replace the older `riscv-pk` bootloader and work with bootloaders such as U-Boot.
- **Versions.** The README states that OpenSBI "fully supports" SBI v0.2 and, since v0.7, the hart-state-management extension, with which S-mode software brings up the other harts; S-mode software without it can boot only one hart.
- **Licence.** BSD-2-Clause; parts of libfdt are dual-licensed GPL-2.0+ or BSD-2-Clause.
- **Domains.** The README links to documentation on OpenSBI domain support, which the wiki has not read.

## How

A project README: purpose, licence, build instructions.

## Limits

A careful reader adds: the README's version statement may be older than the code; the current SBI version is not established here. The README says nothing about verification or about what OpenSBI does at run time beyond implementing the SBI. It runs in M-mode, below any S-mode kernel.

## Against the wiki

- [OpenSBI](https://silentzero.ooo/wiki/systems/opensbi.html.md): created with this source.

## For Silent Zero

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md): the paper says Microkit on RISC-V "relies on SBI firmware such as OpenSBI in machine mode" (Section 3). The reliance is stated in the Microkit manual, which expects "a compatible RISC-V SBI (e.g OpenSBI)" to have run before its loader ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)); this README confirms the role of SBI firmware in M-mode below S-mode kernels. In the paper's terms it is *assumed*.
- Our reading: on a multicore RISC-V board, seL4 depends on OpenSBI's hart-state-management to start its other cores.

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)
- [RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md)
- [OpenSBI](https://silentzero.ooo/wiki/systems/opensbi.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [The RISC-V Instruction Set Manual, Volume II](https://silentzero.ooo/wiki/sources/2024-riscv-privileged-isa-manual.html.md)
