---
type: source
id: nd-sel4-verified-configurations
status: reviewed
read: full
kind: report
sources: [nd-sel4-verified-configurations]
updated: 2026-10-29
---

# seL4 Foundation: Verified Configurations

A documentation page of the seL4 Foundation, undated, read as it stood on 23 October 2026. [Page](https://docs.sel4.systems/projects/sel4/verified-configurations.html).

## What it shows

The page lists which combinations of architecture, platform and kernel configuration have verified properties, and which properties.

| Architecture | Kernel mode, FPU | Verified properties |
| --- | --- | --- |
| AArch32 (ARMv7-A) | EL1, no FPU | C-level functional correctness including fast path; integrity and availability; confidentiality; binary correctness for the C functions with C-level verification; model-level correctness of the capDL system initialiser |
| AArch32 with hypervisor | EL2, no FPU | C-level functional correctness including fast path |
| AArch64 (ARMv8-A) | EL2, FPU | C-level functional correctness including fast path; integrity and availability; confidentiality |
| RISC-V 64-bit | no FPU, no hypervisor | C-level functional correctness without fast path; integrity and availability; confidentiality |
| x86-64 | FPU, no VT-x | C-level functional correctness without fast path |

- No verified configuration covers address translation for devices (SMMU or IOMMU), debug, profiling and printing interfaces, and kernel startup at boot.
- **MCS.** The page calls the configurations with MCS in their name the "ongoing MCS verification" and says the proofs for the Arm MCS configurations are in progress.
- **Platforms.** Among the AArch64 platforms listed are the Raspberry Pi 4B and 5B; among the RISC-V platforms, Ariane (another name for [[cva6]]), Cheshire and the HiFive Premier P550. The configuration files include `AARCH64_bcm2711_verified.cmake` and `RISCV64_MCS_verified.cmake`.
- **Proofs.** The proofs are in Isabelle/HOL in the `seL4/l4v` repository.

## How

A reference page that points to the configuration files in the seL4 sources and to the proofs. It gives no dates for the properties it lists.

## Limits

A careful reader adds:

- **The page is only partly updated on MCS.** Its list of unverified features names only the Arm MCS proofs as in progress, but its RISC-V section still calls the MCS configurations those "for the ongoing MCS verification". The seL4 Foundation announced on 29 June 2026 that the functional-correctness proof for MCS on RISC-V is complete ([[2026-sel4-functional-correctness-proof]]); the RISC-V section had not caught up by 23 October 2026.
- **Binary correctness is listed for AArch32 only.** For AArch64 and RISC-V the page lists C-level properties. Whether binary verification exists elsewhere for these architectures is not said here.
- **Platform support is the configuration, not the whole board.** A board on the list is supported by a verified kernel configuration. The IOMMU and boot code on that board stay outside the proof, as above.

## Against the wiki

- [[sel4]]: **extends** it with which properties hold where.
- [[2026-sel4-functional-correctness-proof]]: the news item is newer on MCS; this page has not been updated.

## For zOS

- [[kernel]]: the paper cites this page for the gaps (kernel boot and IOMMU outside the proof). The page confirms both.
- Our reading: for a first zOS on RISC-V, the verified properties are C-level functional correctness, integrity and confidentiality, without a fast path and without floating point in the kernel configuration. The page does not say whether the MCS proof extends to integrity and confidentiality.
- The pib robot runs on a Raspberry Pi (paper, Section 7). The Pi 4B appears here as a verified AArch64 platform, without MCS. Whether the Pi 4's system has an IOMMU is not answered here.
