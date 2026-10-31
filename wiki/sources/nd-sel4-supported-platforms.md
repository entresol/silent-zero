---
type: source
id: nd-sel4-supported-platforms
status: reviewed
read: partial
kind: report
sources: [nd-sel4-supported-platforms]
updated: 2026-10-31
---

# seL4 Foundation: Supported platforms

The seL4 documentation's list of supported platforms, with its pages for the HiFive Unleashed and the HiFive Premier P550, undated, read on 31 October 2026. [List](https://docs.sel4.systems/Hardware/), [HiFive Unleashed](https://docs.sel4.systems/Hardware/hifive.html), [HiFive Premier P550](https://docs.sel4.systems/Hardware/hifive-p550.html). Read in part: the introduction, the RISC-V table, the Raspberry Pi rows of the Arm table, and the two board pages.

## What it shows

- **The list.** For each board it gives system-on-chip and cores, for Arm boards virtualisation and SMMU support, for RISC-V boards the ISA, and for all proofs and the proof configuration. The legend distinguishes four verification states: unverified, ongoing, "FC" (functional correctness complete) and verified (all proofs, including integrity and information flow).
- **RISC-V boards.** Nine entries link the proof configuration `RISCV64`: Ariane, Banana Pi BPI-F3, Cheshire, HiFive Premier P550, HiFive Unleashed, Microchip PolarFire Icicle Kit, Pine64 Star64, Rocketchip, and Rocketchip on a ZCU102. QEMU's `virt` machine and Spike link none.
- **HiFive Unleashed.** Freedom U540, cores U54-MC and E51, platform name `hifive`, contributed by Data61, maintained by the seL4 Foundation.
- **HiFive Premier P550.** ESWIN EIC7700X, P550 cores, platform name `hifive-p550`, contributed by the community, maintained by the seL4 Foundation. The board boots from SPI flash: firmware, then OpenSBI, then U-Boot, from which an seL4 image is loaded with a device tree.
- **Raspberry Pi 4B and 5B** (BCM2711, BCM2712) link the proof configuration `AARCH64`.

## How

Reference pages of the seL4 documentation.

## Limits

A careful reader adds: in the copy read here, the "Proofs" column of the RISC-V and Arm rows that link a proof configuration shows the same check-mark icon throughout, so the four states of the legend cannot be told apart there. Whether the live page draws the states differently in some browsers was not checked. Which state a board has is better taken from the release notes ([[2026-sel4-release-17]]).

## Against the wiki

- [[nd-sel4-verified-configurations]]: **confirms** the platform names and adds the boot chain of the P550.
- [[sifive-hifive]]: created with this source.

## For zOS

- [[bootloader]]: on the P550 the chain before seL4 is firmware, OpenSBI and U-Boot. The zOS loader would take U-Boot's place or be started by it.
