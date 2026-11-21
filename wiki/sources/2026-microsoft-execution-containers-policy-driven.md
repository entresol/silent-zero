---
type: source
id: 2026-microsoft-execution-containers-policy-driven
status: reviewed
read: full
kind: report
sources: [2026-microsoft-execution-containers-policy-driven]
updated: 2026-11-21
---

# Microsoft 2026: Execution Containers, policy-driven containment for AI agents

Logan Iyer (Microsoft). "Microsoft Execution Containers: Policy-driven containment for AI agents", Windows Developer Blog, 7 October 2026. [Page](https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/). Read in full. A vendor announcement.

## What it shows

- **General availability.** Microsoft Execution Containers (MXC), "now generally available", "provides the containment layer" beside identity and manageability. Windows 365 support for MXC is also stated as generally available.
- **The principle.** "An agent cannot be its own security authority. It must run within a boundary defined by the developer or organization and enforced independently of the agent itself." And of the policy: it "remains outside the agent workload's control, so the agent or generated code cannot grant itself additional access."
- **What MXC is.** "A policy-driven execution layer for untrusted code or dynamically generated workloads", for model output, plugins, tools, an agent harness or a whole agent. Developers declare the resources a workload needs, such as files and network destinations, in one JSON configuration schema with an SDK in several languages; MXC maps them to a backend on Windows, macOS or Linux.
- **Backends.** Process container (Windows 11, macOS, Linux; AppContainer, Seatbelt and Bubblewrap), session container (Windows 11 only), WSL container (Windows 11 only), MicroVM (Windows 11 and Linux, marked "experimental"). "Each containment backend has distinct security properties and workloads should be evaluated for fit with containment backend."
- **What the policy covers.** The isolation environment, the process (command, arguments, working directory, environment), the file system (modify, read only, no access), the network (inbound and outbound, including the host's loopback interface) and the user interface. Organisations can add constraints through management policy such as Intune; Intune policy for process containers is "soon" and Entra's separation of agent from user activity is "coming soon".
- **Operating modes.** Enforcement (ungranted access blocked), Learning (blocked and recorded in a JSON activity report) and Permissive (allowed and recorded), to write a least-privilege policy for a workload; the activity report is Windows-only.
- **NVIDIA and OpenShell.** "NVIDIA has integrated OpenShell into MXC", adding "policy controls for agent access to files and inference services; advanced network controls; credential management, and for enterprises, OCSF auditing".
- **Who uses it.** GitHub Copilot, OpenClaw, OpenAI Codex, Replit, LM Studio and Unsloth AI "already support MXC"; others, among them Claude Code, are named as coming.

## How

A product post with tables of backends, policy areas and modes, and an example of a coding agent whose policy allows its repository and development tools and blocks the rest. It gives no measurement and no detail of the enforcement.

## Limits

No assurance of the containers is claimed; the post says the environment "is designed to prevent" an operation. It does not say how a policy is bound to a task or to the data of a call: the policy is a declaration per workload. The MicroVM backend is experimental, and several management features are future. It was read as published; the linked GitHub Copilot post and the MXC repository were not read.

## Against the wiki

- [[agent-operating-systems]]: **extends** ([[mxc]]).
- [[broker]]: **extends** with a generally available product that keeps policy outside the agent, and a learning mode that records what a workload tried before a policy is enforced.

## For zOS

Our reading: the sentence "an agent cannot be its own security authority" is the paper's argument for a broker outside the agent, stated by a platform vendor, and the paper's Section 6 clause on what hardening leaves out is narrower than written once such a policy exists. What the post does not describe is a grant per call that is bound to recipients, data and parameters, and none of it comes with a proof. See [[mxc]], [[openshell]].
