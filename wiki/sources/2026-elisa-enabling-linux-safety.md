---
type: source
id: 2026-elisa-enabling-linux-safety
status: reviewed
read: full
kind: report
sources: [2026-elisa-enabling-linux-safety]
updated: 2026-11-24
---

# ELISA 2026: NVIDIA joins as a premier member

ELISA project (Linux Foundation). "Enabling Linux in Safety Applications (ELISA) Project Expands Premier Membership with NVIDIA", press release, San Francisco, 26 February 2026. [Announcement](https://elisa.tech/announcement/2026/02/26/enabling-linux-in-safety-applications-elisa-project-expands-premier-membership-with-nvidia/). Read in full; it is a short press release, so the page says what the project says about itself and nothing more.

## What it shows

- **What ELISA is.** "An open source initiative focused on creating a shared set of elements, processes, and tools to help companies develop and certify Linux-based safety-critical applications and systems", hosted by the Linux Foundation.
- **The news.** NVIDIA joined as a premier member and "will contribute to advancing the use of Linux in safety-critical and regulated systems". The two existing premier members are Boeing and Red Hat.
- **Who else is in.** The release lists general members (among them Arm, Bosch, Canonical, Codethink, Elektrobit, Honda, Huawei, Linutronix, Lynx Software Technologies, Nissan and Wind River) and four associate members (Automotive Grade Linux, KernelCI, the Institute of Aircraft Systems Engineering and the Regensburg University of Applied Sciences).
- **Stated motive.** Software-defined and AI-enabled systems in automotive, robotics, industrial automation and aerospace make the safety, reliability and compliance of Linux-based platforms "more important than ever", in the release's own words. The Linux Foundation's Kate Stewart is quoted separately, on Linux as a foundation of software-defined systems and on NVIDIA's expertise.
- **An event.** A Safety-Critical Software track at Open Source Summit North America, Minneapolis, 18 to 20 May 2026.

## How

A vendor-neutral foundation's announcement. It contains no method, test, proof or certificate.

## Limits

The page says nothing on what ELISA has achieved technically: no kernel configuration, no evidence, no standard met, no certified product. A press release states intent and membership. Our reading: the source supports one thing for zOS, that an organised industry effort around hardened Linux for safety applications exists, with robotics named as a target. Whether any of it reaches a certificate for an AI robot is not in this source. The release also does not say what ELISA does not do; that is not in this source.

## Against the wiki

- [[safety-certification]]: **extends**. A new actor around certifying Linux-based systems; the source names no standard.
- [[preempt-rt]]: related. ELISA is the organised effort around Linux in safety use; the sources read here give no latency bound for either.
- [[nvidia-halos]]: related. NVIDIA is both a Halos vendor and now an ELISA premier member; the release does not connect the two.

## For zOS

The paper's Section 6 cites this release for the sentence that ELISA "works on making Linux usable in safety applications". The release supports that sentence: it says the project aims to help companies develop and certify such systems. [[safety-path]]: no change of state. The system page [[elisa]] records the project; the evidence about a certificate remains missing.
