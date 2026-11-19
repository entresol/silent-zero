# Trusted Firmware-A

> Arm’s reference firmware; BL31 stays resident at EL3 below the kernel.

System · LLM reviewed · updated 2026-10-30 · 2 sources · https://silentzero.ooo/wiki/systems/tf-a.html

Arm's reference firmware for boot and for the runtime at EL3. On AArch64 its cold boot runs BL1 from trusted ROM, BL2, then BL31, the runtime firmware at EL3, an optional secure-world payload BL32 and finally BL33, the normal-world loader such as U-Boot or UEFI ([Trusted Firmware-A: firmware design](https://silentzero.ooo/wiki/sources/nd-tfa-firmware-design.html.md)).

## State, October 2026

Version 2.15.0. BL31 runs at EL3 in trusted SRAM and serves runtime services, among them PSCI for power management, through secure monitor calls ([Trusted Firmware-A: firmware design](https://silentzero.ooo/wiki/sources/nd-tfa-firmware-design.html.md)). An optional trusted OS (BL32) can run in the secure world beside the normal-world kernel ([Trusted Firmware-A: firmware design](https://silentzero.ooo/wiki/sources/nd-tfa-firmware-design.html.md)). Microkit warns that when the kernel makes a secure monitor call it cannot preempt the monitor, so its WCET properties are no longer guaranteed ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)); on TF-A platforms that monitor is BL31, in our reading.

## Licence and code

Not yet covered by the wiki's sources.

## Open questions

- How small BL31 can be kept on a Silent Zero board, and which of its services Silent Zero needs. See [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md).

## Sources

- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [Trusted Firmware-A: firmware design](https://silentzero.ooo/wiki/sources/nd-tfa-firmware-design.html.md)

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
