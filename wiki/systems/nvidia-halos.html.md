# NVIDIA Halos for Robotics

> NVIDIA’s safety stack for robots: IGX Thor with a safety island, Halos Core with Linux or Linux plus QNX; inspected for certification readiness, no robotics certificate claimed.

System · LLM reviewed · updated 2026-11-21 · 3 sources · https://silentzero.ooo/wiki/systems/nvidia-halos.html

NVIDIA's safety stack for robots and humanoids, announced on 22 June 2026 as the extension of its automotive Halos stack. Its parts are the IGX Thor board with a safety island and the Holoscan Sensor Bridge, the Halos OS software with a safety operating system called Halos Core and safety blueprints, one of them open source, and an accredited inspection lab ([Halos for Robotics, the announcement](https://silentzero.ooo/wiki/sources/2026-nvidia-announces-halos-robotics.html.md), [Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md)).

## State, June 2026

- **Architecture.** Two configurations of Halos Core are in early access: Linux, and Linux plus QNX, where a hypervisor gives a Linux VM to AI and applications and a QNX VM to safety-critical functions ([Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md), [QNX](https://silentzero.ooo/wiki/systems/qnx.html.md)).
- **Certification.** TÜV Rheinland is inspecting the platform for "certification readiness"; TÜV SÜD has inspected the Thor chip and Halos Core for the automotive standard ISO 26262. No certificate for the robotics use is claimed in the sources. The blog says Halos Core is "certified to automotive safety standards" and that TÜV assessments confirm compliance in both domains, and names no certificate. The first adopter, Agility, plans to check its robot against standards such as IEC 61508, ISO 13849 and ISO/IEC TR 5469 before final third-party certification ([Halos for Robotics, the announcement](https://silentzero.ooo/wiki/sources/2026-nvidia-announces-halos-robotics.html.md)).
- **Safety logic.** The outside-in safety blueprint runs a finite state machine on the safety island that acts on events from AI perception ([Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md)).

## Licence and code

The Outside-In Safety Blueprint is open source (GitHub, early access). The sources say Halos Core is in early access for registered developers and do not give its licence; the safety application note is under NDA ([Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md)).

## Related

[PikeOS](https://silentzero.ooo/wiki/systems/pikeos.html.md), [QNX](https://silentzero.ooo/wiki/systems/qnx.html.md), [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md), [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md), [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md), [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md).

## Open questions

- Which parts of the stack will carry a certificate for robots, and when; the sources describe inspection and readiness.
- Whether Halos Core's source is open, and whether any proof underlies the safety island's logic or the hypervisor; the sources claim none.
- Whether an authority layer for AI agents exists inside the safety partition; the pages read describe none.

## Sources

- [Halos for Robotics, the announcement](https://silentzero.ooo/wiki/sources/2026-nvidia-announces-halos-robotics.html.md)
- [Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md)
- [QNX and NVIDIA deepen their collaboration](https://silentzero.ooo/wiki/sources/2026-qnx-nvidia-deepen-collaboration.html.md)

## Related pages

- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md)
- [ELISA](https://silentzero.ooo/wiki/systems/elisa.html.md)
- [PikeOS](https://silentzero.ooo/wiki/systems/pikeos.html.md)
- [QNX](https://silentzero.ooo/wiki/systems/qnx.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [NVIDIA joins as a premier member](https://silentzero.ooo/wiki/sources/2026-elisa-enabling-linux-safety.html.md)
