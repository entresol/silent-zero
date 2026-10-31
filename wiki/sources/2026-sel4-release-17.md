---
type: source
id: 2026-sel4-release-17
status: reviewed
read: partial
kind: report
sources: [2026-sel4-release-17]
updated: 2026-10-31
---

# seL4 Foundation 2026: release 17.0.0

The release notes (`CHANGES.md`, section 17.0.0) and the list of known caveats (`CAVEATS.md`) of seL4 17.0.0, released on 30 October 2026, read on 31 October 2026 at tag `17.0.0`. [Release](https://github.com/seL4/seL4/releases/tag/17.0.0), [CAVEATS.md](https://github.com/seL4/seL4/blob/17.0.0/CAVEATS.md). Read in part: `CAVEATS.md` in full, of `CHANGES.md` only the section for 17.0.0.

## What it shows

- **Which platforms have a proof.** "The following seL4 architectures have platforms with a C-level functional correctness proof. For the current seL4 release, these are all 64-bit platforms seL4 support, as well as all 32-bit Arm platforms that seL4 supports" (`CAVEATS.md`, Implementation Correctness). The lists that follow name fifteen AArch64 and eight RISC-V platforms; the documentation's platform list links proof configurations for a few more boards, such as Rock3b ([[nd-sel4-supported-platforms]]).
- **RISC-V**, 64-bit, no FPU, no fast path: `hifive`, `ariane`, `bananapi-f3`, `cheshire`, `hifive-p550`, `polarfire`, `rocketchip` and `star64`.
- **RISC-V MCS**, same restrictions, MCS configuration: `hifive` only.
- **AArch64** with hypervisor extensions, FPU and fast path: fifteen platforms, among them `bcm2711` and `bcm2712` (Raspberry Pi 4 and 5).
- **Security properties.** For AArch32 without hypervisor extensions and without FPU, and for RISC-V: integrity, confidentiality and intransitive non-interference, "modulo timing channels". For AArch64 with hypervisor extensions: integrity; "Confidentiality and non-interference proofs for AArch64 with hypervisor extensions are in progress."
- **MCS.** For RISC-V the functional-correctness proof from abstract specification to C "has been completed"; for AArch64 it is in progress.
- **What the proof covers.** "This proof covers the functional behaviour of the C code of the kernel. It does not cover machine code, compiler, linker, boot code, cache or TLB management."
- **A fix that touches verified RISC-V configurations.** A missing instruction-cache flush let a new owner of a memory frame possibly execute stale code of the previous owner; it affected "all Arm and RISC-V configurations, including verified configurations", in all previous versions, with exploitability "low" and severity "Low" (`CHANGES.md`, 17.0.0). The release notes say that the security-relevant changes touching verified configurations lie outside what the proofs guarantee, and that "all issues we are currently aware of that affect verification assumptions have been fixed".

## How

Release documentation of the kernel's maintainers, versioned with the code.

## Limits

The notes state which proofs exist; they do not show them. The proofs themselves are in the `l4v` repository, which the wiki has not read. A careful reader adds: release 16.0.0 of 22 July 2026 (read at commit `6e7c3b7`, the commit of that release) listed `hifive` as the only RISC-V platform and expected "proof support for further platforms for RISC-V" in 2026; 17.0.0 is that extension.

## Against the wiki

- [[nd-sel4-verified-configurations]]: **confirms** the platform names and **extends** it with the proof status per platform: since 17.0.0 the RISC-V proof covers the boards beyond `hifive`, MCS still only `hifive`. On AArch64 security properties it **contradicts** that page, which lists confidentiality for AArch64; these notes say integrity only. See the question on [[kernel]].
- [[sel4]]: **extends** it with the platforms per proof.
- [[cva6]]: **confirms** Ariane among the RISC-V platforms, now with a C-level proof.

## For zOS

- [[kernel]]: the HiFive Premier P550, a board SiFive announced for sale in 2024 ([[2024-sifive-hifive-premier-p550]]), now has a proven seL4 configuration, without MCS. The MCS kernel the paper chooses is proven only for the HiFive Unleashed, which SiFive no longer sells ([[nd-sifive-hifive-unleashed]]).
- [[bootloader]]: the project's boot video uses seL4 16.0.0. The instruction-cache fix of 17.0.0 applies to its configuration.
