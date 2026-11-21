---
type: concept
status: reviewed
sources: [2025-costa-securing-ai-agents, 2025-debenedetti-defeating-prompt-injections, 2026-chinaei-causality-laundering-denial, 2026-zhang-agent-libos-runtime, 2026-zhao-agenticos-intent-oriented, 2026-narisetty-adaptive-evaluation-out, 2026-nikolaou-camelot-camel-orchestrated, 2026-li-pace-provenance-aware]
glossary: Information-flow control
updated: 2026-11-21
---

# Information-flow control

Every piece of data carries labels for where it came from (integrity) and who may see it (confidentiality), and labels propagate with the data. A policy then decides from the labels whether an action may proceed, for instance whether an agent may send an email after reading an untrusted one ([[2025-costa-securing-ai-agents]], §1).

## For agents

- **FIDES** tracks labels through the planner and assigns policies per tool and checks them before each call: the decision to take a consequential action is never based on untrusted data (noninterference for integrity), and there is no explicit flow of confidential data to where it may not go (explicit secrecy). Implicit flows, through control decisions that depend on secrets, are deliberately left open ([[2025-costa-securing-ai-agents]], §4).
- **CaMeL** attaches provenance and allowed readers to every value and checks them before tool calls; its strict mode closes the channel through loops, while some exceptions an adversary triggers through tool data stay open ([[2025-debenedetti-defeating-prompt-injections]], §7).
- Both keep untrusted text away from the part that decides, and both stop the attacks of the AgentDojo benchmark within their policies, at some cost in completed tasks ([[2025-costa-securing-ai-agents]], [[2025-debenedetti-defeating-prompt-injections]]).

- **Agent libOS** joins labels conservatively (highest sensitivity, lowest integrity), clears each external recipient against a registry the host owns, and lets a person release one payload to one recipient without changing its label. It does not trust the plan and does not claim noninterference ([[2026-zhang-agent-libos-runtime]], §3.3, §3.4, §8.3).
- **AgenticOS** proposes labels on inputs and rules at output interfaces, with human confirmation for high-risk flows; it is a design without implementation ([[2026-zhao-agenticos-intent-oriented]], §3.4).
- A June 2026 survey of such defences calls the assignment of the first label the trusted base of every scheme, and finds it under-specified in all of them ([[2026-narisetty-adaptive-evaluation-out]], §8.2).

CaMeLoT turns CaMeL's provenance into a conservative static taint on the plan (anything undecidable before execution counts as tainted) and does not handle reader sets, so confidentiality, directly, leaving them to CaMeL at run time ([[2026-nikolaou-camelot-camel-orchestrated]], §3.2 for the lattice and taint rule; §3, §4, §5.1 for reader sets). PACE combines a minimum cut over declared flow edges with effect-authority checks, takes origin labels from deployment assignment as a stated premise, and says it does not establish noninterference ([[2026-li-pace-provenance-aware]], §4.4, C.6).

## Authority is not information flow

Our reading: capabilities limit what a component can reach; labels limit where data may go once it is reached. A deceived agent with narrow capabilities can still leak what it holds through a channel it is allowed to use. The zOS paper makes the same point (Section 6) and cites [[2025-costa-securing-ai-agents]] for adding information-flow control.

## Open questions

- Where labels would be enforced in zOS: in the [[broker]], in the agent's runtime, or both.
- A refusal is a flow too. A 2026 preprint argues that what an agent infers from a denied tool call leaves no trace for flat tracking over successful calls, naming FIDES as the closest system, and proposes recording denials as events in a provenance graph; its evidence is three constructed scenarios and it does not claim full non-interference for implicit flows ([[2026-chinaei-causality-laundering-denial]], §2.5, §7.6). For zOS: what the broker's replies to refused requests disclose.
- Implicit flows and timing: what the agent's runtime leaks below the labels. See [[time-protection]].
