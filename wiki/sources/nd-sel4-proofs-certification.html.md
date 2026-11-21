# seL4 Foundation: seL4 proofs and certification

> The seL4 Foundation on proof and certification: beyond EAL 7 and ASIL-D evidence by its reading, no certificate named, Isabelle/HOL not yet DO-178C qualified. position, full text.

Source · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/nd-sel4-proofs-certification.html

seL4 Foundation. "seL4 Proofs & Certification", a page of sel4.systems, undated, read on 21 November 2026. [Page](https://sel4.systems/Verification/certification.html). Read in full. The foundation's own argument; it advocates for its kernel.

## What it shows

- **Three terms kept apart.** Verification builds assurance that a system meets its intended behaviour, and formal verification gives the highest level of it. Certification is "a process to assess a system against a pre-existing standard", with verification typically a key component among other requirements. Certifying an seL4-based product in a critical sector "requires addressing a number of requirements".
- **Common Criteria EAL 7.** The page says EAL 7 requires a formal model of the security policy, a functional specification and a design specification with formal correspondence between them, but only an informal mapping from the design to the implementation, while seL4 has a formal proof down to the implementation. It adds that formal modelling is required only from EAL 6, and that using seL4 "does not automatically solve all security objectives".
- **ISO 26262.** The standard recommends formal methods for the highest integrity levels, ASIL-C and ASIL-D, and in it "only the specification is mandated to be formal". The page says the strength of seL4's proofs is "considerably higher than what ISO26262's highest level, ASIL-D, requires".
- **DO-178C.** The page says the proofs provide, "with the strength of mathematical proofs", evidence for objectives at Level A on requirements, architecture and partitioning, and points to the supplement DO-333 on formal methods. On tool qualification (DO-330) it argues that no code is generated from Isabelle/HOL into seL4, and states: "to our knowledge Isabelle/HOL has not been qualified yet for a DO-178C certification", which it thinks it "should be well able" to meet.

## How

A position text with a figure and tables of the standards' requirements. No evidence of any assessment of a product.

## Limits

The page names no certificate and no certified product, and it does not use the word "certificate". It does not mention IEC 61508 or ISO 13849, the standards of the robotics sources in the wiki ([Halos for Robotics, the announcement](https://silentzero.ooo/wiki/sources/2026-nvidia-announces-halos-robotics.html.md), [SYSGO: PikeOS safety certification](https://silentzero.ooo/wiki/sources/nd-sysgo-safety-certification.html.md)). Its readings of what each standard requires are the foundation's own. It is undated.

## Against the wiki

- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md): **extends** with the foundation's account of what the proofs mean for certification, and its statement on tool qualification.
- [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md): **extends**; the page treats the proofs as evidence for standards, not only as a security argument.
- [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md): **creates** its central source on the relation between a proof and a certificate.

## For Silent Zero

It supports a careful statement: the proofs are strong evidence, and the way from evidence to a certificate for a product is separate and open. Our reading: nothing on the page says an seL4-based product is certified to a robotics standard.

## Related pages

- [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md)
- [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [Halos for Robotics, the announcement](https://silentzero.ooo/wiki/sources/2026-nvidia-announces-halos-robotics.html.md)
- [SYSGO: PikeOS safety certification](https://silentzero.ooo/wiki/sources/nd-sysgo-safety-certification.html.md)
