---
type: system
status: reviewed
sources: [nd-coreboot-amd-psp, nd-amd-opensil]
short: AMD's on-die processor that starts first
updated: 2026-11-27
---

# AMD Platform Security Processor (PSP)

According to coreboot's guide, the PSP is an isolated processor on AMD's chips. It runs its own firmware from the same SPI flash as the BIOS, verifies its boot loader's signature and initialises the silicon before the x86 cores leave reset. AMD now calls it the AMD Secure Processor ([[nd-coreboot-amd-psp]]).

## State, November 2026

The only source in the wiki is coreboot's integration guide, which documents how its image carries PSP firmware: a signed boot loader whose public key the on-chip boot code uses, a recovery loader, a "SecureOS" with a firmware TPM, and boot loaders that set up memory before the main cores start. The page does not describe the firmware's behaviour; AMD's details are under non-disclosure ([[nd-coreboot-amd-psp]]).

## Licence and code

The firmware is AMD's and is not open in this source. The coreboot tools `amdfwtool` and `amdcompress` that assemble the image are part of coreboot; their licence is not covered by the wiki's sources.

AMD also publishes an open library for silicon initialisation, [[amd-opensil]]; its README, as the wiki read it, does not mention the PSP and covers a server proof of concept ([[nd-amd-opensil]]).

## Open questions

- Whether any open replacement for the PSP firmware exists, and what the PSP can access once the x86 cores run. See [[root-of-trust]] and [[coreboot]].
