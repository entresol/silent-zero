# Safety certification

> Proof versus certificate: what a certified kernel, a robot stack and seL4 each state; no certified seL4 product in the sources.

Concept · LLM reviewed · updated 2026-11-21 · 5 sources · https://silentzero.ooo/wiki/concepts/safety-certification.html

Certification is "a process to assess a system against a pre-existing standard", with verification typically a key component among other requirements ([seL4 Foundation: seL4 proofs and certification](https://silentzero.ooo/wiki/sources/nd-sel4-proofs-certification.html.md)). A proof of code and a certificate for a product are different things: our reading is that the proof is evidence and the certificate is the result of an assessment against a standard. The sources name IEC 61508 (listed for industrial automation), ISO 13849, ISO 26262 (road vehicles) and DO-178C (airborne software). In NVIDIA's account the final system certificate comes from a third-party certification agency.

## State, November 2026

- **A certified separation kernel exists as a product.** SYSGO lists PikeOS 5.1.3 for DO-178C DAL A, ISO 26262-6 ASIL D, IEC 61508 SIL 3 and others, pre-certified by TÜV SÜD; it gives no scopes ([SYSGO: PikeOS safety certification](https://silentzero.ooo/wiki/sources/nd-sysgo-safety-certification.html.md), [PikeOS](https://silentzero.ooo/wiki/systems/pikeos.html.md)).
- **A robot stack is on the way to certification.** TÜV Rheinland is inspecting NVIDIA's Halos for Robotics for certification readiness, and TÜV SÜD has inspected the Thor chip and Halos Core for the automotive standard ISO 26262. NVIDIA's lab issues an inspection certificate that a partner takes to a certification body for the final system certificate. No robotics certificate is claimed in the sources ([Halos for Robotics, the announcement](https://silentzero.ooo/wiki/sources/2026-nvidia-announces-halos-robotics.html.md), [Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md), [NVIDIA Halos for Robotics](https://silentzero.ooo/wiki/systems/nvidia-halos.html.md)).
- **seL4 has proofs and no certificate named.** The seL4 Foundation argues that its proofs go beyond what Common Criteria EAL 7 and ISO 26262 ASIL-D require and fit DO-178C Level A evidence. Its page names no certificate or certified product and does not mention IEC 61508. It says Isabelle/HOL has, to its knowledge, not been qualified for DO-178C ([seL4 Foundation: seL4 proofs and certification](https://silentzero.ooo/wiki/sources/nd-sel4-proofs-certification.html.md), [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)).
- **A limit on proofs about the world.** An essay argues that proofs about AI systems in the physical world will stay approximate; it expects formal verification to help through proofs about approximate models ([limitations on formal verification for AI safety](https://silentzero.ooo/wiki/sources/2024-dickson-limitations-formal-verification.html.md)).

## Related

[Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md), [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md), [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md), [NVIDIA Halos for Robotics](https://silentzero.ooo/wiki/systems/nvidia-halos.html.md), [PikeOS](https://silentzero.ooo/wiki/systems/pikeos.html.md), [QNX](https://silentzero.ooo/wiki/systems/qnx.html.md).

## Open questions

- How a proof becomes evidence that a certification body accepts for a robot: the seL4 page argues the strength of the proofs standard by standard but states no accepted case for IEC 61508 or ISO 13849.
- Whether any seL4-based product holds a safety certificate; none appears in the wiki's sources.
- How a small open-source project would carry a certificate; none of the sources discusses it.

## Sources

- [Halos for Robotics, the announcement](https://silentzero.ooo/wiki/sources/2026-nvidia-announces-halos-robotics.html.md)
- [Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md)
- [limitations on formal verification for AI safety](https://silentzero.ooo/wiki/sources/2024-dickson-limitations-formal-verification.html.md)
- [seL4 Foundation: seL4 proofs and certification](https://silentzero.ooo/wiki/sources/nd-sel4-proofs-certification.html.md)
- [SYSGO: PikeOS safety certification](https://silentzero.ooo/wiki/sources/nd-sysgo-safety-certification.html.md)

## Related pages

- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [NVIDIA Halos for Robotics](https://silentzero.ooo/wiki/systems/nvidia-halos.html.md)
- [PikeOS](https://silentzero.ooo/wiki/systems/pikeos.html.md)
- [QNX](https://silentzero.ooo/wiki/systems/qnx.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [SYSGO: PikeOS for robotics and humanoids](https://silentzero.ooo/wiki/sources/nd-sysgo-robotics-humanoids.html.md)
