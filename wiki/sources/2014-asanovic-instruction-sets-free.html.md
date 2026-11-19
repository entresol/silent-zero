# Instruction Sets Should Be Free

> Why instruction sets should be free, and why RISC-V. position, full text.

Source · Asanović and Patterson 2014 · LLM reviewed · updated 2026-10-31 · https://silentzero.ooo/wiki/sources/2014-asanovic-instruction-sets-free.html

Krste Asanović and David A. Patterson, *Instruction Sets Should Be Free: The Case For RISC-V*, technical report UCB/EECS-2014-146, University of California at Berkeley, 6 August 2014. Five pages. [Report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2014/EECS-2014-146.html).

## What it shows

- **The claim.** The industry would benefit from free, open instruction sets (ISAs) as it has from open standards and open-source software. The authors see "no good technical reason" for the lack of them.
- **Why ISAs are closed.** Companies with successful ISAs, Arm, IBM and Intel named, hold patents on quirks of their ISAs. The authors give 6 to 24 months and $1M to $10M for a licence negotiation, citing a secondary source, and say an Arm licence lets you use Arm's designs but not design your own Arm core, which only about 15 large companies may do.
- **An ISA is an interface, not an implementation.** Implementations can be closed, licensed or free open source; a proprietary ISA "in practice" allows only the first two.
- **Four requirements** for an ISA meant for small devices, phones and warehouse-scale computers: a base plus extensions, compact encoding, quadruple-precision floating point, and 128-bit as well as 32- and 64-bit addressing.
- **Why RISC-V.** Of three existing free RISC ISAs (SPARC V8, OpenRISC, RISC-V), the authors' table has only RISC-V meeting all four. RISC-V was developed from 2010 by the authors with Andrew Waterman and Yunsup Lee, "partly inspired by ARM's IP restrictions", for research and teaching, and released under a BSD licence.
- **One comparison.** Table 2 sets Berkeley's 64-bit Rocket core against Arm's 32-bit Cortex-A5, both single-issue and in-order, in the same TSMC process (40GPLUS). Its ratio row gives Rocket 1.1 times the Dhrystone performance per MHz, 0.5 times the area without caches and 0.7 with 16 KB caches. The text sums this up as "half the area, half the power, and faster". The figures come from Arm's website and a 2014 conference paper by Lee et al.
- **The plan.** Workshops, and a non-profit foundation to certify implementations and to maintain and evolve the ISA, inspired by foundations such as Apache, the Free Software Foundation and The Open Group (Table 3).

## How

The report is a position paper with five numbered tables and a scoring table. It argues by comparison: why ISAs are proprietary, which ISA style has succeeded, which free ISA meets the requirements. It ends with the hope that RISC-V becomes "the standard ISA for all computing devices", as Linux did for operating systems.

## Limits

The authors say they find it "hard to set aside biases": they designed RISC-V. The figures on licence time and cost rest on a 2013 article, the patent claim on a 2002 letter, and the figure of about 15 companies on no reference; the core comparison rests on one pair of in-order cores. A careful reader adds: the report argues for an open ISA; it does not say that cores or chips built on it will be open, and the open core it measures is Berkeley's own.

## Against the wiki

- [RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md): created with this source and [The RISC-V Instruction Set Manual, Version 1.0](https://silentzero.ooo/wiki/sources/2011-waterman-risc-v-instruction.html.md).
- [SiFive and the HiFive boards](https://silentzero.ooo/wiki/systems/sifive-hifive.html.md): Asanović and his students Waterman and Lee later founded SiFive, which names them as its founders ([SiFive: RISC-V History](https://silentzero.ooo/wiki/sources/nd-sifive-risc-v-history.html.md)).

## For Silent Zero

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md): the paper argues that the first Silent Zero should run on an open RISC-V core, because only there is a proof of timing within reach (Section 4). This report supplies the background: the ISA is open, and implementations can be open too, but need not be.

## Related pages

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md)
- [SiFive and the HiFive boards](https://silentzero.ooo/wiki/systems/sifive-hifive.html.md)
- [RISC-V International: About](https://silentzero.ooo/wiki/sources/nd-riscv-international-about.html.md)
- [SiFive: RISC-V History](https://silentzero.ooo/wiki/sources/nd-sifive-risc-v-history.html.md)
- [The RISC-V Instruction Set Manual, Version 1.0](https://silentzero.ooo/wiki/sources/2011-waterman-risc-v-instruction.html.md)
