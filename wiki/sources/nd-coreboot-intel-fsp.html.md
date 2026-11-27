# coreboot: Intel FSP documentation

> Coreboot’s integration rule for Intel’s FSP and its list of seven FSP bugs. report, full text.

Source · LLM reviewed · updated 2026-11-26 · https://silentzero.ooo/wiki/sources/nd-coreboot-intel-fsp.html

The index page of coreboot's documentation on the Intel Firmware Support Package (FSP); undated, licensed CC-by 4.0. [doc.coreboot.org/soc/intel/fsp](https://doc.coreboot.org/soc/intel/fsp/index.html). The pool holds a snapshot of 2 November 2026. Read in full; the page is short.

## What it shows

- **An integration rule.** It should be possible to replace an FSP-based boot with a native coreboot implementation for a chipset without touching the mainboard code. The devicetree configures coreboot, and coreboot sets some FSP parameters (UPDs); the devicetree is not meant to configure the FSP directly.
- **A bug list.** The page says Intel does not list known bugs, so coreboot collects them. It names seven, each with a release or version and a link to the public tracker (the Braswell entry repeats the issue number printed for a Broadwell-DE one; the Broadwell-DE hang is said to occur on some SKUs only): three for Broadwell-DE (a locked feature-control register in FSP-M, an assertion if the thermal device is disabled, a hang when certain devices are hidden after memory initialisation), two for Kaby Lake (empty DIMM identifiers; forced memory re-training on cold boot on boards with Intel SPS), one for Braswell (the internal UART cannot be disabled) and one for Coffee Lake (a crash in FSP-M when the internal graphics is disabled). Five come with a workaround and two state none.
- **Specifications.** The page links the Open Source FSP specification, versions 1.0 to 2.1, and Intel's official FSP bug tracker.

## How

A reference page; the bug entries link to issues on a public tracker, and the page does not say who reported them.

## Limits

The page does not say what the FSP does; "memory and silicon initialisation" is our reading of the names FSP-M and FSP-S; it gives no source code, no signature checks and no count of how many boards use the FSP. The bug list is a sample of reported problems for four platform families, not a measure of FSP quality.

## Against the wiki

- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md): **extends**. Our reading: the page shows a vendor component whose bugs coreboot works around, since Intel does not list them. [coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md) already lists `fspm.bin` and `fsps.bin` among the read-write firmware.
- [coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md): the FSP binaries appear among the regions measured in its example log.

## For Silent Zero

[Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md): no change of state. Our reading: the page is evidence that on Intel boards code the project cannot repair runs inside coreboot's boot, and that its bugs are collected by coreboot, not listed by the vendor. See [Intel Firmware Support Package (FSP)](https://silentzero.ooo/wiki/systems/intel-fsp.html.md).

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
- [Intel Firmware Support Package (FSP)](https://silentzero.ooo/wiki/systems/intel-fsp.html.md)
- [coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md)
- [coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md)
- [Intel FSP binaries (repository README)](https://silentzero.ooo/wiki/sources/nd-intel-fsp-binaries.html.md)
