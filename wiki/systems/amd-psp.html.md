# AMD Platform Security Processor (PSP)

> AMD’s on-die processor that starts first and runs signed firmware; documented only through coreboot’s image guide.

System · LLM reviewed · updated 2026-11-26 · 1 source · https://silentzero.ooo/wiki/systems/amd-psp.html

According to coreboot's guide, the PSP is an isolated processor on AMD's chips. It runs its own firmware from the same SPI flash as the BIOS, verifies its boot loader's signature and initialises the silicon before the x86 cores leave reset. AMD now calls it the AMD Secure Processor ([coreboot: AMD PSP firmware integration guide](https://silentzero.ooo/wiki/sources/nd-coreboot-amd-psp.html.md)).

## State, November 2026

The only source in the wiki is coreboot's integration guide, which documents how its image carries PSP firmware: a signed boot loader whose public key the on-chip boot code uses, a recovery loader, a "SecureOS" with a firmware TPM, and boot loaders that set up memory before the main cores start. The page does not describe the firmware's behaviour; AMD's details are under non-disclosure ([coreboot: AMD PSP firmware integration guide](https://silentzero.ooo/wiki/sources/nd-coreboot-amd-psp.html.md)).

## Licence and code

The firmware is AMD's and is not open in this source. The coreboot tools `amdfwtool` and `amdcompress` that assemble the image are part of coreboot; their licence is not covered by the wiki's sources.

## Open questions

- Whether any open replacement exists, and what the PSP can access once the x86 cores run. See [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md) and [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md).

## Sources

- [coreboot: AMD PSP firmware integration guide](https://silentzero.ooo/wiki/sources/nd-coreboot-amd-psp.html.md)

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
