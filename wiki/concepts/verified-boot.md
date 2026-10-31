---
type: concept
status: reviewed
sources: [nd-uboot-verified-boot, nd-coreboot-vboot, nd-chromeos-verified-boot, 2018-cook-model-checking-boot, 2020-straznickas-verified-first-stage, 2022-zhang-pa-boot-formally]
short: Each boot stage checks the next's signature
updated: 2026-10-30
---

# Verified boot

Each boot stage checks the next against a signature before running it, starting from code and a public key the attacker cannot change. "If the public key can be changed, then the verification is worthless" ([[nd-uboot-verified-boot]]). Not to be confused with formally verified boot code; see below.

## How it is done

- A read-only first stage holds the root key, usually in write-protected flash; each stage may carry a key for the next, so updates need not touch the root key ([[nd-uboot-verified-boot]], [[nd-chromeos-verified-boot]]).
- coreboot's vboot keeps two signed read-write firmware slots and a read-only recovery firmware, falls back to the other slot when one fails, and enters recovery from external media when neither verifies ([[nd-coreboot-vboot]]).
- Chromium OS designs it against the opportunistic attacker, not against one who opens the device, and keeps the owner able to reset to a known state without remote attestation ([[nd-chromeos-verified-boot]]).

## State of proofs about boot code, October 2026

- Memory safety of stage-1 production boot code at AWS, 783 lines, proved by bounded model checking under stated assumptions that abstract its cryptographic routines ([[2018-cook-model-checking-boot]]).
- A first-stage RISC-V measurement root, which signs rather than checks the image, specified against instruction semantics in Coq; correctness theorem stated, not fully proved ([[2020-straznickas-verified-first-stage]]); see [[measured-boot]].
- A processor-authentication protocol for multiprocessor secure boot, proved in Isabelle/HOL at the model level ([[2022-zhang-pa-boot-formally]]).
- For measured boot, see [[measured-boot]].

## Open questions

- Rollback to an older signed image and writable state that steers verified code are named as weaknesses in the Chromium OS design document ([[nd-chromeos-verified-boot]]); how current implementations handle rollback is not covered by these sources.
- Robustness against a failed update: vboot falls back to a second signed slot, and only then to recovery from external media; the zOS paper's loader has one image and stops. See [[bootloader]].
