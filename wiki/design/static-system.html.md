# The static system

> One description, one image: what Microkit checks, what is not proved, and the run-time swap in LionsOS, the kernel underneath.

Design · LLM reviewed · updated 2026-11-03 · 6 sources · https://silentzero.ooo/wiki/design/static-system.html

The layer between the kernel and the components. In Silent Zero one description declares which isolated programs exist, which of them may talk, and what memory they share; [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md) builds the bootable image from it, and "nothing is loaded into the core at run time" (paper, Section 3).

## What it must do

- Turn the description into exactly the capabilities it declares, and no others.
- Fix sizes and rights at build time, so the system can be checked, scheduled and audited before it runs.
- Give each component a budget and a priority that keep the control loops on time. See [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md).

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| One description, one bootable image (Arm, RISC-V); all paths between components (channels, shared memory regions, extra capabilities) fixed in it | implemented (manual for Microkit 2.3.0; current release 2.4.0) | documentation | [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md), [Microkit 2.4.0 release notes](https://silentzero.ooo/wiki/sources/2026-microkit-release-2-4-0.html.md) |
| The generated capDL specification can be set up on the board (memory, frames) | checked at build time on Arm and RISC-V | tool check, not proof | [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md) |
| The generated capabilities match the description | not proved for Microkit; Viper export of each component's capabilities exists | none yet | [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md) |
| The same, for CAmkES | proved for the capDL refinement and the RPC glue; initialiser proved against a model | proof (2018) | [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md) |
| Protected procedures finish in bounded time | required, not enforced | assumed | [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md) |
| The kernel under it | always the MCS configuration; proved on RISC-V, not on the Raspberry Pi 4 or other Arm boards | see [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md) | [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md), [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) |
| A static OS built this way | LionsOS 0.4.0, under development | system | [Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md) |

## The paper and its sources

- The paper's description of the static system (Section 3) matches [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md).
- LionsOS loads no components at run time, but can swap a component for one of the same type, to change a policy or to reboot a virtual machine with a new Linux kernel ([Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md)). Our reading: the VM case concerns the driver island, which the paper keeps outside the trusted base, so it does not conflict with "nothing is loaded into the core". Microkit's restart of a child runs code already in the image. What remains open is whether a policy component inside the trusted base may be swapped at run time, and who may trigger it; the paper's Section 5 already rejects services that agents replace at run time.

- Microkit 2.4.0 (30 October, year inferred) fixed two leaks in the authority the layer hands out: reply capabilities no longer carry grant-reply permission, and a child no longer receives its parent's fault endpoint. In 2.3.1 a child could send its parent fake faults; in 2.3.0 and earlier it could receive and consume the parent's faults ([Microkit 2.4.0 release notes](https://silentzero.ooo/wiki/sources/2026-microkit-release-2-4-0.html.md)). Our reading: the authority a description declares was not, until then, all the authority a component held, which is why the generated-capabilities row above matters.

## Open

- HACMS proved for CAmkES that the generated capDL matches the architecture ([Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md), §5.2). Nothing comparable exists for Microkit in the sources so far.
- If no component holds the right to destroy kernel objects after boot, the kernel's worst case drops ([Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)). Our reading: a Microkit system creates its objects at boot through the capDL initialiser, which suggests it can be set up that way; no source confirms it.
- Microkit describes IO address spaces backed by an IOMMU or SMMU in general terms and states the mapping explicitly only for x86; see [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md).
- Microkit's domain scheduler, which separates groups of components on a fixed schedule, is supported only on single-core configurations ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)).

## Sources

- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)
- [Microkit 2.4.0 release notes](https://silentzero.ooo/wiki/sources/2026-microkit-release-2-4-0.html.md)
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md)
- [Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md)

## Related pages

- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md)
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md)
- [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md)
