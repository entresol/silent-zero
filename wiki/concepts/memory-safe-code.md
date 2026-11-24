---
type: concept
status: reviewed
sources: [2025-vander-rust-android-move, 2026-xu-safel4-rethinking-safe]
short: Writing new code in Rust or another safe language
updated: 2026-11-22
---

# Memory-safe code

Writing new code in a language such as Rust that prevents memory errors, instead of C or C++. Google's Android team focuses on new and actively developed code ([[2025-vander-rust-android-move]]). Our reading: this is the hardening route, and the paper names it as the case where zOS may not be needed.

## State, November 2026

- Google reports for Android that memory-safety flaws fell below 20 per cent of all vulnerabilities in 2025, for the first time. Its Rust code shows about 0.2 such flaws per million lines against about 1,000 for its C and C++ code. The Rust figure rests on one near-miss in about 5 million lines. Medium and large Rust changes were rolled back about four times less often than C++ changes, and Rust changes spent about 25 per cent less time in review ([[2025-vander-rust-android-move]]).
- The same post says memory-safe languages are one part of a defence in depth and that about 4 per cent of the Rust code sits in `unsafe` blocks, which the post says do not switch off most of Rust's safety checks ([[2025-vander-rust-android-move]]).
- Rust in kernels: Android's 6.12 Linux kernel has Rust enabled and a first production Rust driver ([[2025-vander-rust-android-move]]). KataOS put Rust on seL4 in 2022 ([[kataos]]).
- Research kernels go further and replace hardware isolation between domains with the language. safeL4, a Rust microkernel announced for ASPLOS 2027, uses Rust object capabilities for isolation and reports primitives 1.91 times faster than seL4's on average (geometric mean) on a Raspberry Pi 3B+; legacy code still runs in hardware-isolated tasks. It trusts the Rust toolchain, `unsafe` code (15.1 per cent of its kernel) and DMA-capable devices, has no IOMMU isolation yet, and is not described as formally verified ([[2026-xu-safel4-rethinking-safe]]).
- Memory safety is not a proof of the program's behaviour. [[verus]] proves properties of Rust code, and [[proof-automation]] covers models that write such proofs.

## Related

[[landlock]] and [[preempt-rt]] are the other hardening tools the wiki covers, for confinement and for timing.

## Open questions

- What the wiki's sources say about Rust in the mainline Linux kernel: none yet. News of its status is not read from a primary source.
- Whether hardening reaches what zOS adds: authority for agents over data, credentials and tools, and a provable bound on timing. See [[broker]] and [[real-time-loops]].
