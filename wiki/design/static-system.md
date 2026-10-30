---
type: design
status: reviewed
sources: [nd-sel4-microkit-user-manual, 2026-trustworthy-lionsos, 2018-klein-formally-verified-software, 2026-trustworthy-guaranteeing-timeliness-mcs, nd-sel4-verified-configurations]
updated: 2026-10-29
---

# The static system

The layer between the kernel and the components. In zOS one description declares which isolated programs exist, which of them may talk, and what memory they share; [[microkit]] builds the bootable image from it, and "nothing is loaded into the core at run time" (paper, Section 3).

## What it must do

- Turn the description into exactly the capabilities it declares, and no others.
- Fix sizes and rights at build time, so the system can be checked, scheduled and audited before it runs.
- Give each component a budget and a priority that keep the control loops on time. See [[mixed-criticality]].

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| One description, one bootable image (Arm, RISC-V); all paths between components (channels, shared memory regions, extra capabilities) fixed in it | implemented (Microkit 2.3.0) | documentation | [[nd-sel4-microkit-user-manual]] |
| The generated capDL specification can be set up on the board (memory, frames) | checked at build time on Arm and RISC-V | tool check, not proof | [[nd-sel4-microkit-user-manual]] |
| The generated capabilities match the description | not proved for Microkit; Viper export of each component's capabilities exists | none yet | [[nd-sel4-microkit-user-manual]] |
| The same, for CAmkES | proved for the capDL refinement and the RPC glue; initialiser proved against a model | proof (2018) | [[2018-klein-formally-verified-software]] |
| Protected procedures finish in bounded time | required, not enforced | assumed | [[nd-sel4-microkit-user-manual]] |
| The kernel under it | always the MCS configuration; proved on RISC-V, not on the Raspberry Pi 4 or other Arm boards | see [[kernel]] | [[nd-sel4-microkit-user-manual]], [[nd-sel4-verified-configurations]] |
| A static OS built this way | LionsOS 0.4.0, under development | system | [[2026-trustworthy-lionsos]] |

## The paper and its sources

- The paper's description of the static system (Section 3) matches [[nd-sel4-microkit-user-manual]].
- LionsOS loads no components at run time, but can swap a component for one of the same type, to change a policy or to reboot a virtual machine with a new Linux kernel ([[2026-trustworthy-lionsos]]). Our reading: the VM case concerns the driver island, which the paper keeps outside the trusted base, so it does not conflict with "nothing is loaded into the core". Microkit's restart of a child runs code already in the image. What remains open is whether a policy component inside the trusted base may be swapped at run time, and who may trigger it; the paper's Section 5 already rejects services that agents replace at run time.

## Open

- HACMS proved for CAmkES that the generated capDL matches the architecture ([[2018-klein-formally-verified-software]], §5.2). Nothing comparable exists for Microkit in the sources so far.
- If no component holds the right to destroy kernel objects after boot, the kernel's worst case drops ([[2026-trustworthy-guaranteeing-timeliness-mcs]]). Our reading: a Microkit system creates its objects at boot through the capDL initialiser, which suggests it can be set up that way; no source confirms it.
- Microkit describes IO address spaces backed by an IOMMU or SMMU in general terms and states the mapping explicitly only for x86; see [[drivers]].
- Microkit's domain scheduler, which separates groups of components on a fixed schedule, is supported only on single-core configurations ([[nd-sel4-microkit-user-manual]]).
