---
type: source
id: 2026-xu-safel4-rethinking-safe
status: reviewed
read: partial
kind: measurement
sources: [2026-xu-safel4-rethinking-safe]
updated: 2026-11-22
---

# Xu et al. 2026: safeL4, a Rust microkernel without hardware isolation between its domains

Zheyuan Xu, Xiaobei Zhang, Zihan Li, Zekai Nie, Guangtao Zhu, Zhuang Lu, Qianying Zhang, Shijun Zhao, Haibo Chen and Rui Hou (Institute of Information Engineering of the Chinese Academy of Sciences, UNSW Sydney, Capital Normal University, Shanghai Jiao Tong University). "safeL4: Rethinking Safe-Language-Based Single Address Space Microkernels", arXiv 2610.35999v1 [cs.OS], 26 October 2026; the PDF names ASPLOS '27 (Heraklion, April 2027). [arXiv](https://arxiv.org/abs/2610.35999). Read: the abstract, introduction, design, trusted-base section and evaluation; the implementation details of §5, the case study and the appendix were skimmed.

## What it shows

- **The thesis.** A microkernel can drop hardware isolation between protection domains written in safe Rust, if it keeps the kernel minimal and enforces capability-based access to every resource. Earlier safe-language kernels, the authors say, have large trusted bases or lack fine-grained capabilities (§1, §3; Tables 2 and 3). Legacy applications in unsafe languages still run as user-level tasks, isolated by hardware (§4.1).
- **The design.** The kernel is written in Rust. Unsafe operations are wrapped in low-level abstractions for hardware resources; capabilities are Rust objects with a capability derivation tree, so every access to a resource goes through one (§4). A panic in a callee domain is caught at the call site (§4.5). The kernel has 11,688 lines, of which 1,765 (15.1 per cent) are unsafe; the whole system has 22,018 lines. It supports RISC-V64 and AArch64; the architecture-specific unsafe code is 462 lines for AArch64 and 349 for RISC-V64 (Table 4). Only the AArch64 board is evaluated.
- **Linked code.** Table 5 (§6.2) counts the linked code: 6,248 lines of Rust core and alloc and 2,720 of other trusted code in the trusted base, 8,968 together, plus 6,081 lines outside it (the protection domains), 15,049 in all. For comparison it lists Tock at 6,628 in total, Redleaf 26,410, Theseus 58,774 and Asterinas 78,697. The authors note that Tock targets low-power microcontrollers and that source and linked size do not fully measure the trusted base.
- **Speed against seL4.** On a Raspberry Pi 3B+ (four Cortex-A53 cores, 1.4 GHz), with seL4's benchmark suite reimplemented in Rust for safeL4 (without the virtualisation case), safeL4 is 1.91 times faster in geometric mean (Table 6). A call to a server in another domain takes 32 cycles against 249 in seL4, a reply 12 against 268. Frame-capability allocation is slower (949 against 538 cycles; the authors tie it to initialising locks and reference counts in the capability code, Table 8, and to fine-grained locking against seL4's big kernel lock) and yielding a thread is slightly slower (400 against 382 cycles). Against Redox on a file-system subset the geometric mean is 1.47 times (Table 7); SQLite on YCSB beats an seL4 library OS by 14.3 per cent and Linux by 23.2 per cent on average (§6.4).

## How

A prototype on one board, compared with seL4 as a hardware-isolation microkernel, Redox and Linux 6.6 (Ubuntu 22.04 with ZFS). The seL4 build is not described in the part read. SQLite and YCSB run as user-level tasks.

## Limits

The authors state the assumptions (§4.2): the Rust compiler and linker, core and alloc, the heap allocator and the safeL4 kernel are trusted, as are DMA-capable devices, their drivers and DMA configuration, because unrestricted DMA can bypass Rust's safety; every protection domain must be exclusively safe Rust; processor, memory, platform and boot behave as specified. The current safeL4 does not support IOMMU-based DMA isolation, named as a future extension. They list non-guarantees: no general functional correctness, and a safe-Rust driver can still program a device wrongly. Their Table 3 names Atmosphere, a Rust kernel verified with Verus, as the system with machine-checked proofs; safeL4 itself is not described as verified.

A careful reader adds:

- The comparison measures primitives on one small board against seL4's cycle counts, with benchmarks rewritten by the authors. Whether the seL4 build was a stock one is not stated in the part read.
- The safety of a domain rests on its code being free of `unsafe`; code that needs it runs as a hardware-isolated task instead.
- It is a preprint of a paper announced for 2027, and the evaluation is by the authors.

## Against the wiki

- [[memory-safe-code]]: **extends**. The page covers hardening by language in applications and drivers; this is a research kernel built on the language, with its own trusted base.
- [[sel4]]: **related**. It takes seL4's capability model and measures against it; the authors attribute seL4's cost to hardware isolation, and seL4's frame-allocation advantage to its big kernel lock.
- [[kernel]]: **related**. A rival route to a small capability kernel, with assurance from the type system and no proof of the kernel. See [[2018-klein-formally-verified-software]] for what a proof gives.
- [[drivers]], [[iommu]]: **confirms** that DMA is outside what language safety covers.

## For zOS

[[kernel]]: no change of state. Our reading: the paper's case for a proven kernel is not weakened, since safeL4 offers speed and a small linked base but no proof; and the paper raises no objection to seL4's isolation cost that safeL4 answers (the paper's text on speed concerns Mach and the L4 fix). Our reading: for agent code, safeL4's own answer is its hardware-isolated user-level tasks, which brings back the cost it set out to remove.
