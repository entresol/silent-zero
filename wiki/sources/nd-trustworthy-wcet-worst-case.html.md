# WCET analysis of seL4

> The archived project page: the sound ARM11 analysis and why it stopped. report, full text.

Source · Trustworthy Systems (n.d.) · LLM reviewed · updated 2026-10-29 · https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html

Project page of the Trustworthy Systems group at UNSW Sydney, undated, read on 23 October 2026. [Current address](https://trustworthy.systems/projects/OLD/wcet/).

## What it shows

The project set out to find sound upper bounds on the execution time of every seL4 kernel operation. Hard real-time and mixed-criticality systems need such bounds for their schedulability analysis. A bound is sound when it never underestimates the true worst case, and the page says static analysis of the code makes that possible. The analysis works on the binary so that it does not depend on assumptions about the compiler.

The method follows the usual pipeline. A tool extracts the control-flow graph from the binary and feeds it to an analyser that models the processor, with upper bounds for instruction latencies and a model of the caches. An ILP solver then finds candidate worst-case paths. Loops without a fixed iteration count need bounds from outside. Many candidate paths are infeasible, typically behind mutually exclusive conditions that depend on input data, and they inflate the result unless an external analysis refutes them.

The page lists four main challenges. Static analysis of a binary cannot bound all loops, mainly because compilation loses much of the program's meaning; the binary cannot tell, for example, whether two pointers alias. Refuting infeasible paths needs the same lost knowledge. Without a cache analysis every memory access has to be counted as a miss. And most sound analyses cover programs of a few hundred lines, while seL4 has about 10,000.

The group performed a complete and sound WCET analysis of seL4 on the ARM11 microarchitecture, with a cache analysis and a toolchain built on the Chronos tool. Measurements on the worst-case paths found by the tool put the safe bound at about four times the worst observed time. Much of that gap comes from the cache analysis, since ARM11's 4-way L1 cache with random replacement has to be modelled as a direct-mapped cache of a quarter of its size. The page adds that the true worst case is probably much closer to the observed time, without a proof.

Loop bounds and infeasible paths were first determined by hand. Two tools, Sequoll and Trickle, automated part of it. The most successful approach used translation validation to link the binary to the C code and its proofs, so that hard loop bounds can be proved in the seL4 proof framework. Once those proofs exist, the toolset, graph-to-graph, analyses the whole kernel without manual input.

The project is archived. When Arm moved to out-of-order processors with version 7 of its architecture, it stopped publishing worst-case instruction latencies, and the analysis could no longer be done on recent Arm cores. The page sees hope in open RISC-V implementations, where all latency information can be obtained, names the CVA6 core as an example and says the analysis could in principle be resurrected for such cores. The group was looking for funding to do so.

## How

The page summarises the group's own work from 2007 to 2017 and lists the publications. It reports results. The evidence lies in those publications.

## Limits

The page is undated, and its status section is older than its publication list. The list already includes [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md), while the status still calls the project archived.

The page does not say on which processor graph-to-graph was used.

## Against the wiki

- [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md) replaces the status. The analysis runs again on 64-bit RISC-V, and sound latencies for CVA6 are expected in the first quarter of 2027.
- **Loop bounds were first set by hand.** The page says the sound ARM11 analysis used "manual (informal) analysis to determine loop bounds and infeasible paths"; proved bounds through translation validation came later, and the page does not name the processor for that step. Our reading: "sound and complete" holds for the analysis method, while its loop bounds on ARM11 were not proved.
- The two sources name the old analysis differently. This page says ARM11, and Sillitoe et al. say the "Armv7 (32-bit) version" of seL4. The original paper (Blackham et al. 2011) would settle it and is not yet covered here. Two later sources, [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md) and [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md), say Armv6 and Armv7; see [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md).

## For Silent Zero

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md): the sound bound this page reports is for ARM11, a processor no current Silent Zero candidate uses.

## Related pages

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md)
- [CVA6](https://silentzero.ooo/wiki/systems/cva6.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)
- [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md)
- [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)
