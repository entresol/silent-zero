---
type: system
status: reviewed
sources: [nd-coreboot-architecture, nd-coreboot-vboot, nd-coreboot-measured-boot, nd-coreboot-payloads, nd-coreboot-amd-psp, nd-coreboot-intel-fsp, nd-me-cleaner]
short: Open firmware in stages with a fixed payload
updated: 2026-11-27
---

# coreboot

Open-source firmware that initialises a machine and hands over to a payload. It is built from stages, each loading the next: bootblock, an optional verstage for verified boot, romstage (DRAM), postcar, ramstage (devices, tables, lockdown) and the payload, which is fixed in coreboot's file system and cannot be chosen at run time ([[nd-coreboot-architecture]]).

## State, October 2026

Documentation for version 26.09. Verified boot (vboot) roots trust in the write-protected part of the SPI flash and verifies read-write firmware against a root key there, with A/B update slots and a recovery path; it requires a TPM ([[nd-coreboot-vboot]]). Measured boot records hashes of what runs into TPM registers and works without vboot ([[nd-coreboot-measured-boot]]).

## What remains closed

The read-write firmware includes processor-specific binaries such as `fspm.bin` and `fsps.bin`, in our reading Intel's memory and silicon initialisation ([[nd-coreboot-vboot]]). The first measurement is taken by coreboot's own boot block; Intel Boot Guard and AMD Hardware Validated Boot root only the verification of that block in hardware ([[nd-coreboot-measured-boot]]).

On AMD machines the image also carries firmware for the Platform Security Processor, an on-die processor that, according to coreboot's guide, initialises the silicon before the x86 cores start; coreboot's tools assemble the firmware images into its image ([[nd-coreboot-amd-psp]], [[amd-psp]]). On Intel boards coreboot calls Intel's FSP and collects its bugs itself, since Intel does not list them ([[nd-coreboot-intel-fsp]], [[intel-fsp]]). Free firmware on Intel boards also depends on the ME, a signed co-processor whose firmware the me_cleaner project can only reduce ([[nd-me-cleaner]], [[intel-me]]).

## Payloads

The payload can be any statically linked ELF binary, SeaBIOS, edk2, GRUB2, Linux or Heads ([[nd-coreboot-payloads]]). The documentation page does not say whether any of them can start a Multiboot 2 image, which Microkit needs ([[nd-sel4-microkit-user-manual]]).

## Licence and code

The documentation is licensed CC-by 4.0 ([[nd-coreboot-payloads]]). The licence of the code is not yet covered by the wiki's sources.

## Open questions

- Which boards could run a zOS loader as a coreboot payload, and what of their firmware stays closed. See [[bootloader]].
