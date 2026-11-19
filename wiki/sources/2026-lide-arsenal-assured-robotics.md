---
type: source
id: 2026-lide-arsenal-assured-robotics
status: reviewed
read: partial
kind: report
sources: [2026-lide-arsenal-assured-robotics]
updated: 2026-11-19
---

# Lide 2026: ARSENAL

David Lide (Trusted Science and Technology). "Assured Robotics Embedded Systems and Applications in Ground Vehicles (ARSENAL)", a talk of 15 minutes at the seL4 Summit 2026, Vancouver, on 2 September 2026, in the track "seL4 In Use". [Session page](https://sel4summit2026.sched.com/event/2Prpd). Read: the abstract and speaker line on the session page. The attached slides were not read.

The talk concerns a project for military ground vehicles, a field the schema asks the team about before a source is worked in. The team decided on 2026-11-19 to work it in with this note. The page states what the abstract says and judges neither the use nor the project.

## What it shows

- **The problem as stated.** ROS, the Robot Operating System, was not designed for the performance and determinism, or the safety and security, that critical missions require. The Robotic Technology Kernel is a ROS-based autonomy library for Army platforms. The abstract says its stack of RTK over ROS over Linux carries Linux's large resource overhead and attack surface, so that an attacker may use a known Ubuntu vulnerability to gain a footing on a vehicle.
- **The plan.** ARSENAL is to give a modular, open ROS 2 stack on military embedded platforms, with seL4 as a separation kernel. Two configurations: Option 1 keeps the usual ROS 2 with DDS, the data distribution service, on a minimized Linux kernel on seL4; Option 2 runs DDS and ROS 2 on seL4, to run mission applications with minimal platform resource requirements.
- **Planned services.** Memory separation and process isolation, a data-flow monitor, intrusion detection and policy enforcement, and encryption of data exchanged between applications and between platforms, with TLS on the open transport layer. The abstract introduces them as capabilities the effort will have.
- **State.** The authors have analysed the design and made decisions, and have built a proof of concept for each option. Four thrusts remain: integrating DDS and ROS 2 on seL4, security capabilities, a move of the tooling from CAmkES to Microkit, and a capability demonstration.

## How

A conference abstract, written to propose the talk. It reports no measurements, no latencies and no proofs.

## Limits

A careful reader adds:

- **Plans, not results.** The security services are presented as planned capabilities, and one of the four remaining thrusts is developing them. The abstract says ARSENAL "will provide unprecedented, holistic security and resilience".
- **No timing figure.** It names latency as an example of mission requirements and says nothing about deadlines or determinism achieved.
- **Which kernel.** It does not say which seL4 configuration, whether MCS, or which hardware.
- **Slides unread.** The attached presentation may say more.

## Against the wiki

- [[sel4]]: an example of seL4 as a separation kernel under a robot stack, in a project that moves from CAmkES to [[microkit]].
- [[real-time-loops]]: no change. The abstract names determinism as a need and gives no figure.

## For zOS

Sections 2.4 and 5 of the paper: "a project for US Army unmanned ground vehicles has built proofs of concept that run ROS 2, the common robot middleware, on seL4 (Lide 2026)", and the table row "ROS 2 on seL4: proofs of concept for Army ground vehicles". Confirmed as far as the abstract goes: it reports a proof of concept for each of two configurations, which it defines as ROS 2 on seL4 (Option 1 with a minimized Linux kernel, Option 2 natively), and says integrating DDS and ROS 2 on seL4 is still to be completed. Our reading: the step from a proof of concept "of running ROS2 in reduced OS" to one on seL4 rests on those definitions. The abstract speaks of the Army and of DoD use cases, so "US" is the paper's wording. Section 6 cites the talk, with seL4's helicopter test, for ROS 2 on seL4 "being developed for US Army ground vehicles", which the abstract supports. The abstract names teleoperation, autonomy and swarm use cases and says nothing about weapons. No `design/` page changes state.
