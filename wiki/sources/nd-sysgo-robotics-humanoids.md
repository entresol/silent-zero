---
type: source
id: nd-sysgo-robotics-humanoids
status: reviewed
read: full
kind: report
sources: [nd-sysgo-robotics-humanoids]
updated: 2026-11-21
---

# SYSGO: PikeOS for robotics and humanoids

SYSGO. "Robotics & Humanoids", a page of the vendor's website, undated, read on 21 November 2026. [Page](https://www.sysgo.com/robotics). Read in full. A product page; its claims are SYSGO's.

## What it shows

- **PikeOS as a separation kernel and hypervisor for robots.** The page lists "separation kernel & partitioning for mixed-criticality applications", hard real-time performance with multi-core support, safety certifications ("DO-178C, IEC 61508, ISO 26262, and others"), a security certification (Common Criteria EAL 5+), Linux, POSIX and RTOS guests, and support for x86, ARM, PowerPC and RISC-V.
- **Untrusted AI beside certified control.** Under the heading "Running untrusted AI alongside certified Control", the page says a full ROS 2 distribution runs in an isolated partition, "often using a standard Linux guest OS", "physically separated in memory and CPU time from the Safety-critical real-time control loops, which run directly on PikeOS's certified RTOS kernel". The consequence it claims is that the processing demands of the ROS 2 partition "can never interfere" with the robot's safety and that "the need to certify the entire application" is eliminated.
- **Communication across levels.** A DDS transport in a secure partition is described as carrying commands from an untrusted Linux and ROS 2 application to a safety-certified control application.
- **Regulation.** The page claims readiness for the new EU Machinery Regulation and the AI Act.

## How

Marketing text of a product page. No architecture figure, measurement or case study.

## Limits

The page does not use the word "formal", and it mentions no formal proof of the kernel; its assurance rests on the certifications it lists, whose scope (which architectures, which configurations) it does not give here ([[nd-sysgo-safety-certification]]). It is undated.

## Against the wiki

- [[safety-path]]: **extends**. This is the paper's split, a learned or untrusted side separated in memory and processor time from a certified control loop, offered as a product. Our reading: it answers the same problem as the safety path without a proof of the kernel.
- [[mixed-criticality]]: **extends** with a certified separation kernel that treats mixed criticality through partitions and a hypervisor.
- [[preempt-rt]], [[landlock]]: our reading: the paper's alternative to zOS names hardened Linux routes; a certified separation kernel with Linux as a guest is a further alternative the wiki did not list.

## For zOS

See [[pikeos]] and [[safety-certification]]. The page says nothing about authority for agents, only separation of partitions.
