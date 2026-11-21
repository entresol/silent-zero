# Halos for Robotics, the announcement

> Halos for Robotics, the launch: IGX Thor, Halos OS, an ANAB-accredited inspection lab, Agility as first adopter; readiness inspection, no robotics certificate. report, full text.

Source · NVIDIA 2026 · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/2026-nvidia-announces-halos-robotics.html

NVIDIA. "NVIDIA Announces Halos for Robotics, the Industry's First Full-Stack Safety System for Physical AI", press release of 22 June 2026, NVIDIA Newsroom. [Page](https://nvidianews.nvidia.com/news/nvidia-announces-halos-for-robotics-the-industrys-first-full-stack-safety-system-for-physical-ai). Read in full. A vendor statement; the figures and the word "proven" are NVIDIA's own.

## What it shows

- **A safety stack for robots, in three layers.** NVIDIA IGX Thor and the Holoscan Sensor Bridge give "built-in safety" and sensor connectivity; Halos OS is the software stack, with Halos Core "to support safety-related operating functions" and safety applications built with the Halos Outside-In Safety Blueprint; and the Halos AI Systems Inspection Lab helps partners prepare an integration for third-party certification. NVIDIA presents it as the extension of its automotive safety stack to robots and calls it "the industry's only full-stack, open robotics safety system" (news summary; "A Full-Stack Foundation for Robot Safety").
- **Certification is under way, and none is claimed for robots.** TÜV Rheinland "is inspecting" IGX Thor, Halos OS and the sensor bridge "for functional safety certification readiness", building on TÜV SÜD's inspection of the Thor SoC and Halos Core for ISO 26262 ("A Robotics Safety Ecosystem Built for Scale").
- **The lab prepares partners for certification.** NVIDIA describes the lab as the world's first program for functional and AI safety for physical AI accredited by ANAB, and names TÜV Rheinland, UL Solutions, TÜV SÜD, exida, SGS and CertX as certification bodies that recognise it. It reports "more than 40 companies" taking part.
- **First adopter.** Agility puts IGX Thor and Halos Core into its safe-human-detection system for the humanoid Digit and will use the lab to check that Digit meets "rigorous standards such as IEC 61508, ISO 13849 and ISO/IEC TR 5469 before final third-party certification". The release says Agility's customers include Amazon, GXO, Schaeffler and Toyota Motor Manufacturing Canada.
- **Availability.** Halos Core for IGX is in early access for registered developers, in a Linux configuration and a Linux plus QNX OS for Safety 8.0 configuration. The Outside-In Safety Blueprint is open source and in early access on GitHub ("Availability"). Acontis, FreeRTOS and QNX are named for "the real-time operating environment".

## How

A press release. It gives the layers and the partners and no design detail, measurement or evaluation; the technical blog ([Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md)) gives the architecture.

## Limits

NVIDIA's closing notice says that many of the products and features "remain in various stages" and will be offered "when-and-if-available", and that the statements are not a commitment. A careful reader adds: the release says the system is open and states open source only for the blueprint, and it does not say that the source of Halos Core is open; early access is for registered developers. "Proven" and the engineering-years figure are NVIDIA's claims. Inspection for readiness is not a certificate.

## Against the wiki

- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): **extends** with a product from a vendor that, in the release's words, "unifies AI compute and safety"; the separation into a safety island and virtual machines is in [Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md). Our reading: it is the commercial form of a [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md)-style split, the split the paper's Section 4 builds on.
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md): **extends** with a commercial stack that names a safety RTOS beside Linux ([QNX](https://silentzero.ooo/wiki/systems/qnx.html.md)).

## For Silent Zero

The paper and the wiki did not name this stack. It bears on the [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md) page and on the paper's discussion of alternatives to Silent Zero. Nothing in the release claims a formal proof, a capability model for agents or an authority layer; see [NVIDIA Halos for Robotics](https://silentzero.ooo/wiki/systems/nvidia-halos.html.md) and [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md).

## Related pages

- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md)
- [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md)
- [NVIDIA Halos for Robotics](https://silentzero.ooo/wiki/systems/nvidia-halos.html.md)
- [QNX](https://silentzero.ooo/wiki/systems/qnx.html.md)
- [Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md)
- [QNX and NVIDIA deepen their collaboration](https://silentzero.ooo/wiki/sources/2026-qnx-nvidia-deepen-collaboration.html.md)
- [seL4 Foundation: seL4 proofs and certification](https://silentzero.ooo/wiki/sources/nd-sel4-proofs-certification.html.md)
