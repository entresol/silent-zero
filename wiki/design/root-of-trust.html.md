# Root of trust and firmware

> The firmware below the kernel on Arm, RISC-V, PC and Raspberry Pi; OpenTitan, Caliptra, DICE; all assumed in the paper’s terms.

Design · LLM reviewed · updated 2026-11-02 · 13 sources · https://silentzero.ooo/wiki/design/root-of-trust.html

The bottom of Silent Zero: a root of trust that measures the first code to run, together with the hardware's memory management and IOMMU. Firmware runs here with more privilege than the kernel; on RISC-V, Microkit relies on SBI firmware such as OpenSBI in machine mode, and on Arm trusted firmware at the highest exception level plays that role. "This layer belongs to the trusted base and is *assumed*." (paper, Section 3).

## What it must do

- Measure the first code to run (paper, Section 3); checking the signed image is the [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)'s job.
- Report what it measured, so the bootloader can show it.
- Our reading: let the owner, not only the vendor, control what is trusted.

## What runs below or before the kernel

| Platform | Below the kernel at run time | Where trust starts | Source |
| --- | --- | --- | --- |
| Arm | TF-A's BL31 at EL3, serving secure monitor calls including power management; optionally a trusted OS (BL32) in the secure world | on Arm's reference platforms BL1 in trusted ROM; vendor boards may use their own ROM instead of BL1 and BL2 | [Trusted Firmware-A: firmware design](https://silentzero.ooo/wiki/sources/nd-tfa-firmware-design.html.md) |
| RISC-V | OpenSBI in machine mode | not stated in the sources | [OpenSBI](https://silentzero.ooo/wiki/sources/nd-opensbi.html.md), [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md) |
| PC with coreboot | firmware code such as SMM, locked by ramstage | the read-only part of the SPI flash; Intel Boot Guard or AMD Hardware Validated Boot root the verification of the boot block, the measurement root stays in software | [coreboot: architecture and boot stages](https://silentzero.ooo/wiki/sources/nd-coreboot-architecture.html.md), [coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md), [coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md) |
| Raspberry Pi 4 and 5 | not covered by the sources | closed ROM and EEPROM bootloader; on non-BCM2712 devices such as the Pi 4, a secure-boot key hash in OTP; on the Pi 5 not public in the sources | [Raspberry Pi documentation: boot](https://silentzero.ooo/wiki/sources/nd-raspberrypi-boot.html.md) |

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| Open-source silicon root of trust in production | shipping in Chromebooks since March 2026 | vendor announcement | [OpenTitan shipping in production](https://silentzero.ooo/wiki/sources/2026-google-opentitan-shipping-production.html.md) |
| Post-quantum secure boot (shipping part); ownership transfer (named in the announcement) | announced | vendor announcement | [OpenTitan shipping in production](https://silentzero.ooo/wiki/sources/2026-google-opentitan-shipping-production.html.md) |
| Design quality of OpenTitan | over 90 % coverage, 40,000 nightly tests | vendor statement on design verification, not on the chip | [OpenTitan shipping in production](https://silentzero.ooo/wiki/sources/2026-google-opentitan-shipping-production.html.md) |
| Root of trust for measurement inside data-centre SoCs | Caliptra, open IP and firmware under Apache 2.0 | project documentation | [Caliptra](https://silentzero.ooo/wiki/sources/nd-caliptra.html.md) |
| Verify-and-measure boot without a TPM (DICE) | verified at the level of generated C on a microcontroller | proof | [DICE\*, a Formally Verified Implementation of DICE Measured Boot](https://silentzero.ooo/wiki/sources/2021-tao-dice-formally-verified.html.md) |
| Processors themselves as a supply-chain risk to secure boot | a protocol for multi-chip systems, proved at model level, needs changes to the CPU's boot ROM | proof of a model | [PA-Boot, a Formally Verified Authentication Protocol for Multiprocessor Secure Boot under Hardware Supply-chain Attacks](https://silentzero.ooo/wiki/sources/2022-zhang-pa-boot-formally.html.md) |
| Bootloader replaceable from the SD card on the Pi | `recovery.bin` and self-update, unless OTP settings, `FREEZE_VERSION` or write protection prevent it | documentation | [Raspberry Pi documentation: boot](https://silentzero.ooo/wiki/sources/nd-raspberrypi-boot.html.md) |
| Kernel boot and IOMMU in seL4's proofs | outside every verified configuration | assumed | [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) |
| An enabled IOMMU confines a malicious device | attacked successfully on general-purpose systems in 2019, see [IOMMU](https://silentzero.ooo/wiki/concepts/iommu.html.md) | test | [Thunderclap](https://silentzero.ooo/wiki/sources/2019-markettos-thunderclap-exploring-vulnerabilities.html.md) |
| Microkit boot chain: loader, kernel, capDL initialiser | implemented; the loader is never executed again | documentation | [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md) |

## The paper and its sources

- In brief, Section 3 and Section 5 say OpenTitan has shipped in production Chromebooks since March 2026. Confirmed by [OpenTitan shipping in production](https://silentzero.ooo/wiki/sources/2026-google-opentitan-shipping-production.html.md). The paper classes this layer as *assumed*, and the sources do not change that.
- Section 3's roles for OpenSBI and trusted firmware are confirmed by [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md), [OpenSBI](https://silentzero.ooo/wiki/sources/nd-opensbi.html.md) and [Trusted Firmware-A: firmware design](https://silentzero.ooo/wiki/sources/nd-tfa-firmware-design.html.md).
- Section 6 says firmware below the kernel "has full access to memory and cannot be confined by any kernel". The sources confirm that this firmware runs at higher privilege; they do not discuss confining it.

## Open

- No source so far names a board that carries OpenTitan and runs seL4.
- What the root of trust measures, and how that reaches the Silent Zero bootloader's first screen, is open on every platform. On Arm and RISC-V the Microkit loader expects an earlier bootloader such as U-Boot ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)); see [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md).
- On the Pi, which firmware stays resident below the kernel, and how secure boot is enabled and what it verifies, is not covered by the sources.
- Which parts of the firmware below the kernel a Silent Zero hardware profile accepts: on Arm, how much of BL31 and whether a trusted OS; on a PC, the vendor's closed code. Intel ME, AMD PSP and open alternatives are not yet covered here.

## Sources

- [Caliptra](https://silentzero.ooo/wiki/sources/nd-caliptra.html.md)
- [coreboot: architecture and boot stages](https://silentzero.ooo/wiki/sources/nd-coreboot-architecture.html.md)
- [coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md)
- [coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md)
- [DICE\*, a Formally Verified Implementation of DICE Measured Boot](https://silentzero.ooo/wiki/sources/2021-tao-dice-formally-verified.html.md)
- [OpenSBI](https://silentzero.ooo/wiki/sources/nd-opensbi.html.md)
- [OpenTitan shipping in production](https://silentzero.ooo/wiki/sources/2026-google-opentitan-shipping-production.html.md)
- [PA-Boot, a Formally Verified Authentication Protocol for Multiprocessor Secure Boot under Hardware Supply-chain Attacks](https://silentzero.ooo/wiki/sources/2022-zhang-pa-boot-formally.html.md)
- [Raspberry Pi documentation: boot](https://silentzero.ooo/wiki/sources/nd-raspberrypi-boot.html.md)
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [Thunderclap](https://silentzero.ooo/wiki/sources/2019-markettos-thunderclap-exploring-vulnerabilities.html.md)
- [Trusted Firmware-A: firmware design](https://silentzero.ooo/wiki/sources/nd-tfa-firmware-design.html.md)

## Related pages

- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)
- [IOMMU](https://silentzero.ooo/wiki/concepts/iommu.html.md)
- [OpenTitan](https://silentzero.ooo/wiki/systems/opentitan.html.md)
- [Trusted Firmware-A](https://silentzero.ooo/wiki/systems/tf-a.html.md)
- [CHERI is being standardised](https://silentzero.ooo/wiki/sources/2026-moore-cheri-is-being.html.md)
- [Nuvoton's OpenTitan chip](https://silentzero.ooo/wiki/sources/2025-cnx-nuvoton-introduces-first.html.md)
- [The RISC-V Instruction Set Manual, Volume II](https://silentzero.ooo/wiki/sources/2024-riscv-privileged-isa-manual.html.md)
