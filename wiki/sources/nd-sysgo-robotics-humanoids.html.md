# SYSGO: PikeOS for robotics and humanoids

> PikeOS for robots: an untrusted ROS 2 and Linux partition separated in memory and CPU time from certified control; no proof mentioned. report, full text.

Source · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/nd-sysgo-robotics-humanoids.html

SYSGO. "Robotics & Humanoids", a page of the vendor's website, undated, read on 21 November 2026. [Page](https://www.sysgo.com/robotics). Read in full. A product page; its claims are SYSGO's.

## What it shows

- **PikeOS as a separation kernel and hypervisor for robots.** The page lists "separation kernel & partitioning for mixed-criticality applications", hard real-time performance with multi-core support, safety certifications ("DO-178C, IEC 61508, ISO 26262, and others"), a security certification (Common Criteria EAL 5+), Linux, POSIX and RTOS guests, and support for x86, ARM, PowerPC and RISC-V.
- **Untrusted AI beside certified control.** Under the heading "Running untrusted AI alongside certified Control", the page says a full ROS 2 distribution runs in an isolated partition, "often using a standard Linux guest OS", "physically separated in memory and CPU time from the Safety-critical real-time control loops, which run directly on PikeOS's certified RTOS kernel". The consequence it claims is that the processing demands of the ROS 2 partition "can never interfere" with the robot's safety and that "the need to certify the entire application" is eliminated.
- **Communication across levels.** A DDS transport in a secure partition is described as carrying commands from an untrusted Linux and ROS 2 application to a safety-certified control application.
- **Regulation.** The page claims readiness for the new EU Machinery Regulation and the AI Act.

## How

Marketing text of a product page. No architecture figure, measurement or case study.

## Limits

The page does not use the word "formal", and it mentions no formal proof of the kernel; its assurance rests on the certifications it lists, whose scope (which architectures, which configurations) it does not give here ([SYSGO: PikeOS safety certification](https://silentzero.ooo/wiki/sources/nd-sysgo-safety-certification.html.md)). It is undated.

## Against the wiki

- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): **extends**. This is the paper's split, a learned or untrusted side separated in memory and processor time from a certified control loop, offered as a product. Our reading: it answers the same problem as the safety path without a proof of the kernel.
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md): **extends** with a certified separation kernel that treats mixed criticality through partitions and a hypervisor.
- [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md), [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md): our reading: the paper's alternative to Silent Zero names hardened Linux routes; a certified separation kernel with Linux as a guest is a further alternative the wiki did not list.

## For Silent Zero

See [PikeOS](https://silentzero.ooo/wiki/systems/pikeos.html.md) and [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md). The page says nothing about authority for agents, only separation of partitions.

## Related pages

- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md)
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md)
- [PikeOS](https://silentzero.ooo/wiki/systems/pikeos.html.md)
- [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md)
- [SYSGO: PikeOS safety certification](https://silentzero.ooo/wiki/sources/nd-sysgo-safety-certification.html.md)
