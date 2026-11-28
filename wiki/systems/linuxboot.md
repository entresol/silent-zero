---
type: system
status: reviewed
sources: [nd-linuxboot, nd-heads]
short: Linux kernel and initramfs as the bootloader
updated: 2026-11-28
---

# LinuxBoot

The use of a Linux kernel and an initramfs as the bootloader, in place of the late stages of UEFI firmware. It is a Linux Foundation project whose build system started as NERF at Google in January 2017; its documentation is the LinuxBoot Book ([[nd-linuxboot]]).

## State, November 2026

The project's page names reliability, speed and a customisable runtime as its reasons; its one figure, boot "typically" 20 times faster, comes with no evidence ([[nd-linuxboot]]). In the Heads wiki's summaries of talks from 2017 and 2018, LinuxBoot keeps the vendor's early firmware, including Intel's FSP, and replaces the later stages; Heads is one of its runtimes ([[nd-heads]]). On coreboot, Linux is one of the payloads ([[nd-coreboot-payloads]]). [[oreboot]] currently plans to support only LinuxBoot payloads. The licence of the code is not yet covered by the wiki's sources.

## Open questions

- What LinuxBoot verifies before it starts the next kernel; the project page does not say. See [[bootloader]].
