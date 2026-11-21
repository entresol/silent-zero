---
type: system
status: reviewed
sources: [2026-li-formal-methods-harness]
short: Vision of an OS that verifies AI-written logic
updated: 2026-11-21
---

# SpecOS

A design from the Institute of Software, Chinese Academy of Sciences, for an operating system that continuously verifies AI-generated logic: system state as relational tables, logic as pure functional lambdas, intents held back until a two-phase check passes, all above a verified microkernel such as seL4 or HongMeng ([[2026-li-formal-methods-harness]]).

## State, September 2026

A three-page design paper at the AgenticOS workshop with a sketch of a ROS 2 replacement. No implementation, measurement or proof is reported ([[2026-li-formal-methods-harness]]).

## Licence and code

None stated; nothing is released in the paper.

## Related

[[sel4]], [[safety-path]], [[real-time-loops]], [[agent-operating-systems]].

## Open questions

- Whether the two-phase check can be built and what it costs; the paper claims polynomial time with no figures.
- Who writes the invariants that serve as the root of trust, and how they are checked.
- How the split between control loops at 100 Hz and above and planning at 3 to 10 Hz is enforced in a running system.
