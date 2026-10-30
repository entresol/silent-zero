---
type: source
id: nd-opensbi
status: reviewed
read: partial
kind: report
sources: [nd-opensbi]
updated: 2026-10-30
---

# OpenSBI

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

- [[opensbi]]: created with this source.

## For zOS

- [[root-of-trust]]: the paper says Microkit on RISC-V "relies on SBI firmware such as OpenSBI in machine mode" (Section 3). The reliance is stated in the Microkit manual, which expects "a compatible RISC-V SBI (e.g OpenSBI)" to have run before its loader ([[nd-sel4-microkit-user-manual]]); this README confirms the role of SBI firmware in M-mode below S-mode kernels. In the paper's terms it is *assumed*.
- Our reading: on a multicore RISC-V board, seL4 depends on OpenSBI's hart-state-management to start its other cores.
