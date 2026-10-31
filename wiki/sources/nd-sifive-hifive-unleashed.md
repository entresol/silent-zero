---
type: source
id: nd-sifive-hifive-unleashed
status: reviewed
read: full
kind: report
sources: [nd-sifive-hifive-unleashed]
updated: 2026-10-31
---

# SiFive: HiFive Unleashed

SiFive's product page for the HiFive Unleashed board, undated, read on 31 October 2026. [Page](https://www.sifive.com/boards/hifive-unleashed).

## What it shows

- **Status.** The page title and header mark the board "Discontinued".
- **The chip.** The Freedom U540 (FU540) SoC, which SiFive calls "the world's first Linux-capable, multi-core, RISC-V processor": a U54-MC cluster of application cores plus "a 5th core (monitor core)", which the page says "is also available for real time applications". The page names an S51 (RV64IMAC) for auxiliary functions; seL4's platform page lists the cores as U54-MC and E51 ([[nd-sel4-supported-platforms]]).
- **The board.** 8 GB DDR4 with ECC, 32 MB quad SPI flash, microSD, Gigabit Ethernet, an FMC connector for expansion.
- **Privilege modes.** "3 execution modes (Machine, Supervisor, User)" and Sv39 virtual memory.
- **Expansion.** An expansion board with a PolarFire FPGA as PCI Express root complex turns it into "a RISC-V Linux PC".
- **Link onward.** The page ends with a link to the HiFive Premier P550 ([[2024-sifive-hifive-premier-p550]]); it does not call it a successor.

## How

A vendor's product page with feature list and links to manuals, schematics and firmware.

## Limits

A vendor page. It gives no year; the year 2018 for the board is not stated here. The schematics, manuals and firmware it links to were not read.

## Against the wiki

- [[sifive-hifive]]: created with this source.

## For zOS

- [[kernel]], [[bootloader]]: this is the board of seL4's platform `hifive`, the only platform with a proof of the MCS kernel ([[2026-sel4-release-17]]), and the board QEMU's `sifive_u` machine stands for, according to the project's [loader README](https://github.com/entresol/silent-zero/tree/main/loader). OpenSBI reports "SiFive HiFive Unleashed A00" as platform name in the project's boot recording ([serial log](https://github.com/entresol/silent-zero/blob/main/loader/recording/serial.log)). SiFive no longer sells it.
