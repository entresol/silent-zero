---
type: system
status: drafted
sources: [2026-bower-cohesix-research-operating]
updated: 2026-10-31
---

# Cohesix

A research operating system for edge AI fleets, built on seL4, with a Queen that holds orchestration authority and narrow Worker roles, and control exposed as a tree of named paths ([[2026-bower-cohesix-research-operating]]).

## State, October 2026

Release 1.2.0 is the latest on its documentation page, with targets in QEMU and on the Raspberry Pi 4. The page gives no measurements; what runs on a target is on pages not yet read here ([[2026-bower-cohesix-research-operating]]).

## What it is, and what it is not

- A control layer. The trusted target stays small; models, agents, training and GPU stacks run on Linux or macOS hosts beside it, and command-line tools, gateway and desktop UI run on the host too.
- Capabilities from seL4 plus generated policy and ticket checks decide what a role may do; a model proposes and the target decides.
- Not a desktop or server OS, not POSIX, and not formally verified as a whole; the page says only seL4's proofs apply, under their assumptions.

## Licence and code

The page links a GitHub repository and release bundles; it does not name a licence ([[2026-bower-cohesix-research-operating]]).

## Related

[[broker]] for the same job in zOS, [[sel4]], [[raspberry-pi]].

## Open questions

- Which seL4 configuration it builds on, and whether it uses a verified one.
- What the target enforces today, against what is declared in its profiles.
- Whether any part has real-time claims.
