---
type: source
id: 2026-trustworthy-where-are-we
status: reviewed
read: partial
kind: progress
sources: [2026-trustworthy-where-are-we]
updated: 2026-10-29
---

# Sison 2026: Where are we with Time Protection?

Rob Sison (UNSW Sydney). Talk at the seL4 Summit 2026, Vancouver, 2 September 2026. [Programme entry](https://sel4summit2026.sched.com/event/2Prqx) with abstract and slides. The wiki has read the abstract and the slides; there is no paper.

## What it shows

- **Time protection** adds to memory protection: partition off-core caches, flush on-core and other non-architected state, and pad time on a domain switch. For seL4 it was implemented and evaluated empirically on Arm and x86, and ported to RISC-V with hardware support (slides, citing Ge et al. 2019, Buckley, Sison et al. 2023, and Wistoff et al. 2023).
- **The verification plan of 2024** had three steps for a total-isolation policy: prove time protection for the abstract model (A), carry it through refinement (B) and prove it for the C implementation (C). Two further steps cover one-way communication.
- **The first approach broke too much.** Tracking the set of touched addresses through the refinement layers caused, on the slides' count, more than 685 breakages in existing proofs after the ones already fixed.
- **A new approach** replaces it with an invariant that object references never point outside a static set of touched addresses, checked at C level. The abstract says this rethink "has eliminated the main cause" of the earlier breakages. The abstract model is otherwise integrated into the group's earlier time-protection proofs (Buckley, Sison et al. 2023); the proof of the new invariant across it is "in progress". Both this step and the C-level checks are student thesis work.
- **One-way communication.** For a data diode through shared memory, mere reads by the receiving domain evict lines from the L2 and leak backwards. A 2025 thesis evaluated the options: copying between non-shared memory works but costs about 19 to 34 per cent per page; dedicated cache colours waste space, with only 16 colours on typical Arm boards; a targeted flush by prefetching still leaks if the buffer exceeds the lines per cache set, because of random eviction, and cannot be verified without knowing the eviction policy. The group now uses a dynamically partitionable last-level cache on the RISC-V platform Cheshire, which supports targeted flushes, and is adding the needed time padding.

## How

A status talk: a plan, its revision, and progress on proof and implementation. The figures on breakages and overheads come from the slides without a method.

## Limits

The talk presents work in progress; no proof of time protection at C level is complete.

A careful reader adds:

- **Slides only.** Statements are short and some figures (the breakage counts) are hard to read in the extracted text.
- **No dates for completion** are given.

## Against the wiki

- [[2022-wistoff-systematic-prevention-core]]: **extends** it. Hardware support on RISC-V is now part of seL4's time-protection work, and the problem has moved to verification and to one-way channels.
- [[2018-klein-formally-verified-software]]: consistent with it; seL4's confidentiality proof excludes timing channels (§3.2), which is the gap time protection addresses.
- [[time-protection]]: created with [[2022-wistoff-systematic-prevention-core]] and this source.

## For zOS

- [[kernel]]: time protection on seL4 is implemented in research versions and *not proven*. The paper does not claim otherwise.
- Our reading: one-way channels matter for zOS. Sensor data flows from the control side to the agent, and the agent should not learn more than it is sent. The talk shows that a one-way channel through shared memory is not one-way in timing unless the cache is partitioned and flushed with care.
