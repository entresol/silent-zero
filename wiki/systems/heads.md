---
type: system
status: reviewed
sources: [nd-heads]
short: Coreboot plus a Linux payload with TPM checks
updated: 2026-11-28
---

# Heads

Open-source firmware for laptops and servers that puts a Linux payload into the coreboot ROM, measures each boot step into a TPM and checks signed boot files with keys the user holds ([[nd-heads]]). According to a summary of a 2020 talk on the project's wiki, it is tamper-evident, not tamper-proof: it detects tampering and alerts the user instead of blocking, and the signing keys are the user's.

## State, November 2026

The project wiki lists boards from several makers, among them ThinkPads, MSI PRO Z690 and Z790, NovaCustom and Nitropad ([[nd-heads]]). It is a payload of [[coreboot]]; the closed Intel parts beneath it are measured, not replaced. A summary of a 2024 design session calls re-signing after each kernel update the central usability problem and says it blocks mainstream adoption. The page calls Heads and its wiki free and open source and links its GitHub repository; it gives no release, version or licence text, so the licence is not covered by the wiki's sources.

## Open questions

- Whether Heads' checks could govern a signed static image instead of a Linux kernel, and what Heads would measure then. See [[bootloader]].
