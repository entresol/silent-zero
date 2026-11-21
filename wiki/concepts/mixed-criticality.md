---
type: concept
status: reviewed
sources: [2026-heiser-mcs-safety-os, 2026-trustworthy-guaranteeing-timeliness-mcs, 2026-sel4-functional-correctness-proof, nd-sysgo-robotics-humanoids, 2026-nvidia-inside-halos-robotics, 2026-qnx-nvidia-deepen-collaboration, 2026-abi-research-rtos-robotics-ranking]
glossary: Mixed criticality (MCS)
updated: 2026-10-29
---

# Mixed criticality

A mixed-criticality system runs software of different criticality on one platform, from safety-critical to non-critical. Criticality is set by the impact of a failure, from loss of life to inconvenience. The certification of a critical component must not depend on how less critical components behave, so the OS has to prevent interference in space and in time ([[2026-heiser-mcs-safety-os]]).

## In seL4

[[sel4]]'s MCS configuration makes processor time a capability. A thread runs only if it holds a scheduling context with a period and a budget the kernel enforces. A passive server runs on its client's scheduling context and charges its time to the client. When a budget runs out, the kernel raises a timeout exception and leaves the reaction to user level ([[2026-heiser-mcs-safety-os]]).

## State, October 2026

- Functional correctness of the MCS kernel is proved on RISC-V since June 2026; a port to 64-bit Arm is under way ([[2026-sel4-functional-correctness-proof]]).
- Budgets bound how much time a component may take. They do not yet give a deadline: that needs a WCET bound for the kernel and a schedulability analysis. Both are being built; the group gives September 2027 for the schedulability framework ([[2026-heiser-mcs-safety-os]], [[2026-trustworthy-guaranteeing-timeliness-mcs]]). See [[wcet-analysis]].

## Commercial systems

Two vendors' pages describe it with partitions under a separation kernel or hypervisor and a real-time kernel on the safety side. SYSGO's [[pikeos]] offers partitions with Linux or ROS 2 as an untrusted guest ([[nd-sysgo-robotics-humanoids]]). In one of its two configurations on the IGX Thor board, NVIDIA's Halos Core puts a Linux VM for AI and a QNX VM for safety-critical functions under a hypervisor; the other configuration is Linux only ([[2026-nvidia-inside-halos-robotics]], [[qnx]]). An analyst names mixed-criticality designs with a hypervisor and deterministic scheduling as a trend in robot operating systems ([[2026-abi-research-rtos-robotics-ranking]]). Our reading: these separate by partitioning and a hypervisor, while seL4's MCS makes processor time a capability inside one kernel; the sources give no comparison.

## Open questions

- Which reaction to budget overrun suits a control loop that must not miss its deadline. The slides list emergency budget, rollback, lowering a client's priority and, reluctantly, priority inheritance, and say it is better to prevent timeouts completely ([[2026-heiser-mcs-safety-os]]).
