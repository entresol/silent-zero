# WCET analysis

> Upper bounds on execution time, what they need, and where seL4 stands.

Concept · LLM reviewed · updated 2026-10-29 · 6 sources · https://silentzero.ooo/wiki/concepts/wcet-analysis.html

Worst-case execution time analysis computes an upper bound on how long a piece of code can run. A real-time system needs such bounds for its tasks and for the kernel beneath them, or nobody can show that a deadline holds. A *sound* analysis never underestimates the true worst case, and static analysis of the code makes that possible ([WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)).

## How it is done

Static analysis of the binary, so that nothing has to be assumed about the compiler. A tool extracts the control-flow graph, models the processor's pipeline and caches with upper bounds for each instruction's latency, and turns the result into an integer linear program whose solution is the longest path ([WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)).

Three inputs decide whether the bound is sound and useful:

- **Instruction latencies.** They come from the processor vendor or from the hardware design. Arm stopped publishing them when it moved to out-of-order cores, which ended seL4's analysis on Arm, and later resumed for its in-order cores ([Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md), footnote 1). On an open core such as [CVA6](https://silentzero.ooo/wiki/systems/cva6.html.md) they can be derived from the design itself.
- **Loop bounds.** A loop whose iteration count the analysis cannot see needs a bound from outside. For seL4 these were eventually proved on the C code and carried to the binary by translation validation ([WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)).
- **Infeasible paths.** Paths that can never run, for example behind mutually exclusive conditions, inflate the bound unless they are refuted.

The cache adds pessimism. On ARM11 the sound bound for seL4 was about four times the worst observed time, and much of that came from the cache analysis, because the random replacement policy of its L1 cache forces a pessimistic model ([WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)).

## State for seL4, October 2026

| Target | State | Source |
| --- | --- | --- |
| 32-bit Arm, kernel before MCS | complete, sound analysis existed; archived | [WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md) |
| 64-bit RISC-V, MCS kernel | analysis runs, placeholder latencies and loop bounds, no bound yet; sound CVA6 latencies expected Q1 2027 | [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md) |
| Armv8, in-order core | planned | [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md), §5.2 |

Which 32-bit cores the old analysis covered is told three ways, and the accounts conflict. The archived project page names ARM11, Sillitoe et al. say the first analysis, Blackham et al. 2011, was on Armv7 (§1), and the current project page and the 2026 slides say Armv6 and Armv7 ([Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md), [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)). The ARM1136 is an Armv6 core ([seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md), §5.1). On ARM11 the loop bounds were set by hand; proved bounds came later ([WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)). Our reading: the safe statement is "32-bit Arm, before MCS". [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md) cites Blackham et al. 2011 and Sewell et al. 2016 for it; neither is covered here yet.

The old work could not simply be reused. Besides the missing latencies, the old kernel predated MCS and was much simpler, and the analysis ran on a heavily modified fork of Chronos, which became unmaintained ([Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)).

The project plans a separate bound for each kernel operation, because capabilities let a system use only some of them; object destruction tends to have the highest WCET. The step after WCET is a schedulability framework that accounts for preemption by untrusted components ([Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)), due September 2027 according to [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md).

## Open questions

- Some kernel loops have no static bound and are constrained by system design instead, among them the scheduling-context queues of MCS. A parameterised bound or more preemption points will be needed ([Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md), §5.1). What a static system description can contribute is open; see [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md).

## Sources

- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)
- [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md)
- [seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md)
- [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)
- [WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)

## Related pages

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [CVA6](https://silentzero.ooo/wiki/systems/cva6.html.md)
- [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [CHERIoT, complete memory safety for embedded devices](https://silentzero.ooo/wiki/sources/2023-amar-cheriot-complete-memory.html.md)
- [Linux kernel documentation: real-time preemption](https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html.md)
