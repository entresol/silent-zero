# IOMMU

> The memory management unit for devices: what it limits, and the 2019 attacks that worked although it was on.

Concept · LLM reviewed · updated 2026-11-02 · 3 sources · https://silentzero.ooo/wiki/concepts/iommu.html

A memory management unit for devices. Devices such as network cards, storage controllers and GPUs read and write memory directly (DMA). An IOMMU sits between them and main memory, translates the addresses a device uses and applies access rights, much as the processor's MMU does for processes. Intel calls it VT-d, AMD AMD-Vi, Arm the System MMU (SMMU) ([Thunderclap](https://silentzero.ooo/wiki/sources/2019-markettos-thunderclap-exploring-vulnerabilities.html.md), Section II-D).

## State, as published

- Switching it on is not enough. Thunderclap showed attacks that work although the IOMMU is on: mappings are page-sized, so a buffer drags in its neighbours; mappings stay open too long; and a device can claim a translation feature that skips the IOMMU ([Thunderclap](https://silentzero.ooo/wiki/sources/2019-markettos-thunderclap-exploring-vulnerabilities.html.md)).
- In 2019 the IOMMU was off by default on most systems the authors tested.
- In seL4, no verified kernel configuration covers address translation for devices ([seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)). Microkit describes IO address spaces in general terms and states the mapping explicitly only for x86 ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)).

## Related

[Drivers](https://silentzero.ooo/wiki/design/drivers.html.md), [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md), [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md).

## Open questions

- Which of the Thunderclap attack classes apply to a system with user-mode drivers and page-aligned buffers, as in [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md); no source in the wiki says.
- Whether the Raspberry Pi 4 has an IOMMU at all (see [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md)).

## Sources

- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [Thunderclap](https://silentzero.ooo/wiki/sources/2019-markettos-thunderclap-exploring-vulnerabilities.html.md)

## Related pages

- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md)
- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [LeftoverLocals](https://silentzero.ooo/wiki/sources/2024-trail-leftoverlocals-listening-llm.html.md)
