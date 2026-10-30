---
type: source
id: nd-sel4-x64-platform
status: reviewed
read: full
kind: report
sources: [nd-sel4-x64-platform]
updated: 2026-10-30
---

# seL4 on PC99 (x86-64)

A platform page of the seL4 documentation, undated, read on 30 October 2026. [Page](https://docs.sel4.systems/Hardware/X64.html).

## What it shows

- seL4 runs on 32-bit ia32 and 64-bit x64 machines, in QEMU and on hardware. The page lists virtualisation support, IOMMU (VT-d) support and the proof configuration "X64".
- The build produces a Multiboot-compliant image. The page gives a GRUB2 entry that loads the kernel and the root server as a module, and the developers "usually boot via PXE for convenience", with syslinux; booting from a USB stick with syslinux is described as well.
- On real hardware, console output goes over a serial port.

## How

A short platform page with build and boot instructions.

## Limits

A careful reader adds: the page names the proof configuration without saying what it covers. [[nd-sel4-verified-configurations]] lists C-level functional correctness without fast path for x86-64, and no integrity or confidentiality proof, with VT-x outside the verified configuration; IOMMU support is outside every verified configuration.

## Against the wiki

- [[nd-sel4-verified-configurations]]: **consistent** with it; the proof configuration named here is the one listed there.

## For zOS

- [[bootloader]]: on a PC, seL4 is started by a Multiboot loader such as GRUB or syslinux. Our reading: a zOS loader on x86-64 would be such a loader or replace one. Microkit requires a Multiboot 2 loader ([[nd-sel4-microkit-user-manual]]); the examples on this page use Multiboot 1.
- [[kernel]]: x86-64 has fewer verified properties than Arm or RISC-V ([[nd-sel4-verified-configurations]]).
