# AgentKernel

> AgentKernel: an agent OS on a conventional host with an external monitor and capability intersection; proofs deferred. design, partly read.

Source · Zou et al. 2026 · LLM reviewed · updated 2026-11-03 · https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html

Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li and Zhuotao Liu ("DeepKernel Lab"; the corresponding author's address is at Tsinghua University). "AgentKernel: The Trust-Native Agentic Operating System". [arXiv:2609.29647](https://arxiv.org/abs/2609.29647), version 1 of 29 August 2026. Read in part: the abstract, sections 1 to 3, the summary of the pillars given there, the threat model and invariants in 5.1 and 5.2, the limitations in 5.5 and 7.4, and the insights in 7.1. Section 4 was skimmed. The comparison tables and the related work were only skimmed, and this page makes no claim about them.

## What it shows

- **The claim.** Today's agent governance tools are application-level middleware inside the agent's process boundary. The authors argue for an operating-system layer with mandatory services for identity, input mediation, memory governance and execution control, and call AgentKernel the first trust-native agent operating system (abstract, §1).
- **Four pillars.** Identity, Perception, Cognition and Execution. Identity gives each agent a signed credential from a global registry; delegation to a child agent can only narrow its capabilities. Perception labels and filters inputs in stages, one of them an LLM-based classifier. Cognition tracks taint labels on memory entries. Execution checks tool calls against rules and an intent check, and backs this with eBPF hooks on Linux (§3, §5.2; details in §4, skimmed).
- **Policy intersection.** The effective permission set is the intersection of the developer's, the operator's and the context's sets, never the union (Principle 2, §3).
- **Narrow interface.** The agent reaches the model, tools and storage only through three adapters. The authors state that this does not make the trusted computing base small: the registry, the kernel, the adapters, the host's eBPF subsystem and the cryptographic primitives all belong to it (Principle 5, §5.1).
- **The agent is outside the trusted base.** The design treats the model and agent code as an untrusted substrate to be contained (§7.1).

## How

A design and position paper. Our reading of the parts we read: it reports no measurements. The authors list the latency of eBPF probe installation per tool call as an empirical question still to be characterised (§7.4).

## Limits

What the authors say themselves: the invariants "have not been mechanically verified", and formal proofs in Coq or TLA+ are deferred to companion publications. The security argument rests on a non-bypass assumption that the three adapters are the only path to models, tools and storage, which they call a deployment responsibility. Side channels and compromise of the host operating-system kernel are out of scope. The registry's signing key is a single point of trust. The semantic firewall is an LLM classifier and trades false positives against false negatives. Taint labels can under-approximate when the boundary between trusted and untrusted text is unclear (§5.5, §7.4).

A careful reader adds: the design runs on a general-purpose host kernel and assumes it enforces the eBPF allowlists correctly (§5.1), so its isolation is only as strong as that host; eBPF is native on Linux and limited on macOS and Windows (§5.5). It makes no claim about actuators or timing.

## Against the wiki

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): a second design that puts a mandatory monitor outside the model and narrows delegated authority. Unlike the Silent Zero broker it sits on an unverified host kernel and its checks include model-based classifiers. See also [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md), [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md) and [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md).
- [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md), [Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md): other agent systems; AgentKernel is not built on [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md) in the parts we read.

## For Silent Zero

Section 6 of the paper, under "Others are building this", names designs for the broker's job above the kernel, among them Agent libOS on a conventional host. AgentKernel is another such design on a conventional host kernel. Like the others the paper names, it does not name real-time control as a goal. It contradicts nothing in the paper. No `design/` page changes state.

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md)
- [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md)
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md)
- [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md)
- [Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
