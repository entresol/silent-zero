# Agate, capability microkernels for AI agents

> Agate: capability microkernel with a trusted userspace broker and deadline scheduling for agents; no verification. progress, full text.

Source · Zhao and Fang 2026 · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/2026-zhao-agate-capability-microkernels.html

Zhao Wei and Bin Fang (Huawei Technologies). "Agate: Capability Microkernels as a Natural Substrate for AI Agents", AgenticOS workshop at SOSP 2026, September 2026, paper of three pages. [PDF](https://os-for-agent.github.io/papers/AgenticOS_SOSP_2026_paper_13.pdf). Read in full.

## What it shows

- **The claim.** Capability microkernels are "a natural substrate" for agent workloads "by structural correspondence, not analogy": capability-mediated authorisation, IPC with capability passing and per-agent address spaces cover three of six desiderata the authors list (tool authorisation with cascading revocation, identity-bearing communication, isolated sandboxes for generated code). Three further layers cover the rest (decision provenance, versioned context state, latency-aware scheduling).
- **The kernel.** Agate is an AArch64 capability microkernel "in the tradition of seL4" with 45 system calls and 12 capability types, a derivation tree with subtree revocation, kernel-stamped sender identity on IPC, an audit record on the IPC path, context objects with copy-on-write versions, and an earliest-deadline-first scheduler whose deadline is the "user-response deadline" of an agent and whose budget is an inference slice.
- **A broker.** The capability set a tool needs and the deadline an agent owes "are supplied by a declarative tool manifest and a per-tenant policy broker"; the digest of approval-lifecycle events is "computed by a userspace trusted broker". Generating tight specifications "is a long-standing open problem outside this paper's scope".
- **A narrow claim against Linux.** Against Linux with seccomp, namespaces, Landlock and eBPF, or a restricted-token sandbox such as the Codex Windows sandbox, the authors call the microkernel's advantage "narrower and structural": revocation that cascades by construction, identity stamped at the IPC chokepoint, and no ambient authority as the grant model.
- **Status.** The mechanisms are implemented and unit-tested (1,243 passing self-tests); a bounded agent, tool and reply round trip works; the baseline is single-CPU under QEMU (virt, cortex-a72).

## How

A vision paper with a design, a list of mechanisms and a status report. No workload evaluation, no comparison against Linux and no measurement of the chokepoint.

## Limits

"Agate claims no formal verification." SMP correctness, an end-to-end agent workload, a performance comparison, an adversarial evaluation of the chokepoint and formal verification are future work. The provenance guarantee holds only when agents are not given shared-memory or userspace-RPC capabilities, which the authors call "a design contract, not a law of nature". Reply-receive and notify paths are not audited in this version. Cross-node capability transport and distributed revocation are not implemented.

## Against the wiki

- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md): **extends** with a design on a capability microkernel of its own, in the seL4 tradition without its proofs ([Agate](https://silentzero.ooo/wiki/systems/agate.html.md)).
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): **extends**: a userspace broker beside a capability kernel is the shape Silent Zero has; here the broker's decisions are not specified in the paper.
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md): **mentions** it as part of the Linux baseline.

## For Silent Zero

Our reading: the closest neighbour in design so far. It pairs a capability kernel with a trusted userspace broker and has a deadline scheduler, and it has neither a proof nor a control loop; its deadlines are for waiting on a user, not for motors. The paper's Section 5 says none of the designs it names has real-time control as its aim; Agate has a deadline scheduler and its aim is user responsiveness, which is a different thing. The authors' own account of what a microkernel adds over hardened Linux is the narrow form of the paper's argument. See [Agate](https://silentzero.ooo/wiki/systems/agate.html.md).

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [Agate](https://silentzero.ooo/wiki/systems/agate.html.md)
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md)
