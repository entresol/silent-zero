# Windows platform security for AI agents

> Build 2026: the MXC SDK in early preview, containment, identity and manageability as Windows primitives. report, full text.

Source · Microsoft 2026 · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/2026-microsoft-windows-platform-security-agents.html

Dana Huang and Logan Iyer (Microsoft). "Windows platform security for AI agents", Windows Developer Blog, Microsoft Build, 2 June 2026. [Page](https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/). Read in full. A vendor announcement.

## What it shows

- **The announcement.** An early preview of the Microsoft Execution Containers (MXC) SDK, "a cross-platform, policy-driven execution layer for agents on Windows and WSL". "Containment, identity and manageability are built as foundational primitives in Windows".
- **The idea of containment.** It "bounds what agents can access and do, so non-deterministic behavior doesn't translate into uncontrollable risk", so that agents do useful work "without being granted the full authority of the user's session". The post says "Developers define what to constrain in their apps and agents, and Windows enforces those constraints consistently at runtime."
- **Backends.** Process isolation (fast and lightweight, for model-generated code), session isolation (a distinct Windows account and session, with a local or Entra-backed identity to which all activity is attributed; the first release supports non-interactive sessions). On the roadmap: micro-VMs with hypervisor-backed isolation, Linux containers through WSL, and MXC for Windows 365 for Agents, a cloud PC product described as generally available.
- **Management.** Policy controls through Microsoft Agent 365, Entra and Intune "will be used to apply those MXC constraints to a specific agent".
- **Partners.** GitHub Copilot CLI "has adopted MXC process isolation"; Hermes, Manus, NVIDIA, OpenAI and OpenClaw are named partners. "NVIDIA brings OpenShell to Windows, built on MXC."
- **The base.** The post lists Windows features it counts as a secure foundation, among them production drivers written in Rust, Secure Boot as a hardware root of trust, and Defender with "real-time protection against prompt injection and other emerging agent threats".

## How

An announcement at Build with product descriptions and partner quotations. It gives no policy format, no design detail of the enforcement and no measurement.

## Limits

An announcement of an early preview; some features are "shortly after Build" or on a roadmap, and the post says many are already in Windows Insider builds. The statement that "research at the cutting edge of agent security shows how LLMs are developing capabilities around escaping sandboxes" has no citation. The claim about Defender is not backed by any figure here. No assurance of the containment itself is claimed.

## Against the wiki

- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md): **extends** with a platform vendor putting containment and agent identity into the operating system ([Microsoft Execution Containers (MXC)](https://silentzero.ooo/wiki/systems/mxc.html.md)).
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): **extends**; the policy is declared by developers and organisations and enforced outside the agent.

## For Silent Zero

Our reading: the case that an operating system, not the agent, must hold the boundary is made by a major platform vendor. The post names a micro-VM as the stronger option against escapes, which is a hypervisor boundary and not a proof. The paper does not mention MXC. See [Microsoft Execution Containers (MXC)](https://silentzero.ooo/wiki/systems/mxc.html.md), and the later post [Execution Containers, policy-driven containment for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-execution-containers-policy-driven.html.md) for the generally available version.

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [Microsoft Execution Containers (MXC)](https://silentzero.ooo/wiki/systems/mxc.html.md)
- [Execution Containers, policy-driven containment for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-execution-containers-policy-driven.html.md)
