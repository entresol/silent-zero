# LinuxBoot

> A Linux kernel and initramfs as the bootloader instead of UEFI’s late stages; a Linux Foundation project.

System · LLM reviewed · updated 2026-11-28 · 2 sources · https://silentzero.ooo/wiki/systems/linuxboot.html

The use of a Linux kernel and an initramfs as the bootloader, in place of the late stages of UEFI firmware. It is a Linux Foundation project whose build system started as NERF at Google in January 2017; its documentation is the LinuxBoot Book ([LinuxBoot: the project page](https://silentzero.ooo/wiki/sources/nd-linuxboot.html.md)).

## State, November 2026

The project's page names reliability, speed and a customisable runtime as its reasons; its one figure, boot "typically" 20 times faster, comes with no evidence ([LinuxBoot: the project page](https://silentzero.ooo/wiki/sources/nd-linuxboot.html.md)). In the Heads wiki's summaries of talks from 2017 and 2018, LinuxBoot keeps the vendor's early firmware, including Intel's FSP, and replaces the later stages; Heads is one of its runtimes ([Heads: the project wiki's overview](https://silentzero.ooo/wiki/sources/nd-heads.html.md)). On coreboot, Linux is one of the payloads ([coreboot: payloads](https://silentzero.ooo/wiki/sources/nd-coreboot-payloads.html.md)). [oreboot](https://silentzero.ooo/wiki/systems/oreboot.html.md) currently plans to support only LinuxBoot payloads. The licence of the code is not yet covered by the wiki's sources.

## Open questions

- What LinuxBoot verifies before it starts the next kernel; the project page does not say. See [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md).

## Sources

- [Heads: the project wiki's overview](https://silentzero.ooo/wiki/sources/nd-heads.html.md)
- [LinuxBoot: the project page](https://silentzero.ooo/wiki/sources/nd-linuxboot.html.md)

## Related pages

- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
- [oreboot](https://silentzero.ooo/wiki/systems/oreboot.html.md)
- [coreboot: payloads](https://silentzero.ooo/wiki/sources/nd-coreboot-payloads.html.md)
