# Verified boot

> Each stage checks the next against a key the attacker cannot change; proofs about boot code so far.

Concept · LLM reviewed · updated 2026-10-30 · 6 sources · https://silentzero.ooo/wiki/concepts/verified-boot.html

Each boot stage checks the next against a signature before running it, starting from code and a public key the attacker cannot change. "If the public key can be changed, then the verification is worthless" ([U-Boot: verified boot](https://silentzero.ooo/wiki/sources/nd-uboot-verified-boot.html.md)). Not to be confused with formally verified boot code; see below.

## How it is done

- A read-only first stage holds the root key, usually in write-protected flash; each stage may carry a key for the next, so updates need not touch the root key ([U-Boot: verified boot](https://silentzero.ooo/wiki/sources/nd-uboot-verified-boot.html.md), [Chromium OS: Verified Boot (design document)](https://silentzero.ooo/wiki/sources/nd-chromeos-verified-boot.html.md)).
- coreboot's vboot keeps two signed read-write firmware slots and a read-only recovery firmware, falls back to the other slot when one fails, and enters recovery from external media when neither verifies ([coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md)).
- Chromium OS designs it against the opportunistic attacker, not against one who opens the device, and keeps the owner able to reset to a known state without remote attestation ([Chromium OS: Verified Boot (design document)](https://silentzero.ooo/wiki/sources/nd-chromeos-verified-boot.html.md)).

## State of proofs about boot code, October 2026

- Memory safety of stage-1 production boot code at AWS, 783 lines, proved by bounded model checking under stated assumptions that abstract its cryptographic routines ([Model Checking Boot Code from AWS Data Centers](https://silentzero.ooo/wiki/sources/2018-cook-model-checking-boot.html.md)).
- A first-stage RISC-V measurement root, which signs rather than checks the image, specified against instruction semantics in Coq; correctness theorem stated, not fully proved ([Towards a Verified First-Stage Bootloader in Coq](https://silentzero.ooo/wiki/sources/2020-straznickas-verified-first-stage.html.md)); see [Measured boot](https://silentzero.ooo/wiki/concepts/measured-boot.html.md).
- A processor-authentication protocol for multiprocessor secure boot, proved in Isabelle/HOL at the model level ([PA-Boot, a Formally Verified Authentication Protocol for Multiprocessor Secure Boot under Hardware Supply-chain Attacks](https://silentzero.ooo/wiki/sources/2022-zhang-pa-boot-formally.html.md)).
- For measured boot, see [Measured boot](https://silentzero.ooo/wiki/concepts/measured-boot.html.md).

## Open questions

- Rollback to an older signed image and writable state that steers verified code are named as weaknesses in the Chromium OS design document ([Chromium OS: Verified Boot (design document)](https://silentzero.ooo/wiki/sources/nd-chromeos-verified-boot.html.md)); how current implementations handle rollback is not covered by these sources.
- Robustness against a failed update: vboot falls back to a second signed slot, and only then to recovery from external media; the Silent Zero paper's loader has one image and stops. See [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md).

## Sources

- [Chromium OS: Verified Boot (design document)](https://silentzero.ooo/wiki/sources/nd-chromeos-verified-boot.html.md)
- [coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md)
- [Model Checking Boot Code from AWS Data Centers](https://silentzero.ooo/wiki/sources/2018-cook-model-checking-boot.html.md)
- [PA-Boot, a Formally Verified Authentication Protocol for Multiprocessor Secure Boot under Hardware Supply-chain Attacks](https://silentzero.ooo/wiki/sources/2022-zhang-pa-boot-formally.html.md)
- [Towards a Verified First-Stage Bootloader in Coq](https://silentzero.ooo/wiki/sources/2020-straznickas-verified-first-stage.html.md)
- [U-Boot: verified boot](https://silentzero.ooo/wiki/sources/nd-uboot-verified-boot.html.md)

## Related pages

- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)
- [Measured boot](https://silentzero.ooo/wiki/concepts/measured-boot.html.md)
