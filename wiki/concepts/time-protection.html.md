# Time protection

> Closing timing channels between domains; prototypes on CVA6, proof for seL4 in progress.

Concept · LLM reviewed · updated 2026-10-29 · 3 sources · https://silentzero.ooo/wiki/concepts/time-protection.html

Memory protection stops one program from reading another's memory, but programs that share hardware still change its microarchitectural state, such as caches, predictors and TLBs, and the other can measure the effect in time. Time protection closes these timing channels: partition what can be partitioned in space, flush the rest on every switch between security domains, and pad the switch to a fixed duration ([Where are we with Time Protection?](https://silentzero.ooo/wiki/sources/2026-trustworthy-where-are-we.html.md), [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md), §2.3, §3, §4.3).

## What it needs from hardware

Off-core caches can be partitioned by the OS through cache colouring. On-core state cannot be partitioned efficiently and must be reset, which needs an instruction the mainstream ISAs lack. On [CVA6](https://silentzero.ooo/wiki/systems/cva6.html.md), a custom `fence.t` that resets all non-architectural state closed every measured on-core channel at under 1 per cent cost ([Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md)). The flush must itself be padded, or its duration leaks.

## State for seL4, October 2026

- Implemented in research versions of [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md) on Arm, x86 and RISC-V, the last with hardware support ([Where are we with Time Protection?](https://silentzero.ooo/wiki/sources/2026-trustworthy-where-are-we.html.md)).
- Not proven. seL4's confidentiality proof covers storage channels and leaves timing channels outside its scope ([Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md), §3.2). A proof for the abstract model is in progress under a revised approach; C level is not done ([Where are we with Time Protection?](https://silentzero.ooo/wiki/sources/2026-trustworthy-where-are-we.html.md)).
- One-way channels through shared memory leak backwards through the cache unless it is partitioned and flushed with care; the group is building this on a RISC-V platform with a partitionable last-level cache ([Where are we with Time Protection?](https://silentzero.ooo/wiki/sources/2026-trustworthy-where-are-we.html.md)).

## Open questions

- Cross-core channels on multicore systems are outside [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md).
- Whether Silent Zero needs time protection between agent and control loop for confidentiality only, or also for predictable timing. See [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md).

## Sources

- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)
- [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md)
- [Where are we with Time Protection?](https://silentzero.ooo/wiki/sources/2026-trustworthy-where-are-we.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md)
- [CVA6](https://silentzero.ooo/wiki/systems/cva6.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [CHERIoT, complete memory safety for embedded devices](https://silentzero.ooo/wiki/sources/2023-amar-cheriot-complete-memory.html.md)
- [Linux kernel documentation: real-time preemption](https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html.md)
- [security proofs complete on AArch64](https://silentzero.ooo/wiki/sources/2026-proofcraft-sel4-security-proofs.html.md)
