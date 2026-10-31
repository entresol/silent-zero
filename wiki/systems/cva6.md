---
type: system
status: reviewed
sources: [nd-trustworthy-wcet-worst-case, 2026-sillitoe-resurrecting-sel4-wcet, 2022-wistoff-systematic-prevention-core, nd-sel4-microkit-user-manual, nd-sel4-verified-configurations, 2026-sel4-release-17]
short: Open-source 64-bit RISC-V core, also Ariane
updated: 2026-10-31
---

# CVA6

An open-source 64-bit RISC-V application core, also known as Ariane, developed at ETH Zürich ([[nd-trustworthy-wcet-worst-case]]) and documented today by the Open Hardware Foundation ([[2026-sillitoe-resurrecting-sel4-wcet]], ref. 10). Its SystemVerilog source is public.

## Why it matters for timing

Because the design is open, latency bounds per functional unit can be derived from the design itself instead of being taken from a vendor's documentation. The Trustworthy Systems group named open RISC-V cores as its hope for resurrecting seL4's WCET analysis, with CVA6 as the example ([[nd-trustworthy-wcet-worst-case]]). Its method takes two steps. It first simulates each functional unit with random inputs to find a candidate bound, and then tries to prove that bound with the model checker SymbiYosys. When the proof fails, the authors either tighten the assumptions of the test harness or raise the bound. Our reading: a bound proved under tighter assumptions holds only under them. The authors expect to finish in the first quarter of 2027 ([[2026-sillitoe-resurrecting-sel4-wcet]], §5.2).

Our reading: a proof against the design covers the design; a chip or FPGA built from it is assumed to match.

## Why it matters for timing channels

On CVA6 a custom instruction, `fence.t`, resets all non-architectural state on a context switch. In an FPGA prototype it closed every measured on-core timing channel, at under 1 per cent slowdown with a context switch every 10 million cycles, equivalent to 10 ms at 1 GHz ([[2022-wistoff-systematic-prevention-core]]). See [[time-protection]].

## Boards

Microkit supports CVA6 on the Digilent Genesys2 FPGA board ([[nd-sel4-microkit-user-manual]]); seL4's verified configurations include Ariane ([[nd-sel4-verified-configurations]]), which the Microkit manual calls the former name of CVA6 ([[nd-sel4-microkit-user-manual]]). Since seL4 release 17.0.0, `ariane` is among the RISC-V platforms with a C-level proof, without MCS ([[2026-sel4-release-17]]).

## Not yet in the wiki

Silicon with CVA6, licence.
