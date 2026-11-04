---
type: source
id: 2025-vander-rust-android-move
status: reviewed
read: full
kind: measurement
sources: [2025-vander-rust-android-move]
updated: 2026-11-04
---

# Vander Stoep 2025: Rust in Android

Jeff Vander Stoep wrote this for the Google Android Security blog on 13 November 2025: [Rust in Android: move fast and fix things](https://blog.google/security/rust-in-android-move-fast-fix-things/). Read in full from the page as saved on 23 October 2026. The figures are Google's own, from its own code and tracking.

## What it shows

- **Share of memory-safety flaws.** In 2025, memory-safety vulnerabilities fell below 20 per cent of all Android vulnerabilities for the first time. The data covers first-party and third-party code changes to the Android platform in C, C++, Java, Kotlin and Rust. The post came out in mid-November, in the last weeks of the year; the author expects the figure to be close to final because of the 90-day patch window.
- **Density.** Roughly 5 million lines of Rust in the platform and one potential memory-safety flaw found, fixed before release. The author puts the Rust density at 0.2 per million lines, against about 1,000 per million lines for Android's C and C++ code, "a more than 1000x reduction". The author calls the Rust estimate conservative.
- **The one flaw.** A linear buffer overflow in CrabbyAVIF, tracked as CVE-2025-48530. It never reached a public release. The Scudo hardened allocator, which puts guard pages around secondary allocations, made it non-exploitable and turned silent corruption into a crash.
- **Speed.** For medium and large changes, the rollback rate of Rust changes is about four times lower than that of C++ changes. Rust changes spend about 25 per cent less time in code review, and changes of similar size need about 20 per cent fewer revisions. The author guesses that growing Rust expertise on the team explains the large shift between 2023 and 2024; no cause is given for the rest.
- **Unsafe Rust.** About 4 per cent of the Rust code sits in `unsafe` blocks. The author says that assuming an unsafe line is as bug-prone as a C or C++ line overestimates the risk, and offers three possible reasons without testing them. The claim rests on the same single near-miss.
- **Reach.** Android's 6.12 Linux kernel is the first with Rust support enabled and has the first production Rust driver. Rust is also used in firmware (a collaboration on Rusted Firmware-A is named) and in several applications.
- **The approach.** The post focuses on new and actively developed code, and says memory-safe languages are one part of a defence in depth. C and C++ will persist and hardware and software mechanisms stay critical.

## How

Counts and tracking inside Google. Rust and C++ changes are compared on size, on the pool of developers and on the DORA throughput and stability measures. The author lists the controls used and admits cross-language comparisons are hard.

## Limits

What the author says: the density figure is an estimate from a near-miss. The comparison is between similar-sized changes by overlapping developers, and Rust is slightly denser than C++. A careful reader adds:

- **One case.** The Rust density rests on one flaw found among about 5 million lines. A second flaw would double it, and none would bring it to zero. Our reading: the ratio is large either way, but "1000x" is an order of magnitude, not a measured constant.
- **Own data.** Neither the data nor the method of counting can be checked from outside; the post shows charts without tables.
- **New code.** The post focuses on new and actively developed code, because the author says the data show this to be effective. It also reports that Chromium parsers for PNG, JSON and web fonts were replaced with Rust, which is rewriting old code. It does not say old code should be left alone.
- **Not proof.** Nothing here is a proof, and the post does not discuss formal verification.

## Against the wiki

- [[memory-safe-code]]: created with this source.
- [[kataos]]: **extends**. KataOS used Rust on seL4 in 2022; this post reports Rust in production Android, on Linux.
- [[verus]]: unrelated mechanism. Verus proves properties of Rust code; the post only counts flaws.

## For zOS

Section 6 of the paper writes that memory-safety flaws in Android "fell below 20 per cent of all vulnerabilities in 2025 for the first time". Confirmed for that sentence, with two qualifications it leaves out: the figure covers platform code changes and was published before the year ended. The paper's next sentence, that writing new code in a memory-safe language "without rewriting the old, works", is stronger than the post, which says the data "continue to validate" Google's approach for its own platform and reports some rewriting. The paper's reading that this supports hardening as the alternative is its own argument. No `design/` page changes state.
