---
type: source
id: 2025-heiser-fast-secure-adaptable
status: reviewed
read: full
kind: measurement
sources: [2025-heiser-fast-secure-adaptable]
updated: 2026-11-01
---

# Heiser et al. 2025: Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance

Gernot Heiser, Ivan Velickovic, Peter Chubb and twelve further authors, UNSW Sydney. arXiv:2501.06234, v2 of 27 May 2025. [Paper](https://arxiv.org/abs/2501.06234). Read in full.

## What it shows

- **Design.** LionsOS is built on [[sel4]] and [[microkit]] from a few kinds of small components: drivers that only translate between a device and a device-class interface, virtualisers that share a device between clients, optional copiers, and client libraries such as the IP stack (§4). Policies are written for the use case instead of being general; the authors call this "radical simplicity" (§3).
- **Queues.** All shared-memory communication is single producer, single consumer, in bounded lock-free queues, with the policy-independent state held in shared memory. Because of that a component can be restarted or its code reloaded without touching the rest (§5.2). Components are strictly sequential and use several cores by sitting on different ones, which the authors call location transparency (§5.1, §5.3).
- **Networking.** On a 1 Gb/s Arm board (i.MX8MQ) with everything on one core, Linux plateaus at about 500 Mb/s and uses a full core; LionsOS carries the full gigabit with about a third of the core to spare. Round-trip times are three to ten times lower than Linux's (§6.3.1, Figure 4a, 4b). On an x86 machine with a 10 Gb/s NIC, Linux saturates at about 4 Gb/s while LionsOS keeps about 20 per cent of the CPU free (Figure 5a). Genode 24.11 reaches about 100 Mb/s on the Arm board. A commercial microkernel OS, which the authors may not name (footnote 2), could not run on that board; on another i.MX board, in a multicore set-up, it reaches about 240 Mb/s in the echo benchmark and about 390 Mb/s in a bidirectional iperf3 run, far below LionsOS (§6.3.1).
- **IPC cost.** The authors add the IPC costs reported for Fiasco and Zircon to each seL4 system call, and subtract the kernel's share to simulate free IPC. The system keeps up with the load in all three variants, barely in the Zircon one, and free IPC has minimal impact (Figure 5d, 6a). The authors say the simulation is not precise.
- **Storage.** Throughput on an SD card is similar to Linux's, or slightly better in the authors' discussion, and limited by the card; at small block sizes LionsOS needs a fraction of the CPU (§6.3.2, §7, Figure 7). Reading several small files from a FAT32 file system is slower than on Linux beyond five files because LionsOS does not cache directories, and closing files takes far longer because clean-up is synchronous (§6.3.2).
- **Size.** Ethernet drivers on the three platforms in Table 1 are 4.5 to 26.9 times smaller than Linux's (8.4 times on the i.MX8). A point-of-sale demonstrator has about 3.1 kSLOC of trusted code and 66 kSLOC of untrusted library code; the trusted code was written from scratch (§6.2.1).
- **Driver VMs.** An unmodified Linux driver can run in its own small virtual machine behind a user-space program that talks to the LionsOS queues. The authors report a few weeks of effort per device class. The drivers used were for GPU (an exported framebuffer), Ethernet, SD block and sound on one board (§5.4, §5.5, §6.2.3).
- **Policy swap.** A virtualiser was replaced by a bandwidth limiter at run time in 17 µs on the Arm board, without dropped packets (§6.3.1, Figure 6d).
- **Deadlock freedom.** The signalling protocols between components are modelled and checked with the SPIN model checker (§6.2.2).
- **Deployment.** The authors say several complete systems are in daily use; they name a reference design for a point-of-sale terminal and a deployed web server that hosts the sel4.systems site (§5.5.2).

## How

A systems paper with benchmarks: a UDP echo server under load from an external generator on four machines (MaaXBoard, Odroid-C4, a Compulab IOTGate for the unnamed system, an Intel Xeon machine), compared with Linux (Buildroot or Debian), Genode and the unnamed system. CPU use is counted by an idle thread on each core.

## Limits

What the authors say themselves: verification of LionsOS is out of scope; the design aims to make it feasible ("for now we leave verification out of scope", §1). Verification of the MCS kernel is "in progress" (§1), and dynamic resource management such as taking cores offline is in progress (§5.5.3). The IPC simulation is rough.

A careful reader adds:

- **Throughput and mean times, no bounds.** The measurements are throughput, CPU load and round-trip times as plotted against load; the paper does not say which statistic the round-trip times are. The paper reports no worst-case latency and does not discuss real-time guarantees, though it takes mixed criticality as its setting. For [[real-time-loops]] the numbers say the stack is fast, not that it is timely.
- **Networking is the main case.** The performance claim rests on one workload class, UDP echo, and on storage and a file benchmark; the authors chose networking as the one that stresses context switching most (§6.3).
- **Verification is cited, not shown.** The conclusion says a high-performance NIC driver has been verified with automated techniques (Zhao et al. 2025, not in the pool); the wiki's page on that line of work is [[2026-tyler-smt-based-deductive]].
- **Driver VMs and DMA.** Mapping the data region to the device through the IOMMU is mentioned in passing (§4.1.3); the paper does not say what protects the system when a Linux driver VM's device writes memory, and no proof covers the IOMMU ([[nd-sel4-verified-configurations]]).
- **Authors as evaluators.** The benchmarks were run by the group that built LionsOS; the Genode and Linux set-ups were their own, and the Genode result is described as a disappointment the authors tried to resolve with Genode staff (§6.3.1, footnote 1).

## Against the wiki

- [[lionsos]]: extends. The page now has the design paper behind its description of components, queues and the driver VM.
- [[drivers]]: extends. The driver VM now has its source; the table row for performance against Linux gets a measurement.
- [[microkit]]: confirms the static model and the event-driven programming model, and the SDF.
- [[2026-heiser-mcs-safety-os]] and [[2026-trustworthy-lionsos]]: the later slides and the introduction page repeat the design; the code-size figures of the slides trace back to Table 2 here.
- [[mixed-criticality]]: the paper names mixed criticality as the requirement but evaluates no timing guarantee.

## For zOS

The paper cites this source for the driver island (Section 3) and in its table of building blocks (Section 5). The source supports both: a Linux driver in a VM, and a modular OS that beats Linux in networking and on context-switch-heavy loads. Our reading: the paper's phrase "legacy drivers, above all for graphics and AI accelerators" goes beyond the drivers listed here (a framebuffer, Ethernet, SD, sound); AI accelerators do not appear. The paper's table row also says LionsOS "outperforms Linux" in networking and on context-switch-heavy loads; storage throughput is similar and small-file reads are slower, so the row fits networking best. The [[drivers]] design page does not change state. The [[real-time-loops]] page does not either: no bound is claimed here.
