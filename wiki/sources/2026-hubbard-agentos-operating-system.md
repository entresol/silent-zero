---
type: source
id: 2026-hubbard-agentos-operating-system
status: reviewed
read: full
kind: report
sources: [2026-hubbard-agentos-operating-system]
updated: 2026-11-01
---

# Hubbard 2026: agentOS, an operating system for agents on seL4

Jordan Hubbard, source repository and README. [Repository](https://github.com/jordanhubbard/agentos). Read as saved on 23 October 2026; the documents it links (TCB.md, ROADMAP.md) were not read.

## What it shows

- **Claim.** A bootable, capability-secured I/O and isolation platform on [[sel4]], which owns devices in user mode and hosts Linux and FreeBSD as virtio guests. QEMU is the prototype hardware. Guest-proven rows exist for Buildroot and Ubuntu; FreeBSD boots as a guest, and the concurrent Debian and FreeBSD test is an acceptance gate run on demand.
- **Structure.** seL4 is unmodified and the only kernel-mode code. A root task hands out memory and capabilities to a fixed set of protection domains and then parks. Driver domains own one device class each; virtualiser domains own no device and multiplex over queues shaped after sDDF; VMM domains use libvmm from UNSW. Native agents are meant to be clients of the virtualisers, outside the trusted base; nothing native attaches to a virtualiser yet.
- **Status table.** The README separates levels of evidence: "guest-proven" (an automated test saw real I/O), "boot-proven" (the domain loads), host-tested, lint, and target. The default AArch64 image boots 15 domains. Emulated virtio network, block and console are guest-proven under QEMU on AArch64; the x86-64 image boots the root task only.
- **Not yet.** A separate console virtualiser (the README lists a serial_virt domain among the 15 and also calls the console virtualiser still a library, so it is inconsistent here), a native agent attached to the queues, x86-64 guests, snapshot and migration are target or not implemented. WASM agents, capability hot-swap and agent-facing services (CapStore, MsgBus, ToolSvc, ModelSvc) are called "museum / host models only" and are not in the booted image. The entropy domain has no device on the QEMU machine and answers every request with an error.
- **Build.** Microkit SDK 2.1.0; first-party code in C, Rust or Assembly; BSD 2-Clause licence.

## How

A repository README with a design summary, a status table and test commands. Its claims are tied to named make targets and continuous-integration jobs, which were not run.

## Limits

What the page says itself: host tests stub seL4 IPC and "cannot be cited as proof of I/O". QEMU is described as the emulator used for prototyping, and the same driver domains are "meant to" own real devices on a board; the closing chronicle adds that QEMU is not proof that every real board works.

A careful reader adds:

- **No formal claim.** The word "proof" in the table is a test level, not a formal proof. The page states no verified configuration of seL4 and does not say whether the kernel build is MCS.
- **No real-time or timing claim** appears in the part read.
- **Version unclear.** The README says the current release line is v0.3.x, while the project's releases page, read on 1 November 2026, lists v0.6.0 of 5 October 2026 as the latest.
- **Self-description.** The repository describes itself as built with "agent-native vibe-coding"; no independent evaluation appears.

## Against the wiki

- [[agentos]]: created with this source.
- [[cohesix]]: a neighbour on seL4; agentOS puts guests and device ownership first, Cohesix a Queen deciding what models may do.
- [[lionsos]]: agentOS uses sDDF-shaped queues and libvmm from UNSW, with Microkit. Our reading: this follows the LionsOS design for I/O; the README does not mention LionsOS.

## For zOS

The paper (Section 5) says agentOS aims to give agents capabilities for tools, models and memory and to let them replace services at run time, and that its booted image does not include these services. The README confirms the second point: its table lists WASM agents, capability hot-swap and agent-facing services (CapStore, MsgBus, ToolSvc, ModelSvc) as host models, not in the image, and its contributing section says not to extend them. It does not state the aim itself and names no memory service; the aim is at most inferred from those service names. The paper cites the README as accessed on 20 October 2026; the saved copy read here is of 23 October. No `design/` page changes state.
