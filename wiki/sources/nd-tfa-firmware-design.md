---
type: source
id: nd-tfa-firmware-design
status: reviewed
read: partial
kind: report
sources: [nd-tfa-firmware-design]
updated: 2026-10-30
---

# Trusted Firmware-A: firmware design

The firmware-design chapter of the Trusted Firmware-A documentation, version 2.15.0, read on 30 October 2026. [Page](https://trustedfirmware-a.readthedocs.io/en/latest/design/firmware-design.html). The wiki has read the cold-boot path (§5.4.1), the runtime-services framework (§5.4.2) and the PSCI summary (§5.4.4); the other sections, on exception handling, memory layout, image packaging and architecture extensions, were skimmed. Image authentication is described in a separate document not covered here.

## What it shows

- **What TF-A is.** It implements part of Arm's Trusted Board Boot Requirements for Arm reference platforms, from power-on to the hand-off to firmware in the normal world, and PSCI, the interface for power management such as booting secondary CPUs, as a runtime service.
- **The cold boot on AArch64** has five stages: BL1 (trusted ROM, at EL3), BL2 (trusted boot firmware, at Secure-EL1), BL31 (EL3 runtime software), an optional BL32 (a payload in the secure world) and BL33 (non-trusted firmware such as UEFI or U-Boot) (§5.4.1).
- **BL31 stays.** BL31 runs at EL3 in trusted SRAM, replaces BL1's exception vectors with its own and handles SMC calls, "the only mechanism to access the runtime services implemented by BL31 (PSCI for example)" (§5.4.1.5). It hands over to BL33 at the highest available normal-world level, EL2 if present (§5.4.1.5.5).
- **Runtime services.** Software below EL3, in either security state, requests services through SMC calls following the SMC Calling Convention; the framework lets services from different providers be integrated into product firmware (§5.4.2).
- **PSCI.** All mandatory functions of PSCI v1.1, v1.0 and v0.2 are implemented in the generic code; the level of support depends on the platform port (§5.4.4).
- **Replaceable early stages.** Platforms with their own trusted boot firmware can use TF-A's BL31 alone, through a documented interface; BL2 can also run at EL3 when a vendor boot ROM expects that (§5.4.1.4, §5.4.1.6).

## How

Reference documentation for Arm's open firmware, mainly for Arm's development platforms (FVP, Juno).

## Limits

A careful reader adds:

- The design is described for Arm's reference platforms; what a given board runs at EL3 depends on its vendor's port.
- The document says how images are loaded, not how they are authenticated; that is in TF-A's trusted-board-boot document, not covered here.

## Against the wiki

- [[tf-a]]: created with this source.
- [[nd-sel4-microkit-user-manual]]: **consistent** with its warning that when the kernel makes a secure monitor call it cannot preempt the monitor. Our reading: on TF-A platforms, BL31 is that monitor.

## For zOS

- [[root-of-trust]]: the paper says firmware runs "with more privilege than the kernel" and that on Arm trusted firmware at the highest exception level plays the role OpenSBI plays on RISC-V (Section 3). Confirmed: BL31 runs at EL3 in trusted SRAM and serves SMC calls, including power management; that it stays for the machine's life is our reading. An optional trusted OS (BL32) can also run in the secure world beside the kernel, with BL31 switching worlds on SMCs (§5.4.2, §5.4.6).
- Our reading: for zOS on Arm, how much of BL31 a board needs, and whether any component may make SMC calls, belongs in the hardware profile the paper demands.
