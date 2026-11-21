# Microsoft Execution Containers (MXC)

> Microsoft’s policy-driven containment for agents on Windows, macOS and Linux, generally available as of 7 October 2026, with OpenShell integrated; no assurance claimed.

System · LLM reviewed · updated 2026-11-21 · 3 sources · https://silentzero.ooo/wiki/systems/mxc.html

Microsoft's policy-driven execution layer for untrusted or generated code and for agents: developers declare the files, network destinations and other resources a workload needs, and MXC enforces that boundary with a container backend on Windows, macOS or Linux ([Execution Containers, policy-driven containment for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-execution-containers-policy-driven.html.md)).

## State, June to November 2026

- **2 June 2026 (Build):** an early preview of the SDK for agents on Windows and WSL, with process and session isolation to follow shortly and micro-VMs, Linux containers and Windows 365 integration on the roadmap ([Windows platform security for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-windows-platform-security-agents.html.md)).
- **7 October 2026:** "now generally available", with process containers on Windows 11, macOS and Linux (AppContainer, Seatbelt, Bubblewrap), session and WSL containers on Windows 11, a MicroVM backend marked experimental, and Windows 365 support. NVIDIA has integrated [OpenShell](https://silentzero.ooo/wiki/systems/openshell.html.md) into it ([Execution Containers, policy-driven containment for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-execution-containers-policy-driven.html.md)).
- **17 November 2026 (Ignite):** the vendor repeats the direction, "agent identity, containment, isolation, policy, observability, and governance" ([Windows security at Ignite](https://silentzero.ooo/wiki/sources/2026-microsoft-windows-security-ignite-2026.html.md)).
- Still to come per the October post: Intune policy for process containers ("soon") and Entra's separation of agent from user activity ("coming soon").

## How it limits an agent

- The policy covers the isolation environment, the process, the file system, the network and the user interface, and it "remains outside the agent workload's control" ([Execution Containers, policy-driven containment for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-execution-containers-policy-driven.html.md)).
- Three modes: enforcement, learning (blocked and recorded) and permissive (allowed and recorded); the activity report exists on Windows only.
- Organisations can add constraints by management policy on top of what the agent's developer declares.

## Licence and code

The October post points to an MXC repository on GitHub with the SDK, schema, documentation and samples. The pages read do not state the licence.

## Related

[OpenShell](https://silentzero.ooo/wiki/systems/openshell.html.md), [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md), [The broker](https://silentzero.ooo/wiki/design/broker.html.md), [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md).

## Open questions

- What assurance the containers carry; the sources claim none, and the micro-VM backend is experimental.
- Whether a policy can express a grant per call, bound to recipient, data and parameters; the pages read show a declaration per workload.
- How the Windows, macOS and Linux backends differ in what they can enforce; the post says each has "distinct security properties".
- Whether MXC has any real-time aim; the pages read mention none.

## Sources

- [Execution Containers, policy-driven containment for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-execution-containers-policy-driven.html.md)
- [Windows platform security for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-windows-platform-security-agents.html.md)
- [Windows security at Ignite](https://silentzero.ooo/wiki/sources/2026-microsoft-windows-security-ignite-2026.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md)
- [OpenShell](https://silentzero.ooo/wiki/systems/openshell.html.md)
- [NVIDIA: Overview of OpenShell](https://silentzero.ooo/wiki/sources/nd-nvidia-openshell-overview.html.md)
