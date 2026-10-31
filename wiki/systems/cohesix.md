---
type: system
status: reviewed
sources: [2026-bower-cohesix-research-operating]
updated: 2026-10-31
---

# Cohesix

A research operating system for edge AI fleets, built on seL4, with a Queen that holds orchestration authority and narrow Worker roles, and control exposed as a tree of named paths ([[2026-bower-cohesix-research-operating]]).

## State, October 2026

Release 1.2.0 is the latest on its documentation page, with targets in QEMU and on the Raspberry Pi 4. The page gives no measurements; what runs on a target is on pages not yet read here ([[2026-bower-cohesix-research-operating]]).

## What it is, and what it is not

- A control layer. The trusted target stays small; models, agents, training and GPU stacks run on Linux or macOS hosts beside it, and command-line tools, gateway and desktop UI run on the host too.
- Capabilities from seL4 plus generated role, policy, ticket and lifecycle checks decide what is accepted; a model proposes and the target decides.
- Not a desktop or server OS, not POSIX, and not formally verified as a whole; the page says seL4's proofs apply under documented assumptions and do not make Cohesix as a whole formally verified.

## Licence and code

Apache-2.0, as the page's licence section says; it links a GitHub repository and release bundles ([[2026-bower-cohesix-research-operating]]).

## Related

[[broker]] for the same job in zOS, [[sel4]], [[raspberry-pi]].

## Open questions

- Which seL4 configuration it builds on, and whether it uses a verified one. The page names seL4 16.0.0 and its diagram labels donated scheduling contexts; our reading is that this points to an MCS kernel, which the page does not state.
- What the target enforces today, against what is declared in its profiles.
- Whether any part has real-time claims.
