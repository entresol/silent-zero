# KataOS

> Google’s seL4 and Rust OS for machine-learning devices, 2022; OpenTitan in its Sparrow plan.

System · LLM reviewed · updated 2026-10-31 · 1 source · https://silentzero.ooo/wiki/systems/kataos.html

An operating system from Google Research for embedded devices that run machine-learning applications, built on seL4 and the CAmkES component framework and written almost entirely in Rust. Its reference platform, Sparrow, was to pair it with an OpenTitan root of trust on RISC-V ([Announcing KataOS and Sparrow](https://silentzero.ooo/wiki/sources/2022-google-announcing-kataos-sparrow.html.md)).

## State, October 2022

An early release on GitHub with Rust frameworks for seL4 system calls, a Rust root server for dynamic memory management and kernel changes that reclaim the root server's memory. Running third-party applications worked internally but was not released. The first target was 64-bit Arm in QEMU ([Announcing KataOS and Sparrow](https://silentzero.ooo/wiki/sources/2022-google-announcing-kataos-sparrow.html.md)). What happened after 2022 is not covered by the wiki's sources.

## What it is, and what it is not

- Static, analysable components through CAmkES, with dynamic loading of applications built outside CAmkES on top (internal, not released in 2022).
- The announcement calls the platform "verifiably secure"; our reading: the proofs it can rest on are seL4's, and the post names none for the Rust root server, the kernel modifications or the components ([Announcing KataOS and Sparrow](https://silentzero.ooo/wiki/sources/2022-google-announcing-kataos-sparrow.html.md)).

## Licence and code

Partly open source on GitHub: the announcement released several components, "most of the KataOS core pieces"; the licence is not named there.

## Related

[seL4](https://silentzero.ooo/wiki/systems/sel4.html.md), [OpenTitan](https://silentzero.ooo/wiki/systems/opentitan.html.md), [Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md) (a later seL4-based system for AI fleets), [The broker](https://silentzero.ooo/wiki/design/broker.html.md), [Memory-safe code](https://silentzero.ooo/wiki/concepts/memory-safe-code.html.md).

## Open questions

- Whether KataOS and Sparrow are still developed. The announcement is the only source here.

## Sources

- [Announcing KataOS and Sparrow](https://silentzero.ooo/wiki/sources/2022-google-announcing-kataos-sparrow.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Memory-safe code](https://silentzero.ooo/wiki/concepts/memory-safe-code.html.md)
- [Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md)
- [OpenTitan](https://silentzero.ooo/wiki/systems/opentitan.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [Rust in Android](https://silentzero.ooo/wiki/sources/2025-vander-rust-android-move.html.md)
