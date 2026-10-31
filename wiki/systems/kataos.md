---
type: system
status: reviewed
sources: [2022-google-announcing-kataos-sparrow]
short: Google's seL4 and Rust OS for ML devices, 2022
updated: 2026-10-31
---

# KataOS

An operating system from Google Research for embedded devices that run machine-learning applications, built on seL4 and the CAmkES component framework and written almost entirely in Rust. Its reference platform, Sparrow, was to pair it with an OpenTitan root of trust on RISC-V ([[2022-google-announcing-kataos-sparrow]]).

## State, October 2022

An early release on GitHub with Rust frameworks for seL4 system calls, a Rust root server for dynamic memory management and kernel changes that reclaim the root server's memory. Running third-party applications worked internally but was not released. The first target was 64-bit Arm in QEMU ([[2022-google-announcing-kataos-sparrow]]). What happened after 2022 is not covered by the wiki's sources.

## What it is, and what it is not

- Static, analysable components through CAmkES, with dynamic loading of applications built outside CAmkES on top (internal, not released in 2022).
- The announcement calls the platform "verifiably secure"; our reading: the proofs it can rest on are seL4's, and the post names none for the Rust root server, the kernel modifications or the components ([[2022-google-announcing-kataos-sparrow]]).

## Licence and code

Partly open source on GitHub: the announcement released several components, "most of the KataOS core pieces"; the licence is not named there.

## Related

[[sel4]], [[opentitan]], [[cohesix]] (a later seL4-based system for AI fleets), [[broker]].

## Open questions

- Whether KataOS and Sparrow are still developed. The announcement is the only source here.
