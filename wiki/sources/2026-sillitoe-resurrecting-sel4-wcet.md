---
type: source
id: 2026-sillitoe-resurrecting-sel4-wcet
status: reviewed
read: full
kind: progress
sources: [2026-sillitoe-resurrecting-sel4-wcet]
updated: 2026-10-29
---

# Sillitoe et al. 2026: Resurrecting seL4's WCET Analysis

Simon Sillitoe, Abdul Basit, Massimiliano Giacometti and Gernot Heiser (UNSW Sydney and PlanV Tech, Munich). Workshop paper, OSPERT 2026, Lund, July 2026 (venue and date from the publication list in [[nd-trustworthy-wcet-worst-case]]). [Abstract and PDF](https://trustworthy.systems/publications/papers/Sillitoe_BGH_26.abstract).

## What it shows

- **The analysis runs again, on the current kernel.** The authors analyse the complete, unmodified seL4 kernel for 64-bit RISC-V, built from the verified MCS configuration (`RISCV64_MCS_verified.cmake`, seL4 commit `deec818`). To make the binary analysable, they switch off compressed instructions and tell the compiler to emit no jump tables (§4).
- **The numbers do not mean anything yet.** The analysis uses placeholder values: 3 cycles for every non-memory instruction, 1 cycle for an L1 hit, 10 for an L2 hit, 100 for an L2 miss, and a bound of 10 for every loop. Infeasible paths are not yet removed. Under these values the kernel's worst case from entry to exit is about 21 million cycles, which the authors call "no more than an order-of-magnitude estimate" (§4).
- **Per entry point** (Table 1, same placeholders): system call 21,000 k cycles on a longest path of 730 k instructions; interrupt 470 k; exception 430 k; the Call fastpath 19 k and the ReplyRecv fastpath 27 k. The slow system-call path dominates.
- **The problem is large for this kind of analysis.** The kernel's control-flow graph is small (154 functions, about 3.2 k basic blocks, 13 k instructions, 50 loops). Context-sensitive analysis expands it to about 110 k calling contexts and 1.5 M contextual basic blocks, and the integer linear program has about 3.1 M variables and 5.9 M constraints (§4). One run over the kernel's roughly 11,000 lines takes about 3 hours (§3).
- **The tool is open and the cost was moderate.** The authors chose the open-source WCET tool Heptane. They added the RISC-V supervisor instructions it lacked and the kernel's control flow (the `sret` exit, non-local jumps, bounded recursion), taught it tail calls and a cache analysis for arbitrary pointers, and replaced algorithms that did not scale. The change touched 102 files. A recent graduate without prior experience in WCET analysis or formal methods did it in five to six months of full-time work. The changes are upstream in Heptane (§3, §6).
- **What is still to come** (§5):
  - Loop bounds and infeasible-path refutations proved on the C code and carried into the binary analysis, by reviving the toolchain of Sewell et al. (2017). It runs on the RISC-V kernel again.
  - Sound instruction latencies for the open CVA6 core. A candidate bound per functional unit comes from simulating the core's SystemVerilog source; the model checker SymbiYosys then has to prove it as an assertion. Expected in the first quarter of 2027. Until then, approximate latencies from simulation, which the authors call unsound.
  - The same analysis on an in-order Armv8 processor.
  - Separate bounds per system call, then optimising the kernel's worst-case paths.

## How

The authors analyse the kernel binary statically. Heptane extracts the control-flow graph and models caches and pipeline with given latencies, and an ILP solver finds the longest path. The earlier seL4 analysis used the same method with a different tool. The paper reports how far the pipeline has come and gives no bound yet.

## Limits

The authors say themselves that the figures are placeholders and the result is not yet meaningful. They also name a limit of the method:

- **Some loops have no static bound.** A handful of kernel loops walk structures sized at run time, such as capability lookup tables, message cancellation queues and the scheduling-context queues that MCS introduces. The authors say these loops are constrained by system design instead, for example by the kernel's preemption mechanism or the static system configuration. They will need a parameterised WCET or more preemption points (§5.1).

A careful reader adds:

- **The analysed binary is built with two extra settings.** The paper does not say whether the translation validation that links the proof to the binary covers exactly this build.
- **A proof against the RTL is not a proof about the chip.** The planned latencies are proved for CVA6's SystemVerilog design. A chip or FPGA built from it is still assumed to behave like the design.
- **Two descriptions of the old analysis.** The paper places it on the "Armv7 (32-bit) version" of seL4 (§1), and the project page names the ARM11 microarchitecture ([[nd-trustworthy-wcet-worst-case]]). Blackham et al. (2011), not yet covered here, would settle which is meant. The current project page and the 2026 slides name both Armv6 and Armv7 ([[2026-trustworthy-guaranteeing-timeliness-mcs]], [[2026-heiser-mcs-safety-os]]); see [[wcet-analysis]].

## Against the wiki

- [[nd-trustworthy-wcet-worst-case]]: **replaces** its status. The project page says the work is archived and that RISC-V is the hope; this paper shows the analysis running on RISC-V. It also **extends** one detail. The project page says Arm stopped publishing latencies when it moved to out-of-order cores. This paper adds that Arm stopped even for its in-order cores at the time, and later resumed for them (footnote 1).
- [[wcet-analysis]], [[sel4]], [[cva6]]: created with this source.

## For zOS

- [[kernel]]: a bound on the kernel's WCET is the precondition for real time. Since this paper, it is work in progress with a date (sound latencies for CVA6 in the first quarter of 2027), no longer an archived project.
- The paper's Section 4 says Arm stopped publishing latencies "for its out-of-order cores" and concludes that the first zOS should run on an open RISC-V core, "because only there is a proof of its timing within reach". This source plans the same analysis on an in-order Armv8 core and says Arm publishes latencies for those cores again. It does not say where the Armv8 latencies will come from. Our reading: the paper's conclusion stands, and only its wording "for its out-of-order cores" is narrower than this source; the difference left is the kind of evidence. On CVA6 the latencies can be proved against the hardware design, while on Arm they would rest on the vendor's documentation and stay assumed.
- Our reading: the loops without a static bound (§5.1) favour a static system. A Microkit system declares its protection domains, channels and memory at build time, so the sizes of these kernel structures follow from the system description. Whether that is enough for the bounds the analysis needs is open.
