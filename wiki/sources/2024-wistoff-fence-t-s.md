---
type: source
id: 2024-wistoff-fence-t-s
status: reviewed
read: full
kind: measurement
sources: [2024-wistoff-fence-t-s]
updated: 2026-11-21
---

# Wistoff, Heiser and Benini 2024: fence.t.s for out-of-order cores

Nils Wistoff, Gernot Heiser and Luca Benini (ETH Zurich, UNSW Sydney, University of Bologna). "fence.t.s: Closing Timing Channels in High-Performance Out-of-Order Cores through ISA-Supported Temporal Partitioning", slides of the talk at APPLEPIES, Turin, 20 September 2024. [PDF](https://pulp-platform.org/docs/applepies2024/Nils_Wistoff_APPLEPIES24_fencets.pdf). Read: all 20 slides in full. Slides are terse and give no method detail, no confidence bounds and no per-benchmark numbers, and the leakage plots are read only through the figures printed on them.

## What it shows

- **A new problem on out-of-order cores.** The earlier temporal fence `fence.t` was built on [[cva6]], a 6-stage in-order core. The slides ask whether it can be implemented in out-of-order cores and at what cost (slide 4), and name two new challenges (slides 7 to 12).
- **Mixed state.** The register allocation table and the physical register file cannot be reached by software, so they count as microarchitectural state and should be cleared. The physical registers also hold the architectural register values, which must survive. The authors' answer is to save the architectural registers to main memory, clear everything including the table and the file, and load the registers back. They note that the table is then history-independent (slides 7 to 11).
- **Reusability.** One monolithic instruction would not reuse existing mechanisms, would give no fine control over what is cleared, and would need complex control logic. The authors split the fence into several steps (slide 12).
- **The sequence.** Save the architectural registers to the stack; save the stack pointer to a well-known protected location; write back the dirty L1 data cache; invalidate the SRAMs; clear the flip-flops; restore the stack pointer and the registers; pad the execution time so that the switch latency does not leak (slide 13).
- **On OpenC910.** The target is T-Head's OpenC910: 64-bit, 12 stages, superscalar, out-of-order, RV64GCXtheadc, Verilog open-sourced in 2021 under the Apache licence; reorder buffer up to 192 instructions, decode width 3, issue width 8 (slide 6). Most of the sequence uses standard RISC-V loads and stores plus the vendor's custom `dcache.call`, `sync.i` and the `mcor` and `mrvbr` registers. One new instruction, `ff.clr`, clears all on-core flip-flops except the control and status registers (slides 14, 20).
- **Channels closed.** In the authors' channel benchmark on an FPGA (VCU128), the slide gives "M" and the noise level "M0" with the label "mb" and cites "Channel bench [4]" (slide 16); our reading is that M is the mutual information in millibits, the metric of the 2022 paper, which the slides do not state. Unmitigated, and with `fence.t.s`:

| Channel | Unmitigated M (M0) | With fence.t.s M (M0) |
| --- | --- | --- |
| L1 data cache | 4283 (0.7) | 64.3 (71.0) |
| L1 instruction cache | 5940 (0.8) | 3.2 (3.5) |
| Branch history table | 698.8 (1.1) | 3.3 (6.4) |

  The slides vary in strength. Slide 5 says it "closes all on-core timing channels in OpenC910" at a performance overhead of 1.0 per cent; slide 16 says it "closes all timing channels!"; slide 18 says "all observed". The measured channels are the three above (slide 5). In each shielded case M is of the same order as M0 or below it.
- **Cost.** Average 1.0 per cent overhead on Splash-2, with two threads (one benchmark and one idle), a 1 GHz system clock, a 10 ms time slice and a context switch every 10 million cycles. The slide gives the average and shows a bar chart without printed per-benchmark values. Synthesis in GF12 LP+ FinFET at 2 GHz showed "negligible hardware costs", with no figure on the slide (slides 5, 17, 18).
- **Standardisation.** The authors found that OpenC910 already provides most of the mechanisms time protection needs, and say that specifying them would enable time protection across implementations. The closing slide shows only "uSC SIG / Timing Fences TG" (slide 18); our reading is that this is the RISC-V micro-architecture special interest group and its task group.

## How

OpenC910 on a Xilinx VCU128 FPGA, with an operating system and an application on top, and the channel benchmark of Ge et al. (2018) measuring leakage as mutual information; "N = 106" is printed beside the setup, probably 10^6 with the superscript lost in extraction; the slide does not say what N counts (slide 15). The OS is not named on the slides.

## Limits

On the slides the authors limit the claim to the channels they observed, on one core, in the channel benchmark (slides 16, 18), and state nothing further.

A careful reader adds the following, as inference.

- Slides are not the paper. The method, the way noise is bounded and what N counts are not given; "mb" is read here as millibits and the metric as the 2022 paper's mutual information, both inference.
- Three channels are shown, in the L1 data cache, the L1 instruction cache and the branch history table. Other on-core state may have channels the benchmark did not probe, and a claim of "all" depends on what was looked for.
- The L1 data cache figure with `fence.t.s` (64.3) is below its noise figure (71.0), and the branch history table's (3.3) below 6.4. The slides do not say how the noise level was fixed, so the comparison stays qualitative.
- The padding time is not given, nor how it was chosen for OpenC910.
- The sequence relies on vendor extensions of one core (`dcache.call`, `mcor`, `mrvbr`, `sync.i`). The new `ff.clr` is a custom instruction; none of this is in the ratified ISA.
- The overhead is for a 10 ms slice with an idle second thread; a shorter slice would raise it, since the cost is paid per switch (our reading).
- No cross-core channels, no multicore result and no physical channels appear on the slides. The earlier paper put cross-core out of scope.

## Against the wiki

- [[time-protection]]: **extends**. The page's statement that closing on-core channels needs an instruction the mainstream ISAs lack stays. This source adds one measurement on an out-of-order core, for one open-sourced commercial design, at 1.0 per cent against under 1 per cent on [[cva6]] ([[2022-wistoff-systematic-prevention-core]]). The setups differ, since that paper's FPGA ran at 50 MHz and the slides give a 1 GHz clock; the comparison stays qualitative.
- [[2022-wistoff-systematic-prevention-core]]: **extends**. That paper left out-of-order cores as possibly harder (§4.2.3); this talk reports the challenge, mixed state, and a working answer. The 2024 sequence keeps a hardware flip-flop clear (`ff.clr`, slides 13 and 14); what is new is the software save and restore of the architectural registers around it.
- [[cva6]]: **extends** only by contrast. The new result is on a different core, so the page about the CVA6 changes nothing.
- [[risc-v]]: **extends**. The fence is not ratified; the slides point to a task group working on timing fences. This source does not report its status.
- [[wcet-analysis]]: no direct link. The padded switch is a fixed duration, which helps WCET reasoning (our reading); no bound is given.
- The paper's Section 4 **confirms** that the hardware instruction exists only as prototypes; this source is the paper's 2024 reference and adds the out-of-order case. No contradiction.

## For zOS

- [[kernel]]: no change of state. Our reading is that the table row on time protection (prototype, measurement) stays, and the source widens the prototype evidence from an in-order core to one out-of-order core, and shows the standardisation route is a task group, not a ratified extension.
- [[real-time-loops]]: no change of state. The padding step makes a context switch of fixed length, which a loop could count on, but the slides give no length.
- Nothing in zOS is built, and nothing here bears on [[safety-path]] directly.
