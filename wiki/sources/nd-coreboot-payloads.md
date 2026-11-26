---
type: source
id: nd-coreboot-payloads
status: reviewed
read: full
kind: report
sources: [nd-coreboot-payloads]
updated: 2026-11-26
---

# coreboot: payloads

The "Payloads" page of coreboot's documentation, by the coreboot project; undated, documentation licensed CC-by 4.0. [doc.coreboot.org/payloads](https://doc.coreboot.org/payloads.html). The pool holds a snapshot of 2 November 2026. Read in full; the page is short.

## What it shows

- **The role.** coreboot does hardware initialisation and then passes control to a payload carried in the firmware storage. The project says it does not mandate how the boot process should look.
- **The payloads it names.** Any statically linked ELF binary, loaded by the project's SELF mechanism; SeaBIOS, which implements the PC BIOS interface, runs option ROMs more completely than coreboot and "also supports Multiboot"; edk2 for UEFI; GRUB2; Linux, loaded through a trampoline on x86, often a rather small kernel that loads another through kexec; and Heads, a distribution of coreboot, Linux, busybox and tools aiming at reproducible ROMs, with measured boot, kexec, GPG, OTP, TLS and firmware updates, on a limited number of mainboards.
- **The case for Linux as payload.** The page says proponents stress well-tested drivers and boot policy written in ordinary tools.
- **Multiboot in practice.** The page's example has GRUB2 start SeaBIOS (our reading: GRUB2 is a payload in the firmware's file system, since the entry's root is `cbfsdisk`) through a Multiboot menu entry, and a second example boots SeaBIOS from a USB drive.

## How

A reference page, with no measurements. The page describes each payload in a few lines and refers only to the Heads wiki.

## Limits

The page does not say which payloads are verified, signed or measured. It names GRUB2 as a bootloader that can be built as a payload but does not say that it can start a Multiboot 2 image. "Supports Multiboot" for SeaBIOS can mean that it can be started that way, as the example shows, or that it can start Multiboot kernels; the page does not say which.

## Against the wiki

- [[nd-coreboot-architecture]]: **confirms** that the payload is the last stage and fixed at build time; this page adds which payloads exist.
- [[nd-sel4-x64-platform]]: **extends**. seL4 on a PC boots through a Multiboot loader; this page names GRUB2, a bootloader, as a possible payload but does not say it can start such an image.
- [[coreboot]] and [[bootloader]]: extended, see the pages.

## For zOS

[[bootloader]]: no change of state. Our reading: if a zOS loader were built as a statically linked ELF binary, which the paper does not specify, it would be the kind of binary this page says a payload can be. Whether it can also start a Microkit image, which needs a Multiboot 2 loader ([[nd-sel4-microkit-user-manual]]), is not answered here.
