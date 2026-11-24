# SpecOS

> Vision of an OS that verifies AI-written logic before its intents run, above a verified kernel; no implementation reported.

System · LLM reviewed · updated 2026-11-21 · 1 source · https://silentzero.ooo/wiki/systems/specos.html

A design from the Institute of Software, Chinese Academy of Sciences, for an operating system that continuously verifies AI-generated logic: system state as relational tables, logic as pure functional lambdas, intents held back until a two-phase check passes, all above a verified microkernel such as seL4 or HongMeng ([Formal methods as the harness for AIOS (SpecOS)](https://silentzero.ooo/wiki/sources/2026-li-formal-methods-harness.html.md)).

## State, September 2026

A three-page design paper at the AgenticOS workshop with a sketch of a ROS 2 replacement. No implementation, measurement or proof is reported ([Formal methods as the harness for AIOS (SpecOS)](https://silentzero.ooo/wiki/sources/2026-li-formal-methods-harness.html.md)).

## Licence and code

None stated; nothing is released in the paper.

## Related

[seL4](https://silentzero.ooo/wiki/systems/sel4.html.md), [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md), [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md), [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md).

## Open questions

- Whether the two-phase check can be built and what it costs; the paper claims polynomial time with no figures.
- Who writes the invariants that serve as the root of trust, and how they are checked.
- How the split between control loops at 100 Hz and above and planning at 3 to 10 Hz is enforced in a running system.

## Sources

- [Formal methods as the harness for AIOS (SpecOS)](https://silentzero.ooo/wiki/sources/2026-li-formal-methods-harness.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
