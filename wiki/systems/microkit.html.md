# Microkit

> The build system for static seL4 systems: protection domains, channels, budgets, one image.

System · LLM reviewed · updated 2026-11-03 · 4 sources · https://silentzero.ooo/wiki/systems/microkit.html

A small operating system on [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md) for systems whose structure is fixed at build time. One XML description declares the protection domains, memory regions, channels and interrupts, and the Microkit tool turns it into a single bootable image on Arm and RISC-V ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)). [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md) is built with it ([Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md)).

## State, November 2026

Version 2.4.0, dated 30 October on the releases page (year inferred), on seL4 17.0.0. It closed two authority leaks: a server could send capabilities over a reply, and a child domain received its parent's fault endpoint, so that in 2.3.1 it could send its parent fake faults and in 2.3.0 and earlier it could receive and consume the parent's faults ([Microkit 2.4.0 release notes](https://silentzero.ooo/wiki/sources/2026-microkit-release-2-4-0.html.md)). The manual read for this page describes version 2.3.0 ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)). It always uses seL4's MCS configuration; multicore configurations exist beside the single-core default; boards include the Raspberry Pi 4B and CVA6 on a Genesys2 FPGA board ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)). The manual calls Microkit "in principle, amenable to formal analysis" of safety and security, leaves such analysis "beyond the initial scope", and claims no verification of its tool, loader or initialiser; the tool can export each protection domain's capabilities in the Viper language for verification ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)).

## The model in brief

- Protection domains are single-threaded event handlers with entry points for initialisation, notifications, protected procedure calls and faults of children; at most 63 per system.
- Channels connect exactly two protection domains. Memory regions can be shared, and the description can hand one domain capabilities to another's thread or address space; every path is declared in the description.
- Protected procedures go only to strictly higher priority, along an acyclic call graph, and must finish in bounded time, which is not enforced.
- Each domain has priority, budget and period, or runs passive on the scheduling context of whoever calls or notifies it. See [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md).
- There are no timers or sleep calls; activity starts from interrupts.
- On Arm and RISC-V the tool checks at build time that the generated specification can be set up on the board.

All from [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md).

## Licence and code

Not yet covered by the wiki's sources.

## Open questions

- How IOMMU-backed IO address spaces work on Arm and RISC-V; the manual describes them in general terms and states the mapping explicitly only for x86.
- What it would take to prove that a system description and its generated capDL specification enforce the intended authority, as CAmkES did for its descriptions ([Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md), §5.2).

## Sources

- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)
- [Microkit 2.4.0 release notes](https://silentzero.ooo/wiki/sources/2026-microkit-release-2-4-0.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md)

## Related pages

- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md)
- [The static system](https://silentzero.ooo/wiki/design/static-system.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md)
- [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md)
- [seL4 Foundation: Development roadmap](https://silentzero.ooo/wiki/sources/nd-sel4-sel4-roadmap.html.md)
