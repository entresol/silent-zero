# OpenShell

> Open-source sandbox runtime for agents: Landlock, seccomp, network namespaces and a policy engine; outbound traffic denied by default; credentials as placeholders; a Developer Preview in OpenShift AI 3.5.

System · LLM reviewed · updated 2026-11-21 · 3 sources · https://silentzero.ooo/wiki/systems/openshell.html

An open-source runtime that runs autonomous agents in sandboxes with kernel-level isolation and a declarative YAML policy. NVIDIA documents it; Red Hat describes it as an industry collaboration backed by NVIDIA, Red Hat, Docker, GitHub, SAP, Google and Dell ([NVIDIA: Overview of OpenShell](https://silentzero.ooo/wiki/sources/nd-nvidia-openshell-overview.html.md), [Kernel-level agent security in OpenShift AI 3.5](https://silentzero.ooo/wiki/sources/2026-red-hat-beyond-container-boundaries.html.md)).

## State, September to November 2026

- The documentation's current version is v0.1.9, which lists a "stable release cadence" and "new isolation primitives" as new in the 0.1.x line ([NVIDIA: Overview of OpenShell](https://silentzero.ooo/wiki/sources/nd-nvidia-openshell-overview.html.md)).
- Red Hat OpenShift AI 3.5 ships it as a Developer Preview (8 September 2026); the post names SPIFFE-based agent identity, an operator and deeper observability as what comes next ([Kernel-level agent security in OpenShift AI 3.5](https://silentzero.ooo/wiki/sources/2026-red-hat-beyond-container-boundaries.html.md)).
- Microsoft says NVIDIA has integrated OpenShell into [Microsoft Execution Containers (MXC)](https://silentzero.ooo/wiki/systems/mxc.html.md) (7 October 2026), adding policy controls for files and inference services, network controls, credential management and OCSF auditing ([Execution Containers, policy-driven containment for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-execution-containers-policy-driven.html.md)).

## How it limits an agent

- Four layers: filesystem and process rules fixed when the sandbox is created, network rules that can be reloaded at run time, and provider credentials that are opaque placeholders resolved only at profile-authorised endpoints ([NVIDIA: Overview of OpenShell](https://silentzero.ooo/wiki/sources/nd-nvidia-openshell-overview.html.md)).
- On Linux the enforcement rests on Landlock, seccomp, network namespaces and an Open Policy Agent engine that decides by destination, URL path, method and headers; outbound traffic is denied until a rule allows it ([Kernel-level agent security in OpenShift AI 3.5](https://silentzero.ooo/wiki/sources/2026-red-hat-beyond-container-boundaries.html.md)). See [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md).
- An agent can propose a rule that a person approves, or, for low-risk changes, that four automatic checks approve ([Kernel-level agent security in OpenShift AI 3.5](https://silentzero.ooo/wiki/sources/2026-red-hat-beyond-container-boundaries.html.md)).

## Licence and code

The pages read call it open source and do not name the licence. Red Hat's example installs it from a Helm chart published under `ghcr.io/nvidia/openshell` ([Kernel-level agent security in OpenShift AI 3.5](https://silentzero.ooo/wiki/sources/2026-red-hat-beyond-container-boundaries.html.md)).

## Related

[Microsoft Execution Containers (MXC)](https://silentzero.ooo/wiki/systems/mxc.html.md), [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md), [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md), [The broker](https://silentzero.ooo/wiki/design/broker.html.md), [Confused deputy](https://silentzero.ooo/wiki/concepts/confused-deputy.html.md).

## Open questions

- What assurance exists beyond the documented mechanisms: the sources name no proof or audit of the sandbox itself; Red Hat lists red-team testing with Garak as a layer and gives no results.
- Whether a grant can be bound to a task, a recipient and the data of a call; the pages read describe grants by endpoint, binary, method and path.
- What the "formal prover" in the auto-approval path guarantees: the post names four checks and does not say against which model they are proved ([Kernel-level agent security in OpenShift AI 3.5](https://silentzero.ooo/wiki/sources/2026-red-hat-beyond-container-boundaries.html.md)).
- How the sandbox fares against an agent that is itself trying to escape; our remark: the Linux kernel underneath is not a verified one, and the sources do not discuss its flaws.

## Sources

- [Execution Containers, policy-driven containment for AI agents](https://silentzero.ooo/wiki/sources/2026-microsoft-execution-containers-policy-driven.html.md)
- [Kernel-level agent security in OpenShift AI 3.5](https://silentzero.ooo/wiki/sources/2026-red-hat-beyond-container-boundaries.html.md)
- [NVIDIA: Overview of OpenShell](https://silentzero.ooo/wiki/sources/nd-nvidia-openshell-overview.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [Confused deputy](https://silentzero.ooo/wiki/concepts/confused-deputy.html.md)
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md)
- [Microsoft Execution Containers (MXC)](https://silentzero.ooo/wiki/systems/mxc.html.md)
