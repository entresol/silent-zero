# seL4, Formal Verification of an OS Kernel

> The first proof that seL4’s C code implements its specification; assumptions, cost, bugs found. proof, full text.

Source · Klein et al. 2009 · LLM reviewed · updated 2026-10-29 · https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html

Gerwin Klein, Kevin Elphinstone, Gernot Heiser, June Andronick and nine co-authors (NICTA, UNSW, Open Kernel Labs, ANU). SOSP 2009, Big Sky, October 2009. [PDF](https://trustworthy.systems/publications/papers/Klein_EHACDEEKNSTW_09.pdf).

## What it shows

- **A machine-checked proof that the C code implements the specification.** The authors prove in Isabelle/HOL that the C implementation of [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md) refines an abstract specification of its behaviour, through an executable specification generated from a Haskell prototype in between (§2.3, §4.5). They call it, to their knowledge, the first formal proof of functional correctness of a complete, general-purpose OS kernel (abstract). See [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md).
- **What follows from the proof.** Under the assumptions below, the kernel never crashes, never accesses a null or misaligned pointer, every assertion in it holds, and every system call terminates and returns to user level. Because the abstract interface is binary compatible with the implementation, argument checking is correct, and buggy or malicious arguments from user level cannot subvert the kernel (§4.5).
- **Every user program is covered.** User programs are modelled as fully non-deterministic, so the proof holds for benign, buggy and malicious ones alike (§4.5).
- **Size.** 8,700 lines of C and 600 lines of assembler (abstract). The abstract specification has 4,900 lines of Isabelle, the executable specification 13,000; the proof has about 200,000 lines including framework and libraries, and over 150 invariants were proved (Table 1, §4.5).
- **Cost.** Kernel design and implementation, including the Haskell prototype, took about 2.2 person-years. The proof took about 20 person-years, of which about 9 went into frameworks, tools and libraries and 11 into the seL4-specific proof. The authors expect a similar verification of a new kernel to cost about 6 person-years of proof, 8 in total (§5.2). These are estimates, not measurements of a repeat.
- **Bugs.** Before verification began in earnest, testing and use had found 16 defects in the C code; the C verification found another 144 (§5.2).
- **Performance.** A one-way IPC on the optimised C path took 224 cycles on an ARM1136 at 532 MHz, against 206 for OKL4's hand-written assembly path. The optimised path was not yet in the verified code base at the time (§5.1).
- **Design for verification.** An event-based kernel with a single kernel stack, interrupts mostly disabled and polled at a few preemption points, and drivers in user mode except the timer. The authors found these choices made the design simpler without costing performance (§3, §7).

## How

The team wrote a Haskell prototype that ran against a hardware simulator, translated it automatically into Isabelle as the executable specification, and wrote the C implementation by hand. Two refinement proofs link the three layers: abstract to executable, executable to C (Theorems 1 to 3). The C code is read into Isabelle under a formal semantics of a large subset of C99. The platform was ARMv6 on a Freescale i.MX31 (§4.5).

## Limits

The authors state the assumptions themselves (§4.4, §4.5):

- the compiler (GCC), the assembly code and the hardware are correct;
- cache and TLB maintenance are assumed correct and tested, not proved;
- about 1.2 kLOC of boot and initialisation code are outside the proof;
- in-kernel virtual memory is argued informally;
- the proof is for a single processor; multicore is left for future work (§3.3);
- the access-control security model was proved separately and not yet connected to this proof (§2.3).

They also note that the proof cannot show that the specification describes what a user expects (§4.5).

A careful reader adds: the result is from 2009, for ARMv6. Later work closed several of these gaps (binary verification, security proofs, other architectures); see [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md) and [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) for the state they report.

## Against the wiki

- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md): **extends** it with the origin of the proof, its assumptions and its cost. The wiki so far cited the proof only through [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md).
- [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md): created with this source.

## For Silent Zero

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md): this is the source of the paper's claim that the kernel's functional correctness is *proven*. It holds for the configuration it covers and under the assumptions above.
- The paper (Section 2.3) puts the first proof at "roughly 25 person-years" with a repeat "under ten", citing this source and a project page. This source gives about 22 (2.2 for the kernel, about 20 for the proof) and estimates 8 for a repeat. The project page gives about 25 in total, including documentation, and a repeat under ten ([Trustworthy Systems n.d.: Proof Statistics](https://silentzero.ooo/wiki/sources/nd-trustworthy-proof-statistics.html.md)). The paper's effort figures follow the project page.

## Related pages

- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md)
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md)
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)
- [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md)
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)
- [Trustworthy Systems n.d.: Proof Statistics](https://silentzero.ooo/wiki/sources/nd-trustworthy-proof-statistics.html.md)
