---
type: source
id: nd-raspberrypi-boot
status: reviewed
read: partial
kind: report
sources: [nd-raspberrypi-boot]
updated: 2026-10-30
---

# Raspberry Pi documentation: boot

The boot chapters of the Raspberry Pi documentation, read on 30 October 2026 from the documentation's source repository, because the web page could not be fetched automatically. [Page](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html); source files: the EEPROM boot flow, the bootloader configuration, the boot EEPROM, the legacy boot sequence and the OTP register list. The secure-boot documentation in the separate `usbboot` repository is not covered.

## What it shows

- **Two stages before any user code.** Since the Raspberry Pi 4, a ROM (first stage) reads OTP settings and then runs the second-stage bootloader from SPI EEPROM, or a `recovery.bin` from the SD card that reflashes the EEPROM (EEPROM boot flow).
- **The second stage** initialises clocks and SDRAM, reads its EEPROM configuration and tries boot modes in the configured order: SD card, network, USB mass storage, NVMe and others. It loads "firmware" from the chosen medium.
- **Raspberry Pi 5 differs.** "Instead of loading `start.elf`, the firmware loads the Linux kernel. Effectively, the bootloader has an embedded version of `start.elf`." On the Pi 4 the GPU firmware file `start4.elf` is loaded from the boot partition.
- **Bootloader updates.** If a valid `recovery.bin` is on the SD card, the ROM runs it instead of the EEPROM contents, and it reflashes the EEPROM. With self-update enabled, the bootloader applies update files found in the boot file system. The accompanying `.sig` file holds "the hexadecimal sha256 checksum" of the image and an optional timestamp. Whether SD recovery is allowed is read from OTP; `FREEZE_VERSION` and hardware write protection of the EEPROMs are the countermeasures the documentation names.
- **Fallback.** `tryboot` loads an alternative configuration once, for fail-safe OS updates, on all models; `tryboot_a_b` and `PARTITION_WALK` support A/B schemes and search further partitions when the chosen one does not boot.
- **Secure-boot fields in OTP.** For non-BCM2712 devices, including the BCM2711 of the Pi 4, the OTP list gives "SHA256 of RSA public key for secure-boot" (rows 47 to 54), secure-boot flags (row 55) and a 256-bit device-specific private key (rows 56 to 63); a bit in row 17, marked BCM2711, disables ROM RSA key 0, "secure boot enabled if set". When secure boot is enabled, `tryboot` loads `tryboot.img` instead of `boot.img`.
- **BCM2712 (Pi 5).** The public OTP list for the BCM2712 shows boot-mode bits, serial number, MAC addresses and customer rows, and no secure-boot rows; the page says registers not listed are not public.

## How

User documentation, written as configuration reference.

## Limits

The documentation says that OTP registers or bits not listed are not public.

A careful reader adds:

- The ROM, the EEPROM bootloader and the GPU firmware are Raspberry Pi's closed code; the documentation describes their behaviour, not their contents.
- Secure boot is documented here only through its OTP rows and its effect on `tryboot`; how it is enabled and what it verifies is in material not covered.

## Against the wiki

- [[raspberry-pi]]: created with this source.
- [[bootloader]]: the Pi's own firmware already provides fallback (`tryboot`, partition walk) below any zOS loader.

## For zOS

- [[root-of-trust]], [[bootloader]]: the paper's pib runs on a Raspberry Pi (Section 7), and this source covers the Pi 4 and the Pi 5. Our reading: on both boards, closed ROM and EEPROM code runs before any zOS code, and on the Pi 5 the bootloader itself loads the kernel image. A zOS loader would run after that code and could not measure it.
- The paper says the Raspberry Pi 4 can carry seL4 with pib's Linux as a driver island, "but only as a demonstrator before Silent Zero 0.01" (Section 7). This source does not bear on that claim directly; it shows what runs before seL4.
- [[root-of-trust]]: our reading: whoever can write the SD card or the boot partition can replace the bootloader through `recovery.bin` or self-update, unless OTP settings, `FREEZE_VERSION` or write protection prevent it; the checksum file is not a signature.
