---
type: design
status: reviewed
sources: [2026-google-opentitan-shipping-production, nd-caliptra, nd-coreboot-architecture, nd-coreboot-vboot, nd-coreboot-measured-boot, nd-tfa-firmware-design, nd-opensbi, nd-raspberrypi-boot, 2021-tao-dice-formally-verified, 2022-zhang-pa-boot-formally, nd-sel4-verified-configurations, nd-sel4-microkit-user-manual]
updated: 2026-10-30
---

# Root of trust and firmware

The bottom of zOS: a root of trust that measures the first code to run, together with the hardware's memory management and IOMMU. Firmware runs here with more privilege than the kernel; on RISC-V, Microkit relies on SBI firmware such as OpenSBI in machine mode, and on Arm trusted firmware at the highest exception level plays that role. "This layer belongs to the trusted base and is *assumed*." (paper, Section 3).

## What it must do

- Measure the first code to run (paper, Section 3); checking the signed image is the [[bootloader]]'s job.
- Report what it measured, so the bootloader can show it.
- Our reading: let the owner, not only the vendor, control what is trusted.

## What runs below or before the kernel

| Platform | Below the kernel at run time | Where trust starts | Source |
| --- | --- | --- | --- |
| Arm | TF-A's BL31 at EL3, serving secure monitor calls including power management; optionally a trusted OS (BL32) in the secure world | on Arm's reference platforms BL1 in trusted ROM; vendor boards may use their own ROM instead of BL1 and BL2 | [[nd-tfa-firmware-design]] |
| RISC-V | OpenSBI in machine mode | not stated in the sources | [[nd-opensbi]], [[nd-sel4-microkit-user-manual]] |
| PC with coreboot | firmware code such as SMM, locked by ramstage | the read-only part of the SPI flash; Intel Boot Guard or AMD Hardware Validated Boot root the verification of the boot block, the measurement root stays in software | [[nd-coreboot-architecture]], [[nd-coreboot-vboot]], [[nd-coreboot-measured-boot]] |
| Raspberry Pi 4 and 5 | not covered by the sources | closed ROM and EEPROM bootloader; on non-BCM2712 devices such as the Pi 4, a secure-boot key hash in OTP; on the Pi 5 not public in the sources | [[nd-raspberrypi-boot]] |

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| Open-source silicon root of trust in production | shipping in Chromebooks since March 2026 | vendor announcement | [[2026-google-opentitan-shipping-production]] |
| Post-quantum secure boot (shipping part); ownership transfer (named in the announcement) | announced | vendor announcement | [[2026-google-opentitan-shipping-production]] |
| Design quality of OpenTitan | over 90 % coverage, 40,000 nightly tests | vendor statement on design verification, not on the chip | [[2026-google-opentitan-shipping-production]] |
| Root of trust for measurement inside data-centre SoCs | Caliptra, open IP and firmware under Apache 2.0 | project documentation | [[nd-caliptra]] |
| Verify-and-measure boot without a TPM (DICE) | verified at the level of generated C on a microcontroller | proof | [[2021-tao-dice-formally-verified]] |
| Processors themselves as a supply-chain risk to secure boot | a protocol for multi-chip systems, proved at model level, needs changes to the CPU's boot ROM | proof of a model | [[2022-zhang-pa-boot-formally]] |
| Bootloader replaceable from the SD card on the Pi | `recovery.bin` and self-update, unless OTP settings, `FREEZE_VERSION` or write protection prevent it | documentation | [[nd-raspberrypi-boot]] |
| Kernel boot and IOMMU in seL4's proofs | outside every verified configuration | assumed | [[nd-sel4-verified-configurations]] |
| Microkit boot chain: loader, kernel, capDL initialiser | implemented; the loader is never executed again | documentation | [[nd-sel4-microkit-user-manual]] |

## The paper and its sources

- In brief, Section 3 and Section 5 say OpenTitan has shipped in production Chromebooks since March 2026. Confirmed by [[2026-google-opentitan-shipping-production]]. The paper classes this layer as *assumed*, and the sources do not change that.
- Section 3's roles for OpenSBI and trusted firmware are confirmed by [[nd-sel4-microkit-user-manual]], [[nd-opensbi]] and [[nd-tfa-firmware-design]].
- Section 6 says firmware below the kernel "has full access to memory and cannot be confined by any kernel". The sources confirm that this firmware runs at higher privilege; they do not discuss confining it.

## Open

- No source so far names a board that carries OpenTitan and runs seL4.
- What the root of trust measures, and how that reaches the zOS bootloader's first screen, is open on every platform. On Arm and RISC-V the Microkit loader expects an earlier bootloader such as U-Boot ([[nd-sel4-microkit-user-manual]]); see [[bootloader]].
- On the Pi, which firmware stays resident below the kernel, and how secure boot is enabled and what it verifies, is not covered by the sources.
- Which parts of the firmware below the kernel a zOS hardware profile accepts: on Arm, how much of BL31 and whether a trusted OS; on a PC, the vendor's closed code. Intel ME, AMD PSP and open alternatives are not yet covered here.
