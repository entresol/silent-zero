---
type: system
status: drafted
sources: [nd-me-cleaner]
short: Intel's signed co-processor inside PC chipsets
updated: 2026-11-27
---

# Intel Management Engine (ME)

According to the me_cleaner project, Intel ME is a co-processor in all Intel boards since 2006, with full access to the system through DMA and invisible network access. Its firmware is signed, tied into the boot and cannot be reimplemented ([[nd-me-cleaner]]). This page rests on that one source, the project's own account; Intel's description is not in the wiki.

## State, November 2026

The README says that before Nehalem (ME version 6) the ME could be removed by flash-descriptor bits, and that from Nehalem on a missing firmware shuts the PC down after 30 minutes. The tool me_cleaner cuts the image to the modules the boot needs, about 90 kB for versions 6 to 10 and about 300 kB from version 11 on, so that the ME is active only during boot, at the price of its features and, on some boards, of the boot itself ([[nd-me-cleaner]]). Our reading: it reduces the ME and does not remove it, and the README states no check of what a reduced ME can still do.

## Licence and code

The firmware is Intel's, signed and closed. me_cleaner is a script of its own project; its licence is not covered by the wiki's sources.

## Open questions

- What a reduced ME can still reach once running, and which ME generations the tool covers today. See [[root-of-trust]], [[coreboot]] and [[intel-fsp]].
