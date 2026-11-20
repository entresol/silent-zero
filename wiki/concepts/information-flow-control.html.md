# Information-flow control

> Labels for where data came from and who may see it; FIDES and CaMeL for agents; explicit flows only; refusals as a channel; Agent libOS.

Concept · LLM reviewed · updated 2026-11-19 · 6 sources · https://silentzero.ooo/wiki/concepts/information-flow-control.html

Every piece of data carries labels for where it came from (integrity) and who may see it (confidentiality), and labels propagate with the data. A policy then decides from the labels whether an action may proceed, for instance whether an agent may send an email after reading an untrusted one ([Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md), §1).

## For agents

- **FIDES** tracks labels through the planner and assigns policies per tool and checks them before each call: the decision to take a consequential action is never based on untrusted data (noninterference for integrity), and there is no explicit flow of confidential data to where it may not go (explicit secrecy). Implicit flows, through control decisions that depend on secrets, are deliberately left open ([Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md), §4).
- **CaMeL** attaches provenance and allowed readers to every value and checks them before tool calls; its strict mode closes the channel through loops, while some exceptions an adversary triggers through tool data stay open ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), §7).
- Both keep untrusted text away from the part that decides, and both stop the attacks of the AgentDojo benchmark within their policies, at some cost in completed tasks ([Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md), [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)).

- **Agent libOS** joins labels conservatively (highest sensitivity, lowest integrity), clears each external recipient against a registry the host owns, and lets a person release one payload to one recipient without changing its label. It does not trust the plan and does not claim noninterference ([Agent libOS](https://silentzero.ooo/wiki/sources/2026-zhang-agent-libos-runtime.html.md), §3.3, §3.4, §8.3).
- **AgenticOS** proposes labels on inputs and rules at output interfaces, with human confirmation for high-risk flows; it is a design without implementation ([AgenticOS](https://silentzero.ooo/wiki/sources/2026-zhao-agenticos-intent-oriented.html.md), §3.4).
- A June 2026 survey of such defences calls the assignment of the first label the trusted base of every scheme, and finds it under-specified in all of them ([adaptive evaluation of out-of-band defenses](https://silentzero.ooo/wiki/sources/2026-narisetty-adaptive-evaluation-out.html.md), §8.2).

## Authority is not information flow

Our reading: capabilities limit what a component can reach; labels limit where data may go once it is reached. A deceived agent with narrow capabilities can still leak what it holds through a channel it is allowed to use. The Silent Zero paper makes the same point (Section 6) and cites [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md) for adding information-flow control.

## Open questions

- Where labels would be enforced in Silent Zero: in the [The broker](https://silentzero.ooo/wiki/design/broker.html.md), in the agent's runtime, or both.
- A refusal is a flow too. A 2026 preprint argues that what an agent infers from a denied tool call leaves no trace for flat tracking over successful calls, naming FIDES as the closest system, and proposes recording denials as events in a provenance graph; its evidence is three constructed scenarios and it does not claim full non-interference for implicit flows ([Causality laundering](https://silentzero.ooo/wiki/sources/2026-chinaei-causality-laundering-denial.html.md), §2.5, §7.6). For Silent Zero: what the broker's replies to refused requests disclose.
- Implicit flows and timing: what the agent's runtime leaks below the labels. See [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md).

## Sources

- [adaptive evaluation of out-of-band defenses](https://silentzero.ooo/wiki/sources/2026-narisetty-adaptive-evaluation-out.html.md)
- [Agent libOS](https://silentzero.ooo/wiki/sources/2026-zhang-agent-libos-runtime.html.md)
- [AgenticOS](https://silentzero.ooo/wiki/sources/2026-zhao-agenticos-intent-oriented.html.md)
- [Causality laundering](https://silentzero.ooo/wiki/sources/2026-chinaei-causality-laundering-denial.html.md)
- [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)
- [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md)
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md)
- [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md)
- [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md)
- [Can CaMeLs Talk?](https://silentzero.ooo/wiki/sources/2026-peters-gill-can-camels.html.md)
- [Towards an Agent Operating System](https://silentzero.ooo/wiki/sources/2026-steinder-towards-agent-operating.html.md)
