# agentOS

> SeL4-based I/O platform for agents: device-owning domains, Linux and FreeBSD guests under QEMU; agent services not yet booted.

System · LLM reviewed · updated 2026-11-01 · 1 source · https://silentzero.ooo/wiki/systems/agentos.html

An open-source operating system project on [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md) by Jordan Hubbard. It owns devices in user mode through driver and virtualiser domains, runs Linux and FreeBSD as virtio guests (FreeBSD without a guest-proven row), and means native agents to be untrusted clients ([agentOS, an operating system for agents on seL4](https://silentzero.ooo/wiki/sources/2026-hubbard-agentos-operating-system.html.md)).

## State, October 2026

The README's status table puts virtio network, block and console under QEMU on AArch64 at "guest-proven", meaning an automated test saw real I/O. On x86-64 only the root task boots. The agent-facing services are not in the booted image ([agentOS, an operating system for agents on seL4](https://silentzero.ooo/wiki/sources/2026-hubbard-agentos-operating-system.html.md)).

## Licence and code

BSD 2-Clause; the repository is github.com/jordanhubbard/agentos, with libvmm vendored under its own licences ([agentOS, an operating system for agents on seL4](https://silentzero.ooo/wiki/sources/2026-hubbard-agentos-operating-system.html.md)).

## Related

[Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md), [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md), [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md).

## Open questions

- Whether the kernel build is a verified configuration, and whether MCS.
- Which release is current: the README says v0.3.x, the releases page v0.6.0.
- Whether any real-time aim exists.

## Sources

- [agentOS, an operating system for agents on seL4](https://silentzero.ooo/wiki/sources/2026-hubbard-agentos-operating-system.html.md)

## Related pages

- [Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md)
- [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md)
- [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md)
- [Microkit 2.4.0 release notes](https://silentzero.ooo/wiki/sources/2026-microkit-release-2-4-0.html.md)
