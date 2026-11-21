# two interfaces for seL4 kernel verification

> SeL4 verification abstract: hardware flushes made time-protection proofs feasible; system-call Hoare triples that userland proofs assume are not yet proved. progress, full text.

Source · Sison 2026 · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/2026-sison-two-interfaces-sel4.html

Rob Sison (UNSW Sydney). "Two interfaces for seL4 kernel verification: Time Protection and the Kernel-Userland Gap", extended abstract for a talk at the Isabelle Workshop 2026 (the venue is as listed in the pool). [Abstract](https://trustworthy.systems/publications/papers/Sison_26.abstract), [PDF](https://trustworthy.systems/publications/papers/Sison_26.pdf). Read: the full text and the reference list. It is an abstract, so most statements come without figures or a method. The talk itself was not read.

## What it shows

The author presents two case studies at the two ends of seL4's Isabelle/HOL specifications. Both describe ongoing work.

**Time protection (§1)**

- **The hardware-software contract.** Following Ge et al., every part of the microarchitectural state must be either spatially partitionable, given exclusively to one domain, or temporally partitionable. The latter means the OS makes the effects of the sender's actions deterministic before a context switch, by flushing and by padding until the worst-case execution time of the switch (§1, citing Ge et al. 2019).
- **What can be partitioned.** Off-core caches (L2, L3) can be partitioned by cache colouring, with costs the author names: a maximum number of colours fixed by the cache, regions of equal size in fixed positions, poor memory utilisation, a cost for shared kernel data, and a flush of all affected lines on a switch. On-core state (L1 caches, branch target buffer, TLB) cannot be partitioned, because it is small and indexed by virtual addresses (§1).
- **What hardware lacks.** Ge's thesis found that x86 and both Arm platforms it evaluated lacked a flush primitive for many on-core elements, sometimes without a way to disable the feature, leaving some channels impossible to close. x86 had no instruction to flush the L1 alone. No platform offered hardware support for waiting until a deterministic time, although software padding was measurably effective (§1).
- **The proof effort.** The group formalises these requirements and integrates them into seL4's correctness, security and refinement proofs in Isabelle/HOL, so as to prove that seL4 enforces time protection provided the hardware has primitives that meet them. The work also has to accommodate time-protected cross-domain communication against backwards flows, which is under development (§1).
- **Hardware primitives made verification feasible.** The author reports that dedicated primitives made verification feasible compared with software approaches for legacy hardware. Prefetching, which stands in for flushing, was found infeasible to verify without an accurate model of every cache's replacement policy. So the work also needs flexible flushes of chosen partitions of the off-core caches, without prefetching (§1).
- **A platform with all three.** With ETH Zürich the group now has the RISC-V platform Cheshire, built on CVA6, with `fence.t` (flushes all on-core state and pads until a configured time) and a dynamically partitionable last-level cache with a primitive that flushes partitions individually (§1). The author hopes the demonstration will make the value of the contract clear.

**The kernel-userland gap (§2)**

- **The gap.** seL4 is proved to refine an abstract specification, but nobody has proved that this specification meets the Hoare triples (precondition and postcondition) that the English descriptions in the seL4 reference manual imply for its system calls (§2).
- **Why it matters.** The verification of the user-level Microkit library's main handler loop by Paturel et al. (documented by Weibel et al.) shows userland verification is possible, assuming seL4 satisfies certain Hoare triples for its system calls. seL4 has never been verified to satisfy them (§2).
- **Blocking calls.** The author's investigation suggests ("apparently") that no OS kernel verification in the literature has verified such triples for system calls that block until another process acts. The example is `Recv`, which returns to the Microkit loop only after another process calls `Signal`. Of the two nearest cases the author names, Verve's Nucleus exported only nonblocking functions, and CertiKOS verified a call that blocks on I/O but not on another user process (§2).
- **The two tasks.** New lemmas about the existing abstract specification, more specific about the state a call concerns and also showing that the call changes no other state the caller can see. And a composition of these into one triple when a call spans several kernel entries: the blocking `Recv`, any finite sequence of unrelated kernel entries, and the final `Signal` (§2).
- **Progress.** Proofs are "almost complete for some motivating cases". Next come more system calls, first those the Microkit libraries use; in the long run the reference manual's descriptions would be formalised (§2).

## How

An abstract of two case studies. The author describes proof work in Isabelle/HOL on seL4's existing specifications, with student theses and a prior formalisation as the base (references 3, 4, 14, 17, 21, 22). There are no measurements and no results table; the abstract gives no figures.

## Limits

The author says the following.

- Both efforts are ongoing. The proofs for the gap are "almost complete" for "some motivating cases", not for the interface.
- Time-protection proofs hold "provided" the hardware has primitives meeting the requirements. Modern hardware is "largely missing at least some of the needed supporting features" (§1); the author names one platform that has them.
- The claim that no other kernel verification covers blocking system calls rests on the group's own investigation ("seems", "apparently").
- The abstract speaks of hope and expectation for the composition and for the hardware's value; these are not results.

A careful reader adds the following. This is inference.

- No result is shown, not even a count of lemmas or breakages; the abstract cannot be checked against evidence. The status of the time-protection proof (what is done, at which level) is not stated here; the earlier talk [Where are we with Time Protection?](https://silentzero.ooo/wiki/sources/2026-trustworthy-where-are-we.html.md) gives it.
- The statement that hardware primitives made verification feasible is the group's experience, given without a comparison that could be checked.
- Of the group's newest work the abstract cites three student theses (references 14, 17, 21), which are not peer-reviewed papers.

## Against the wiki

- [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md): **extends**. It confirms the page's scheme (partition, flush, pad) and names the spatial limits of off-core caches and the reasons on-core state cannot be partitioned. New: the author found prefetching-based flushing infeasible to verify, so the proof depends on real flush primitives, and the page's "not proven" state stands, since the abstract says the proofs are in progress.
- [Where are we with Time Protection?](https://silentzero.ooo/wiki/sources/2026-trustworthy-where-are-we.html.md): **consistent**. Both name the Cheshire platform with a partitionable last-level cache and the work on one-way communication. The abstract adds the argument about verifiability of prefetching, which the talk's slides state more briefly.
- [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md): **confirms** that `fence.t` on CVA6 is the flush primitive the group relies on; the abstract also cites the later `fence.t.s` and a further article by the same authors in IEEE Transactions on Computers (2023).
- [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md): **extends**. The page says properties proved about the abstract specification carry down to the C code. The abstract says what that does not yet give a userland programmer: the specification has not been shown to meet the Hoare triples the reference manual's text implies. Our reading: a correct kernel is not the same as a kernel proved to behave as the manual describes.
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md) and [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md): **extend**. The verification of the Microkit handler loop by Paturel et al. assumes triples about seL4 that are not proved.
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md): **consistent**. The page's table lists functional correctness as proven and time protection as implemented but unproven; neither changes.

## For Silent Zero

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md): no change of state. Our reading (an inference): a Silent Zero component verified on top of seL4 would rest on assumptions about system call behaviour that are not yet proved against the specification, and the abstract names the Microkit handler loop as an example. The abstract says nothing about Silent Zero.
- Our reading: the abstract supports the paper's caution that hardware must supply instructions for timing isolation, and CVA6 is such a platform. It gives no timeline for the proof.
- Our reading: a design that relies on a verified Microkit would depend on this work. Nothing in Silent Zero is built.

## Related pages

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md)
- [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md)
- [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md)
- [Where are we with Time Protection?](https://silentzero.ooo/wiki/sources/2026-trustworthy-where-are-we.html.md)
