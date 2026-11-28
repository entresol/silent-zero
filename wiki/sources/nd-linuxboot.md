---
type: source
id: nd-linuxboot
status: reviewed
read: full
kind: report
sources: [nd-linuxboot]
updated: 2026-11-28
---

# LinuxBoot: the project page

The LinuxBoot project's home page, [linuxboot.org](https://www.linuxboot.org/). A short project description, snapshot of 2 November 2026, undated. Read in full; it has few claims.

## What it shows

- **The idea.** LinuxBoot is the use of a Linux kernel and an initramfs as a bootloader. The page says it has been implemented many times.
- **Its stated reasons.** Replacing lightly tested firmware drivers with hardened Linux drivers; faster boot ("typically" 20 times, no figure behind it on this page); a customisable initramfs with site-specific drivers and programs; and a proven approach "for almost 20 years" in military, consumer electronics and supercomputing systems.
- **The project.** A Linux Foundation project with a technical charter. Its build system, primarily targeting servers and PCs, started as NERF at Google in January 2017. It names three members of its technical steering committee and a subset of organisations involved (Google, Facebook, Netflix, 9elements and others). Documentation is the LinuxBoot Book.

## How

The page describes no method and gives no measurement.

## Limits

Every claim is the project's own and has no source on the page. The page says nothing about verification, signing or measurement of what LinuxBoot loads, and nothing about which firmware stays beneath it. Our reading: the stated reasons are claims about reliability, not security properties.

## Against the wiki

- [[coreboot]]: **extends**. Linux is one of coreboot's payloads ([[nd-coreboot-payloads]]); the Heads page ([[nd-heads]]) describes LinuxBoot as replacing UEFI's later stages while keeping vendor early firmware, including Intel's FSP.
- [[bootloader]]: **extends**. Our reading: a whole kernel as the loader is the opposite of a small loader in size; the page itself gives no sizes. See [[linuxboot]].

## For zOS

[[bootloader]]: no change of state. Our reading: LinuxBoot shows the other end of the design range. Its argument, reuse well-tested drivers, runs against a loader that, in the paper's words, checks one signed, static image and starts it or stops.
