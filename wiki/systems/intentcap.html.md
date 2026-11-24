# Intent-bound capabilities (IntentCap and its neighbour)

> Capability leases from task intent, checked outside the model (IntentCap), and a vision paper on the same idea.

System · LLM reviewed · updated 2026-11-21 · 2 sources · https://silentzero.ooo/wiki/systems/intentcap.html

Two short papers at the AgenticOS workshop derive an agent's authority from the task. IntentCap composes a lease from four context sources, with field-level ownership and monotonic narrowing, a deterministic checker outside the language model, and tool-level and eBPF enforcement ([agent capabilities should follow task intent (IntentCap)](https://silentzero.ooo/wiki/sources/2026-zheng-llm-agent-capabilities.html.md)). The vision paper from Lisbon and Oracle Labs proposes capabilities derived from the user's prompt and enforced at the system-call boundary ([securing agentic AI with OS-level intent-driven capabilities](https://silentzero.ooo/wiki/sources/2026-lourenco-securing-agentic-ai.html.md)).

## State, September 2026

IntentCap has a prototype and a preliminary evaluation on replayed events: zero unsafe accepts across 3,746 security-sensitive events, with end-to-end attack success, latency and adaptive attacks left as future work. The other paper has no implementation ([agent capabilities should follow task intent (IntentCap)](https://silentzero.ooo/wiki/sources/2026-zheng-llm-agent-capabilities.html.md), [securing agentic AI with OS-level intent-driven capabilities](https://silentzero.ooo/wiki/sources/2026-lourenco-securing-agentic-ai.html.md)).

## Licence and code

Neither paper links code or names a licence in the text read.

## Related

[The broker](https://silentzero.ooo/wiki/design/broker.html.md), [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md), [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md), [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md).

## Open questions

- Whether a lease derived with a model's help can be trusted when the model reads untrusted text; IntentCap keeps the model outside the decision, and the Lisbon paper names the derivation as its central challenge.
- How either would sit on a verified kernel; both rest on a conventional host.

## Sources

- [agent capabilities should follow task intent (IntentCap)](https://silentzero.ooo/wiki/sources/2026-zheng-llm-agent-capabilities.html.md)
- [securing agentic AI with OS-level intent-driven capabilities](https://silentzero.ooo/wiki/sources/2026-lourenco-securing-agentic-ai.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md)
- [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md)
