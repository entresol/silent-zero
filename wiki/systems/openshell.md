---
type: system
status: reviewed
sources: [nd-nvidia-openshell-overview, 2026-red-hat-beyond-container-boundaries, 2026-microsoft-execution-containers-policy-driven]
short: Open-source sandbox runtime for agents
updated: 2026-11-21
---

# OpenShell

An open-source runtime that runs autonomous agents in sandboxes with kernel-level isolation and a declarative YAML policy. NVIDIA documents it; Red Hat describes it as an industry collaboration backed by NVIDIA, Red Hat, Docker, GitHub, SAP, Google and Dell ([[nd-nvidia-openshell-overview]], [[2026-red-hat-beyond-container-boundaries]]).

## State, September to November 2026

- The documentation's current version is v0.1.9, which lists a "stable release cadence" and "new isolation primitives" as new in the 0.1.x line ([[nd-nvidia-openshell-overview]]).
- Red Hat OpenShift AI 3.5 ships it as a Developer Preview (8 September 2026); the post names SPIFFE-based agent identity, an operator and deeper observability as what comes next ([[2026-red-hat-beyond-container-boundaries]]).
- Microsoft says NVIDIA has integrated OpenShell into [[mxc]] (7 October 2026), adding policy controls for files and inference services, network controls, credential management and OCSF auditing ([[2026-microsoft-execution-containers-policy-driven]]).

## How it limits an agent

- Four layers: filesystem and process rules fixed when the sandbox is created, network rules that can be reloaded at run time, and provider credentials that are opaque placeholders resolved only at profile-authorised endpoints ([[nd-nvidia-openshell-overview]]).
- On Linux the enforcement rests on Landlock, seccomp, network namespaces and an Open Policy Agent engine that decides by destination, URL path, method and headers; outbound traffic is denied until a rule allows it ([[2026-red-hat-beyond-container-boundaries]]). See [[landlock]].
- An agent can propose a rule that a person approves, or, for low-risk changes, that four automatic checks approve ([[2026-red-hat-beyond-container-boundaries]]).

## Licence and code

The pages read call it open source and do not name the licence. Red Hat's example installs it from a Helm chart published under `ghcr.io/nvidia/openshell` ([[2026-red-hat-beyond-container-boundaries]]).

## Related

[[mxc]], [[landlock]], [[agent-operating-systems]], [[broker]], [[confused-deputy]].

## Open questions

- What assurance exists beyond the documented mechanisms: the sources name no proof or audit of the sandbox itself; Red Hat lists red-team testing with Garak as a layer and gives no results.
- Whether a grant can be bound to a task, a recipient and the data of a call; the pages read describe grants by endpoint, binary, method and path.
- What the "formal prover" in the auto-approval path guarantees: the post names four checks and does not say against which model they are proved ([[2026-red-hat-beyond-container-boundaries]]).
- How the sandbox fares against an agent that is itself trying to escape; our remark: the Linux kernel underneath is not a verified one, and the sources do not discuss its flaws.
