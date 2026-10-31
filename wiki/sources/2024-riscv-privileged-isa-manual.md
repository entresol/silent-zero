---
type: source
id: 2024-riscv-privileged-isa-manual
status: reviewed
read: partial
kind: design
sources: [2024-riscv-privileged-isa-manual]
updated: 2026-10-31
---

# RISC-V International 2024: The RISC-V Instruction Set Manual, Volume II

*The RISC-V Instruction Set Manual, Volume II: Privileged Architecture*, version 20240411, RISC-V International. [Release](https://github.com/riscv/riscv-isa-manual/releases/tag/20240411). Read in part: preface and Chapter 1 (Introduction). The chapters on control registers, machine, supervisor and hypervisor modes are not covered here.

## What it shows

- **Privilege levels.** Three are "currently defined": User (U), Supervisor (S) and Machine (M) (Section 1.2, Table 1). Machine mode "has the highest privileges and is the only mandatory privilege level"; code there "is usually inherently trusted, as it has low-level access to the machine implementation". U-mode and S-mode are meant for applications and operating systems.
- **Combinations.** One level (M) for simple embedded systems, two (M, U) for secure embedded systems, three (M, S, U) for systems running Unix-like operating systems (Section 1.2, Table 2).
- **The SBI.** An operating system talks to its supervisor execution environment (SEE) through the supervisor binary interface (SBI). The SEE "can be a simple boot loader and BIOS-style IO system" on a small platform, a hypervisor's virtual machine, or a thin translation layer over a host operating system in a simulator (Section 1.1). The authors call ABI, SBI and HBI "still a work-in-progress".
- **Replaceable design.** The authors note that the whole privileged design "could be replaced with an entirely different privileged-level design" without changing the unprivileged ISA (Chapter 1).
- **Status.** The preface lists the machine ISA at version 1.13 as a draft and the supervisor ISA 1.0.0 as ratified. It is headed "Preface to Version 20240326" and names "version 20240213", although the title page says 20240411.

## How

The normative specification of everything beyond the unprivileged ISA, with commentary set apart.

## Limits

Only the introduction was read. A careful reader adds: the version labels in the preface do not match the title page; for anything beyond the introduction, the current release should be checked.

## Against the wiki

- [[risc-v]]: created with this source.
- [[opensbi]], [[nd-opensbi]]: **consistent with** them. Our reading: the specification places no SEE in M-mode explicitly, but S-mode "can be added to provide isolation between a supervisor-level operating system and the SEE" (Section 1.2), which fits SBI firmware in M-mode below a kernel in S-mode.

## For zOS

- [[root-of-trust]], [[bootloader]]: in the boot chain of the project's video, OpenSBI runs in M-mode, then the zOS loader and seL4 run in S-mode, the root task in U-mode. Our reading: by the specification's own words, M-mode code is "usually inherently trusted", so whatever runs there before the loader is *assumed*, as the paper says of firmware.
