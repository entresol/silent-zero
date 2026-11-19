# Mixed criticality

> Software of different criticality on one platform; processor time as a capability in seL4 MCS.

Concept · LLM reviewed · updated 2026-10-29 · 3 sources · https://silentzero.ooo/wiki/concepts/mixed-criticality.html

A mixed-criticality system runs software of different criticality on one platform, from safety-critical to non-critical. Criticality is set by the impact of a failure, from loss of life to inconvenience. The certification of a critical component must not depend on how less critical components behave, so the OS has to prevent interference in space and in time ([MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)).

## In seL4

[seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)'s MCS configuration makes processor time a capability. A thread runs only if it holds a scheduling context with a period and a budget the kernel enforces. A passive server runs on its client's scheduling context and charges its time to the client. When a budget runs out, the kernel raises a timeout exception and leaves the reaction to user level ([MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)).

## State, October 2026

- Functional correctness of the MCS kernel is proved on RISC-V since June 2026; a port to 64-bit Arm is under way ([MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)).
- Budgets bound how much time a component may take. They do not yet give a deadline: that needs a WCET bound for the kernel and a schedulability analysis. Both are being built; the group gives September 2027 for the schedulability framework ([MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md), [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)). See [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md).

## Open questions

- Which reaction to budget overrun suits a control loop that must not miss its deadline. The slides list emergency budget, rollback, lowering a client's priority and, reluctantly, priority inheritance, and say it is better to prevent timeouts completely ([MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)).

## Sources

- [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)
- [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [The static system](https://silentzero.ooo/wiki/design/static-system.html.md)
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md)
- [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md)
- [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md)
- [Linux kernel documentation: real-time preemption](https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [The seL4 Device Driver Framework](https://silentzero.ooo/wiki/sources/2022-parker-sel4-device-driver.html.md)
