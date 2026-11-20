# Verifying Device Drivers with Pancake

> Pancake: language, compiler and a verified Ethernet driver; the transpiler is unverified. proof, full text.

Source · Zhao et al. 2025 · LLM reviewed · updated 2026-11-20 · https://silentzero.ooo/wiki/sources/2025-zhao-verifying-device-drivers.html

Junming Zhao, Miki Tanaka, Johannes Åman Pohjola, Alessandro Legnani, Tiana Tsang Ung, H. Truong, Tsun Wang Sau, Thomas Sewell, Rob Sison, Hira Syeda, Magnus Myreen, Michael Norrish and Gernot Heiser (UNSW Sydney, ETH Zürich, University of Melbourne, Chalmers, University of Gothenburg, Australian National University). "Verifying Device Drivers with Pancake", arXiv 2501.08249v2, 30 May 2025. [arXiv](https://arxiv.org/abs/2501.08249). The text does not name a venue; it reads as a preprint. Read in full.

## What it shows

- **The claim.** The authors say that, to their knowledge, this is the first formal verification of a demonstrably performant driver for a realistic, non-trivial device: the Ethernet NIC common to several NXP i.MX 8M processors (Abstract, §8). They say that, to their knowledge, earlier efforts either left a gap between the analysed model and the real code or gave no performance figures (§1, §7).
- **Pancake, a language for it.** Pancake is a small imperative language without a static type system. Its data are machine words, code pointers and structs, with no pointers into the stack and no allocation. Its semantics fits in a few hundred lines of HOL4, with no undefined behaviour and a fixed evaluation order (§2.1, §2.2). It has no concurrency primitives, because the driver design is single-threaded (§2.1.1).
- **A verified compiler.** Pancake reuses the lower passes of the verified CakeML compiler. The top-level theorem says the source program and the generated machine code show the same observable I/O events, if enough stack space is available. The compiler also predicts the stack bound, provided recursion is only in tail position (§2.3). Shared-memory loads and stores are observable events, so device registers and shared queues need no foreign-function layer (§2.4).
- **A verification front-end.** A transpiler turns annotated Pancake into Viper, which an SMT-based back-end checks (§3). Overflow is treated as a verification failure; the authors note the original C driver used intended overflow, avoided in Pancake with a one-line change (§3.1).
- **Four classes of properties for the Ethernet driver** (§4.1 to §4.5):
  1. Device interface: accesses lie in the right address ranges, and values written obey the device's requirements. The verifier rejects any shared-memory access not covered by an annotation (§4.2).
  2. OS interface: the driver follows the queue signalling protocol. It notifies the OS if and only if the OS requested a signal and the queue state changed, and it clears the request afterwards (§4.1, §4.3).
  3. Data integrity: packet addresses and lengths are tracked on all pathways between the hardware rings and the queues, and queue operations match ring changes, so no data is lost in the driver (§4.4). The driver never touches the packet data itself (§4.1).
  4. Region isolation: only the transmit paths touch transmit state and only the receive paths touch receive state, checked with Viper's permissions (§4.5).
- **Size and effort.** The C driver has 351 lines and the Pancake driver 411. The proofs add 558 lines of annotations, a 391-line device model and a 298-line model of the OS interface (Table 1). The authors say the verification took around three person-months, by the one team member without prior verification experience, who ported the driver from C and then verified it (§1, §8).
- **Verification time.** Full verification takes around 20 minutes on a typical laptop; the device model alone 10 minutes and each driver function about 1 minute (§5).
- **Performance.** The test board is an AVnet MaaXBoard (NXP i.MX8MQ, four Cortex-A53 cores, fixed at 1 GHz) running an echo client on LionsOS. The Pancake driver reached the requested throughput like the C driver, up to 1,000 Mb/s requested (Figure 4). It used slightly more driver CPU time, about 10 per cent as read off Figure 4 (the text does not say whether relative or in percentage points). The difference in total CPU becomes unnoticeable, and the round-trip time differences are well within the variance (§5, Figure 5). The authors conclude the cost "is in the noise". They set it against LionsOS using less than half the CPU of Linux for a given load, a figure they cite from Heiser et al. 2025 ([Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md)) and that they did not measure here.

## How

The driver was ported from C to Pancake. The device is modelled in Viper as methods whose loads return any value allowed by the `ensures` clauses, so the proof must hold for every such value. The state is the transmit and receive descriptor rings, each split into integer sequences for addresses, lengths and bitfields. The neighbouring OS components are modelled the same way, with the shared queues treated as non-deterministic (§3.3, §4.1, §4.3). Machine words become unbounded integers, and bit masks are rewritten to modulo operations to keep SMT queries fast (§3.1). Everything but the shared regions is encoded as an array of words (§3.2). The evaluation compares the verified Pancake driver with the C driver on one board.

## Limits

The authors state (§2.4, §3, §6):

- The transpiler is not yet verified, so it is in the trusted base: a mistake in it could yield a Viper query that proves true although the Pancake property is false. They are working on a proof in HOL4. The Viper tool chain and the SMT solvers are trusted as well.
- There is no single theorem linking the driver proof with the compiler theorem; the authors say the compiler "should preserve" the verified properties, and a unified statement is future work.
- The compiler proof accounts only for the `main` entry point. The driver needs several entry points and re-entry; the proof does not cover them yet, though the authors say the verified properties include behaviour after re-entry.
- The proofs trust the device to meet its contract, including a valid initial state, and trust the neighbouring components to keep the queue protocols with the driver as the only consumer or producer. Nothing here verifies the hardware.
- The compiler proof trusts HOL4, the Arm ISA specification as implemented by the CPU, and an unverified linker.
- The kernel is trusted. seL4 is verified not to crash, Microkit's main loop is verified free of undefined behaviour, and the individual system calls Microkit relies on are not yet verified (§6.1).
- Concurrency and thread safety beyond the single-threaded driver are left to future work (§6.1, §6.2). Error messages refer to the Viper code, some annotations are written by hand, and the VS Code environment lacks support for the separate device model (§6.3).
- The authors say the driver will be offered in LionsOS "soon" (§1) as a choice of network drivers beside the C version (§4.1).

A careful reader adds the following.

- Nothing here says what the properties exclude. Our reading, there is no functional specification of the NIC's networking behaviour beyond the four classes. Data integrity is about addresses and lengths of buffers, not packet contents, which the driver never sees.
- The result covers a single driver, device and board. The performance result comes from a single echo workload at a clock the authors set to 1 GHz; they say a low clock rate magnifies software overhead.
- The text gives "around 10 per cent" for CPU and does not state a worst-case latency. Our reading, that fits an average-case comparison and says nothing about a timing bound, which a motion loop would need.
- The text gives three person-months. [SMT-based Deductive Verification of Device Drivers](https://silentzero.ooo/wiki/sources/2026-tyler-smt-based-deductive.html.md), a later paper on a Pancake Ethernet driver, gives 11.5 person-weeks with 1,501 lines of annotations and 10 to 20 per cent more driver CPU. Our reading, the two papers do not say whether they describe the same driver, and the figures do not line up, so we keep them apart.
- The 1,057 CVEs and the 19 per cent concurrency share of Linux driver bugs are cited from other sources (§1, §2.1.1); we did not check them.
- A preprint; the text names no peer-reviewed venue.

## Against the wiki

- [SMT-based Deductive Verification of Device Drivers](https://silentzero.ooo/wiki/sources/2026-tyler-smt-based-deductive.html.md): **extends** it from the other side. That paper reports the proof of a Pancake Ethernet driver for LionsOS. This one gives the language, the compiler and the transpiler behind it, with its own effort and overhead figures (above). Our reading: it is likely the same line of work; neither text says whether they describe one driver, and this one never mentions the other.
- [The seL4 Device Driver Framework](https://silentzero.ooo/wiki/sources/2022-parker-sel4-device-driver.html.md): **confirms** the design the proof rests on. The single-threaded driver and the lock-free single-producer, single-consumer queues are the interface the model captures (§4.1).
- [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md): **extends** the statement that a Pancake Ethernet driver is verified. Here the authors say the driver "will be made available" for LionsOS as a choice beside the C one; whether it has shipped is not stated.
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md) and [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md): **confirm** the division of labour. The driver proof stands on the kernel and Microkit proofs without covering them (§6.1). The text also quotes $350 per line for the seL4 C proof (from Klein et al. 2009), as the reason to seek a simpler language.
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md): related. The authors mention a separate attempt to verify Rust drivers with Verus and say that without a formal semantics for Rust or a verified compiler, end-to-end assurance for such drivers "seems remote" (§7). They add that Pancake is not meant to replace Rust (§2.1.1).
- [IOMMU](https://silentzero.ooo/wiki/concepts/iommu.html.md): **no contact**. The text does not discuss the IOMMU or DMA protection. It models the NIC's DMA descriptor rings and says the Ethernet device is documented not to touch the ring indices (§7). Our reading, the proof cannot say whether the device writes outside its buffers.

## For Silent Zero

- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md): no change of state. The page's row on the Pancake driver stays *proven* with the listed trusted parts. This source adds the language and compiler behind it. Our reading: the trusted parts overlap with those in the later paper in the transpiler, Viper and the solvers, while this paper lists others, such as HOL4 and the unverified linker; and the proof is on the driver's source, with the compiler theorem covering the binary only by the argument in §6.1, not by one theorem. The paper's Section 5 phrase "verified with automated proofs" fits that.
- Our reading, the proof covers the driver's use of its device registers and queues. The IOMMU and DMA, which the page marks as assumed, remain outside it. For a motion bus (serial, CAN, I²C) the method would have to be repeated; the page already lists that as open, and this source offers no such driver.
- [The static system](https://silentzero.ooo/wiki/design/static-system.html.md): our reading, the Pancake driver is a component of a LionsOS system, which the wiki describes as static. Nothing here changes what the page says about Microkit.

## Related pages

- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md)
- [The static system](https://silentzero.ooo/wiki/design/static-system.html.md)
- [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md)
- [IOMMU](https://silentzero.ooo/wiki/concepts/iommu.html.md)
- [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md)
- [Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md)
- [SMT-based Deductive Verification of Device Drivers](https://silentzero.ooo/wiki/sources/2026-tyler-smt-based-deductive.html.md)
- [The seL4 Device Driver Framework](https://silentzero.ooo/wiki/sources/2022-parker-sel4-device-driver.html.md)
