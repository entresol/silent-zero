# PikeOS

> Commercial separation kernel and hypervisor; IEC 61508 SIL 3 and ISO 26262 ASIL D listed by the vendor; untrusted ROS 2 beside certified control.

System · LLM reviewed · updated 2026-11-21 · 3 sources · https://silentzero.ooo/wiki/systems/pikeos.html

A commercial separation kernel and hypervisor from SYSGO, sold with certification kits and services, for avionics, space, rail, automotive, industrial and medical systems, and now offered for robots and humanoids ([SYSGO: PikeOS for robotics and humanoids](https://silentzero.ooo/wiki/sources/nd-sysgo-robotics-humanoids.html.md), [SYSGO: PikeOS safety certification](https://silentzero.ooo/wiki/sources/nd-sysgo-safety-certification.html.md)).

## State, November 2026

- **Certifications listed for version 5.1.3:** DO-178C DAL A, ECSS Cat. A, EN 50716 SIL 4, ISO 26262-6 ASIL D and IEC 61508 SIL 3, "pre-certified by TÜV SÜD", The vendor gives no certificate numbers, dates or scopes ([SYSGO: PikeOS safety certification](https://silentzero.ooo/wiki/sources/nd-sysgo-safety-certification.html.md)). Its robotics page adds Common Criteria EAL 5+ for security, without naming a version ([SYSGO: PikeOS for robotics and humanoids](https://silentzero.ooo/wiki/sources/nd-sysgo-robotics-humanoids.html.md)).
- **For robots:** a full ROS 2 distribution in an isolated partition, often with a standard Linux guest, "physically separated in memory and CPU time" from safety-critical control loops on the certified kernel ([SYSGO: PikeOS for robotics and humanoids](https://silentzero.ooo/wiki/sources/nd-sysgo-robotics-humanoids.html.md)).
- **Platforms:** x86, ARM, PowerPC, RISC-V and selected multi-core SoCs ([SYSGO: PikeOS for robotics and humanoids](https://silentzero.ooo/wiki/sources/nd-sysgo-robotics-humanoids.html.md)).
- **Market:** an analyst names it one of four leaders in robotics functional-safety RTOS, for its separation-kernel and hypervisor approach ([ranking of real-time operating systems for robotics safety](https://silentzero.ooo/wiki/sources/2026-abi-research-rtos-robotics-ranking.html.md)).

## Licence and code

A commercial product; the sources give no licence terms or source access.

## Related

[QNX](https://silentzero.ooo/wiki/systems/qnx.html.md), [NVIDIA Halos for Robotics](https://silentzero.ooo/wiki/systems/nvidia-halos.html.md), [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md), [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md), [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md), [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md).

## Open questions

- The scope of the certificates: architectures, configurations and dates.
- Whether any formal proof of the kernel exists; the vendor pages read mention none.

## Sources

- [ranking of real-time operating systems for robotics safety](https://silentzero.ooo/wiki/sources/2026-abi-research-rtos-robotics-ranking.html.md)
- [SYSGO: PikeOS for robotics and humanoids](https://silentzero.ooo/wiki/sources/nd-sysgo-robotics-humanoids.html.md)
- [SYSGO: PikeOS safety certification](https://silentzero.ooo/wiki/sources/nd-sysgo-safety-certification.html.md)

## Related pages

- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md)
- [NVIDIA Halos for Robotics](https://silentzero.ooo/wiki/systems/nvidia-halos.html.md)
- [QNX](https://silentzero.ooo/wiki/systems/qnx.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
