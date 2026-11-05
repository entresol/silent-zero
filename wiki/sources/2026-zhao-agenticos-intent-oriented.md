---
type: source
id: 2026-zhao-agenticos-intent-oriented
status: reviewed
read: full
kind: design
sources: [2026-zhao-agenticos-intent-oriented]
updated: 2026-11-05
---

# Zhao et al. 2026: AgenticOS

Zhen Zhao, Yu Zhang, Yanpeng Zhu, Jia Wang, Songqiao Tao, Xin Cheng (Tencent) and Jiexin Gao (South-Central Minzu University). "AgenticOS: An Intent-Oriented Secure Operating System Architecture for Autonomous AI Agents". [arXiv:2606.21129](https://arxiv.org/abs/2606.21129), version 1 of 19 June 2026. A preprint. Read in full.

## What it shows

- **The claim.** Operating systems expose resources, while a user authorizes a task. An agent that holds file, network and process primitives can combine them far beyond its task once prompt injection or a poisoned dependency has turned it. So the system should ask whether an external effect fits the declared intent, not whether a process may touch a resource (§1, §3.1).
- **Four layers.** The Ghost Kernel is the minimal trusted base. It runs in a hypervisor root, a hardware trusted-execution domain or an equivalent, and offers capsules no runtime interface. The Logic Shutter parses intents, checks capability tokens, labels information and audits. The Agent Capsule runs the agent. The Semantic Boundary Gateway is the only road to the outside world and keeps protocols and credentials on its side (§3.2 to §3.6).
- **The manifest.** Before it starts, an agent submits a structured declaration of its network domains, file scopes, tools, model sessions, outputs and the points where a person must confirm. Only what the manifest declares gets an interface in the capsule: with no network entry there are no sockets or DNS stubs. Network permissions are tuples of domain, path prefix, method, data type and budget (§4.2).
- **The Intent ABI.** Six families of semantic calls (documents, network, toolchain, model inference and others) replace raw system calls; open, read, write, socket, connect, bind, mmap, execve, fork, ptrace, dlopen and syscall are excluded for good. A builder called Weaver checks that code and manifest agree and must fail the build if a prohibited entry appears (§4.2 to §4.5).
- **Skills.** Agents may help write new skills in a development state. A skill enters the runtime only through declaration, static analysis, tests or proofs, signature and registration, so runtime capabilities do not grow by themselves (§4.6, §6.2).
- **Threat analysis.** The paper discusses the removal of system-call attack surface, chains of individually allowed calls, intent drift, covert channels by timing, size and presence, and the trusted base of the Logic Shutter and Weaver, with a mitigation for each (§5).

## How

A conceptual architecture. The text contains no implementation, no measurements and no case study. It says it does not elaborate a specific engineering implementation (§3.5).

## Limits

What the authors say. Intent cannot be decided for arbitrary code in finite time, so drift cannot be ruled out. Semantic calls cost context switches and add latency, and unmodified POSIX software no longer runs. End-to-end verification from manifest to capsule behaviour "remains difficult", and covert channels are made narrower, not removed. Human confirmation is a capability of its own, because responsibility cannot be handed to a machine (§5.3, §5.4, §7).

A careful reader adds:

- **Assumed, not shown.** The Ghost Kernel's isolation logic is assumed formally verifiable "or intensively audited" (§2.2). The paper points to seL4 as the model but places the kernel in a hypervisor or trusted-execution domain, so its base includes that hardware.
- **The Logic Shutter is large.** The paper itself says its trusted base is more complex than the kernel's and proposes to split it into smaller isolated parts (§5.5).
- **Declared intent.** The manifest is trusted policy input from a management plane (§2.2). How a user's task becomes a manifest is not worked out; agents may draft manifests in a development state (§4.6, §7.1).

## Against the wiki

- [[broker]]: a closely related design, not built. Where the broker hands out authority bound to a person's intent, AgenticOS derives a whole capsule from a declaration. Our reading: both put the decision outside the model, and AgenticOS adds checks on chains of calls and a gateway that holds credentials.
- [[information-flow-control]]: labels on inputs and rules at output interfaces, left at the level of a design.
- [[object-capabilities]]: capability tokens bound to identity, manifest, call chain and budget; unforgeable by assumption.
- [[agent-operating-systems]]: one of the designs listed there.

## For zOS

Section 5 of the paper: "AgenticOS lets agents declare intents instead of requesting resources and derives a least-capability environment from them, so far as an architecture without an implementation (Zhao et al. 2026)". Confirmed: the text calls itself a conceptual architecture and reports no implementation. Its scheduling is mentioned as deterministic time slices against covert channels (§3.3); real-time control is not a goal in the text, as the paper says. No `design/` page changes state.
