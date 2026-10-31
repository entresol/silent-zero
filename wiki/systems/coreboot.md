---
type: system
status: reviewed
sources: [nd-coreboot-architecture, nd-coreboot-vboot, nd-coreboot-measured-boot]
short: Open firmware in stages with a fixed payload
updated: 2026-10-30
---

# coreboot

Open-source firmware that initialises a machine and hands over to a payload. It is built from stages, each loading the next: bootblock, an optional verstage for verified boot, romstage (DRAM), postcar, ramstage (devices, tables, lockdown) and the payload, which is fixed in coreboot's file system and cannot be chosen at run time ([[nd-coreboot-architecture]]).

## State, October 2026

Documentation for version 26.09. Verified boot (vboot) roots trust in the write-protected part of the SPI flash and verifies read-write firmware against a root key there, with A/B update slots and a recovery path; it requires a TPM ([[nd-coreboot-vboot]]). Measured boot records hashes of what runs into TPM registers and works without vboot ([[nd-coreboot-measured-boot]]).

## What remains closed

The read-write firmware includes processor-specific binaries such as `fspm.bin` and `fsps.bin`, in our reading Intel's memory and silicon initialisation ([[nd-coreboot-vboot]]). The first measurement is taken by coreboot's own boot block; Intel Boot Guard and AMD Hardware Validated Boot root only the verification of that block in hardware ([[nd-coreboot-measured-boot]]).

## Licence and code

Not yet covered by the wiki's sources.

## Open questions

- Which boards could run a zOS loader as a coreboot payload, and what of their firmware stays closed. See [[bootloader]].
