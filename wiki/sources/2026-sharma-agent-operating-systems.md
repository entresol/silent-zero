---
type: source
id: 2026-sharma-agent-operating-systems
status: reviewed
read: partial
kind: design
sources: [2026-sharma-agent-operating-systems]
updated: 2026-11-06
---

# Sharma and Shah 2026: Agent Operating Systems

Ankur Sharma and Deep Shah, independent researchers. "Agent Operating Systems (AOS): Integrating Agentic Control Planes into, and Beyond, Traditional Operating Systems". [arXiv:2606.01508](https://arxiv.org/abs/2606.01508), version 1 of 1 June 2026. The authors say the work was done in the Unified Intelligent Infrastructure workstream of the Open Compute Project. Read in part: sections 1 to 6, 8 to 11 and the conclusion. Sections 7.3 to 7.5, which compare Linux and Windows primitives for scheduling, networking and observability, were skimmed, and this page makes no claim about them.

## What it shows

- **The claim.** Classical operating-system abstractions (process, scheduler, memory, syscall, identity) do not fit long-lived, goal-directed agents "cleanly" and are incomplete for them; the authors do not call them incorrect and list discarding them wholesale as a non-goal (§1, §1.2, §2). The authors define an Agent Operating System as a layer that manages the lifecycle, execution and governance of agents while keeping enforcement deterministic at the boundary where actions have side effects (§2, §3.1).
- **Three planes.** Reasoning is probabilistic and "must be treated as untrusted with respect to policy". Execution runs tool calls and side effects in least-privilege sandboxes. Policy decides authorisation and denies by default where a case is ambiguous. Model output counts as a proposal, not a command (§3.3, §8.4).
- **Trusted base.** The policy engine, capability validation, the mediation layer, sandbox controls and the audit subsystem are inside it; model inference, retrieval models and heuristic classifiers are outside. The authors concede that some policy decisions, such as semantic data classification, depend on probabilistic classifiers, and say determinism then applies to the policy outcome, not to the classifier (§3.4).
- **Capabilities.** Tools sit in a registry. A capability names the tools, resource scopes, parameter ranges and time windows allowed, and whether a person must approve. Checks deny by default, where a case is ambiguous (§4.5) and for side-effecting tools not explicitly allowed (§8.3), and capabilities are revocable. Tools discovered at run time need a privileged admission step that binds them to scopes before use (§4.5, §8.3).
- **Four invariants.** No side effect without a deterministic "allow"; every outcome is recorded in an append-only record before the agent is rescheduled; scheduling depends on observable state and budgets, not on reasoning tokens; the underlying OS stays the only mediator of hardware (§4.8).
- **Four ways to build it.** As a user-space runtime on an unchanged OS, as an OS extension with new primitives such as agent identity, capability tokens and scheduler hooks (hooks such as Linux security modules and eBPF are named as the pragmatic middle way), as a distributed control plane, or, over a long horizon, by taking over higher-level OS duties. In the long-horizon model the authors say core kernel duties, among them memory paging, low-level scheduling, drivers and file systems, should stay with the kernel, and Invariant 4 keeps the OS as the sole mediator of hardware (§5.4, §4.8). This is a design position. The reference architecture "does not require kernel modifications" (§4).
- **Threats.** At least seven categories (§8.1), among them tool misuse, privilege escalation, exfiltration, audit evasion and compromise of the control plane itself. Sequences of individually allowed actions can add up to harm, so per-action enforcement is "necessary but not sufficient" (§8.1, §8.2).

## How

A position and design paper. It presents a reference architecture, mappings onto Linux (namespaces, cgroups, seccomp, eBPF) and Windows (tokens, job objects), and proposed evaluation criteria and benchmark scenarios (§6, §7, §10). Nothing was built or measured.

## Limits

What the authors say themselves: multi-agent delegation chains, cascading revocation and policy arbitration across cooperating agents are open problems, as are formal scheduling models, memory semantics and "formal verification boundaries for enforcement pipelines" (§10.3, §11). They list agent bypass of mediation as a risk of the user-space model and call for operating-system and network controls that force all side effects through it (§5.1).

A careful reader adds: the paper has no implementation, no results and no proofs, so every statement is a design goal. It runs above a general-purpose kernel and takes that kernel's isolation as given. It names no real-time or actuator goal in the parts we read; its scheduler allocates "goal progress" under cost and risk budgets (§4.3).

## Against the wiki

- [[broker]]: a design for the same job in a different place. The three planes, deny-by-default and revocable scoped capabilities resemble the zOS broker's duties. Unlike zOS, the enforcement points run on a conventional host and a registry admits tools at run time. The stateful-attack remark in §8.2 matches the open question on sequences of allowed calls there.
- [[prompt-injection]]: §8.4 treats injection as untrusted input and constrains execution rather than trusting the model, the stance of [[2025-debenedetti-defeating-prompt-injections]], without an experiment of its own.
- [[object-capabilities]]: our reading is that the paper's capabilities are registry entries with scopes; it does not say how they are held, though it speaks of capability tokens (§5.2). Its reference list has Levy's 1984 book on capability systems and no later work on them.
- [[2026-zou-agentkernel-trust-native]], [[agentos]]: other agent-OS designs; this one is a control plane over Linux or Windows and says so.

## For zOS

It bears on the *broker* page as one more design for the authority layer on a conventional host, with the same absence of proofs and of real-time goals. It does not change the state of any `design/` page. The paper (Section 5) does not cite it; whether to cite it is for the team.
