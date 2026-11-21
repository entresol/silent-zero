---
type: concept
status: reviewed
sources: [2026-hubbard-agentos-operating-system, 2026-bower-cohesix-research-operating, 2022-google-announcing-kataos-sparrow, 2026-zou-agentkernel-trust-native, 2026-zhao-agenticos-intent-oriented, 2026-zhang-agent-libos-runtime, 2026-ke-quine-realizing-llm, 2026-steinder-towards-agent-operating, nd-nvidia-openshell-overview, 2026-red-hat-beyond-container-boundaries, 2026-microsoft-windows-platform-security-agents, 2026-microsoft-execution-containers-policy-driven, 2026-microsoft-windows-security-ignite-2026]
short: OS-layer designs that bound what agents may do
updated: 2026-11-21
---

# Agent operating systems

Designs that give language-model agents a runtime in which the operating-system layer, not the agent or an application framework, limits what the agent may do. The wiki's sources show a spread, from a kernel of its own to a library inside a Python process.

## State, November 2026

| Design | Where it sits | How it limits an agent | Evidence |
| --- | --- | --- | --- |
| [[agentos]] | seL4 with user-mode drivers, Linux and FreeBSD as guests | agents meant as untrusted clients; agent services not in the booted image | README, tested under QEMU |
| [[cohesix]] | seL4 target beside a host that runs the models | a Queen decides what workers may do; target-side checks | landing page only |
| [[kataos]] | seL4 and Rust for embedded machine-learning devices, 2022 | static components with a Rust root server; announcement describes no agent mechanism | announcement |
| [[2026-zou-agentkernel-trust-native]] | a conventional host kernel with an external monitor | capabilities that delegation can only narrow, labels on memory | design, proofs deferred |
| [[2026-zhao-agenticos-intent-oriented]] | a hypervisor or trusted-execution domain | a declared intent decides which semantic calls exist at all | conceptual, no implementation |
| [[2026-zhang-agent-libos-runtime]] | a library in a Python process on a host | typed capabilities, task ceilings and label checks at every primitive | own test suites, one model |
| [[2026-ke-quine-realizing-llm]] | processes of an ordinary POSIX system | what the kernel gives any process; no capability model | feasibility runs |
| [[openshell]] | Linux (Landlock, seccomp, network namespaces) and, through MXC, Windows | a policy per sandbox; outbound traffic denied until a rule allows it; credentials as placeholders | documentation and a vendor post; Developer Preview in OpenShift AI 3.5 |
| [[mxc]] | Windows, macOS and Linux with the platform's own process sandbox, plus session and WSL backends on Windows and a MicroVM backend (Windows and Linux, experimental) | a declared policy per workload for files, network, process and UI, enforced outside the agent | vendor posts; generally available as of 7 October 2026 |

Three of the nine build on seL4, the others on a host kernel, a hypervisor or an ordinary process model. The paper makes the remark that none of the designs it names has real-time control as its aim, and it does not name Quine; it holds for AgenticOS, Agent libOS and Quine as read here; for [[agentos]] whether it has a real-time aim is open. The pages read on OpenShell and MXC name none either.

- IBM researchers argue for an "Agent-OS" for enterprise deployments with 13 platform primitives; their prototype, rossoctl, is a Kubernetes control plane with sidecars, authorization and an MCP gateway, limited to cloud and datacentre deployments. The paper reports no measurements and has no verified component ([[2026-steinder-towards-agent-operating]]).

- The two industry sandboxes, [[openshell]] and [[mxc]], are products, not research designs: both are described by their vendors only, with no proof, audit or evaluation in the sources read. MXC says it is generally available and OpenShell is a Developer Preview in one distribution. NVIDIA has integrated OpenShell into MXC ([[2026-microsoft-execution-containers-policy-driven]]).

## What they share

- The agent and the model are untrusted, and the check sits outside the model, in the designs that have one.
- Most bind authority to something finer than a user, a declared task, a capability or a ceiling; Quine has no capability model, and the KataOS announcement describes none.
- OpenShell and MXC grant by resource, such as a path, an endpoint, a binary, a method or a network destination; the pages read do not describe a grant bound to the recipient and data of one call (OpenShell's HTTP rules look at the URL path, method and headers of each request, which is a narrower thing).
- AgenticOS requires that every external effect be recorded, and Agent libOS records the effects that pass through its primitives.

## Open questions

- Which of them could carry a proof. Those on seL4 have a verified kernel under them in some configurations, and the agent-facing parts are not covered by that proof. See [[kernel]], [[broker]].
- How any of them treats a deadline. See [[real-time-loops]].
