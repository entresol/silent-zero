---
type: system
status: reviewed
sources: [2026-zhao-agate-capability-microkernels]
short: Capability microkernel for agents, unverified
updated: 2026-11-21
---

# Agate

A capability microkernel for AI agents from Huawei, in the tradition of seL4: AArch64, 45 system calls, 12 capability types, kernel-stamped identity on IPC, versioned context objects and a deadline scheduler for user-response deadlines ([[2026-zhao-agate-capability-microkernels]]).

## State, September 2026

A three-page paper at the AgenticOS workshop. The mechanisms are implemented and unit-tested (1,243 self-tests), a bounded agent, tool and reply round trip works, and the baseline is a single CPU under QEMU. An end-to-end agent workload, performance comparison, SMP correctness and formal verification are future work ([[2026-zhao-agate-capability-microkernels]]).

## Licence and code

The paper links no repository and names no licence.

## Related

[[sel4]], [[broker]], [[agent-operating-systems]], [[landlock]].

## Open questions

- What the userspace trusted broker decides and how; the paper leaves the policy to a manifest and a per-tenant broker.
- Whether its deadlines, set for user responsiveness, could carry a control loop's timing; nothing in the paper says so.
- Whether the chokepoint holds against an adversarial agent; the authors list that evaluation as future work.
