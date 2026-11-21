---
type: system
status: reviewed
sources: [2026-qnx-nvidia-deepen-collaboration, 2026-nvidia-inside-halos-robotics, 2026-abi-research-rtos-robotics-ranking]
short: Commercial microkernel RTOS for safety systems
updated: 2026-11-21
---

# QNX

A commercial microkernel real-time operating system from QNX, a division of BlackBerry. QNX OS for Safety 8.0 is the safety-oriented product ([[2026-qnx-nvidia-deepen-collaboration]]).

## State, April to November 2026

- QNX OS for Safety 8.0 was integrated with NVIDIA IGX Thor and the Halos safety stack, announced on 20 April 2026, for robots, medical devices and industrial systems ([[2026-qnx-nvidia-deepen-collaboration]]).
- In NVIDIA's Halos Core configuration with QNX, a QNX virtual machine under a hypervisor carries the safety-critical functions while a Linux VM carries AI and applications. NVIDIA calls QNX "a real-time operating system with a long pedigree in certified safety systems" ([[2026-nvidia-inside-halos-robotics]], [[nvidia-halos]]).
- An analyst ranking of April 2026 names QNX as the leader among commercial real-time operating systems for robotics functional safety, for its microkernel architecture, safety certifications and ecosystem ([[2026-abi-research-rtos-robotics-ranking]]).

## Licence and code

The sources do not give licence terms. Our reading: a commercial product sold by QNX; the pages read describe early access for select customers.

## Related

[[pikeos]], [[nvidia-halos]], [[mixed-criticality]], [[safety-path]], [[safety-certification]].

## Open questions

- Which safety levels the product holds, and for which configuration on IGX Thor; the release names none ([[2026-qnx-nvidia-deepen-collaboration]]).
- Whether any formal proof of the QNX kernel exists; none is mentioned in the sources.
