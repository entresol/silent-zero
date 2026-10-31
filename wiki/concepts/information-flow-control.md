---
type: concept
status: reviewed
sources: [2025-costa-securing-ai-agents, 2025-debenedetti-defeating-prompt-injections]
glossary: Information-flow control
updated: 2026-10-31
---

# Information-flow control

Every piece of data carries labels for where it came from (integrity) and who may see it (confidentiality), and labels propagate with the data. A policy then decides from the labels whether an action may proceed, for instance whether an agent may send an email after reading an untrusted one ([[2025-costa-securing-ai-agents]], §1).

## For agents

- **FIDES** tracks labels through the planner and assigns policies per tool and checks them before each call: the decision to take a consequential action is never based on untrusted data (noninterference for integrity), and there is no explicit flow of confidential data to where it may not go (explicit secrecy). Implicit flows, through control decisions that depend on secrets, are deliberately left open ([[2025-costa-securing-ai-agents]], §4).
- **CaMeL** attaches provenance and allowed readers to every value and checks them before tool calls; its strict mode closes the channel through loops, while some exceptions an adversary triggers through tool data stay open ([[2025-debenedetti-defeating-prompt-injections]], §7).
- Both keep untrusted text away from the part that decides, and both stop the attacks of the AgentDojo benchmark within their policies, at some cost in completed tasks ([[2025-costa-securing-ai-agents]], [[2025-debenedetti-defeating-prompt-injections]]).

## Authority is not information flow

Our reading: capabilities limit what a component can reach; labels limit where data may go once it is reached. A deceived agent with narrow capabilities can still leak what it holds through a channel it is allowed to use. The zOS paper makes the same point (Section 6) and cites [[2025-costa-securing-ai-agents]] for adding information-flow control.

## Open questions

- Where labels would be enforced in zOS: in the [[broker]], in the agent's runtime, or both.
- Implicit flows and timing: what the agent's runtime leaks below the labels. See [[time-protection]].
