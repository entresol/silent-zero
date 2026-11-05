# Memory-safe code

> New code in Rust instead of C: Android’s memory-safety flaws below 20 % in 2025; the hardening rival to a verified base.

Concept · LLM reviewed · updated 2026-11-04 · 1 source · https://silentzero.ooo/wiki/concepts/memory-safe-code.html

Writing new code in a language such as Rust that prevents memory errors, instead of C or C++. Google's Android team focuses on new and actively developed code ([Rust in Android](https://silentzero.ooo/wiki/sources/2025-vander-rust-android-move.html.md)). Our reading: this is the hardening route, and the paper names it as the case where Silent Zero may not be needed.

## State, November 2026

- Google reports for Android that memory-safety flaws fell below 20 per cent of all vulnerabilities in 2025, for the first time. Its Rust code shows about 0.2 such flaws per million lines against about 1,000 for its C and C++ code. The Rust figure rests on one near-miss in about 5 million lines. Medium and large Rust changes were rolled back about four times less often than C++ changes, and Rust changes spent about 25 per cent less time in review ([Rust in Android](https://silentzero.ooo/wiki/sources/2025-vander-rust-android-move.html.md)).
- The same post says memory-safe languages are one part of a defence in depth and that about 4 per cent of the Rust code sits in `unsafe` blocks, which the post says do not switch off most of Rust's safety checks ([Rust in Android](https://silentzero.ooo/wiki/sources/2025-vander-rust-android-move.html.md)).
- Rust in kernels: Android's 6.12 Linux kernel has Rust enabled and a first production Rust driver ([Rust in Android](https://silentzero.ooo/wiki/sources/2025-vander-rust-android-move.html.md)). KataOS put Rust on seL4 in 2022 ([KataOS](https://silentzero.ooo/wiki/systems/kataos.html.md)).
- Memory safety is not a proof of the program's behaviour. [Verus](https://silentzero.ooo/wiki/systems/verus.html.md) proves properties of Rust code, and [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md) covers models that write such proofs.

## Related

[Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md) and [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md) are the other hardening tools the wiki covers, for confinement and for timing.

## Open questions

- What the wiki's sources say about Rust in the mainline Linux kernel: none yet. News of its status is not read from a primary source.
- Whether hardening reaches what Silent Zero adds: authority for agents over data, credentials and tools, and a provable bound on timing. See [The broker](https://silentzero.ooo/wiki/design/broker.html.md) and [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md).

## Sources

- [Rust in Android](https://silentzero.ooo/wiki/sources/2025-vander-rust-android-move.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [KataOS](https://silentzero.ooo/wiki/systems/kataos.html.md)
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md)
- [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md)
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md)
