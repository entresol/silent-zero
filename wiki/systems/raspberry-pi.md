---
type: system
status: reviewed
sources: [nd-raspberrypi-boot, nd-sel4-verified-configurations, nd-sel4-microkit-user-manual, 2026-bower-cohesix-research-operating]
short: Single-board computers; pib runs on one
updated: 2026-10-31
---

# Raspberry Pi

Single-board computers; pib, the zOS paper's possible first robot, runs on one (paper, Section 7).

## Boot, October 2026

Since the Pi 4, a ROM runs a second-stage bootloader from SPI EEPROM, which loads firmware from SD card, USB, network or NVMe. On the Pi 4 that firmware includes the GPU firmware file `start4.elf`; on the Pi 5 the bootloader embeds it and loads the kernel itself. A `recovery.bin` on the SD card replaces the EEPROM bootloader unless OTP settings forbid it, and self-update applies new images from the boot file system; the files that accompany them carry SHA-256 checksums, not signatures. The EEPROMs can be write-protected in hardware. For non-BCM2712 devices, the Pi 4 among them, OTP holds the hash of a secure-boot public key; for the Pi 5 the public OTP list shows no such rows ([[nd-raspberrypi-boot]]).

## seL4 and Microkit

The Pi 4B and 5B are verified AArch64 platforms for seL4, without MCS ([[nd-sel4-verified-configurations]]). Microkit supports the Pi 4B in four memory sizes, booted through U-Boot ([[nd-sel4-microkit-user-manual]]); since Microkit always uses MCS, a Microkit system on the Pi runs on an unverified kernel configuration today (see [[kernel]]). Cohesix names the Pi 4 as a target for its seL4-based control layer ([[cohesix]]).

## Licence and code

The ROM, EEPROM bootloader and GPU firmware are closed; our reading from [[nd-raspberrypi-boot]], which documents their behaviour but not their source.

## Open questions

- How secure boot is enabled and what it verifies on the Pi 4 and Pi 5; the documentation for it is not yet covered here.
- Whether the Pi's system-on-chip has an IOMMU. The paper says "its public documentation describes no IOMMU" (Section 7); no source in the wiki backs that yet.
- What stays resident below the kernel on the Pi, in EL3 or in the GPU firmware; the sources do not say.
