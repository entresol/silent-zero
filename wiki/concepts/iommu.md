---
type: concept
status: reviewed
sources: [2019-markettos-thunderclap-exploring-vulnerabilities, nd-sel4-verified-configurations, nd-sel4-microkit-user-manual]
short: Memory protection against DMA devices
updated: 2026-11-02
---

# IOMMU

A memory management unit for devices. Devices such as network cards, storage controllers and GPUs read and write memory directly (DMA). An IOMMU sits between them and main memory, translates the addresses a device uses and applies access rights, much as the processor's MMU does for processes. Intel calls it VT-d, AMD AMD-Vi, Arm the System MMU (SMMU) ([[2019-markettos-thunderclap-exploring-vulnerabilities]], Section II-D).

## State, as published

- Switching it on is not enough. Thunderclap showed attacks that work although the IOMMU is on: mappings are page-sized, so a buffer drags in its neighbours; mappings stay open too long; and a device can claim a translation feature that skips the IOMMU ([[2019-markettos-thunderclap-exploring-vulnerabilities]]).
- In 2019 the IOMMU was off by default on most systems the authors tested.
- In seL4, no verified kernel configuration covers address translation for devices ([[nd-sel4-verified-configurations]]). Microkit describes IO address spaces in general terms and states the mapping explicitly only for x86 ([[nd-sel4-microkit-user-manual]]).

## Related

[[drivers]], [[root-of-trust]], [[sel4]].

## Open questions

- Which of the Thunderclap attack classes apply to a system with user-mode drivers and page-aligned buffers, as in [[lionsos]]; no source in the wiki says.
- Whether the Raspberry Pi 4 has an IOMMU at all (see [[drivers]]).
