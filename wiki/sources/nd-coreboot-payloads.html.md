# coreboot: payloads

> The payloads coreboot can start: ELF, SeaBIOS, edk2, GRUB2, Linux, Heads; nothing on verification. report, full text.

Source · LLM reviewed · updated 2026-11-26 · https://silentzero.ooo/wiki/sources/nd-coreboot-payloads.html

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

- [coreboot: architecture and boot stages](https://silentzero.ooo/wiki/sources/nd-coreboot-architecture.html.md): **confirms** that the payload is the last stage and fixed at build time; this page adds which payloads exist.
- [seL4 on PC99 (x86-64)](https://silentzero.ooo/wiki/sources/nd-sel4-x64-platform.html.md): **extends**. seL4 on a PC boots through a Multiboot loader; this page names GRUB2, a bootloader, as a possible payload but does not say it can start such an image.
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md) and [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md): extended, see the pages.

## For Silent Zero

[The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md): no change of state. Our reading: if a Silent Zero loader were built as a statically linked ELF binary, which the paper does not specify, it would be the kind of binary this page says a payload can be. Whether it can also start a Microkit image, which needs a Multiboot 2 loader ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)), is not answered here.

## Related pages

- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
- [LinuxBoot](https://silentzero.ooo/wiki/systems/linuxboot.html.md)
- [coreboot: architecture and boot stages](https://silentzero.ooo/wiki/sources/nd-coreboot-architecture.html.md)
- [Heads: the project wiki's overview](https://silentzero.ooo/wiki/sources/nd-heads.html.md)
- [LinuxBoot: the project page](https://silentzero.ooo/wiki/sources/nd-linuxboot.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [seL4 on PC99 (x86-64)](https://silentzero.ooo/wiki/sources/nd-sel4-x64-platform.html.md)
