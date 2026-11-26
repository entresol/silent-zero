# coreboot: AMD PSP firmware integration guide

> How the AMD PSP’s firmware is laid out in a coreboot image; AMD’s details under non-disclosure. report, partly read.

Source · LLM reviewed · updated 2026-11-26 · https://silentzero.ooo/wiki/sources/nd-coreboot-amd-psp.html

The coreboot project's guide to how AMD's Platform Security Processor (PSP) firmware is laid out in a coreboot image; undated, documentation licensed CC-by 4.0. [doc.coreboot.org/soc/amd/psp_integration](https://doc.coreboot.org/soc/amd/psp_integration.html). The pool holds a snapshot of 2 November 2026. Read partly: the overview, the flash structures, the tools and the references; the per-entry description of the directory types is read only for what each type is for, and the byte layouts are not checked.

## What it shows

- **What the PSP is.** An on-die, isolated security processor that runs independently of the x86 cores, runs its own firmware and shares the SPI flash with the system BIOS. The page says security-sensitive components run on it unaffected by software on the x86 cores. AMD's current name is "AMD Secure Processor".
- **How it is found.** The PSP looks for an Embedded Firmware Structure at one of six fixed flash addresses, the structure points to a PSP directory table (the images the PSP loads) and a BIOS directory table (the components the x86 side can reach). Tables carry a checksum, entry types and addresses.
- **What the entries are.** The type list includes a public key used by the on-chip boot code to verify the signature of the PSP's boot loader, a second-stage boot loader, a recovery boot loader, a "SecureOS" that also hosts a firmware TPM as a trusted application, power-management firmware, secure-debug unlock material and "AGESA boot loaders". The page says the last are executed by the PSP and initialise the silicon, including the memory interface, before the main cores are released from reset. A "BIOS reset image" is the code the PSP decompresses into DRAM where the x86 starts executing; coreboot's `amdcompress` builds it from the boot block.
- **What the page leaves out.** Details of each firmware blob and feature "are beyond the scope of this document" and are in AMD documents under non-disclosure; two are cited by number. `amdfwtool` assembles the monolithic image that goes into the coreboot image.

## How

A reference document for people building coreboot images. It describes formats, not behaviour, and has no measurements.

## Limits

The page documents layout, not what the PSP firmware does; nothing on the page says what the PSP can read or write, whether its firmware has been audited, or how its firmware is delivered; it mentions only level-2 tables that allow updates without risking the primary table. Whether an unsigned image would be refused is not stated beyond the signature check on the PSP's own boot loader.

## Against the wiki

- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md): **extends** the list of closed parts. On AMD machines the image also carries PSP firmware that coreboot does not build.
- [coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md): **consistent**. That page says vendor hardware roots stand behind the first measurement.

## For Silent Zero

[Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md): no change of state. Our reading: this page shows that on an AMD PC a processor other than the x86 cores starts first, and its code and the AGESA boot loaders are binaries the Silent Zero bootloader's first screen cannot check. That adds a case to the firmware the paper already counts as assumed. The page is the project's documentation, not AMD's; the claims about what the PSP is are the project's wording. See [AMD Platform Security Processor (PSP)](https://silentzero.ooo/wiki/systems/amd-psp.html.md).

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [AMD Platform Security Processor (PSP)](https://silentzero.ooo/wiki/systems/amd-psp.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
- [coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md)
