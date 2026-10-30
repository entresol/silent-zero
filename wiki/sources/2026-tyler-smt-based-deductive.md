---
type: source
id: 2026-tyler-smt-based-deductive
status: reviewed
read: full
kind: proof
sources: [2026-tyler-smt-based-deductive]
updated: 2026-10-29
---

# Tyler et al. 2026: SMT-based Deductive Verification of Device Drivers

Samuel Tyler, Alessandro Legnani, Junming Zhao, Zhewen Shen, Rihui Wu, Miki Tanaka and Gernot Heiser (UNSW Sydney, ETH Zürich). Workshop paper, PLOS 2026, Prague, September/October 2026. [PDF](https://trustworthy.systems/publications/papers/Tyler_LZSWTH_26.pdf).

## What it shows

- **A real driver, verified.** The authors verify a 1 Gb/s Ethernet driver for LionsOS, written in the language Pancake, and the library implementing its queues (§1, §4). They call it, to their knowledge, "the most comprehensive verification of a non-toy device driver to date" (§3.3).
- **Four properties are proved** (§3.3):
  - the driver follows the device protocol, as formalised from the hardware manual;
  - queue integrity: it touches only the head of queues it consumes and the tail of queues it produces, never overflows or underflows them, and honours their ownership contracts;
  - correct buffer movement: every buffer taken from the OS goes to the device and back, and the driver never dereferences buffer pointers;
  - a completion condition: if work is waiting and the device's queue is empty, the driver hands the device a buffer; the authors note this condition "will eventually be true under correct operation of the device".
- **Multicore-safe.** The proofs do not assume the driver runs on the same core as the rest of the OS (§4).
- **Bugs found.** One violation of a queue contract and two weak-memory bugs, all subtle (§4).
- **Cost.** 11.5 person-weeks and 1,501 lines of annotations (Table 2), by an undergraduate without prior experience in automated verification (§4.1). Most functions verify in seconds to minutes; the four most involved take one to three hours (§4.1).
- **Performance.** On an i.MX8MQ (four Cortex-A53 cores at 1 GHz), the verified Pancake driver uses 10 to 20 per cent more driver CPU than the C original, the unverified Pancake version 0 to 10 per cent. All three handle the load; the authors expect work on the Pancake compiler to remove most of the overhead (§4.2).
- **Reuse expected.** All Ethernet drivers in LionsOS share the same OS interface, so the authors expect much of the interface model to be reusable, and similar device classes to benefit (§4.1).

## How

Pancake, a C-like language with a verified compiler, is translated by a new transpiler into the Viper intermediate language and checked by Viper's SMT-backed verifier. The device interface and the OS interface are written as Viper contracts on shared-memory loads and stores. Concurrency is handled by modelling the driver's view of shared state as possibly outdated, and weak memory by applying state updates at memory barriers (§2, §3.2).

## Limits

The authors state (§3.3.1, §7):

- The device protocol is translated by hand from the hardware manual's prose, which is error-prone; their concurrent work aims at device specifications extracted from the device's Verilog.
- The transpiler is written in Rust and is part of the trusted computing base; a rewrite in HOL4 is under way.
- The weak-memory model is encoded by hand in annotations and model files. The authors use "our own encoding for weak memory that we aim to prove to correspond to the underlying hardware concurrency model" (§3.2.2); the multicore result rests on it.
- The soundness of the Viper backend is not established; the authors are "exploring choices for stronger backend correctness guarantees" (§7).
- The proofs are against contracts for the device and the OS side. That the rest of the OS keeps its side of the contract is expected for other LionsOS modules, not shown (§1).
- Annotations are duplicated across similar paths; mixed integer and bitwise reasoning is handled poorly.

A careful reader adds:

- **Automated proof is evidence of a different kind.** Besides the transpiler and the backend, the result rests on SMT solvers. Our reading: that is a different strength of evidence from seL4's Isabelle proofs; the paper's Section 5 says the driver was "verified with automated proofs", which keeps the distinction.
- **A single driver so far.** Reuse for other drivers is what the authors expect; it has yet to be shown.

## Against the wiki

- [[2026-heiser-mcs-safety-os]]: **confirms** "demonstrated on NIC driver" and gives the detail.
- [[2022-parker-sel4-device-driver]]: **extends** it. The queues of 2022 are now formally specified and their implementation is verified.
- [[lionsos]]: verification of drivers has its first complete result.

## For zOS

- [[drivers]]: the paper's "a first driver, for Ethernet, has been verified with automated proofs" (Section 5) and "a verified real-world Ethernet driver" (In brief) are confirmed. In the paper's terms the driver is *proven* for these four properties, under the trusted transpiler, backend and weak-memory encoding, against a device model taken from the manual, and assuming the OS keeps its queue contracts.
- Our reading: for zOS the same method would have to cover the drivers on the motion path, for example a serial or CAN bus to motor controllers. None exists yet.
