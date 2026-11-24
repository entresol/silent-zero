# Mixed criticality

> Software of different criticality on one platform; processor time as a capability in seL4 MCS; partitions under a hypervisor in commercial robot stacks.

Concept · LLM reviewed · updated 2026-10-29 · 7 sources · https://silentzero.ooo/wiki/concepts/mixed-criticality.html

A mixed-criticality system runs software of different criticality on one platform, from safety-critical to non-critical. Criticality is set by the impact of a failure, from loss of life to inconvenience. The certification of a critical component must not depend on how less critical components behave, so the OS has to prevent interference in space and in time ([MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)).

## In seL4

[seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)'s MCS configuration makes processor time a capability. A thread runs only if it holds a scheduling context with a period and a budget the kernel enforces. A passive server runs on its client's scheduling context and charges its time to the client. When a budget runs out, the kernel raises a timeout exception and leaves the reaction to user level ([MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)).

## State, October 2026

- Functional correctness of the MCS kernel is proved on RISC-V since June 2026; a port to 64-bit Arm is under way ([MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)).
- Budgets bound how much time a component may take. They do not yet give a deadline: that needs a WCET bound for the kernel and a schedulability analysis. Both are being built; the group gives September 2027 for the schedulability framework ([MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md), [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)). See [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md).

## Commercial systems

Two vendors' pages describe it with partitions under a separation kernel or hypervisor and a real-time kernel on the safety side. SYSGO's [PikeOS](https://silentzero.ooo/wiki/systems/pikeos.html.md) offers partitions with Linux or ROS 2 as an untrusted guest ([SYSGO: PikeOS for robotics and humanoids](https://silentzero.ooo/wiki/sources/nd-sysgo-robotics-humanoids.html.md)). In one of its two configurations on the IGX Thor board, NVIDIA's Halos Core puts a Linux VM for AI and a QNX VM for safety-critical functions under a hypervisor; the other configuration is Linux only ([Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md), [QNX](https://silentzero.ooo/wiki/systems/qnx.html.md)). An analyst names mixed-criticality designs with a hypervisor and deterministic scheduling as a trend in robot operating systems ([ranking of real-time operating systems for robotics safety](https://silentzero.ooo/wiki/sources/2026-abi-research-rtos-robotics-ranking.html.md)). Our reading: these separate by partitioning and a hypervisor, while seL4's MCS makes processor time a capability inside one kernel; the sources give no comparison.

## Open questions

- Which reaction to budget overrun suits a control loop that must not miss its deadline. The slides list emergency budget, rollback, lowering a client's priority and, reluctantly, priority inheritance, and say it is better to prevent timeouts completely ([MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)).

## Sources

- [Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md)
- [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)
- [QNX and NVIDIA deepen their collaboration](https://silentzero.ooo/wiki/sources/2026-qnx-nvidia-deepen-collaboration.html.md)
- [ranking of real-time operating systems for robotics safety](https://silentzero.ooo/wiki/sources/2026-abi-research-rtos-robotics-ranking.html.md)
- [SYSGO: PikeOS for robotics and humanoids](https://silentzero.ooo/wiki/sources/nd-sysgo-robotics-humanoids.html.md)
- [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [The static system](https://silentzero.ooo/wiki/design/static-system.html.md)
- [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md)
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md)
- [Atmosphere](https://silentzero.ooo/wiki/systems/atmosphere.html.md)
- [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md)
- [NVIDIA Halos for Robotics](https://silentzero.ooo/wiki/systems/nvidia-halos.html.md)
- [PikeOS](https://silentzero.ooo/wiki/systems/pikeos.html.md)
- [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md)
- [QNX](https://silentzero.ooo/wiki/systems/qnx.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [Atmosphere, practical verified kernels with Rust and Verus](https://silentzero.ooo/wiki/sources/2025-chen-atmosphere-practical-verified.html.md)
- [context-dependent regions of attraction for a multi-candidate Simplex](https://silentzero.ooo/wiki/sources/2026-jager-context-dependent-runtime.html.md)
- [Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md)
- [Halos for Robotics, the announcement](https://silentzero.ooo/wiki/sources/2026-nvidia-announces-halos-robotics.html.md)
- [Linux kernel documentation: real-time preemption](https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [The seL4 Device Driver Framework](https://silentzero.ooo/wiki/sources/2022-parker-sel4-device-driver.html.md)
