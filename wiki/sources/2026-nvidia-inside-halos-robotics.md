---
type: source
id: 2026-nvidia-inside-halos-robotics
status: reviewed
read: full
kind: report
sources: [2026-nvidia-inside-halos-robotics]
updated: 2026-11-21
---

# NVIDIA 2026: Inside Halos for Robotics

Suhas Hariharapura Sheshadri, Riccardo Mariani, Samuel Ochoa, Deep Rodge and Sarah Todd (NVIDIA). "Inside NVIDIA Halos for Robotics: A Full-Stack Functional Safety System for Physical AI", NVIDIA Technical Blog, 22 June 2026. [Page](https://developer.nvidia.com/blog/inside-nvidia-halos-for-robotics-a-full-stack-functional-safety-system-for-physical-ai/). Read in full. A vendor's technical description; every claim is NVIDIA's.

## What it shows

- **Heritage, in NVIDIA's figures.** More than 18,000 engineering years on vehicle safety, over 7 million lines of safety-assessed code and more than 30 certificates and assessment reports. The same development process, tools and foundational standards are said to carry over from the car (ISO 26262) to the robot (IEC 61508, ISO 13849), with third-party assessments by TÜV SÜD and TÜV Rheinland said to "confirm compliance across both domains". The post says NVIDIA convenes work on IEC 61508 and on ISO/IEC TS 22440, an emerging standard for functional safety and AI.
- **Hardware.** IGX Thor carries a Functional Safety Island described as "IEC 61508 SIL 3 capable", with its own I/O, power and clocks, "physically isolated from the main compute domain"; over 22,000 safety mechanisms; features for freedom from interference such as an SMMU in the CPU complex and the GPU, and NOC firewalls ([[iommu]]). The Holoscan Sensor Bridge carries an end-to-end IEC 61508 SIL 2 safety protocol.
- **Software.** Halos Core is "the next generation of NVIDIA DriveOS and certified to automotive safety standards"; the post names no certificate or body for that sentence. Two configurations are in early access: Linux, and Linux plus QNX. In the second an "NV Hypervisor" splits the board into virtual machines, "a Linux VM for AI and application workloads, and a QNX VM for safety-critical functions", ; the post says including QNX "enables stronger software partitioning for higher safety integrity use cases" ([[qnx]]). Robotics middleware and Halos Infra tools are "available but not yet for safety applications".
- **An outside-in safety blueprint (open source).** External cameras feed an AI perception pipeline; a monitor flags inputs that leave what the model was trained for, an integrator fuses events and discards stale ones, and a decision maker, a finite state machine on the Functional Safety Island, sends safe-stop signals, changes speed or mutes the robot's onboard safety when the area is confirmed clear. A reference case, automated trailer loading, is "a safety concept inspected by TÜV Rheinland". The post says the blueprint provides documentation support for ISO/IEC TR 5469 and the upcoming TS 22440.
- **The inspection lab.** An ISO/IEC 17020 inspection body accredited by ANAB. A partner asks the lab to inspect its integration; NVIDIA's experts assess it against pre-assessed Halos elements and issue an Inspection Certificate and Report; the partner takes that to a certification agency (TÜV Rheinland, TÜV SÜD, SGS, exida, CertX or UL Solutions) "to obtain final system certification". NVIDIA says this cuts time and cost, with no figures.

## How

A product description with architecture figures, a reference use case and an account of the process. It reports no measurement of the safety function and no evaluation of the AI monitor.

## Limits

An application note on safety is "available under NDA", and the architecture documents are for registered developers, so the design cannot be checked from public text. A careful reader adds: "certified" statements name no certificate; the claims of reduced time and cost are unsupported; the post does not say whether Halos Core's source is open; and it describes no authority model for the AI side beyond the partition and the decision maker.

## Against the wiki

- [[safety-path]]: **extends**. The decision maker is a finite state machine on an isolated safety island, fed by AI perception. Our reading: this is the shape of a [[simplex]] split, "AI proposes, a simple part decides"; the post claims no proof of the decision logic.
- [[mixed-criticality]]: **extends**. A hypervisor, not a microkernel's own mixed-criticality scheduling, separates the Linux and the safety VM; our reading: a different route to the same separation.
- [[sel4]]: nothing contradicts it; the post claims no formal proof.

## For zOS

It is the closest commercial neighbour of the safety path and was missing from the wiki. It is bound to NVIDIA hardware, and the post describes its assurance through inspection and a certification process, with no proof claimed. See [[nvidia-halos]], [[safety-certification]].
