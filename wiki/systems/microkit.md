---
type: system
status: reviewed
sources: [nd-sel4-microkit-user-manual, 2026-trustworthy-lionsos, 2018-klein-formally-verified-software]
updated: 2026-10-29
---

# Microkit

A small operating system on [[sel4]] for systems whose structure is fixed at build time. One XML description declares the protection domains, memory regions, channels and interrupts, and the Microkit tool turns it into a single bootable image on Arm and RISC-V ([[nd-sel4-microkit-user-manual]]). [[lionsos]] is built with it ([[2026-trustworthy-lionsos]]).

## State, October 2026

Version 2.3.0. It always uses seL4's MCS configuration; multicore configurations exist beside the single-core default; boards include the Raspberry Pi 4B and CVA6 on a Genesys2 FPGA board ([[nd-sel4-microkit-user-manual]]). The manual calls Microkit "in principle, amenable to formal analysis" of safety and security, leaves such analysis "beyond the initial scope", and claims no verification of its tool, loader or initialiser; the tool can export each protection domain's capabilities in the Viper language for verification ([[nd-sel4-microkit-user-manual]]).

## The model in brief

- Protection domains are single-threaded event handlers with entry points for initialisation, notifications, protected procedure calls and faults of children; at most 63 per system.
- Channels connect exactly two protection domains. Memory regions can be shared, and the description can hand one domain capabilities to another's thread or address space; every path is declared in the description.
- Protected procedures go only to strictly higher priority, along an acyclic call graph, and must finish in bounded time, which is not enforced.
- Each domain has priority, budget and period, or runs passive on the scheduling context of whoever calls or notifies it. See [[mixed-criticality]].
- There are no timers or sleep calls; activity starts from interrupts.
- On Arm and RISC-V the tool checks at build time that the generated specification can be set up on the board.

All from [[nd-sel4-microkit-user-manual]].

## Licence and code

Not yet covered by the wiki's sources.

## Open questions

- How IOMMU-backed IO address spaces work on Arm and RISC-V; the manual describes them in general terms and states the mapping explicitly only for x86.
- What it would take to prove that a system description and its generated capDL specification enforce the intended authority, as CAmkES did for its descriptions ([[2018-klein-formally-verified-software]], §5.2).
