# Intel Firmware Support Package (FSP)

> Intel’s binary initialisation code that coreboot calls; seven bugs collected by coreboot; Intel posts the binaries per platform.

System · LLM reviewed · updated 2026-11-27 · 2 sources · https://silentzero.ooo/wiki/systems/intel-fsp.html

The page names Intel's Firmware Support Package, which coreboot configures through parameters called UPDs ([coreboot: Intel FSP documentation](https://silentzero.ooo/wiki/sources/nd-coreboot-intel-fsp.html.md)). Our reading: it is Intel's binary firmware for initialisation, the names FSP-M and FSP-S point to a memory part and a silicon part, and [coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md) lists `fspm.bin` and `fsps.bin` in the read-write firmware.

## State, November 2026

coreboot's documentation links the open FSP specification, versions 1.0 to 2.1, and the official FSP bug tracker. It says Intel does not list known bugs and collects seven for four platform families, two without a workaround. Its integration rule is that an FSP-based boot should be replaceable by a native implementation without touching the mainboard code ([coreboot: Intel FSP documentation](https://silentzero.ooo/wiki/sources/nd-coreboot-intel-fsp.html.md)).

Intel posts the binaries in a GitHub repository, one directory per platform: seventeen in the README, from Skylake and Braswell to Raptor Lake, with Atom and Xeon parts, mostly at specification v2.0 to v2.3, older ones in a legacy branch ([Intel FSP binaries (repository README)](https://silentzero.ooo/wiki/sources/nd-intel-fsp-binaries.html.md)).

## Licence and code

The repository holds binaries; its README names licences only for three third-party components (EDK2, EDK2-Platforms, OpenSSL). The licence of the binaries themselves is not covered by the wiki's sources ([Intel FSP binaries (repository README)](https://silentzero.ooo/wiki/sources/nd-intel-fsp-binaries.html.md)). Our reading: the FSP is distributed only as binaries; Intel's other proprietary component on the same boards is [Intel Management Engine (ME)](https://silentzero.ooo/wiki/systems/intel-me.html.md).

## Open questions

- Which Intel boards boot without the FSP, and what runs in it that nothing else can check. See [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md) and [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md).

## Sources

- [coreboot: Intel FSP documentation](https://silentzero.ooo/wiki/sources/nd-coreboot-intel-fsp.html.md)
- [Intel FSP binaries (repository README)](https://silentzero.ooo/wiki/sources/nd-intel-fsp-binaries.html.md)

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
- [Intel Management Engine (ME)](https://silentzero.ooo/wiki/systems/intel-me.html.md)
- [coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md)
- [Heads: the project wiki's overview](https://silentzero.ooo/wiki/sources/nd-heads.html.md)
