# seL4 on PC99 (x86-64)

> SeL4 on PCs boots through a Multiboot loader. report, full text.

Source · LLM reviewed · updated 2026-10-30 · https://silentzero.ooo/wiki/sources/nd-sel4-x64-platform.html

A platform page of the seL4 documentation, undated, read on 30 October 2026. [Page](https://docs.sel4.systems/Hardware/X64.html).

## What it shows

- seL4 runs on 32-bit ia32 and 64-bit x64 machines, in QEMU and on hardware. The page lists virtualisation support, IOMMU (VT-d) support and the proof configuration "X64".
- The build produces a Multiboot-compliant image. The page gives a GRUB2 entry that loads the kernel and the root server as a module, and the developers "usually boot via PXE for convenience", with syslinux; booting from a USB stick with syslinux is described as well.
- On real hardware, console output goes over a serial port.

## How

A short platform page with build and boot instructions.

## Limits

A careful reader adds: the page names the proof configuration without saying what it covers. [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) lists C-level functional correctness without fast path for x86-64, and no integrity or confidentiality proof, with VT-x outside the verified configuration; IOMMU support is outside every verified configuration.

## Against the wiki

- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md): **consistent** with it; the proof configuration named here is the one listed there.

## For Silent Zero

- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md): on a PC, seL4 is started by a Multiboot loader such as GRUB or syslinux. Our reading: a Silent Zero loader on x86-64 would be such a loader or replace one. Microkit requires a Multiboot 2 loader ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)); the examples on this page use Multiboot 1.
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md): x86-64 has fewer verified properties than Arm or RISC-V ([seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)).

## Related pages

- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md)
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
