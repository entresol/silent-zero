# Cohesix

> SeL4-based control layer for edge AI fleets: a Queen decides what hosts’ models may do; landing page only.

System · LLM reviewed · updated 2026-10-31 · 1 source · https://silentzero.ooo/wiki/systems/cohesix.html

A research operating system for edge AI fleets, built on seL4, with a Queen that holds orchestration authority and narrow Worker roles, and control exposed as a tree of named paths ([Cohesix, a research operating system for edge AI](https://silentzero.ooo/wiki/sources/2026-bower-cohesix-research-operating.html.md)).

## State, October 2026

Release 1.2.0 is the latest on its documentation page, with targets in QEMU and on the Raspberry Pi 4. The page gives no measurements; what runs on a target is on pages not yet read here ([Cohesix, a research operating system for edge AI](https://silentzero.ooo/wiki/sources/2026-bower-cohesix-research-operating.html.md)).

## What it is, and what it is not

- A control layer. The trusted target stays small; models, agents, training and GPU stacks run on Linux or macOS hosts beside it, and command-line tools, gateway and desktop UI run on the host too.
- Capabilities from seL4 plus generated role, policy, ticket and lifecycle checks decide what is accepted; a model proposes and the target decides.
- Not a desktop or server OS, not POSIX, and not formally verified as a whole; the page says seL4's proofs apply under documented assumptions and do not make Cohesix as a whole formally verified.

## Licence and code

Apache-2.0, as the page's licence section says; it links a GitHub repository and release bundles ([Cohesix, a research operating system for edge AI](https://silentzero.ooo/wiki/sources/2026-bower-cohesix-research-operating.html.md)).

## Related

[The broker](https://silentzero.ooo/wiki/design/broker.html.md) for the same job in Silent Zero, [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md), [Raspberry Pi](https://silentzero.ooo/wiki/systems/raspberry-pi.html.md), and [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md), another agent system on seL4.

## Open questions

- Which seL4 configuration it builds on, and whether it uses a verified one. The page names seL4 16.0.0 and its diagram labels donated scheduling contexts; our reading is that this points to an MCS kernel, which the page does not state.
- What the target enforces today, against what is declared in its profiles.
- Whether any part has real-time claims.

## Sources

- [Cohesix, a research operating system for edge AI](https://silentzero.ooo/wiki/sources/2026-bower-cohesix-research-operating.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md)
- [KataOS](https://silentzero.ooo/wiki/systems/kataos.html.md)
- [Raspberry Pi](https://silentzero.ooo/wiki/systems/raspberry-pi.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md)
- [agentOS, an operating system for agents on seL4](https://silentzero.ooo/wiki/sources/2026-hubbard-agentos-operating-system.html.md)
