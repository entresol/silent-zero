# Information-flow control

> Labels for where data came from and who may see it; FIDES and CaMeL for agents; explicit flows only.

Concept · LLM reviewed · updated 2026-10-31 · 2 sources · https://silentzero.ooo/wiki/concepts/information-flow-control.html

Every piece of data carries labels for where it came from (integrity) and who may see it (confidentiality), and labels propagate with the data. A policy then decides from the labels whether an action may proceed, for instance whether an agent may send an email after reading an untrusted one ([Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md), §1).

## For agents

- **FIDES** tracks labels through the planner and assigns policies per tool and checks them before each call: the decision to take a consequential action is never based on untrusted data (noninterference for integrity), and there is no explicit flow of confidential data to where it may not go (explicit secrecy). Implicit flows, through control decisions that depend on secrets, are deliberately left open ([Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md), §4).
- **CaMeL** attaches provenance and allowed readers to every value and checks them before tool calls; its strict mode closes the channel through loops, while some exceptions an adversary triggers through tool data stay open ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), §7).
- Both keep untrusted text away from the part that decides, and both stop the attacks of the AgentDojo benchmark within their policies, at some cost in completed tasks ([Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md), [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)).

## Authority is not information flow

Our reading: capabilities limit what a component can reach; labels limit where data may go once it is reached. A deceived agent with narrow capabilities can still leak what it holds through a channel it is allowed to use. The Silent Zero paper makes the same point (Section 6) and cites [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md) for adding information-flow control.

## Open questions

- Where labels would be enforced in Silent Zero: in the [The broker](https://silentzero.ooo/wiki/design/broker.html.md), in the agent's runtime, or both.
- Implicit flows and timing: what the agent's runtime leaks below the labels. See [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md).

## Sources

- [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)
- [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md)
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md)
- [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md)
- [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md)
