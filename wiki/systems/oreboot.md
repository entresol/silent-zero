---
type: system
status: reviewed
sources: [nd-oreboot]
short: A Rust fork of coreboot for LinuxBoot payloads
updated: 2026-11-28
---

# oreboot

A downstream fork of [[coreboot]] written mostly in Rust, which plans to start only LinuxBoot payloads ([[nd-oreboot]], [[linuxboot]]). Its licence is the GPL, version 2 or "version 2 or any later" depending on the file, with other GPL-compatible licences for derived parts; the code lives at github.com/oreboot/oreboot.

## State

The README shows a RISC-V board (Allwinner D1) starting a Linux kernel through RustSBI, and lists Arm and RISC-V demos in QEMU. Earlier x86 and Arm approaches are documented as previous implementations, and three emulation targets are parked. The README gives no dates or releases, so how active the project is today is not covered by the wiki's sources.

## Open questions

- Whether a Rust boot stage of this kind could start a Microkit image; the README says it plans to support only LinuxBoot payloads. See [[bootloader]].
