---
type: concept
status: reviewed
sources: [2026-hubbard-agentos-operating-system, 2026-bower-cohesix-research-operating, 2022-google-announcing-kataos-sparrow, 2026-zou-agentkernel-trust-native, 2026-zhao-agenticos-intent-oriented, 2026-zhang-agent-libos-runtime, 2026-ke-quine-realizing-llm]
short: OS-layer designs that bound what agents may do
updated: 2026-11-05
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

Three of the seven build on seL4, the others on a host kernel, a hypervisor or an ordinary process model. The paper makes the remark that none of the designs it names has real-time control as its aim, and it does not name Quine; it holds for AgenticOS, Agent libOS and Quine as read here; for [[agentos]] whether it has a real-time aim is open.

## What they share

- The agent and the model are untrusted, and the check sits outside the model, in the designs that have one.
- Most bind authority to something finer than a user, a declared task, a capability or a ceiling; Quine has no capability model, and the KataOS announcement describes none.
- AgenticOS requires that every external effect be recorded, and Agent libOS records the effects that pass through its primitives.

## Open questions

- Which of them could carry a proof. Those on seL4 have a verified kernel under them in some configurations, and the agent-facing parts are not covered by that proof. See [[kernel]], [[broker]].
- How any of them treats a deadline. See [[real-time-loops]].
