# oreboot

> A coreboot fork in Rust that plans to start only LinuxBoot payloads.

System · LLM reviewed · updated 2026-11-28 · 1 source · https://silentzero.ooo/wiki/systems/oreboot.html

A downstream fork of [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md) written mostly in Rust, which plans to start only LinuxBoot payloads ([oreboot: the README](https://silentzero.ooo/wiki/sources/nd-oreboot.html.md), [LinuxBoot](https://silentzero.ooo/wiki/systems/linuxboot.html.md)). Its licence is the GPL, version 2 or "version 2 or any later" depending on the file, with other GPL-compatible licences for derived parts; the code lives at github.com/oreboot/oreboot.

## State

The README shows a RISC-V board (Allwinner D1) starting a Linux kernel through RustSBI, and lists Arm and RISC-V demos in QEMU. Earlier x86 and Arm approaches are documented as previous implementations, and three emulation targets are parked. The README gives no dates or releases, so how active the project is today is not covered by the wiki's sources.

## Open questions

- Whether a Rust boot stage of this kind could start a Microkit image; the README says it plans to support only LinuxBoot payloads. See [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md).

## Sources

- [oreboot: the README](https://silentzero.ooo/wiki/sources/nd-oreboot.html.md)

## Related pages

- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
- [LinuxBoot](https://silentzero.ooo/wiki/systems/linuxboot.html.md)
