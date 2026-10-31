---
type: source
id: 2024-riscv-unprivileged-isa-manual
status: reviewed
read: partial
kind: design
sources: [2024-riscv-unprivileged-isa-manual]
updated: 2026-10-31
---

# RISC-V International 2024: The RISC-V Instruction Set Manual, Volume I

*The RISC-V Instruction Set Manual, Volume I: Unprivileged Architecture*, version 20240411, RISC-V International. [Release](https://github.com/riscv/riscv-isa-manual/releases/tag/20240411). Read in part: preamble, preface and Chapter 1 (Introduction). The instruction chapters are not covered here.

## What it shows

- **What RISC-V is.** "A new instruction-set architecture (ISA) that was originally designed to support computer architecture research and education", which the authors now hope "will also become a standard free and open architecture for industry implementations" (Chapter 1). The first goal they list is "a completely open ISA that is freely available to academia and industry".
- **An interface, not a chip.** The ISA "should be read as the software-visible interface to a wide variety of implementations rather than as the design of a particular hardware artifact" (Chapter 1).
- **A family of ISAs.** RISC-V has "currently four base ISAs": RV32I and RV64I, and the reduced RV32E and RV64E for small microcontrollers; a future RV128I is sketched. Standard extensions add multiply and divide (M), atomics (A), single- and double-precision floating point (F, D) and compressed 16-bit instructions (C) (Section 1.3).
- **Standard and custom.** Standard extensions and encodings are defined by RISC-V International; custom encodings are left for vendor-specific extensions and "shall never be used for standard extensions" (Section 1.3).
- **Harts and execution environments.** A hart is a hardware thread. A program's behaviour depends on its execution environment interface, for example the Linux ABI or the RISC-V Supervisor Binary Interface (SBI). Examples of environments are bare hardware, operating systems, hypervisors and emulators such as QEMU (Sections 1.1 and 1.2).
- **Status.** The preface marks each module ratified, frozen or draft; RV32I and RV64I (2.1), M, A, F, D and C are among the ratified modules.
- **Licence.** The document is released under Creative Commons Attribution 4.0 (preamble).

## How

The normative specification, with commentary on design decisions set apart from the normative text.

## Limits

Only the introduction was read. A careful reader adds: the specification defines what software sees; it says nothing about which chips exist, how fast they are, or whether a particular implementation is correct.

## Against the wiki

- [[risc-v]]: created with this source.
- [[2011-waterman-risc-v-instruction]]: this document descends from that first report; it holds ratified modules alongside frozen and draft ones.

## For zOS

- [[kernel]]: seL4's verified RISC-V configurations are 64-bit and without FPU ([[nd-sel4-verified-configurations]]). Our reading: in this vocabulary that is RV64 without the F and D extensions in use.
