# RISC-V

> The open instruction set: what is open (the ISA) and what need not be (cores, chips, boards); privilege levels and the SBI.

Concept · LLM reviewed · updated 2026-10-31 · 11 sources · https://silentzero.ooo/wiki/concepts/risc-v.html

An instruction set architecture (ISA): the specification of the instructions a processor understands, which software is written against. RISC-V was started in Berkeley in May 2010 for research and teaching ([RISC-V International: About](https://silentzero.ooo/wiki/sources/nd-riscv-international-about.html.md), [The RISC-V Instruction Set Manual, Version 1.0](https://silentzero.ooo/wiki/sources/2011-waterman-risc-v-instruction.html.md)). Today it is an open standard that RISC-V International maintains and that anyone may implement without paying royalties ([RISC-V International: About](https://silentzero.ooo/wiki/sources/nd-riscv-international-about.html.md)). The specification itself is under a Creative Commons licence ([The RISC-V Instruction Set Manual, Volume I](https://silentzero.ooo/wiki/sources/2024-riscv-unprivileged-isa-manual.html.md)).

## What is open, and what is not

The specification calls the ISA "the software-visible interface to a wide variety of implementations rather than [...] the design of a particular hardware artifact" ([The RISC-V Instruction Set Manual, Volume I](https://silentzero.ooo/wiki/sources/2024-riscv-unprivileged-isa-manual.html.md), Chapter 1). Asanović and Patterson distinguish three kinds of implementation: closed, licensed, and free open source. A proprietary ISA in practice allows only the first two ([Instruction Sets Should Be Free](https://silentzero.ooo/wiki/sources/2014-asanovic-instruction-sets-free.html.md)). RISC-V International maintains only the specifications and "does not manage or make available any open RISC-V implementations" ([RISC-V International: About](https://silentzero.ooo/wiki/sources/nd-riscv-international-about.html.md)).

From specification to board there are four layers. Our reading, with the two boards that matter to Silent Zero:

| Layer | What it is | HiFive Unleashed | HiFive Premier P550 |
| --- | --- | --- | --- |
| ISA | the instruction set, a document | RV64 | RV64 |
| Core design | a processor core, often licensed as IP | SiFive U54, plus a monitor core | SiFive P550 |
| SoC | a chip with cores, memory controller, devices | SiFive Freedom U540 | Eswin EIC7700 (EIC7700X in seL4's list) |
| Board | what one buys | HiFive Unleashed (discontinued) | HiFive Premier P550 |

Sources for the rows: [SiFive: HiFive Unleashed](https://silentzero.ooo/wiki/sources/nd-sifive-hifive-unleashed.html.md), [the HiFive Premier P550](https://silentzero.ooo/wiki/sources/2024-sifive-hifive-premier-p550.html.md), [seL4 Foundation: Supported platforms](https://silentzero.ooo/wiki/sources/nd-sel4-supported-platforms.html.md). The ISA is open. Cores, chips and boards can be open, as [CVA6](https://silentzero.ooo/wiki/systems/cva6.html.md) is, or offered commercially, as SiFive offers its "processor core IP" ([SiFive: RISC-V History](https://silentzero.ooo/wiki/sources/nd-sifive-risc-v-history.html.md)).

## How the ISA is built

A small base integer ISA plus optional standard extensions. The bases are RV32I and RV64I and the reduced RV32E and RV64E; a future RV128I is sketched. The common extensions are M (multiply, divide), A (atomics), F and D (floating point) and C (compressed instructions). The encoding space is split three ways: standard encodings, reserved ones saved for future standard extensions, and custom ones for vendor-specific extensions, which standard extensions never use ([The RISC-V Instruction Set Manual, Volume I](https://silentzero.ooo/wiki/sources/2024-riscv-unprivileged-isa-manual.html.md), Section 1.3). To keep customisation from splitting the software base, profiles such as RVA23 fix a set of extensions software can rely on ([SiFive: RISC-V History](https://silentzero.ooo/wiki/sources/nd-sifive-risc-v-history.html.md)).

## Privilege levels

Three levels: Machine (M), the only mandatory one, whose code is "usually inherently trusted"; Supervisor (S) for operating systems; User (U) for applications. An operating system reaches the level below it through the supervisor binary interface (SBI) ([The RISC-V Instruction Set Manual, Volume II](https://silentzero.ooo/wiki/sources/2024-riscv-privileged-isa-manual.html.md), Sections 1.1 and 1.2). [OpenSBI](https://silentzero.ooo/wiki/systems/opensbi.html.md) implements the SBI in M-mode ([OpenSBI](https://silentzero.ooo/wiki/sources/nd-opensbi.html.md)).

## State, October 2026

- The ISA modules most software needs are ratified: RV32I and RV64I 2.1, M, A, F, D and C ([The RISC-V Instruction Set Manual, Volume I](https://silentzero.ooo/wiki/sources/2024-riscv-unprivileged-isa-manual.html.md), preface, version 20240411).
- seL4's C-level proof covers the eight RISC-V platforms its release notes list, boards as well as FPGA designs such as Ariane and Rocket; the proof of the MCS configuration covers one, the HiFive Unleashed ([release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md)).

## Open questions

- Which RISC-V boards can show a picture before the kernel runs, as the Silent Zero loader needs.
- Whether the RVA23 profile matters for Silent Zero, or only the base and the extensions seL4's verified configuration uses.

## Sources

- [Instruction Sets Should Be Free](https://silentzero.ooo/wiki/sources/2014-asanovic-instruction-sets-free.html.md)
- [OpenSBI](https://silentzero.ooo/wiki/sources/nd-opensbi.html.md)
- [release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md)
- [RISC-V International: About](https://silentzero.ooo/wiki/sources/nd-riscv-international-about.html.md)
- [seL4 Foundation: Supported platforms](https://silentzero.ooo/wiki/sources/nd-sel4-supported-platforms.html.md)
- [SiFive: HiFive Unleashed](https://silentzero.ooo/wiki/sources/nd-sifive-hifive-unleashed.html.md)
- [SiFive: RISC-V History](https://silentzero.ooo/wiki/sources/nd-sifive-risc-v-history.html.md)
- [the HiFive Premier P550](https://silentzero.ooo/wiki/sources/2024-sifive-hifive-premier-p550.html.md)
- [The RISC-V Instruction Set Manual, Version 1.0](https://silentzero.ooo/wiki/sources/2011-waterman-risc-v-instruction.html.md)
- [The RISC-V Instruction Set Manual, Volume I](https://silentzero.ooo/wiki/sources/2024-riscv-unprivileged-isa-manual.html.md)
- [The RISC-V Instruction Set Manual, Volume II](https://silentzero.ooo/wiki/sources/2024-riscv-privileged-isa-manual.html.md)

## Related pages

- [CHERIoT](https://silentzero.ooo/wiki/systems/cheriot.html.md)
- [CVA6](https://silentzero.ooo/wiki/systems/cva6.html.md)
- [OpenSBI](https://silentzero.ooo/wiki/systems/opensbi.html.md)
- [SiFive and the HiFive boards](https://silentzero.ooo/wiki/systems/sifive-hifive.html.md)
