---
type: concept
status: reviewed
sources: [2011-waterman-risc-v-instruction, 2014-asanovic-instruction-sets-free, 2024-riscv-unprivileged-isa-manual, 2024-riscv-privileged-isa-manual, nd-riscv-international-about, nd-sifive-risc-v-history, 2026-sel4-release-17, nd-opensbi, nd-sel4-supported-platforms, nd-sifive-hifive-unleashed, 2024-sifive-hifive-premier-p550]
updated: 2026-10-31
---

# RISC-V

An instruction set architecture (ISA): the specification of the instructions a processor understands, which software is written against. RISC-V was started in Berkeley in May 2010 for research and teaching ([[nd-riscv-international-about]], [[2011-waterman-risc-v-instruction]]). Today it is an open standard that RISC-V International maintains and that anyone may implement without paying royalties ([[nd-riscv-international-about]]). The specification itself is under a Creative Commons licence ([[2024-riscv-unprivileged-isa-manual]]).

## What is open, and what is not

The specification calls the ISA "the software-visible interface to a wide variety of implementations rather than [...] the design of a particular hardware artifact" ([[2024-riscv-unprivileged-isa-manual]], Chapter 1). Asanović and Patterson distinguish three kinds of implementation: closed, licensed, and free open source. A proprietary ISA in practice allows only the first two ([[2014-asanovic-instruction-sets-free]]). RISC-V International maintains only the specifications and "does not manage or make available any open RISC-V implementations" ([[nd-riscv-international-about]]).

From specification to board there are four layers. Our reading, with the two boards that matter to zOS:

| Layer | What it is | HiFive Unleashed | HiFive Premier P550 |
| --- | --- | --- | --- |
| ISA | the instruction set, a document | RV64 | RV64 |
| Core design | a processor core, often licensed as IP | SiFive U54, plus a monitor core | SiFive P550 |
| SoC | a chip with cores, memory controller, devices | SiFive Freedom U540 | Eswin EIC7700 (EIC7700X in seL4's list) |
| Board | what one buys | HiFive Unleashed (discontinued) | HiFive Premier P550 |

Sources for the rows: [[nd-sifive-hifive-unleashed]], [[2024-sifive-hifive-premier-p550]], [[nd-sel4-supported-platforms]]. The ISA is open. Cores, chips and boards can be open, as [[cva6]] is, or offered commercially, as SiFive offers its "processor core IP" ([[nd-sifive-risc-v-history]]).

## How the ISA is built

A small base integer ISA plus optional standard extensions. The bases are RV32I and RV64I and the reduced RV32E and RV64E; a future RV128I is sketched. The common extensions are M (multiply, divide), A (atomics), F and D (floating point) and C (compressed instructions). The encoding space is split three ways: standard encodings, reserved ones saved for future standard extensions, and custom ones for vendor-specific extensions, which standard extensions never use ([[2024-riscv-unprivileged-isa-manual]], Section 1.3). To keep customisation from splitting the software base, profiles such as RVA23 fix a set of extensions software can rely on ([[nd-sifive-risc-v-history]]).

## Privilege levels

Three levels: Machine (M), the only mandatory one, whose code is "usually inherently trusted"; Supervisor (S) for operating systems; User (U) for applications. An operating system reaches the level below it through the supervisor binary interface (SBI) ([[2024-riscv-privileged-isa-manual]], Sections 1.1 and 1.2). [[opensbi]] implements the SBI in M-mode ([[nd-opensbi]]).

## State, October 2026

- The ISA modules most software needs are ratified: RV32I and RV64I 2.1, M, A, F, D and C ([[2024-riscv-unprivileged-isa-manual]], preface, version 20240411).
- seL4's C-level proof covers the eight RISC-V platforms its release notes list, boards as well as FPGA designs such as Ariane and Rocket; the proof of the MCS configuration covers one, the HiFive Unleashed ([[2026-sel4-release-17]]).

## Open questions

- Which RISC-V boards can show a picture before the kernel runs, as the zOS loader needs.
- Whether the RVA23 profile matters for zOS, or only the base and the extensions seL4's verified configuration uses.
