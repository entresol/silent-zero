---
type: system
status: reviewed
sources: [2026-hubbard-agentos-operating-system]
short: seL4-based I/O platform for agents, in prototype
updated: 2026-11-01
---

# agentOS

An open-source operating system project on [[sel4]] by Jordan Hubbard. It owns devices in user mode through driver and virtualiser domains, runs Linux and FreeBSD as virtio guests (FreeBSD without a guest-proven row), and means native agents to be untrusted clients ([[2026-hubbard-agentos-operating-system]]).

## State, October 2026

The README's status table puts virtio network, block and console under QEMU on AArch64 at "guest-proven", meaning an automated test saw real I/O. On x86-64 only the root task boots. The agent-facing services are not in the booted image ([[2026-hubbard-agentos-operating-system]]).

## Licence and code

BSD 2-Clause; the repository is github.com/jordanhubbard/agentos, with libvmm vendored under its own licences ([[2026-hubbard-agentos-operating-system]]).

## Related

[[cohesix]], [[lionsos]], [[microkit]].

## Open questions

- Whether the kernel build is a verified configuration, and whether MCS.
- Which release is current: the README says v0.3.x, the releases page v0.6.0.
- Whether any real-time aim exists.
