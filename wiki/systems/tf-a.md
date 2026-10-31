---
type: system
status: reviewed
sources: [nd-tfa-firmware-design, nd-sel4-microkit-user-manual]
short: Arm's reference firmware; its BL31 stays at EL3
updated: 2026-10-30
---

# Trusted Firmware-A

Arm's reference firmware for boot and for the runtime at EL3. On AArch64 its cold boot runs BL1 from trusted ROM, BL2, then BL31, the runtime firmware at EL3, an optional secure-world payload BL32 and finally BL33, the normal-world loader such as U-Boot or UEFI ([[nd-tfa-firmware-design]]).

## State, October 2026

Version 2.15.0. BL31 runs at EL3 in trusted SRAM and serves runtime services, among them PSCI for power management, through secure monitor calls ([[nd-tfa-firmware-design]]). An optional trusted OS (BL32) can run in the secure world beside the normal-world kernel ([[nd-tfa-firmware-design]]). Microkit warns that when the kernel makes a secure monitor call it cannot preempt the monitor, so its WCET properties are no longer guaranteed ([[nd-sel4-microkit-user-manual]]); on TF-A platforms that monitor is BL31, in our reading.

## Licence and code

Not yet covered by the wiki's sources.

## Open questions

- How small BL31 can be kept on a zOS board, and which of its services zOS needs. See [[root-of-trust]].
