---
type: source
id: 2026-bower-cohesix-research-operating
status: drafted
read: partial
kind: report
sources: [2026-bower-cohesix-research-operating]
updated: 2026-10-31
---

# Bower 2026: Cohesix, a research operating system for edge AI

Lukas Bower, project documentation page. [Page](https://lukeb-aidev.github.io/cohesix/). Read from the landing page as saved on 23 October 2026; the architecture, security, status and build-plan pages it links were not read.

## What it shows

- **Idea.** An AI fleet should have "air-traffic control" rather than tools holding unrestricted credentials. Each *hive* has one Queen, the central orchestration authority, and narrow Worker roles for heartbeat telemetry, GPU lease and status records, and LoRA adapter and model lifecycle records.
- **Kernel.** seL4 is the kernel foundation. The page says seL4's proofs "apply under documented assumptions" and that they "do not make Cohesix as a whole formally verified".
- **Authority.** Kernel-enforced capabilities combined with generated role, policy, ticket and lifecycle checks; Worker tickets are mandatory, Queen tickets optional. Models, agents and operators submit intent through approved host tools, and target-side checks decide what is accepted and keep evidence of the outcome ("AI can propose; Cohesix decides").
- **Interface.** Control and state appear as a bounded, role-visible tree of named paths, after Plan 9; the host server speaks a bounded subset of 9P2000.L called Secure9P. On a target the same namespace is reached through an authenticated console, with its own text protocol, not 9P on the wire.
- **Size and scheduling.** The selected QEMU and Raspberry Pi 4 profiles each admit 256 passive Worker instances in three executable roles, served by two bounded executor lanes. Workers run on scheduling contexts donated by calls.
- **Hardware.** On the Pi 4, physical devices run in manifest-declared Rust driver runtimes admitted through a hardware abstraction layer; the root task does not own their steady-state drivers.
- **Release.** Cohesix 1.2.0 is named the latest release, for a Mac or Linux host with a QEMU or Pi 4 target. Direct TCP to the console is authenticated but not encrypted.
- **Authorship.** The page says OpenAI Codex wrote the Cohesix-specific code and the author directed the design and gave final approval.

## How

A documentation landing page: statements of design and scope, a diagram, videos and install instructions. It gives no measurements and no test results.

## Limits

What the page says itself: it separates building, flashing, booting, device readiness, raw TCP, authenticated console and benchmark results as "separate proof states", and says that a role's declaration in a target profile is not evidence that a particular QEMU or Pi run created or accepted its tasks. Cohesix is not a general-purpose, POSIX or in-VM GPU system; the AI stack, models and training stay on host operating systems.

A careful reader adds:

- **Design statements, not results.** Which of the stated checks hold on a running target is on pages not read here.
- **Partial reading.** Anything about the kernel configuration (whether MCS, whether a verified one), IOMMU use, timing or real-time behaviour is unknown from this page.
- **One author, public project page.** No independent evaluation appears on the page.

## Against the wiki

- [[cohesix]]: created with this source.
- [[broker]]: a neighbouring design for the same job, with the decision made on the target and the agent held outside; see its Related section.
- [[raspberry-pi]]: names the Pi 4 as a target.

## For zOS

The paper (Section 2) lists Cohesix among agent operating systems on seL4 that coordinate edge AI fleets (Bower 2026). The page says the design is for coordinating hives of GPU-backed AI systems, so the wording fits as design intent, not as evidence of operation. The paper's further point, that no such project names real-time control as its goal, is consistent with this page, which mentions scheduling contexts but states no real-time aim; the unread pages could say more. No `design/` page changes state.
