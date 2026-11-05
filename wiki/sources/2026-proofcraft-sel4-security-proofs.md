---
type: source
id: 2026-proofcraft-sel4-security-proofs
status: reviewed
read: full
kind: report
sources: [2026-proofcraft-sel4-security-proofs, nd-sel4-microkit-user-manual]
updated: 2026-11-05
---

# seL4 Foundation 2026: security proofs complete on AArch64

A news item on sel4.systems, dated 24 August 2026, titled "seL4 security proofs now complete on AArch64". Read on the [news page for 2026](https://sel4.systems/news/2026.html), saved on 5 November 2026. The item links to a Proofcraft announcement of 21 August 2026 that we could not open from the research environment, so this page rests on the news item alone.

## What it shows

- Proofcraft has established the proof that seL4 enforces confidentiality on AArch64: a formal proof that the kernel prevents an application running on top of it from learning information without authorisation.
- The item says this completes the formal proof that the seL4 implementation code on AArch64 enforces security isolation of the applications above it, "under the assumptions" it links to. Functional correctness and integrity on AArch64 were completed earlier; its links point to Proofcraft announcements of 1 April 2024 and 29 April 2025, which we did not open.
- The item gives the purpose: attacks on non-critical applications should not reach critical ones.

## How

An announcement of one paragraph with links. It gives no theorem statement, proof size or configuration file.

## Limits

A careful reader adds:

- **Configuration not named.** The item does not say whether the proof covers the MCS configuration. The MCS proof of functional correctness is announced for RISC-V only, with the port to 64-bit Arm under way ([[2026-sel4-functional-correctness-proof]]).
- **Storage channels, not timing.** The item does not mention timing channels. The earlier proofs concern storage channels only ([[sel4]]). Timing is the subject of [[time-protection]].
- **Assumptions by link.** What the proof assumes is on a separate page, not in the item. The assumptions page was not read for this entry.
- **Non-interference** is not named in the item.

## Against the wiki

- [[sel4]] and [[kernel]]: **confirm** the statement, taken from [[nd-sel4-verified-configurations]], that confidentiality is proven on AArch64, and add a dated announcement as a second source. Neither page claims it for MCS, and the item does not change that.

## For zOS

[[kernel]]: no change of state. The paper's AArch64 sentence is about the MCS kernel with Microkit and stays right (C-level verification planned for the third quarter of 2027, per [[nd-sel4-sel4-roadmap]]). Our reading: it bears on a zOS built on the non-MCS kernel on AArch64, and the Microkit manual says Microkit always uses MCS ([[nd-sel4-microkit-user-manual]]).
