---
type: system
status: reviewed
sources: [2026-microsoft-windows-platform-security-agents, 2026-microsoft-execution-containers-policy-driven, 2026-microsoft-windows-security-ignite-2026]
short: Microsoft's policy-driven containment for agents
updated: 2026-11-21
---

# Microsoft Execution Containers (MXC)

Microsoft's policy-driven execution layer for untrusted or generated code and for agents: developers declare the files, network destinations and other resources a workload needs, and MXC enforces that boundary with a container backend on Windows, macOS or Linux ([[2026-microsoft-execution-containers-policy-driven]]).

## State, June to November 2026

- **2 June 2026 (Build):** an early preview of the SDK for agents on Windows and WSL, with process and session isolation to follow shortly and micro-VMs, Linux containers and Windows 365 integration on the roadmap ([[2026-microsoft-windows-platform-security-agents]]).
- **7 October 2026:** "now generally available", with process containers on Windows 11, macOS and Linux (AppContainer, Seatbelt, Bubblewrap), session and WSL containers on Windows 11, a MicroVM backend marked experimental, and Windows 365 support. NVIDIA has integrated [[openshell]] into it ([[2026-microsoft-execution-containers-policy-driven]]).
- **17 November 2026 (Ignite):** the vendor repeats the direction, "agent identity, containment, isolation, policy, observability, and governance" ([[2026-microsoft-windows-security-ignite-2026]]).
- Still to come per the October post: Intune policy for process containers ("soon") and Entra's separation of agent from user activity ("coming soon").

## How it limits an agent

- The policy covers the isolation environment, the process, the file system, the network and the user interface, and it "remains outside the agent workload's control" ([[2026-microsoft-execution-containers-policy-driven]]).
- Three modes: enforcement, learning (blocked and recorded) and permissive (allowed and recorded); the activity report exists on Windows only.
- Organisations can add constraints by management policy on top of what the agent's developer declares.

## Licence and code

The October post points to an MXC repository on GitHub with the SDK, schema, documentation and samples. The pages read do not state the licence.

## Related

[[openshell]], [[agent-operating-systems]], [[broker]], [[landlock]].

## Open questions

- What assurance the containers carry; the sources claim none, and the micro-VM backend is experimental.
- Whether a policy can express a grant per call, bound to recipient, data and parameters; the pages read show a declaration per workload.
- How the Windows, macOS and Linux backends differ in what they can enforce; the post says each has "distinct security properties".
- Whether MXC has any real-time aim; the pages read mention none.
