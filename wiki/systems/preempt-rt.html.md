# PREEMPT_RT

> The Linux real-time configuration: preemptible kernel, threaded interrupts; no latency bound stated.

System · LLM reviewed · updated 2026-11-03 · 1 source · https://silentzero.ooo/wiki/systems/preempt-rt.html

The configuration of the Linux kernel that makes it real-time in the kernel developers' sense: sleeping locks with priority inheritance and forced-threaded interrupts leave only a few critical paths non-preemptible ([Linux kernel documentation: real-time preemption](https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html.md)).

## State, November 2026

Documented in the core API manual of kernel 7.4.0-rc1, with chapters on theory of operation, how real-time kernels differ, porting and configuration; virtualization, networking and firmware appear as sections of the hardware chapter. The theory, differences and hardware chapters were read. The text says the aim is lower latency between a high-priority task becoming runnable and its running, and names no bound in the chapters read ([Linux kernel documentation: real-time preemption](https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html.md)).

## Licence and code

Part of the Linux kernel; the sources read do not state the licence.

## Related

[Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md), [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md), [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md), [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md).

## Open questions

- Whether any worst-case latency has been proven or measured for PREEMPT_RT on a board Silent Zero targets; the chapters read give none.

## Sources

- [Linux kernel documentation: real-time preemption](https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [Memory-safe code](https://silentzero.ooo/wiki/concepts/memory-safe-code.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md)
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md)
