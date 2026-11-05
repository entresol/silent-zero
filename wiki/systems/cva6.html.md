# CVA6

> Open 64-bit RISC-V core whose design lets latency bounds be proved; fence.t prototype.

System · LLM reviewed · updated 2026-10-31 · 6 sources · https://silentzero.ooo/wiki/systems/cva6.html

An open-source 64-bit RISC-V application core, also known as Ariane, developed at ETH Zürich ([WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)) and documented today by the Open Hardware Foundation ([Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md), ref. 10). Its SystemVerilog source is public.

## Why it matters for timing

Because the design is open, latency bounds per functional unit can be derived from the design itself instead of being taken from a vendor's documentation. The Trustworthy Systems group named open RISC-V cores as its hope for resurrecting seL4's WCET analysis, with CVA6 as the example ([WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)). Its method takes two steps. It first simulates each functional unit with random inputs to find a candidate bound, and then tries to prove that bound with the model checker SymbiYosys. When the proof fails, the authors either tighten the assumptions of the test harness or raise the bound. Our reading: a bound proved under tighter assumptions holds only under them. The authors expect to finish in the first quarter of 2027 ([Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md), §5.2).

Our reading: a proof against the design covers the design; a chip or FPGA built from it is assumed to match.

## Why it matters for timing channels

On CVA6 a custom instruction, `fence.t`, resets all non-architectural state on a context switch. In an FPGA prototype it closed every measured on-core timing channel, at under 1 per cent slowdown with a context switch every 10 million cycles, equivalent to 10 ms at 1 GHz ([Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md)). See [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md).

## Boards

Microkit supports CVA6 on the Digilent Genesys2 FPGA board ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)); seL4's verified configurations include Ariane ([seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)), which the Microkit manual calls the former name of CVA6 ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)). Since seL4 release 17.0.0, `ariane` is among the RISC-V platforms with a C-level proof, without MCS ([release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md)).

## Not yet in the wiki

Silicon with CVA6, licence.

## Sources

- [release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md)
- [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md)
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md)
- [WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)

## Related pages

- [RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md)
- [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md)
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md)
