---
type: source
id: 2026-trustworthy-guaranteeing-timeliness-mcs
status: reviewed
read: full
kind: progress
sources: [2026-trustworthy-guaranteeing-timeliness-mcs]
updated: 2026-10-29
---

# Trustworthy Systems: Guaranteeing timeliness of MCS on seL4

The project page of the Trustworthy Systems group at UNSW Sydney, undated, read on 29 October 2026; its latest news entry is from 8 December 2025. [Page](https://trustworthy.systems/projects/RTA).

## What it shows

- **The aim.** The project wants a framework that guarantees deadlines in mixed-criticality systems built on [[sel4]], and plans three steps: re-establish WCET for the current MCS kernel on RISC-V; extract worst-case instruction latencies from an actual RISC-V processor implementation; and build a reasoning framework that guarantees deadlines of critical components despite preemption by untrusted ones.
- **WCET per kernel operation.** Because capabilities can restrict a system to a subset of kernel operations, the page argues for a separate analysis per operation. A system that never destroys objects after initialisation can then have a lower bound; object destruction "tends to have the highest WCET of all kernel operations".
- **Why the old work cannot be reused.** It was done for 32-bit Armv6 and Armv7 processors, for which Arm published latencies and no longer does for later generations; for the kernel before MCS, which was much simpler; and on a heavily modified fork of the Chronos tool, which became unmaintained.
- **State.** The group's fork of Heptane performs a complete static analysis of the entire kernel; the timing outputs are not yet meaningful because latencies, cache-miss penalties and loop bounds are placeholders. The integration of verified loop bounds and infeasible-path refutations from the seL4 proofs is still to be re-established. The Heptane changes were merged upstream (news of 8 December 2025).
- **Latencies.** The group is working with its partner PlanV to extract sound latencies from the Verilog implementation of the open-source RISC-V processor used in the PISTIs-V project.
- **Funding.** Cyberagentur, as part of PISTIs-V in the programme "Ecosystem formally verifiable IT – Provable cybersecurity" (EvIT).

## How

A project page: aims, method and status, with a news list and publications. Results appear in the papers it lists, among them [[2026-sillitoe-resurrecting-sel4-wcet]].

## Limits

The page says itself that the timing outputs are not yet meaningful.

A careful reader adds:

- **The page calls MCS "currently undergoing formal verification".** The functional-correctness proof on RISC-V was announced complete on 29 June 2026 ([[2026-sel4-functional-correctness-proof]]); this sentence is older.
- **The page does not name the processor.** It says "the open-source RISC-V processor used in the PISTIs-V Project"; [[2026-sillitoe-resurrecting-sel4-wcet]] names CVA6.
- **No dates for the framework.** For a date, see [[2026-heiser-mcs-safety-os]] (September 2027).

## Against the wiki

- [[wcet-analysis]], [[nd-trustworthy-wcet-worst-case]], [[2026-sillitoe-resurrecting-sel4-wcet]]: **extends** them. The page names Armv6 and Armv7 for the old analysis, which adds a third account of which cores were covered; see [[wcet-analysis]].
- [[kernel]]: **extends** it with the per-operation analysis.

## For zOS

- [[kernel]]: the three steps are the path from today's state (budgets enforced) to the paper's goal (deadlines provable). None is finished.
- Our reading: per-operation WCET suits a static system. If zOS hands no component the right to destroy kernel objects after boot, the most expensive operation drops out of the worst case. Whether Microkit systems can be configured that way is a question for the static-system page.
