---
type: source
id: 2026-trustworthy-lionsos
status: reviewed
read: full
kind: report
sources: [2026-trustworthy-lionsos]
updated: 2026-10-29
---

# Trustworthy Systems: LionsOS

The introduction page of LionsOS, for version 0.4.0, read on 29 October 2026. [Page](https://lionsos.org/). Only the introduction was read; the site's status, roadmap and example pages are not part of this source.

## What it shows

- **What it is.** An operating system on [[sel4]], developed by the Trustworthy Systems group at UNSW Sydney, "with the goal of making the achievements of seL4 accessible". It is not a conventional OS but a set of composable components for building task-specific systems, joined with the Microkit tool.
- **State.** "Currently undergoing active research and development." Verification of the device drivers and device-class components is under way and "not yet complete". The base device classes (network, block, serial, I²C and others) are expected to be mostly stable; newer ones are more in flux.
- **Principles** (in brief; the full set is in the sDDF design document):
  - components connected by lock-free queues with a model-checked signalling mechanism;
  - each component does one thing as far as practical; a driver only converts between a hardware interface and queues;
  - *virtualisers* handle multiplexing and the translation between virtual and IO addresses for drivers;
  - information is shared only where necessary, through the queues or published information pages.
- **Static, with one exception.** The system does not adapt to changing hardware and does not load components at run time. It can swap components of the same type at run time, to change a policy or to reboot a virtual machine with a new Linux kernel.

## How

A project page. It cites no measurements and points to the sDDF design document and the project's own pages.

## Limits

The page says itself that verification is not complete and that many more components are needed.

A careful reader adds: the run-time swap is named but not described here. Whether a swapped-in component was already in the image is not said; what the swap allows, and who may trigger it, needs the sDDF design document or Heiser et al. 2025, which the wiki does not cover yet.

## Against the wiki

- [[2026-heiser-mcs-safety-os]]: **confirms** the design the slides present (static architecture, single-purpose components, lock-free queues). The slides' note "static architecture ≠ static code" sits beside a diagram of replaceable components and does not say whether replacement happens at run time.
- [[lionsos]]: created with this source.

## For zOS

- [[static-system]], [[drivers]]: the paper says LionsOS already composes seL4, Microkit and user-mode drivers into a static, modular system and that zOS should build on it (Section 5). The page confirms the composition and its static character, and that verification of the drivers is under way and not complete.
- Our reading: the swap reboots a Linux VM or replaces a policy component. The VM is the driver island, outside the paper's core; whether a trusted policy component may be swapped is open. See [[static-system]].
