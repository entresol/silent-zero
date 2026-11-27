---
type: source
id: nd-amd-opensil
status: reviewed
read: full
kind: report
sources: [nd-amd-opensil]
updated: 2026-11-27
---

# AMD openSIL (repository README)

The README of AMD's openSIL repository, "Genoa Proof-of-Concept"; undated, and the build notes name toolchain versions "today (June 2023)". [github.com/openSIL/openSIL](https://github.com/openSIL/openSIL). The pool holds a snapshot of 2 November 2026. Read in full; it is a short page.

## What it shows

- **What it is.** A collection of C libraries for x86 host firmware, linked statically or built from source: xSIM (silicon initialisation), xPRF (platform reference) and xUSL (utilities and services). The licence is MIT; the code is copyright AMD.
- **Status.** The page calls the branch a proof of concept that is not for production firmware and not eligible for AMD's bug bounty. Its roadmap lists three evaluation-only phases as complete (internal proof of concept; open-sourced for AMD 4th Gen EPYC on a reference board; further platforms) and a production phase, a "POR with UEFI Host FW", marked "trending 2026".
- **Scope of support.** This release supports 4th Gen EPYC on one reference board, Onyx, with UEFI firmware. The integration with earlier UEFI-AGESA installations sits in a separate repository, available through an AMD representative.

## How

A project README. It reports no test results or measurements; it says only that all testing was done on the Onyx reference board.

## Limits

The page does not mention the Platform Security Processor, so nothing here says what the library does or does not replace; "does not replace the PSP" is our reading of the name and the scope. The README is not dated, and the "trending 2026" line was not checked against AMD's current roadmap. It says nothing on coreboot.

## Against the wiki

- [[amd-psp]]: **extends**. The wiki had no source on open AMD silicon-initialisation code; this one is open (MIT) and covers a server part only.
- [[coreboot]]: no change.

## For zOS

[[root-of-trust]]: no change of state. Our reading: AMD's open library is a server proof of concept as of the page, nothing on the page points to a PC profile; it lists only a server part, and the "additional platforms" of phase III are not itemised.
