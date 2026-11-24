# agent capabilities should follow task intent (IntentCap)

> IntentCap: single-use leases from four context sources, a deterministic checker, zero unsafe accepts in 3,746 replayed events. test, full text.

Source · Zheng, Zhang and Mao 2026 · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/2026-zheng-llm-agent-capabilities.html

Yusheng Zheng (UC Santa Cruz), Wenhui Zhang (Roblox) and Yu Mao (Bytedance). "LLM Agent Capabilities Should Follow Task Intent and Context Source", AgenticOS workshop at SOSP 2026, September 2026, short paper. [PDF](https://os-for-agent.github.io/papers/AgenticOS_SOSP_2026_paper_29.pdf). Read in full.

## What it shows

- **The claim.** Capabilities for an agent should be scoped to the current task intent and not to a sandbox or session, and "no single context source defines a complete capability". Current defences "control allowed operations, not which inputs influence which decisions".
- **IntentCap.** A capability lease is composed from four context sources: user intent, workflow instructions (system policy, skills), tool schemas and the runtime environment (tool results, file state). Each decision field of a lease, such as the destination, the approval scope or the tool name, has exactly one owning source ("field-level ownership"), and a lease "only narrows the user's authorized authority, never widens it" ("monotonic narrowing"). A lease binds an operation, an object, arguments, a budget, an expiry and a delegation depth; it is consumed on use, and a delegated subtask gets only capabilities narrower than its parent's.
- **Who decides.** A language model compiles candidate leases and "propose but never decide"; a deterministic checker, with an intent issuer, a source labeler and the enforcement layer, is the trusted base. Enforcement is at the tool level (adapters that check each argument comes from its owner source) and at the OS level (leases compiled to file, exec and network policies for the eBPF-based ActPlane, a system the paper cites).
- **The worked case.** A user asks for two PDFs to be extracted and one issue created in a named repository. An injected candidate naming another repository has no witnessing span in the user's intent, so the checker denies it before the call.
- **Preliminary results.** Zero unsafe accepts across 3,746 security-sensitive events replayed from AgentDojo, MCPTox, InjecAgent and tau2-bench; all 3,813 benign reference actions in a tau2-style proxy covered, and 2,554 of 2,556 applicable ground-truth checks passed. Collapsing the four sources into one trusted context falsely accepts 3,593 of 3,823 events that should be denied (94 per cent). On seven crafted multi-step workflows, a policy language without field ownership falsely accepts all seven.

## How

A short paper with a design and a preliminary evaluation by replaying recorded events and constructed workflows.

## Limits

The authors list as future work: composition by meet, end-to-end attack success, enforcement latency and "adaptive attacks on labeling and lease generation". The events are replayed, not live attacks. Copy-witness provenance is conservative: values from other sources are confined to data fields or user-authorised selectors. User-pasted documents with ambiguous provenance are denied authority fields in the prototype. A model writes the leases, so the checker's rules are the guarantee.

## Against the wiki

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): **extends**: the closest published neighbour to the broker's job, with attenuated, single-use grants that bind arguments and a checker outside the model ([Intent-bound capabilities (IntentCap and its neighbour)](https://silentzero.ooo/wiki/systems/intentcap.html.md)).
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md): **extends**.
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md): **extends** with field-level source ownership as an information-flow rule on decisions.

## For Silent Zero

Our reading: it states what the paper's Section 5 asks of the broker (bind each action to recipients, data and parameters, narrow on delegation, keep the model out of the decision) and builds it in user space and eBPF on a conventional host, tested on replayed events. Section 5 of the paper places Silent Zero's contribution in integrating the parts, the broker among them, and names AgenticOS and Agent libOS as the first designs for its job; this is a further one, with a checker and measurements. What it does not have is a proven kernel beneath it or a real-time base. See [Intent-bound capabilities (IntentCap and its neighbour)](https://silentzero.ooo/wiki/systems/intentcap.html.md), [ToolFence](https://silentzero.ooo/wiki/sources/2026-li-toolfence-fine-grained.html.md), [PACE, provenance-aware capability enforcement](https://silentzero.ooo/wiki/sources/2026-li-pace-provenance-aware.html.md).

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md)
- [Intent-bound capabilities (IntentCap and its neighbour)](https://silentzero.ooo/wiki/systems/intentcap.html.md)
- [PACE, provenance-aware capability enforcement](https://silentzero.ooo/wiki/sources/2026-li-pace-provenance-aware.html.md)
- [securing agentic AI with OS-level intent-driven capabilities](https://silentzero.ooo/wiki/sources/2026-lourenco-securing-agentic-ai.html.md)
- [ToolFence](https://silentzero.ooo/wiki/sources/2026-li-toolfence-fine-grained.html.md)
