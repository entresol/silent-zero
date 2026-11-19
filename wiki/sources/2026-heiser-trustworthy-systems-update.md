---
type: source
id: 2026-heiser-trustworthy-systems-update
status: reviewed
read: partial
kind: progress
sources: [2026-heiser-trustworthy-systems-update]
updated: 2026-11-14
---

# Heiser 2026: Trustworthy Systems R&D update

Gernot Heiser, Trustworthy Systems Group, School of Computer Science & Engineering, UNSW. Talk at the seL4 Summit, September 2026, 40 slides under CC BY 4.0 ([abstract and slides](https://trustworthy.systems/publications/papers/Heiser_26:sel4s.abstract)). Read from the slides alone; the video was not watched, and the plots on the multikernel slides carry no numbers in their text, so their values are not read. Slide numbers below are those printed on the slides.

## What it shows

- **Microkit** (slide 4). Dynamic features: protection domains can be started, stopped and upgraded at run time, as the Carrels talk of the same summit uses them. Virtualisation support has matured: "x86_64 UEFI fully supported", and Windows 11 boots on x86-64 (the slide points to another talk). Acacia is named as tooling for system composition ("much improved").
- **sDDF and [[lionsos]]** (slides 5 to 9). The device driver framework gains ACPI and PCIe support, has a zero-copy data plane and control queues that are bounded, lock-free and single-producer, single-consumer, and "outperforms Linux" (no figure on the slide). LionsOS has a community firewall project, released in November 2025, and a virtual network switch. Pancake, the C-like language with a verified compiler, is used to implement and verify drivers, virtualisers and libmicrokit, with performance "approaching C".
- **Verification agenda for the next year** (slide 10). Titled "for next year", a diagram with the words mixed criticality, confinement including timing, verification and formalisation. It gives no dates.
- **WCET analysis of the kernel** (slides 16 to 26). The old analysis for Armv6 and Armv7 "bit-rotted": its tool lost support, and Arm stopped (the slide adds "for a while") giving instruction latencies when it moved to out-of-order cores. The revival targets `RISCV64_MCS_verified` with the tool Heptane (University of Rennes). The static control-flow graph has 154 functions, 3.2 k basic blocks and 50 loops. Context sensitivity expands it to 110 k calling contexts and 1.5 M contextual blocks, and the integer linear program has 3.1 M variables and 5.9 M constraints (slide 22). The cache analysis never finished, because its worklist grew to 600 k entries (slide 23). Iterating strongly connected components in topological order fixed that, together with what the slide calls engineering hygiene (fewer variables in the integer program, better memory management, less copying of analysis state): "all full-kernel cache analyses" went "from infeasible to ≈ 1 h" (slide 24). The first end-to-end result is an order-of-magnitude figure of about 21 M cycles, dominated by the slow path of the system call entry, from placeholder latencies and uniform loop bounds, without infeasible-path elimination, for a single-core in-order target (slide 25). The slide on work in progress ticks the revival of verified loop-bound import and leaves infeasible-path refutation, sound latencies from the RISC-V Verilog and a per-entry-point model open. The stated aim is a verified response-time analysis (slide 26).
- **SMP against multikernel** (slides 27 to 39). The talk revisits a 2015 comparison. The slides repeat its findings that a big kernel lock adds 10 per cent to a system call and fine-grained locking 20 to 70 per cent, measured on x86 Haswell and Arm A9 (slide 29; the slide does not say which figure belongs to which). In the interference benchmark the text says the big kernel lock gives "strong interference" and the multikernel none (slide 33); an earlier benchmark is marked "No cross-core operations!" (slide 32). For cross-core notifications it says doing everything in the kernel "is more expensive than in userland" (slide 36). For a passive server, it says "cores compete for server", hence "frequent migrations", and quotes Liedtke's minimality principle (slide 38). The last section is titled "SMP"; its slide holds no text beyond the title. No conclusion is stated in the slides' text.

## How

A progress talk. The figures come from the group's own tools and benchmarks, and the slides give no method for the benchmarks.

## Limits

- Slides only: no text for the multikernel argument. Slide 34 ("Observations") recalls the 2015 argument that SMP is preferred for cores sharing a cache and asks "Really?"; the slides do not answer in words for that case, only for notifications (slide 36).
- The WCET figures are the ones of [[2026-sillitoe-resurrecting-sel4-wcet]], and the page there stays the main source. The new facts here are the scaling fix and the run time of the cache analyses; the slides give no time for the integer program or the whole pipeline.
- A careful reader adds: "≈ 1 h" for the cache analyses (slide 24) and the "about 3 hours" for one run in the July paper (§3) may describe different things; this page does not decide which is current.

## Against the wiki

- [[wcet-analysis]] and [[2026-sillitoe-resurrecting-sel4-wcet]]: gives the same 21 M cycles and placeholders and the same graph size; extends them with the cause of the scaling problem and its fix, and with the tick for verified loop bounds.
- [[kernel]] and [[sel4]]: the slides give no date or status for the multikernel proof. The plan stays that of [[nd-sel4-sel4-roadmap]].
- [[microkit]]: adds the dynamic features and x86-64 UEFI support, beyond the manual of version 2.3.0.
- [[lionsos]]: adds the firewall and the virtual network switch.

## For zOS

The [[kernel]] page's real-time rows do not change: still no bound, still single-core and in-order. The slides state no conclusion on SMP against multikernel and no proof status, so the paper's sentence that a proven Silent Zero starts on a single core per kernel instance (Section 4) rests on the roadmap alone.
