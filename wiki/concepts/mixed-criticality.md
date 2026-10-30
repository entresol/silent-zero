---
type: concept
status: reviewed
sources: [2026-heiser-mcs-safety-os, 2026-trustworthy-guaranteeing-timeliness-mcs, 2026-sel4-functional-correctness-proof]
updated: 2026-10-29
---

# Mixed criticality

A mixed-criticality system runs software of different criticality on one platform, from safety-critical to non-critical. Criticality is set by the impact of a failure, from loss of life to inconvenience. The certification of a critical component must not depend on how less critical components behave, so the OS has to prevent interference in space and in time ([[2026-heiser-mcs-safety-os]]).

## In seL4

[[sel4]]'s MCS configuration makes processor time a capability. A thread runs only if it holds a scheduling context with a period and a budget the kernel enforces. A passive server runs on its client's scheduling context and charges its time to the client. When a budget runs out, the kernel raises a timeout exception and leaves the reaction to user level ([[2026-heiser-mcs-safety-os]]).

## State, October 2026

- Functional correctness of the MCS kernel is proved on RISC-V since June 2026; a port to 64-bit Arm is under way ([[2026-sel4-functional-correctness-proof]]).
- Budgets bound how much time a component may take. They do not yet give a deadline: that needs a WCET bound for the kernel and a schedulability analysis. Both are being built; the group gives September 2027 for the schedulability framework ([[2026-heiser-mcs-safety-os]], [[2026-trustworthy-guaranteeing-timeliness-mcs]]). See [[wcet-analysis]].

## Open questions

- Which reaction to budget overrun suits a control loop that must not miss its deadline. The slides list emergency budget, rollback, lowering a client's priority and, reluctantly, priority inheritance, and say it is better to prevent timeouts completely ([[2026-heiser-mcs-safety-os]]).
