---
type: source
id: nd-sel4-sel4-roadmap
status: reviewed
read: full
kind: report
sources: [nd-sel4-sel4-roadmap]
updated: 2026-11-02
---

# seL4 Foundation: Development roadmap

The roadmap page of the seL4 Foundation, undated, read from a snapshot of 23 October 2026. [Page](https://sel4.systems/roadmap.html). Read in full; the page is short and consists of two lists.

## What it shows

- **Systems side.** Microkit, the seL4 Device Driver Framework (sDDF) and LionsOS, all by UNSW, are in "ongoing research and development". Microkit and sDDF are "available for use"; for LionsOS "an initial release containing a non-trivial example system has been made".
- **Verification side, three projects, all by Proofcraft.**
  - *MCS kernel extensions*: functional-correctness proofs for the scheduling model for mixed-criticality systems. "C verification completed for RISC-V, to complete for AArch64 Q3/27."
  - *Automated platform port verification*: to reduce the need for verification experts for new ports and to widen the supported configurations. "Verification support for all Arm platforms now available", further platform and configuration support ongoing, project to complete Q3/27.
  - *Multikernel verification*: specifications, tools and proofs for the multikernel configuration, giving "gradually increasing assurance" for multi-core systems. Scheduled to complete Q3/28.
- The page says some items could be accelerated by funding or volunteers.

## How

A project page that lists planned work. It gives quarters, not evidence.

## Limits

A careful reader adds:

- The page is undated. The snapshot shows the date it was read, not the date it was written.
- The page does not say which AArch64 platforms the MCS proof will cover, nor whether it includes integrity and confidentiality.
- It says "MCS" and "C verification" together; it gives no separate date for the binary level.

## Against the wiki

- [[2026-sel4-functional-correctness-proof]]: **confirms** the RISC-V result and supplies the date for AArch64 that the announcement lacked.
- [[kernel]]: **confirms** the paper's Section 3 sentence (C-level complete for RISC-V; AArch64 in the third quarter of 2027) as far as MCS goes.
- [[sel4]], [[microkit]], [[lionsos]]: no change. The multicore item is the first dated plan in the wiki for verified multi-core seL4: a multikernel by the third quarter of 2028.

## For zOS

- [[kernel]]: the date for a verified MCS kernel on 64-bit Arm is the third quarter of 2027, a plan and not a result. Our reading: the paper makes the Raspberry Pi a demonstrator partly because that proof is not expected before 2027, so the date bears on how long the demonstrator stays one.
- Our reading: a single RISC-V core needs no multikernel proof. A robot with several cores would.
