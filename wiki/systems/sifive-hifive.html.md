# SiFive and the HiFive boards

> SiFive and its boards: the discontinued HiFive Unleashed with seL4’s MCS proof, the HiFive Premier P550 one can buy.

System · LLM reviewed · updated 2026-10-31 · 5 sources · https://silentzero.ooo/wiki/systems/sifive-hifive.html

SiFive is a company founded in 2015 by Krste Asanović, Andrew Waterman and Yunsup Lee, who started RISC-V in Berkeley. It designs RISC-V processor cores and offers them as "processor core IP" ([SiFive: RISC-V History](https://silentzero.ooo/wiki/sources/nd-sifive-risc-v-history.html.md)). HiFive is its line of development boards, the first of which, the HiFive1, came out in 2016 by SiFive's account ([SiFive: RISC-V History](https://silentzero.ooo/wiki/sources/nd-sifive-risc-v-history.html.md)). Two of them matter to Silent Zero: the board seL4's MCS proof is for, and a newer board SiFive announced for sale in 2024.

## The boards

| | HiFive Unleashed | HiFive Premier P550 |
| --- | --- | --- |
| SoC | SiFive Freedom U540 | Eswin EIC7700 (EIC7700X in seL4's list) |
| Cores | U54-MC cluster plus a monitor core | four P550, out-of-order |
| Memory | 8 GB DDR4 with ECC | 16 GB LPDDR5 |
| Sold | no, marked "Discontinued" by SiFive | announced 9 April 2024, through Arrow Electronics |
| seL4 platform | `hifive` | `hifive-p550` |
| seL4 proof (17.0.0) | C level; MCS C level | C level; no MCS proof |
| Boot chain before seL4 | in the project's video: OpenSBI, the Silent Zero loader, seL4's ELF loader | firmware, OpenSBI, U-Boot |

Sources: [SiFive: HiFive Unleashed](https://silentzero.ooo/wiki/sources/nd-sifive-hifive-unleashed.html.md), [the HiFive Premier P550](https://silentzero.ooo/wiki/sources/2024-sifive-hifive-premier-p550.html.md), [seL4 Foundation: Supported platforms](https://silentzero.ooo/wiki/sources/nd-sel4-supported-platforms.html.md), [release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md).

## State, October 2026

The project's boot video runs on QEMU's model of the HiFive Unleashed, with seL4 built from the preset for `hifive` ([The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)). Our reading: that board was chosen because it is the platform of seL4's proven MCS configuration. Since seL4 17.0.0, the P550 has a C-level proof without MCS ([release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md)). Our reading: no board on sale today runs a proven MCS kernel; the one board with that proof is marked discontinued.

## Licence and code

The boards are commercial products, and SiFive offers its cores as IP ([SiFive: RISC-V History](https://silentzero.ooo/wiki/sources/nd-sifive-risc-v-history.html.md)). The ISA they implement is open ([RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md)).

## Open questions

- Whether the P550 can show a picture before the kernel runs. The press release lists a GPU and MIPI DSI for the SoC and names no display connector on the board ([the HiFive Premier P550](https://silentzero.ooo/wiki/sources/2024-sifive-hifive-premier-p550.html.md)).
- When seL4's MCS proof extends to further RISC-V platforms. Neither release notes nor platform list give a date.

## Sources

- [release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md)
- [seL4 Foundation: Supported platforms](https://silentzero.ooo/wiki/sources/nd-sel4-supported-platforms.html.md)
- [SiFive: HiFive Unleashed](https://silentzero.ooo/wiki/sources/nd-sifive-hifive-unleashed.html.md)
- [SiFive: RISC-V History](https://silentzero.ooo/wiki/sources/nd-sifive-risc-v-history.html.md)
- [the HiFive Premier P550](https://silentzero.ooo/wiki/sources/2024-sifive-hifive-premier-p550.html.md)

## Related pages

- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md)
- [Instruction Sets Should Be Free](https://silentzero.ooo/wiki/sources/2014-asanovic-instruction-sets-free.html.md)
