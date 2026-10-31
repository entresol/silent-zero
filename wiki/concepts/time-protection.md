---
type: concept
status: reviewed
sources: [2022-wistoff-systematic-prevention-core, 2026-trustworthy-where-are-we, 2018-klein-formally-verified-software]
short: Closing timing channels between domains
updated: 2026-10-29
---

# Time protection

Memory protection stops one program from reading another's memory, but programs that share hardware still change its microarchitectural state, such as caches, predictors and TLBs, and the other can measure the effect in time. Time protection closes these timing channels: partition what can be partitioned in space, flush the rest on every switch between security domains, and pad the switch to a fixed duration ([[2026-trustworthy-where-are-we]], [[2022-wistoff-systematic-prevention-core]], §2.3, §3, §4.3).

## What it needs from hardware

Off-core caches can be partitioned by the OS through cache colouring. On-core state cannot be partitioned efficiently and must be reset, which needs an instruction the mainstream ISAs lack. On [[cva6]], a custom `fence.t` that resets all non-architectural state closed every measured on-core channel at under 1 per cent cost ([[2022-wistoff-systematic-prevention-core]]). The flush must itself be padded, or its duration leaks.

## State for seL4, October 2026

- Implemented in research versions of [[sel4]] on Arm, x86 and RISC-V, the last with hardware support ([[2026-trustworthy-where-are-we]]).
- Not proven. seL4's confidentiality proof covers storage channels and leaves timing channels outside its scope ([[2018-klein-formally-verified-software]], §3.2). A proof for the abstract model is in progress under a revised approach; C level is not done ([[2026-trustworthy-where-are-we]]).
- One-way channels through shared memory leak backwards through the cache unless it is partitioned and flushed with care; the group is building this on a RISC-V platform with a partitionable last-level cache ([[2026-trustworthy-where-are-we]]).

## Open questions

- Cross-core channels on multicore systems are outside [[2022-wistoff-systematic-prevention-core]].
- Whether zOS needs time protection between agent and control loop for confidentiality only, or also for predictable timing. See [[kernel]].
