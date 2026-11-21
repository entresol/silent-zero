# Agate

> Capability microkernel for agents with a userspace broker and user-response deadlines; unit-tested, not verified.

System · LLM reviewed · updated 2026-11-21 · 1 source · https://silentzero.ooo/wiki/systems/agate.html

A capability microkernel for AI agents from Huawei, in the tradition of seL4: AArch64, 45 system calls, 12 capability types, kernel-stamped identity on IPC, versioned context objects and a deadline scheduler for user-response deadlines ([Agate, capability microkernels for AI agents](https://silentzero.ooo/wiki/sources/2026-zhao-agate-capability-microkernels.html.md)).

## State, September 2026

A three-page paper at the AgenticOS workshop. The mechanisms are implemented and unit-tested (1,243 self-tests), a bounded agent, tool and reply round trip works, and the baseline is a single CPU under QEMU. An end-to-end agent workload, performance comparison, SMP correctness and formal verification are future work ([Agate, capability microkernels for AI agents](https://silentzero.ooo/wiki/sources/2026-zhao-agate-capability-microkernels.html.md)).

## Licence and code

The paper links no repository and names no licence.

## Related

[seL4](https://silentzero.ooo/wiki/systems/sel4.html.md), [The broker](https://silentzero.ooo/wiki/design/broker.html.md), [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md), [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md).

## Open questions

- What the userspace trusted broker decides and how; the paper leaves the policy to a manifest and a per-tenant broker.
- Whether its deadlines, set for user responsiveness, could carry a control loop's timing; nothing in the paper says so.
- Whether the chokepoint holds against an adversarial agent; the authors list that evaluation as future work.

## Sources

- [Agate, capability microkernels for AI agents](https://silentzero.ooo/wiki/sources/2026-zhao-agate-capability-microkernels.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
