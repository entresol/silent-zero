# coreboot: verified boot (vboot)

> Verified boot rooted in write-protected flash, A/B slots, automatic recovery. report, full text.

Source · LLM reviewed · updated 2026-10-30 · https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html

A page of the coreboot documentation (version 26.09) on Google's verified boot, undated, read on 30 October 2026. [Page](https://doc.coreboot.org/security/vboot/index.html).

## What it shows

- **What vboot does.** It verifies the firmware, records measurements in the TPM and provides an update mechanism. A TPM is required, and so is non-volatile storage in CMOS, the embedded controller or the flash.
- **The root of trust** "is basically the read-only portion of the SPI flash". The page lists what must hold for that: the compiler adds no code, the CPU executes reset and instructions as documented, the flash returns only what was programmed, and the flash honours its write-protect pin. On x86 the protected area is typically a quarter of the flash.
- **Layout.** A read-only section holds recovery firmware and the Google Binary Blob (GBB) with a 4096- or 8192-bit root RSA key. Two read-write sections, A and B, each hold a firmware signing key, a signature and a subset of the firmware (romstage to payload), with processor-specific files (`fspm.bin`, `fsps.bin`; Intel's FSP, our reading).
- **Boot flow.** The reset vector and the only bootblock lie in the read-only area. Verstage verifies section A with the root key, then the firmware with the signing key from A; if that fails and B is not valid, the system falls back to recovery.
- **Updates.** The operating system writes a read-write section that is not in the state "successfully booted"; vboot tries it on the next boot and falls back if it fails. Only the operating system marks a section as successfully booted. "As long as the SPI write protection is in place then the system is always recoverable."
- **Chromebooks.** Developer mode lets the user boot another operating system and erases local data on entry. A write-protect screw grounds the flash's write-protect pin; removing it allows any firmware and voids the warranty.

## How

Developer documentation, with an example signing script for the Intel Galileo board.

## Limits

The page itself lists the assumptions behind the root of trust: the compiler, the CPU and the flash chip behave as documented.

A careful reader adds: the read-write sections contain processor-specific binaries (`fspm.bin`, `fsps.bin`), in our reading Intel's memory and silicon initialisation. Verified boot checks that these are the signed binaries; it says nothing about what they do.

## Against the wiki

- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md), [Verified boot](https://silentzero.ooo/wiki/concepts/verified-boot.html.md): created with this source.

## For Silent Zero

- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md): vboot falls back automatically between two signed read-write slots, and to a read-only recovery firmware that reinstalls from external media such as a USB stick, possibly with the user's help. The paper's loader "starts it, or stops" (Section 3) and has no second image. Our reading: the difference is robustness against a failed update; once nothing verifies, both end with a person.
- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md): vboot shows the usual answer to where the public key lives: in hardware-write-protected flash, protected by a pin someone with the case open can bypass.

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)
- [Verified boot](https://silentzero.ooo/wiki/concepts/verified-boot.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
- [Chromium OS: Verified Boot (design document)](https://silentzero.ooo/wiki/sources/nd-chromeos-verified-boot.html.md)
- [coreboot: architecture and boot stages](https://silentzero.ooo/wiki/sources/nd-coreboot-architecture.html.md)
