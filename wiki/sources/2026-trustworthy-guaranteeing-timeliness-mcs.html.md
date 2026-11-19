# Trustworthy Systems: Guaranteeing timeliness of MCS on seL4

> The project to get from budgets to provable deadlines on RISC-V. progress, full text.

Source · LLM reviewed · updated 2026-10-29 · https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html

The project page of the Trustworthy Systems group at UNSW Sydney, undated, read on 29 October 2026; its latest news entry is from 8 December 2025. [Page](https://trustworthy.systems/projects/RTA).

## What it shows

- **The aim.** The project wants a framework that guarantees deadlines in mixed-criticality systems built on [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md), and plans three steps: re-establish WCET for the current MCS kernel on RISC-V; extract worst-case instruction latencies from an actual RISC-V processor implementation; and build a reasoning framework that guarantees deadlines of critical components despite preemption by untrusted ones.
- **WCET per kernel operation.** Because capabilities can restrict a system to a subset of kernel operations, the page argues for a separate analysis per operation. A system that never destroys objects after initialisation can then have a lower bound; object destruction "tends to have the highest WCET of all kernel operations".
- **Why the old work cannot be reused.** It was done for 32-bit Armv6 and Armv7 processors, for which Arm published latencies and no longer does for later generations; for the kernel before MCS, which was much simpler; and on a heavily modified fork of the Chronos tool, which became unmaintained.
- **State.** The group's fork of Heptane performs a complete static analysis of the entire kernel; the timing outputs are not yet meaningful because latencies, cache-miss penalties and loop bounds are placeholders. The integration of verified loop bounds and infeasible-path refutations from the seL4 proofs is still to be re-established. The Heptane changes were merged upstream (news of 8 December 2025).
- **Latencies.** The group is working with its partner PlanV to extract sound latencies from the Verilog implementation of the open-source RISC-V processor used in the PISTIs-V project.
- **Funding.** Cyberagentur, as part of PISTIs-V in the programme "Ecosystem formally verifiable IT – Provable cybersecurity" (EvIT).

## How

A project page: aims, method and status, with a news list and publications. Results appear in the papers it lists, among them [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md).

## Limits

The page says itself that the timing outputs are not yet meaningful.

A careful reader adds:

- **The page calls MCS "currently undergoing formal verification".** The functional-correctness proof on RISC-V was announced complete on 29 June 2026 ([MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)); this sentence is older.
- **The page does not name the processor.** It says "the open-source RISC-V processor used in the PISTIs-V Project"; [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md) names CVA6.
- **No dates for the framework.** For a date, see [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md) (September 2027).

## Against the wiki

- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md), [WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md), [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md): **extends** them. The page names Armv6 and Armv7 for the old analysis, which adds a third account of which cores were covered; see [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md).
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md): **extends** it with the per-operation analysis.

## For Silent Zero

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md): the three steps are the path from today's state (budgets enforced) to the paper's goal (deadlines provable). None is finished.
- Our reading: per-operation WCET suits a static system. If Silent Zero hands no component the right to destroy kernel objects after boot, the most expensive operation drops out of the worst case. Whether Microkit systems can be configured that way is a question for the static-system page.

## Related pages

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [The static system](https://silentzero.ooo/wiki/design/static-system.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)
- [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md)
- [WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md)
