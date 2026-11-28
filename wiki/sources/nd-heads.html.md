# Heads: the project wiki's overview

> The Heads wiki’s overview: coreboot with a Linux payload, TPM measurement, user-signed /boot; summaries of talks. report, full text.

Source · LLM reviewed · updated 2026-11-28 · https://silentzero.ooo/wiki/sources/nd-heads.html

The "About" page of the Heads wiki, [osresearch.net](https://osresearch.net/). Snapshot of 2 November 2026, undated. Read in full: the overview and the one-paragraph summaries of talks and articles about Heads and LinuxBoot. The linked talks, articles, threat model and hardware list were not read, and the summaries are the wiki's own words, not the talks.

## What it shows

- **What Heads is.** Open-source custom firmware and OS configuration for laptops and servers, aimed at "slightly better" physical security of data that stays on the machine. It combines hardware-specific hardening with custom coreboot firmware and a Linux boot loader in the ROM. The page says this moves the root of trust into the write-protected region of the SPI flash and, on platforms that support it, Intel Boot Guard enforces verified boot of the firmware.
- **Measured and tamper-evident, not blocking.** Because Heads controls the first instruction, it measures every boot step and its configuration into the TPM, so the machine can show a user or a remote system that it was not tampered with. Hypervisor, kernel and initrd images are signed with keys the user controls. A summary of a 2020 talk quotes the contrast with UEFI Secure Boot: Heads detects tampering and alerts instead of blocking, and "does not provide tamper proofing".
- **Closed parts stay, and are measured.** The page says modern Intel CPUs need binary blobs to boot; these are included in the measurement. A summary of a 2023 talk describes the builds as neutering or deactivating the Intel ME, with one external flash needed once to overwrite locked regions; see [Intel Management Engine (ME)](https://silentzero.ooo/wiki/systems/intel-me.html.md).
- **Mechanisms, from the 2016 talk's summary.** The TPM seals disk keys and a TOTP secret to the measured state; on a clean boot the machine shows a six-digit code the user compares with a phone. Kernel and initrd in /boot are checked against GPG signatures; the summary lists countermeasures for the Thunderstrike DMA attack (VT-d, bus mastering off before handoff) and for SPI-flash overwrites (write-protect bits), and a boot to a recovery shell in under a second.
- **Costs the page's own sources name.** A 2024 design-session summary says users must re-sign after every kernel update because Heads checks exact hashes of the /boot files, called "a burden" that blocks mainstream adoption, and lists a unified kernel image as a possible fix.
- **Scope.** A hardware list of ThinkPads, Dell, HP, MSI, NovaCustom, Nitropad and others is linked from the page.

## How

The page is documentation and a reading list. It reports no test, proof or measurement of its own; the 2016 talk's boot time and the other figures are the summaries' statements.

## Limits

The statements are the project's own and its summaries' of talks. The page says Boot Guard enforces verified boot "on platforms that support it"; which platforms those are, it does not say here. The page says the closed firmware beneath Heads is measured and, in its words, at least guaranteed to be unchanging; it gives no assurance about what that firmware does. A careful reader adds that measuring closed code shows that it changed, not what it does.

## Against the wiki

- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md): **extends**. Heads is the payload that [coreboot: payloads](https://silentzero.ooo/wiki/sources/nd-coreboot-payloads.html.md) lists, and it builds on coreboot's measured boot ([coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md)): coreboot's early stages extend the measurements and Heads adds more. See [Heads](https://silentzero.ooo/wiki/systems/heads.html.md).
- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md): **extends**. Heads fills the row for PC firmware with a payload that measures and checks signed files with keys the user holds. Our reading: it is a Linux kernel in ROM, not a small loader.
- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md): **extends**. The page claims the write-protected flash as the root and a TPM as the record, the arrangement the PC row names; a 2023 summary lists flash write protection under "what's next", so how far it holds on each board is open. The closed Intel parts remain assumed.
- [Intel Firmware Support Package (FSP)](https://silentzero.ooo/wiki/systems/intel-fsp.html.md), [Intel Management Engine (ME)](https://silentzero.ooo/wiki/systems/intel-me.html.md): related. The page speaks of Intel's binary blobs, kept and measured; our reading: these include the FSP, which the 2017 LinuxBoot summary names. A 2023 summary describes a neutered ME.

## For Silent Zero

[The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md) and [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md): no change of state. Our reading: Heads is the nearest working example of a measured, user-keyed boot chain on x86, and its re-signing burden is a warning for a loader that checks one exact image: every update changes the hash. The source does not say how Heads would handle a kernel that is not Linux.

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
- [Heads](https://silentzero.ooo/wiki/systems/heads.html.md)
- [Intel Firmware Support Package (FSP)](https://silentzero.ooo/wiki/systems/intel-fsp.html.md)
- [Intel Management Engine (ME)](https://silentzero.ooo/wiki/systems/intel-me.html.md)
- [LinuxBoot](https://silentzero.ooo/wiki/systems/linuxboot.html.md)
- [coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md)
- [coreboot: payloads](https://silentzero.ooo/wiki/sources/nd-coreboot-payloads.html.md)
- [LinuxBoot: the project page](https://silentzero.ooo/wiki/sources/nd-linuxboot.html.md)
