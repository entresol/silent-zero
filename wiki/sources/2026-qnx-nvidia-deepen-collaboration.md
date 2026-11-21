---
type: source
id: 2026-qnx-nvidia-deepen-collaboration
status: reviewed
read: full
kind: report
sources: [2026-qnx-nvidia-deepen-collaboration]
updated: 2026-11-21
---

# QNX 2026: QNX and NVIDIA deepen their collaboration

QNX, a division of BlackBerry Limited. "QNX and NVIDIA Deepen Collaboration to Advance Safety-Critical Edge AI Across Robotics, Medical, and Industrial Systems", press release, Hannover, 20 April 2026 (via Newswire.com). [Page](https://www.newswire.com/news/qnx-and-nvidia-deepen-collaboration-to-advance-safety-critical-edge-ai-across). Read in full. A vendor statement.

## What it shows

- **QNX OS for Safety 8.0 is integrated with NVIDIA IGX Thor and its Halos safety stack.** Developers can "consolidate real-time controls and safety concepts on a deterministic, microkernel-based RTOS while using NVIDIA accelerated compute for AI-driven capabilities such as perception, planning, and decision-making". The release calls it a "unified mixed-criticality approach" that "supports safety certification processes".
- **Targets.** Autonomous mobile robots, humanoids, surgical robotics, medical imaging and industrial automation. It extends an earlier QNX integration with the NVIDIA DRIVE AGX Thor development kit for vehicles.
- **Availability.** Early-access registration for the IGX Thor developer kit with QNX is open to select customers.
- **QNX's own figures.** Its software runs in more than 275 million vehicles, and nine of the top ten medical-device manufacturers use it (company description in the release).

## How

A press release with a quotation from QNX's president. It describes no architecture; the NVIDIA technical blog ([[2026-nvidia-inside-halos-robotics]]) shows how the QNX configuration is laid out.

## Limits

The release names no safety level, no certificate and no body: "supports safety certification processes" is its only statement on the subject. It describes no measurement. The figures on vehicles and device makers are QNX's.

## Against the wiki

- [[mixed-criticality]]: **extends** with a commercial microkernel RTOS used for the safety side of a mixed-criticality platform ([[qnx]]).
- [[safety-path]]: **extends** together with [[2026-nvidia-announces-halos-robotics]].

## For zOS

It shows the safety side of a robot being offered on a microkernel RTOS beside NVIDIA compute for the AI side; the Halos blog ([[2026-nvidia-inside-halos-robotics]]) lays both out as virtual machines on one board. The paper does not name it. See [[qnx]] and [[nvidia-halos]].
