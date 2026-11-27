# coreboot

> Open firmware in stages with a fixed payload; verified and measured boot; closed vendor parts on x86, its payloads.

System · LLM reviewed · updated 2026-11-27 · 7 sources · https://silentzero.ooo/wiki/systems/coreboot.html

Open-source firmware that initialises a machine and hands over to a payload. It is built from stages, each loading the next: bootblock, an optional verstage for verified boot, romstage (DRAM), postcar, ramstage (devices, tables, lockdown) and the payload, which is fixed in coreboot's file system and cannot be chosen at run time ([coreboot: architecture and boot stages](https://silentzero.ooo/wiki/sources/nd-coreboot-architecture.html.md)).

## State, October 2026

Documentation for version 26.09. Verified boot (vboot) roots trust in the write-protected part of the SPI flash and verifies read-write firmware against a root key there, with A/B update slots and a recovery path; it requires a TPM ([coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md)). Measured boot records hashes of what runs into TPM registers and works without vboot ([coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md)).

## What remains closed

The read-write firmware includes processor-specific binaries such as `fspm.bin` and `fsps.bin`, in our reading Intel's memory and silicon initialisation ([coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md)). The first measurement is taken by coreboot's own boot block; Intel Boot Guard and AMD Hardware Validated Boot root only the verification of that block in hardware ([coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md)).

On AMD machines the image also carries firmware for the Platform Security Processor, an on-die processor that, according to coreboot's guide, initialises the silicon before the x86 cores start; coreboot's tools assemble the firmware images into its image ([coreboot: AMD PSP firmware integration guide](https://silentzero.ooo/wiki/sources/nd-coreboot-amd-psp.html.md), [AMD Platform Security Processor (PSP)](https://silentzero.ooo/wiki/systems/amd-psp.html.md)). On Intel boards coreboot calls Intel's FSP and collects its bugs itself, since Intel does not list them ([coreboot: Intel FSP documentation](https://silentzero.ooo/wiki/sources/nd-coreboot-intel-fsp.html.md), [Intel Firmware Support Package (FSP)](https://silentzero.ooo/wiki/systems/intel-fsp.html.md)). Free firmware on Intel boards also depends on the ME, a signed co-processor whose firmware the me_cleaner project can only reduce ([me_cleaner (repository README)](https://silentzero.ooo/wiki/sources/nd-me-cleaner.html.md), [Intel Management Engine (ME)](https://silentzero.ooo/wiki/systems/intel-me.html.md)).

## Payloads

The payload can be any statically linked ELF binary, SeaBIOS, edk2, GRUB2, Linux or Heads ([coreboot: payloads](https://silentzero.ooo/wiki/sources/nd-coreboot-payloads.html.md)). The documentation page does not say whether any of them can start a Multiboot 2 image, which Microkit needs ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)).

## Licence and code

The documentation is licensed CC-by 4.0 ([coreboot: payloads](https://silentzero.ooo/wiki/sources/nd-coreboot-payloads.html.md)). The licence of the code is not yet covered by the wiki's sources.

## Open questions

- Which boards could run a Silent Zero loader as a coreboot payload, and what of their firmware stays closed. See [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md).

## Sources

- [coreboot: AMD PSP firmware integration guide](https://silentzero.ooo/wiki/sources/nd-coreboot-amd-psp.html.md)
- [coreboot: architecture and boot stages](https://silentzero.ooo/wiki/sources/nd-coreboot-architecture.html.md)
- [coreboot: Intel FSP documentation](https://silentzero.ooo/wiki/sources/nd-coreboot-intel-fsp.html.md)
- [coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md)
- [coreboot: payloads](https://silentzero.ooo/wiki/sources/nd-coreboot-payloads.html.md)
- [coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md)
- [me_cleaner (repository README)](https://silentzero.ooo/wiki/sources/nd-me-cleaner.html.md)

## Related pages

- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)
- [AMD openSIL](https://silentzero.ooo/wiki/systems/amd-opensil.html.md)
- [AMD Platform Security Processor (PSP)](https://silentzero.ooo/wiki/systems/amd-psp.html.md)
- [Intel Firmware Support Package (FSP)](https://silentzero.ooo/wiki/systems/intel-fsp.html.md)
- [Intel Management Engine (ME)](https://silentzero.ooo/wiki/systems/intel-me.html.md)
- [AMD openSIL (repository README)](https://silentzero.ooo/wiki/sources/nd-amd-opensil.html.md)
- [Intel FSP binaries (repository README)](https://silentzero.ooo/wiki/sources/nd-intel-fsp-binaries.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
