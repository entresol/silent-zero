---
type: system
status: reviewed
sources: [nd-linux-landlock-unprivileged-access]
short: Linux sandbox that processes apply to themselves
updated: 2026-11-03
---

# Landlock

A Linux security module that lets a process, including an unprivileged one, restrict its own filesystem, network, capability and namespace rights, and those of its future children. Rulesets stack with the system-wide access controls ([[nd-linux-landlock-unprivileged-access]]). It is the sandboxing route the paper names for a hardened-Linux agent.

## State, November 2026

First in Linux 5.13; the documentation page, dated October 2026 and built for kernel 7.4.0-rc1, describes interface version 12, with network rules for TCP (version 4) and UDP (version 10) and rules for capabilities and namespaces (version 12). It limits rulesets to 16 layers and cannot restrict some special files ([[nd-linux-landlock-unprivileged-access]]).

## Licence and code

Part of the Linux kernel; the sources read do not state the licence.

## Related

[[preempt-rt]], [[object-capabilities]], [[confused-deputy]].

## Open questions

- Whether any assurance beyond testing exists for the module; the documentation read makes no claim.
- How Landlock rules would express an agent's per-task authority, the job of the [[broker]] in zOS.
