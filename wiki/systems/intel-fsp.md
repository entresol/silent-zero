---
type: system
status: reviewed
sources: [nd-coreboot-intel-fsp]
short: Intel's binary init code that coreboot calls
updated: 2026-11-26
---

# Intel Firmware Support Package (FSP)

The page names Intel's Firmware Support Package, which coreboot configures through parameters called UPDs ([[nd-coreboot-intel-fsp]]). Our reading: it is Intel's binary firmware for initialisation, the names FSP-M and FSP-S point to a memory part and a silicon part, and [[nd-coreboot-vboot]] lists `fspm.bin` and `fsps.bin` in the read-write firmware.

## State, November 2026

coreboot's documentation links the open FSP specification, versions 1.0 to 2.1, and the official FSP bug tracker. It says Intel does not list known bugs and collects seven for four platform families, two without a workaround. Its integration rule is that an FSP-based boot should be replaceable by a native implementation without touching the mainboard code ([[nd-coreboot-intel-fsp]]).

## Licence and code

Our reading: the binaries are Intel's. Their licence is not covered by the wiki's sources.

## Open questions

- Which Intel boards boot without the FSP, and what runs in it that nothing else can check. See [[root-of-trust]] and [[coreboot]].
