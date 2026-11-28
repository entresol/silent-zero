---
type: source
id: nd-oreboot
status: reviewed
read: full
kind: report
sources: [nd-oreboot]
updated: 2026-11-28
---

# oreboot: the README

The README of the oreboot repository, [github.com/oreboot/oreboot](https://github.com/oreboot/oreboot). Snapshot of 2 November 2026, undated. Read in full. It has no release history, dates or activity information (its boot log prints version strings), so the project's current state is not covered here.

## What it shows

- **What it is.** A downstream fork of coreboot, "coreboot without c", written mostly in Rust with assembly where needed. It currently plans to support only LinuxBoot payloads, and does not aim to become an operating system.
- **Targets.** The README lists demos for Arm and for a RISC-V HiFive Unleashed in QEMU, and a sample boot log on an Allwinner D1 board, which names a Sipeed Lichee RV Dock and a C906 manual and ends in a Linux kernel started through RustSBI. Earlier x86 and Arm approaches are documented separately, and three emulation targets (qemu-armv7, qemu-aarch64, qemu-q35) are parked for revival. Its build tree is per vendor and mainboard, as in coreboot.
- **Drivers.** The project keeps drivers few: loading code needs some (SPI flash, SD card, eMMC, USB, Ethernet, UART), in many cases only reading. It advises keeping firmware and operating system on separate storage.
- **Rules.** All code in Rust, none in C; GitHub for review and CI for now, with flexibility promised; GPL, version 2 or "or any later" per file, other GPL-compatible licences for derived parts.

## How

The README gives build and porting instructions and a boot log. It reports no tests, proofs or measurements beyond a boot log with one memory test line.

## Limits

It is a project's own account. It says nothing about verification or signing of what the firmware loads, nor about Rust's memory safety as a goal. Our reading: the boot log shows one board starting Linux, not a claim about security.

## Against the wiki

- [[coreboot]]: **extends**. oreboot is a Rust fork that keeps coreboot's per-board layout; our reading: it drops coreboot's payload choice, since it plans only LinuxBoot payloads; see [[oreboot]].
- [[memory-safe-code]]: related. The README bans C but states no safety argument.
- [[opensbi]]: related. The log shows RustSBI as the machine-mode layer; OpenSBI is the one the wiki covers.
- [[bootloader]]: **extends**, see below.

## For zOS

[[bootloader]]: no change of state. Our reading: oreboot is at most a precedent for a loader written in Rust. The README says only that oreboot's own code is Rust and that it plans LinuxBoot payloads; nothing here shows that an image other than Linux can be started. Our reading of the paper: a zOS loader would not be a LinuxBoot payload.
