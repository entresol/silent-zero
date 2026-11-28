# Intel Management Engine (ME)

> Intel’s signed co-processor in PC chipsets; a script reduces its firmware but cannot remove it.

System · LLM reviewed · updated 2026-11-27 · 1 source · https://silentzero.ooo/wiki/systems/intel-me.html

According to the me_cleaner project, Intel ME is a co-processor in all Intel boards since 2006 which, in the README's words, requires full access to the system, including memory through DMA and network access invisible to the user. Its firmware is signed, tied into the boot and cannot be reimplemented ([me_cleaner (repository README)](https://silentzero.ooo/wiki/sources/nd-me-cleaner.html.md)). This page rests on that one source, the project's own account; Intel's description is not in the wiki.

## State, as the README reads in the snapshot of 2 November 2026

The README says that before Nehalem (ME version 6) the ME could be removed by flash-descriptor bits, and that from Nehalem on a missing firmware shuts the PC down after 30 minutes. The tool me_cleaner cuts the image to the modules the boot needs, about 90 kB for versions 6 to 10 and about 300 kB from version 11 on, so that, as the README aims, the ME is active only during boot, at the price of its features and, on some boards, of the boot itself ([me_cleaner (repository README)](https://silentzero.ooo/wiki/sources/nd-me-cleaner.html.md)). Our reading: it reduces the ME and does not remove it, and the README states no check of what a reduced ME can still do.

## Licence and code

The firmware is Intel's, signed and closed. me_cleaner is a script of its own project; its licence is not covered by the wiki's sources.

## Open questions

- What a reduced ME can still reach once running, and which ME generations the tool covers today. See [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md), [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md) and [Intel Firmware Support Package (FSP)](https://silentzero.ooo/wiki/systems/intel-fsp.html.md).

## Sources

- [me_cleaner (repository README)](https://silentzero.ooo/wiki/sources/nd-me-cleaner.html.md)

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
- [Intel Firmware Support Package (FSP)](https://silentzero.ooo/wiki/systems/intel-fsp.html.md)
- [Heads: the project wiki's overview](https://silentzero.ooo/wiki/sources/nd-heads.html.md)
