---
type: source
id: 2022-parker-sel4-device-driver
status: reviewed
read: partial
kind: measurement
sources: [2022-parker-sel4-device-driver]
updated: 2026-10-29
---

# Parker 2022: The seL4 Device Driver Framework

Lucy Parker (UNSW Sydney, Trustworthy Systems). Talk at the 4th seL4 Summit, Munich, October 2022 (venue from the zOS paper's reference list, month from the slides). [Abstract and slides](https://trustworthy.systems/publications/papers/Parker_22:sel4s.abstract). There is no paper; the wiki has read the slides, and the charts in them carry no readable numbers.

## What it shows

- **The framework.** The seL4 Device Driver Framework (sDDF) provides interfaces and a protocol for writing fast device drivers as seL4 user-level programs. In 2022 it supported a networking-focused system and ran on both CAmkES and the seL4 Core Platform (in our reading the predecessor of Microkit; no source in the wiki says so yet).
- **Why user level.** The slides cite drivers as having seven times the bug density of other OS code, and argue for fewer privileges and better fault containment.
- **Design.** Three memory regions: control, metadata and data; the driver does not need access to the data. Transport between components uses lock-free, bounded, single-producer, single-consumer queues, two per direction, zero copy. The driver is purely reactive, single-threaded and simple.
- **Trust.** In the scaled architecture, "only MUX and driver are trusted"; components can run on separate cores.
- **Rate limiting.** The driver runs at the highest priority to minimise round-trip time, so CPU time has to be limited through the budgets and periods of higher-priority scheduling contexts, or through queue size.
- **Performance, as stated on the slides.** The new transport on CAmkES gave a 50 per cent improvement over the old one; the Core Platform a further 70 per cent, 150 per cent over old CAmkES. Against Linux, the slides claim smaller latencies and higher throughput, and set 3,000 lines of code against under 500 (the slide does not say which code is counted). A module crossing costs "only 10%" more.

## How

A benchmark in which IPbench sends UDP packets from four machines to a client that echoes them, measuring throughput, latency and CPU utilisation on single-core systems. The slides do not name the board or the Linux version.

## Limits

The slides list further work: a passive driver model, more complex clients, budgets for asymmetric traffic, a multiplexer, other device classes, multicore.

A careful reader adds:

- **A talk, not a paper.** The performance claims cannot be checked from the slides; the setup lacks hardware details and the charts lack values.
- **2022.** The framework has developed since; [[2026-tyler-smt-based-deductive]] describes the sDDF of 2026: the same two queues per direction, now formally specified, with cache management in a module separate from the driver.

## Against the wiki

- [[2026-heiser-mcs-safety-os]]: **confirms** the queue design and the line counts in the same range (400 lines for the network driver in 2026).
- [[mixed-criticality]]: **extends** it with a practical case. A driver at the highest priority needs budgets to stop it from starving others.

## For zOS

- [[drivers]]: the paper cites this source for "drivers run in user mode, each with access only to its own device registers" (Section 3). The slides support user-mode drivers and the reduced privileges. They do not say in these words that each driver sees only its own registers. Our reading: Microkit lets the system description give each driver only its own registers, but does not enforce that, except for interrupts ([[nd-sel4-microkit-user-manual]]).
