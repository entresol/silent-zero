# coreboot

> Open firmware in stages with a fixed payload; verified and measured boot; closed vendor parts on x86.

System · LLM reviewed · updated 2026-10-30 · 3 sources · https://silentzero.ooo/wiki/systems/coreboot.html

Open-source firmware that initialises a machine and hands over to a payload. It is built from stages, each loading the next: bootblock, an optional verstage for verified boot, romstage (DRAM), postcar, ramstage (devices, tables, lockdown) and the payload, which is fixed in coreboot's file system and cannot be chosen at run time ([coreboot: architecture and boot stages](https://silentzero.ooo/wiki/sources/nd-coreboot-architecture.html.md)).

## State, October 2026

Documentation for version 26.09. Verified boot (vboot) roots trust in the write-protected part of the SPI flash and verifies read-write firmware against a root key there, with A/B update slots and a recovery path; it requires a TPM ([coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md)). Measured boot records hashes of what runs into TPM registers and works without vboot ([coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md)).

## What remains closed

The read-write firmware includes processor-specific binaries such as `fspm.bin` and `fsps.bin`, in our reading Intel's memory and silicon initialisation ([coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md)). The first measurement is taken by coreboot's own boot block; Intel Boot Guard and AMD Hardware Validated Boot root only the verification of that block in hardware ([coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md)).

## Licence and code

Not yet covered by the wiki's sources.

## Open questions

- Which boards could run a Silent Zero loader as a coreboot payload, and what of their firmware stays closed. See [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md).

## Sources

- [coreboot: architecture and boot stages](https://silentzero.ooo/wiki/sources/nd-coreboot-architecture.html.md)
- [coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md)
- [coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md)

## Related pages

- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)
