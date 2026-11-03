---
type: system
status: reviewed
sources: [nd-linux-real-time-preemption]
short: Linux build option for low-latency scheduling
updated: 2026-11-03
---

# PREEMPT_RT

The configuration of the Linux kernel that makes it real-time in the kernel developers' sense: sleeping locks with priority inheritance and forced-threaded interrupts leave only a few critical paths non-preemptible ([[nd-linux-real-time-preemption]]).

## State, November 2026

Documented in the core API manual of kernel 7.4.0-rc1, with chapters on theory of operation, how real-time kernels differ, porting and configuration; virtualization, networking and firmware appear as sections of the hardware chapter. The theory, differences and hardware chapters were read. The text says the aim is lower latency between a high-priority task becoming runnable and its running, and names no bound in the chapters read ([[nd-linux-real-time-preemption]]).

## Licence and code

Part of the Linux kernel; the sources read do not state the licence.

## Related

[[landlock]], [[wcet-analysis]], [[mixed-criticality]], [[real-time-loops]].

## Open questions

- Whether any worst-case latency has been proven or measured for PREEMPT_RT on a board zOS targets; the chapters read give none.
