---
type: source
id: 2026-nguyen-booting-windows-x86-64
status: reviewed
read: partial
kind: report
sources: [2026-nguyen-booting-windows-x86-64]
updated: 2026-11-16
---

# Nguyen 2026: Booting Windows on an x86-64 seL4-based VMM

Bill Nguyen (UNSW Sydney, Trustworthy Systems). Talk at the 8th seL4 Summit, Vancouver, September 2026. [Abstract and slides](https://trustworthy.systems/publications/papers/Nguyen_26:sel4s.abstract). There is no paper; the wiki has read the 36 slides. The last slide's feature matrix lost its check marks in text extraction and is not used.

## What it shows

- **Result (slide 2).** libvmm, the library for virtual machine monitors on [[microkit]], runs an unmodified Windows 11 Pro installed from retail media on x86-64. The talk itself was run on it, as slides 26 to 29 reveal, and slide 33 says it works on hardware too: an Intel Xeon W-1250 with Windows loaded from an NVMe disk through a native sDDF driver.
- **Motivation (slide 3).** Mixed-criticality systems that need both a legacy Windows workload and seL4's guarantees.
- **Against the CAmkES VMM (slide 4).** The slides tabulate the two. libvmm integrates with sDDF drivers, boots Linux directly or through OVMF UEFI firmware, supports Windows 10 and 11 (x86 only) beside Linux, and lists hardware-accelerated APIC virtualisation (Intel APICv) as its performance feature, although the kernel change for it is still a request for comments (slide 17); the CAmkES VMM brings its own drivers, loads a Linux kernel directly, supports Linux only and emulates the APIC in software.
- **Boot path (slides 5 to 11).** Windows expects UEFI services, so direct kernel loading does not work. libvmm loads the OVMF firmware and lets it load the guest. The slides credit this to seL4 pull request 1600, "x86/vcpu: Support guest-managed mode transitions and Unrestricted Guest", which landed in seL4 15.0.0.
- **Speed (slides 12 to 17).** After UEFI worked, Windows booted but took more than ten minutes to reach an unusably slow desktop. The slides trace it to Windows reprogramming the APIC's task priority register about 50,000 times a second, each time costing a VM exit; Linux uses `cli` and `sti`, which do not exit. With APICv, boot time fell to 60 seconds. A kernel RFC is "in discussions", and the slides point to an earlier review for the Bhyve BSD hypervisor.
- **Debugging (slides 18 to 25).** Windows gives little information when it stops early; the author used a kernel debugger over serial in a second VM and a disassembler on the Windows kernel, and found missing CPU features to fix one by one.
- **Demo setup (slides 30 to 32).** The demo runs on Microkit with libvmm and the sDDF network and block subsystems. The guest gets VirtIO devices, PS/2 input and a framebuffer. The slide gives line counts per component whose assignment the extraction does not keep.

## How

An engineering talk on a working system with a live demonstration. No performance figures beyond the boot times above, no test method, no security or timing claims.

## Limits

- The slides do not discuss isolation: what the guest, the firmware and the VMM can reach, what part of this is covered by the kernel proof, or whether the proved x86-64 kernel configuration includes the virtualisation extensions. [[nd-sel4-verified-configurations]] lists "AArch32 with hypervisor" and RISC-V "no hypervisor" among its verified configurations; whether it has an x86-64 virtualisation entry is not checked here.
- Windows 10, 11 and Linux support is a statement of the author on a slide, backed by the demonstration, not by a test suite.
- The APICv change is a kernel RFC (slide 17); our reading is that it was not part of a release at the time of the talk.

## Against the wiki

- [[microkit]]: **extends** the x86-64 line of the 2.4.0 notes ([[2026-microkit-release-2-4-0]]), which mention VMs on x86-64. This talk is the application, with Windows as a guest.
- [[lionsos]]: **extends**. The driver VM for unmodified drivers ([[2025-heiser-fast-secure-adaptable]]) was shown on Arm; here the VM is a whole desktop operating system on x86-64.

## For zOS

[[drivers]]: the paper's driver island runs a Linux VM. This talk shows the VM machinery on x86-64 for a non-Linux guest; it does not bear on the island's isolation, which stays *assumed*. [[bootloader]]: a PC route that boots guests through OVMF, which is firmware inside the guest, not the platform's own. No state changes.
