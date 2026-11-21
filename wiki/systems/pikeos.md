---
type: system
status: reviewed
sources: [nd-sysgo-robotics-humanoids, nd-sysgo-safety-certification, 2026-abi-research-rtos-robotics-ranking]
short: Commercial separation kernel and hypervisor
updated: 2026-11-21
---

# PikeOS

A commercial separation kernel and hypervisor from SYSGO, sold with certification kits and services, for avionics, space, rail, automotive, industrial and medical systems, and now offered for robots and humanoids ([[nd-sysgo-robotics-humanoids]], [[nd-sysgo-safety-certification]]).

## State, November 2026

- **Certifications listed for version 5.1.3:** DO-178C DAL A, ECSS Cat. A, EN 50716 SIL 4, ISO 26262-6 ASIL D and IEC 61508 SIL 3, "pre-certified by TÜV SÜD", The vendor gives no certificate numbers, dates or scopes ([[nd-sysgo-safety-certification]]). Its robotics page adds Common Criteria EAL 5+ for security, without naming a version ([[nd-sysgo-robotics-humanoids]]).
- **For robots:** a full ROS 2 distribution in an isolated partition, often with a standard Linux guest, "physically separated in memory and CPU time" from safety-critical control loops on the certified kernel ([[nd-sysgo-robotics-humanoids]]).
- **Platforms:** x86, ARM, PowerPC, RISC-V and selected multi-core SoCs ([[nd-sysgo-robotics-humanoids]]).
- **Market:** an analyst names it one of four leaders in robotics functional-safety RTOS, for its separation-kernel and hypervisor approach ([[2026-abi-research-rtos-robotics-ranking]]).

## Licence and code

A commercial product; the sources give no licence terms or source access.

## Related

[[qnx]], [[nvidia-halos]], [[sel4]], [[mixed-criticality]], [[safety-path]], [[safety-certification]].

## Open questions

- The scope of the certificates: architectures, configurations and dates.
- Whether any formal proof of the kernel exists; the vendor pages read mention none.
