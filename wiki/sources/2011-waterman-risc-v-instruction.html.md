# The RISC-V Instruction Set Manual, Version 1.0

> The first RISC-V manual, Berkeley, May 2011: an open ISA for research and teaching. design, introduction only.

Source · Waterman et al. 2011 · LLM reviewed · updated 2026-10-31 · https://silentzero.ooo/wiki/sources/2011-waterman-risc-v-instruction.html

Andrew Waterman, Yunsup Lee, David A. Patterson and Krste Asanović, *The RISC-V Instruction Set Manual, Volume I: Base User-Level ISA*, Version 1.0, technical report UCB/EECS-2011-62, University of California at Berkeley, 13 May 2011. [Report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2011/EECS-2011-62.html). Read in part: the introduction (Section 1) and the start of Section 2; the instruction definitions that follow are not covered here.

## What it shows

- **The first publication of RISC-V.** RISC-V International calls this report "the first publication that describes the RISC-V instruction set" ([RISC-V International: About](https://silentzero.ooo/wiki/sources/nd-riscv-international-about.html.md)).
- **Purpose.** RISC-V is "a new instruction set architecture (ISA) designed to support computer architecture research and education". Its goals include "a realistic but open ISA" suitable for direct hardware implementation, a small base that does not favour one microarchitecture, 32- and 64-bit variants, support for many cores, and the ability to experiment with new supervisor-level designs.
- **The name.** RISC-V is the fifth major RISC design from Berkeley, after RISC-I, RISC-II, SOAR and SPUR; the "V" also stands for "variations" and "vectors".
- **Openness.** The authors intend documentation, tools and implementations to be made available "under open licenses (either modified BSD or GPL/LGPL)".
- **Base and extensions.** The base user-level ISA has the variants RV32 and RV64; it may be extended, but its instructions "cannot be redefined".
- **A snapshot.** The manual calls itself "only a snapshot" of an ISA "still under active development".

## How

A specification with commentary on design decisions, as a Berkeley technical report.

## Limits

The authors say the ISA may still change. Version 1.0 differs from today's specification ([The RISC-V Instruction Set Manual, Volume I](https://silentzero.ooo/wiki/sources/2024-riscv-unprivileged-isa-manual.html.md)), whose preface to version 2.0 lists the changes "since Version 1.0". A careful reader adds: this report is the starting point in history, not a reference for today's instructions.

## Against the wiki

- [RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md): created with this source and [Instruction Sets Should Be Free](https://silentzero.ooo/wiki/sources/2014-asanovic-instruction-sets-free.html.md).

## For Silent Zero

No design page changes. The report dates the beginning: an ISA designed for research and teaching, open from the start.

## Related pages

- [RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md)
- [Instruction Sets Should Be Free](https://silentzero.ooo/wiki/sources/2014-asanovic-instruction-sets-free.html.md)
- [RISC-V International: About](https://silentzero.ooo/wiki/sources/nd-riscv-international-about.html.md)
- [The RISC-V Instruction Set Manual, Volume I](https://silentzero.ooo/wiki/sources/2024-riscv-unprivileged-isa-manual.html.md)
