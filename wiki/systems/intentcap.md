---
type: system
status: reviewed
sources: [2026-zheng-llm-agent-capabilities, 2026-lourenco-securing-agentic-ai]
short: Task-scoped capability leases, checked outside the model
updated: 2026-11-21
---

# Intent-bound capabilities (IntentCap and its neighbour)

Two short papers at the AgenticOS workshop derive an agent's authority from the task. IntentCap composes a lease from four context sources, with field-level ownership and monotonic narrowing, a deterministic checker outside the language model, and tool-level and eBPF enforcement ([[2026-zheng-llm-agent-capabilities]]). The vision paper from Lisbon and Oracle Labs proposes capabilities derived from the user's prompt and enforced at the system-call boundary ([[2026-lourenco-securing-agentic-ai]]).

## State, September 2026

IntentCap has a prototype and a preliminary evaluation on replayed events: zero unsafe accepts across 3,746 security-sensitive events, with end-to-end attack success, latency and adaptive attacks left as future work. The other paper has no implementation ([[2026-zheng-llm-agent-capabilities]], [[2026-lourenco-securing-agentic-ai]]).

## Licence and code

Neither paper links code or names a licence in the text read.

## Related

[[broker]], [[agent-operating-systems]], [[information-flow-control]], [[object-capabilities]].

## Open questions

- Whether a lease derived with a model's help can be trusted when the model reads untrusted text; IntentCap keeps the model outside the decision, and the Lisbon paper names the derivation as its central challenge.
- How either would sit on a verified kernel; both rest on a conventional host.
