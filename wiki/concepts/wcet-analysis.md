---
type: concept
status: reviewed
sources: [2009-klein-sel4-formal-verification, nd-trustworthy-wcet-worst-case, 2026-sillitoe-resurrecting-sel4-wcet, 2026-trustworthy-guaranteeing-timeliness-mcs, 2026-heiser-mcs-safety-os, 2018-klein-formally-verified-software]
updated: 2026-10-29
---

# WCET analysis

Worst-case execution time analysis computes an upper bound on how long a piece of code can run. A real-time system needs such bounds for its tasks and for the kernel beneath them, or nobody can show that a deadline holds. A *sound* analysis never underestimates the true worst case, and static analysis of the code makes that possible ([[nd-trustworthy-wcet-worst-case]]).

## How it is done

Static analysis of the binary, so that nothing has to be assumed about the compiler. A tool extracts the control-flow graph, models the processor's pipeline and caches with upper bounds for each instruction's latency, and turns the result into an integer linear program whose solution is the longest path ([[nd-trustworthy-wcet-worst-case]]).

Three inputs decide whether the bound is sound and useful:

- **Instruction latencies.** They come from the processor vendor or from the hardware design. Arm stopped publishing them when it moved to out-of-order cores, which ended seL4's analysis on Arm, and later resumed for its in-order cores ([[2026-sillitoe-resurrecting-sel4-wcet]], footnote 1). On an open core such as [[cva6]] they can be derived from the design itself.
- **Loop bounds.** A loop whose iteration count the analysis cannot see needs a bound from outside. For seL4 these were eventually proved on the C code and carried to the binary by translation validation ([[nd-trustworthy-wcet-worst-case]]).
- **Infeasible paths.** Paths that can never run, for example behind mutually exclusive conditions, inflate the bound unless they are refuted.

The cache adds pessimism. On ARM11 the sound bound for seL4 was about four times the worst observed time, and much of that came from the cache analysis, because the random replacement policy of its L1 cache forces a pessimistic model ([[nd-trustworthy-wcet-worst-case]]).

## State for seL4, October 2026

| Target | State | Source |
| --- | --- | --- |
| 32-bit Arm, kernel before MCS | complete, sound analysis existed; archived | [[nd-trustworthy-wcet-worst-case]] |
| 64-bit RISC-V, MCS kernel | analysis runs, placeholder latencies and loop bounds, no bound yet; sound CVA6 latencies expected Q1 2027 | [[2026-sillitoe-resurrecting-sel4-wcet]] |
| Armv8, in-order core | planned | [[2026-sillitoe-resurrecting-sel4-wcet]], §5.2 |

Which 32-bit cores the old analysis covered is told three ways, and the accounts conflict. The archived project page names ARM11, Sillitoe et al. say the first analysis, Blackham et al. 2011, was on Armv7 (§1), and the current project page and the 2026 slides say Armv6 and Armv7 ([[2026-trustworthy-guaranteeing-timeliness-mcs]], [[2026-heiser-mcs-safety-os]]). The ARM1136 is an Armv6 core ([[2009-klein-sel4-formal-verification]], §5.1). On ARM11 the loop bounds were set by hand; proved bounds came later ([[nd-trustworthy-wcet-worst-case]]). Our reading: the safe statement is "32-bit Arm, before MCS". [[2018-klein-formally-verified-software]] cites Blackham et al. 2011 and Sewell et al. 2016 for it; neither is covered here yet.

The old work could not simply be reused. Besides the missing latencies, the old kernel predated MCS and was much simpler, and the analysis ran on a heavily modified fork of Chronos, which became unmaintained ([[2026-trustworthy-guaranteeing-timeliness-mcs]]).

The project plans a separate bound for each kernel operation, because capabilities let a system use only some of them; object destruction tends to have the highest WCET. The step after WCET is a schedulability framework that accounts for preemption by untrusted components ([[2026-trustworthy-guaranteeing-timeliness-mcs]]), due September 2027 according to [[2026-heiser-mcs-safety-os]].

## Open questions

- Some kernel loops have no static bound and are constrained by system design instead, among them the scheduling-context queues of MCS. A parameterised bound or more preemption points will be needed ([[2026-sillitoe-resurrecting-sel4-wcet]], §5.1). What a static system description can contribute is open; see [[kernel]].
