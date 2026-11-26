# Intel Firmware Support Package (FSP)

> Intel’s binary initialisation code that coreboot calls; seven bugs collected by coreboot.

System · LLM reviewed · updated 2026-11-26 · 1 source · https://silentzero.ooo/wiki/systems/intel-fsp.html

The page names Intel's Firmware Support Package, which coreboot configures through parameters called UPDs ([coreboot: Intel FSP documentation](https://silentzero.ooo/wiki/sources/nd-coreboot-intel-fsp.html.md)). Our reading: it is Intel's binary firmware for initialisation, the names FSP-M and FSP-S point to a memory part and a silicon part, and [coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md) lists `fspm.bin` and `fsps.bin` in the read-write firmware.

## State, November 2026

coreboot's documentation links the open FSP specification, versions 1.0 to 2.1, and the official FSP bug tracker. It says Intel does not list known bugs and collects seven for four platform families, two without a workaround. Its integration rule is that an FSP-based boot should be replaceable by a native implementation without touching the mainboard code ([coreboot: Intel FSP documentation](https://silentzero.ooo/wiki/sources/nd-coreboot-intel-fsp.html.md)).

## Licence and code

Our reading: the binaries are Intel's. Their licence is not covered by the wiki's sources.

## Open questions

- Which Intel boards boot without the FSP, and what runs in it that nothing else can check. See [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md) and [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md).

## Sources

- [coreboot: Intel FSP documentation](https://silentzero.ooo/wiki/sources/nd-coreboot-intel-fsp.html.md)

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
- [coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md)
