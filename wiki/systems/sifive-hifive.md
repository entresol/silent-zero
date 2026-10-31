---
type: system
status: reviewed
sources: [nd-sifive-risc-v-history, nd-sifive-hifive-unleashed, 2024-sifive-hifive-premier-p550, nd-sel4-supported-platforms, 2026-sel4-release-17]
short: RISC-V core designer and its development boards
updated: 2026-10-31
---

# SiFive and the HiFive boards

SiFive is a company founded in 2015 by Krste Asanović, Andrew Waterman and Yunsup Lee, who started RISC-V in Berkeley. It designs RISC-V processor cores and offers them as "processor core IP" ([[nd-sifive-risc-v-history]]). HiFive is its line of development boards, the first of which, the HiFive1, came out in 2016 by SiFive's account ([[nd-sifive-risc-v-history]]). Two of them matter to zOS: the board seL4's MCS proof is for, and a newer board SiFive announced for sale in 2024.

## The boards

| | HiFive Unleashed | HiFive Premier P550 |
| --- | --- | --- |
| SoC | SiFive Freedom U540 | Eswin EIC7700 (EIC7700X in seL4's list) |
| Cores | U54-MC cluster plus a monitor core | four P550, out-of-order |
| Memory | 8 GB DDR4 with ECC | 16 GB LPDDR5 |
| Sold | no, marked "Discontinued" by SiFive | announced 9 April 2024, through Arrow Electronics |
| seL4 platform | `hifive` | `hifive-p550` |
| seL4 proof (17.0.0) | C level; MCS C level | C level; no MCS proof |
| Boot chain before seL4 | in the project's video: OpenSBI, the zOS loader, seL4's ELF loader | firmware, OpenSBI, U-Boot |

Sources: [[nd-sifive-hifive-unleashed]], [[2024-sifive-hifive-premier-p550]], [[nd-sel4-supported-platforms]], [[2026-sel4-release-17]].

## State, October 2026

The project's boot video runs on QEMU's model of the HiFive Unleashed, with seL4 built from the preset for `hifive` ([[bootloader]]). Our reading: that board was chosen because it is the platform of seL4's proven MCS configuration. Since seL4 17.0.0, the P550 has a C-level proof without MCS ([[2026-sel4-release-17]]). Our reading: no board on sale today runs a proven MCS kernel; the one board with that proof is marked discontinued.

## Licence and code

The boards are commercial products, and SiFive offers its cores as IP ([[nd-sifive-risc-v-history]]). The ISA they implement is open ([[risc-v]]).

## Open questions

- Whether the P550 can show a picture before the kernel runs. The press release lists a GPU and MIPI DSI for the SoC and names no display connector on the board ([[2024-sifive-hifive-premier-p550]]).
- When seL4's MCS proof extends to further RISC-V platforms. Neither release notes nor platform list give a date.
