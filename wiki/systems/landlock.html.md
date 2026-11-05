# Landlock

> Linux sandbox a process applies to itself: filesystem, network, capability and namespace rules; part of the hardened-Linux route.

System · LLM reviewed · updated 2026-11-03 · 1 source · https://silentzero.ooo/wiki/systems/landlock.html

A Linux security module that lets a process, including an unprivileged one, restrict its own filesystem, network, capability and namespace rights, and those of its future children. Rulesets stack with the system-wide access controls ([Linux kernel documentation: Landlock](https://silentzero.ooo/wiki/sources/nd-linux-landlock-unprivileged-access.html.md)). It is the sandboxing route the paper names for a hardened-Linux agent.

## State, November 2026

First in Linux 5.13; the documentation page, dated October 2026 and built for kernel 7.4.0-rc1, describes interface version 12, with network rules for TCP (version 4) and UDP (version 10) and rules for capabilities and namespaces (version 12). It limits rulesets to 16 layers and cannot restrict some special files ([Linux kernel documentation: Landlock](https://silentzero.ooo/wiki/sources/nd-linux-landlock-unprivileged-access.html.md)).

## Licence and code

Part of the Linux kernel; the sources read do not state the licence.

## Related

[PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md), [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md), [Confused deputy](https://silentzero.ooo/wiki/concepts/confused-deputy.html.md), [Memory-safe code](https://silentzero.ooo/wiki/concepts/memory-safe-code.html.md).

## Open questions

- Whether any assurance beyond testing exists for the module; the documentation read makes no claim.
- How Landlock rules would express an agent's per-task authority, the job of the [The broker](https://silentzero.ooo/wiki/design/broker.html.md) in Silent Zero.

## Sources

- [Linux kernel documentation: Landlock](https://silentzero.ooo/wiki/sources/nd-linux-landlock-unprivileged-access.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Confused deputy](https://silentzero.ooo/wiki/concepts/confused-deputy.html.md)
- [Memory-safe code](https://silentzero.ooo/wiki/concepts/memory-safe-code.html.md)
- [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md)
- [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md)
