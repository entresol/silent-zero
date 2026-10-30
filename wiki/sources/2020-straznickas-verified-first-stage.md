---
type: source
id: 2020-straznickas-verified-first-stage
status: reviewed
read: full
kind: progress
sources: [2020-straznickas-verified-first-stage]
updated: 2026-10-30
---

# Straznickas 2020: Towards a Verified First-Stage Bootloader in Coq

Zygimantas Straznickas. Master of Engineering thesis, MIT, May 2020, supervised by Adam Chlipala. [PDF](https://adam.chlipala.net/theses/zygi.pdf).

## What it shows

- **A measurement root.** The thesis builds a first-stage bootloader for RISC-V after the Sanctum project's measurement root. It copies the boot image from untrusted storage into memory, hashes it and *signs* it with a device-specific key for attestation, and leaves the machine otherwise in a clean state (abstract, Chapter 1, §3.1). It does not check a signature on the image; it records what was loaded.
- **The property.** Functional correctness: under stated assumptions, the bootloader terminates from any state and leaves the signed image in memory with all other memory and state zeroed. Cryptographic security is out of scope (Chapter 1).
- **The method.** Written in Coq with the Bedrock2 framework and specified against the riscv-coq semantics of RISC-V instructions, including a model of a DMA-style loading mechanism. The cryptography (SHA-3, Ed25519) is written in C, and only the call bridge into it is verified, assuming the C compiler follows the calling convention (Chapter 1, Chapter 3).
- **The result.** The correctness theorem is stated. The abstract says "a few major lemmas" are proved; Chapter 1 and §4.2.3 say "most" of the necessary lemmas. The author has "not succeeded in unconditionally proving the full correctness theorem" (§4.2.3).

## How

A case study in verifying a low-level program down to instruction semantics, against a model of the hardware.

## Limits

The author states:

- The full correctness theorem is not proved; the remaining parts are believed to be mechanical (§4.2.3).
- Some proofs end with `Admitted` because Coq's final check took hours without finishing; a guard makes them fail if goals remain, which "provides enough confidence" in the author's view, though "we lose some correctness guarantees" (§4.1.2).
- The biggest weakness is the C cryptography and therefore trust in GCC (§4.2.1).
- Running time is not fully accounted for: each call into C counts as one step (§4.2.2).
- The design follows Sanctum's "while making a few simplifications and assumptions about the hardware" (§2.7.1).

A careful reader adds: no run on real hardware is reported.

## Against the wiki

- [[measured-boot]]: a measurement root that signs what it loads, with a partial proof against instruction semantics.

## For zOS

- [[bootloader]]: our reading: this is prior work on proving a first-stage loader on RISC-V against instruction semantics, though for a measurement root, not for a loader that checks signatures. It shows where such a proof gets hard: cryptography, compiler trust and the size of proof terms.
