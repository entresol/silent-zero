# Agent operating systems

> Designs that put the limit on an agent in the OS layer: agentOS, Cohesix, KataOS, AgentKernel, AgenticOS, Agent libOS, Quine, OpenShell and MXC as shipped products; IBM’s Agent-OS position paper.

Concept · LLM reviewed · updated 2026-11-21 · 13 sources · https://silentzero.ooo/wiki/concepts/agent-operating-systems.html

Designs that give language-model agents a runtime in which the operating-system layer, not the agent or an application framework, limits what the agent may do. The wiki's sources show a spread, from a kernel of its own to a library inside a Python process.

## State, November 2026

| Design | Where it sits | How it limits an agent | Evidence |
| --- | --- | --- | --- |
| [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md) | seL4 with user-mode drivers, Linux and FreeBSD as guests | agents meant as untrusted clients; agent services not in the booted image | README, tested under QEMU |
| [Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md) | seL4 target beside a host that runs the models | a Queen decides what workers may do; target-side checks | landing page only |
| [KataOS](https://silentzero.ooo/wiki/systems/kataos.html.md) | seL4 and Rust for embedded machine-learning devices, 2022 | static components with a Rust root server; announcement describes no agent mechanism | announcement |
| [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md) | a conventional host kernel with an external monitor | capabilities that delegation can only narrow, labels on memory | design, proofs deferred |
| [AgenticOS](https://silentzero.ooo/wiki/sources/2026-zhao-agenticos-intent-oriented.html.md) | a hypervisor or trusted-execution domain | a declared intent decides which semantic calls exist at all | conceptual, no implementation |
| [Agent libOS](https://silentzero.ooo/wiki/sources/2026-zhang-agent-libos-runtime.html.md) | a library in a Python process on a host | typed capabilities, task ceilings and label checks at every primitive | own test suites, one model |
| [Quine](https://silentzero.ooo/wiki/sources/2026-ke-quine-realizing-llm.html.md) | processes of an ordinary POSIX system | what the kernel gives any process; no capability model | feasibility runs |
| [OpenShell](https://silentzero.ooo/wiki/systems/openshell.html.md) | Linux (Landlock, seccomp, network namespaces) and, through MXC, Windows | a policy per sandbox; outbound traffic denied until a rule allows it; credentials as placeholders | documentation and a vendor post; Developer Preview in OpenShift AI 3.5 |
| [Microsoft Execution Containers (MXC)](https://silentzero.ooo/wiki/systems/mxc.html.md) | Windows, macOS and Linux with the platform's own process sandbox, plus session and WSL backends on Windows and a MicroVM backend (Windows and Linux, experimental) | a declared policy per workload for files, network, process and UI, enforced outside the agent | vendor posts; generally available as of 7 October 2026 |

Three of the nine build on seL4, the others on a host kernel, a hypervisor or an ordinary process model. The paper makes the remark that none of the designs it names has real-time control as its aim, and it does not name Quine; it holds for AgenticOS, Agent libOS and Quine as read here; for [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md) whether it has a real-time aim is open. The pages read on OpenShell and MXC name none either.

- IBM researchers argue for an "Agent-OS" for enterprise deployments with 13 platform primitives; their prototype, rossoctl, is a Kubernetes control plane with sidecars, authorization and an MCP gateway, limited to cloud and datacentre deployments. The paper reports no measurements and has no verified component ([Towards an Agent Operating System](https://silentzero.ooo/wiki/sources/2026-steinder-towards-agent-operating.html.md)).

- The two industry sandboxes, [OpenShell](https://silentzero.ooo/wiki/systems/openshell.html.md) and [Microsoft Execution Containers (MXC)](https://silentzero.ooo/wiki/systems/mxc.html.md), are products, not research designs: both are described by their vendors only, with no proof, audit or evaluation in the sources read. MXC says it is generally available and OpenShell is a Developer Preview in one distribution. NVIDIA has integrated OpenShell into MXC ([Execution Containers, policy-driven containment for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-execution-containers-policy-driven.html.md)).

## What they share

- The agent and the model are untrusted, and the check sits outside the model, in the designs that have one.
- Most bind authority to something finer than a user, a declared task, a capability or a ceiling; Quine has no capability model, and the KataOS announcement describes none.
- OpenShell and MXC grant by resource, such as a path, an endpoint, a binary, a method or a network destination; the pages read do not describe a grant bound to the recipient and data of one call (OpenShell's HTTP rules look at the URL path, method and headers of each request, which is a narrower thing).
- AgenticOS requires that every external effect be recorded, and Agent libOS records the effects that pass through its primitives.

## Open questions

- Which of them could carry a proof. Those on seL4 have a verified kernel under them in some configurations, and the agent-facing parts are not covered by that proof. See [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md), [The broker](https://silentzero.ooo/wiki/design/broker.html.md).
- How any of them treats a deadline. See [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md).

## Sources

- [Agent libOS](https://silentzero.ooo/wiki/sources/2026-zhang-agent-libos-runtime.html.md)
- [AgenticOS](https://silentzero.ooo/wiki/sources/2026-zhao-agenticos-intent-oriented.html.md)
- [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md)
- [agentOS, an operating system for agents on seL4](https://silentzero.ooo/wiki/sources/2026-hubbard-agentos-operating-system.html.md)
- [Announcing KataOS and Sparrow](https://silentzero.ooo/wiki/sources/2022-google-announcing-kataos-sparrow.html.md)
- [Cohesix, a research operating system for edge AI](https://silentzero.ooo/wiki/sources/2026-bower-cohesix-research-operating.html.md)
- [Execution Containers, policy-driven containment for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-execution-containers-policy-driven.html.md)
- [Kernel-level agent security in OpenShift AI 3.5](https://silentzero.ooo/wiki/sources/2026-red-hat-beyond-container-boundaries.html.md)
- [NVIDIA: Overview of OpenShell](https://silentzero.ooo/wiki/sources/nd-nvidia-openshell-overview.html.md)
- [Quine](https://silentzero.ooo/wiki/sources/2026-ke-quine-realizing-llm.html.md)
- [Towards an Agent Operating System](https://silentzero.ooo/wiki/sources/2026-steinder-towards-agent-operating.html.md)
- [Windows platform security for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-windows-platform-security-agents.html.md)
- [Windows security at Ignite](https://silentzero.ooo/wiki/sources/2026-microsoft-windows-security-ignite-2026.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md)
- [Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md)
- [KataOS](https://silentzero.ooo/wiki/systems/kataos.html.md)
- [Microsoft Execution Containers (MXC)](https://silentzero.ooo/wiki/systems/mxc.html.md)
- [OpenShell](https://silentzero.ooo/wiki/systems/openshell.html.md)
