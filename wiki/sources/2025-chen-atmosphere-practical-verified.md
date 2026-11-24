---
type: source
id: 2025-chen-atmosphere-practical-verified
status: reviewed
read: partial
kind: proof
sources: [2025-chen-atmosphere-practical-verified]
updated: 2026-11-21
---

# Chen et al. 2025: Atmosphere, practical verified kernels with Rust and Verus

Xiangdong Chen, Zhaofeng Li, Jerry Zhang, Vikram Narayanan and Anton Burtsev (University of Utah; Narayanan's work done there, now Palo Alto Networks). "Atmosphere: Practical Verified Kernels with Rust and Verus", SOSP 2025, Seoul, 13 to 16 October 2025, 16 pages. [DOI](https://doi.org/10.1145/3731569.3764821), [PDF](https://mars-research.github.io/doc/2025-sosp-atmo.pdf). Read in part: abstract, introduction, the isolation and access-control passages, the noninterference section, the trusted computing base, the evaluation of verification effort and the IPC microbenchmarks, and the conclusion. Not read: the proof details, the device-driver and application benchmarks.

## What it shows

- **A verified kernel in Rust.** Atmosphere is "a full-featured microkernel with support for strict isolation in mixed-criticality systems". All code is Rust; functional correctness, "refinement of a high-level specification", is proved with Verus. It runs on multi-CPU hardware under one big lock and has processes, threads, dynamic memory management, IPC, virtual address spaces, IOMMU support and "containers", groups of isolated processes.
- **Effort.** 6K lines of executable code and 20.1K lines of proof code (14.3K of specification, 5.8K of hints and proofs); "less than 2.5 person-years", of which 1.5 went to the verified parts and the rest to unverified parts such as boot, user-level drivers, benchmarks and the build environment. The proof-to-code ratio is 3.32:1, against 20:1 for seL4 and 14.9:1 for CertiKOS in the authors' table; verification takes under 20 seconds on 32 threads and 47 seconds on one thread of a recent laptop processor (an Intel i9-13900HX), and about 1 minute 7 seconds with 8 threads on a CloudLab server.
- **Authority is by containers, not capabilities.** Containers form a tree; a parent can terminate a child and harvest its resources. The authors "prohibit fine-grained revocation": "the only way to revoke resources of a container is to terminate it". They say this simplifies the verification of user code.
- **Noninterference for one configuration.** For a system of two untrusted, unverified containers A and B and a verified shared container V, the paper proves that A and B do not interfere with each other and can communicate with V. It rests on V's functional correctness. V has one process with one thread. The proof covers the effects of system calls and not user code.
- **What is trusted.** Verus and the Z3 solver, the Rust compiler and core library, specifications and about 700 lines of axioms for core Rust data structures, setter functions for permissions (300 lines of code with 1,900 of specification), 172 lines of assembly, around 3,000 lines of trusted Rust (among them the IOMMU setup, interrupt handling and tables), a minimal boot loader, and the processor, microcode, firmware, memory and the management engine. Devices behind the IOMMU are not trusted.
- **Speed.** An IPC call and reply takes about 1,058 cycles against 1,026 in seL4; mapping a page about 1,984 against 2,650, "although the system calls are not strictly equivalent". Measured under KVM on CloudLab servers.

## How

A systems paper with a verified implementation, a proof of one noninterference scenario and measurements on servers. The measurements use x86 machines; the trusted code it lists (system-call entry, descriptor tables, interrupt controller) is x86 as well, which is our reading of the platform.

## Limits

- The authors say the noninterference proof ignores timing channels through shared caches, and that long-running system calls under the big lock can block other processes and leak timing information.
- It has no real-time analysis or worst-case execution time in the sections read, and no mention of AI agents or models writing the proofs.
- On the ratios, the authors say "arguably, VeriSMo is semantically less complex" than Atmosphere and that its team prioritised proof effort over verification speed. Our reading: figures from different projects need not count the same way. The project page gives a different figure for Atmosphere itself ([[nd-mars-research-atmosphere]]).
- It names no repository or software licence in the text read; the paper itself is under a Creative Commons Attribution 4.0 licence.

## Against the wiki

- [[kernel]]: **extends** with a second formally verified microkernel, not on seL4's proof method, at much lower reported proof effort and with weaker features: one big lock and containers instead of capabilities; the paper describes containers with reserved memory and CPU cores and describes no time budgets.
- [[verus]]: **extends** with a feature-rich microkernel verified with it ([[atmosphere]]). Our reading: the "verified microkernel (reported proof-to-code ratio 7.5 to 1)" that [[2024-lattuada-verus-practical-foundation]] lists among other users may be an earlier state of this kernel, since the project page gives the same ratio; neither text says so.
- [[proof-automation]]: **extends** the cost side: 3.32 lines of proof per line of code, against figures of 3.9 to 13.3 for Verus case studies.
- [[mixed-criticality]]: **extends** with a verified separation kernel for mixed-criticality systems, by the authors' description.

## For zOS

Our reading: the paper's Section 2.3 says Verus checks faster than other verifiers; Atmosphere is a worked case of a kernel verified that way, and a different route to the kernel from seL4 and Microkit. It does not replace the choices zOS makes: no capability tree with fine-grained revocation, no time budgets described, no multi-core proof beyond a big lock. The paper does not name Atmosphere. See [[atmosphere]].
