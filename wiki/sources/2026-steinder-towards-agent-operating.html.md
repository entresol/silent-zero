# Towards an Agent Operating System

> IBM position paper: an Agent-OS with 13 primitives on a Kubernetes control plane; no measurements. position, full text.

Source · Steinder and Franke 2026 · LLM reviewed · updated 2026-11-20 · https://silentzero.ooo/wiki/sources/2026-steinder-towards-agent-operating.html

Gosia Steinder and Hubertus Franke (IBM T. J. Watson Research Center). "Towards an Agent Operating System - Lessons from Classical and Cloud OS", arXiv 2607.25076v1, 27 July 2026. A preprint. [arXiv](https://arxiv.org/abs/2607.25076). Read in full, including the reference list; the figures were not inspected beyond their captions.

## What it shows

The paper measures nothing. It is an argument with a table of proposals, and every figure in it comes from other work.

- **The thesis.** Platform software has gone through three phases twice, experimentation, articulation and consolidation, ending in POSIX for the classical OS and Kubernetes for the cloud. The authors place agentic systems in the first phase, with frameworks and protocols (they name CrewAI, LangGraph, AutoGen, MCP, A2A) that say how to write agent code and not what the platform must guarantee (§I, §II.A). They call for an "Agent-OS" and say it will take considerable time to mature.
- **Reliability and safety as infrastructure properties.** Models cannot be relied on to find and fix their own mistakes, so the guarantees of resilience, security and cost belong to the platform, which must enforce what prompts can only request (§II). The authors cite other work for this and do not test it. Lesson 4 (§VI) repeats it: authorization, guardrails, context limits and observability go in infrastructure, not in agent code.
- **Two breaks in prior semantics (§III).** The first is structural: agents act on the external world, with consequences that may be irreversible, and no existing OS abstraction classifies operations as reversible, compensable or irreversible. Permissions cannot be declared at deployment time for an agent that discovers APIs from its reasoning. The second is intrinsic to stochasticity. Worst-case execution time is not computable because the number of model calls depends on the agent's own trajectory (§III.A). Replay debugging, temporal-locality eviction and declarative desired state also fail. A process's self-reported status can no longer be assumed truthful; the authors cite studies of agents that conceal failures. They add that capability-based security on declared interfaces is insufficient, since the tool calls are decided at inference time and runtime verification would need a complete formal specification of intended behaviour, which they call an open problem.
- **Thirteen primitives (Table I, §IV).** For each, the authors give the OS origin, the cloud origin, the semantic gap, a status and a horizon. Status: 6 Partial, 5 Open, 2 Early. Horizon: 2 Near, 5 Mid, 6 Long. Near are agent lifecycle and identity and authorization. The primitives are agent lifecycle, orchestrator, skills registry, tool mediation, context management, agent-to-agent communication, agent memory, identity and authorization, behavioural guardrails, failure detection, saga and checkpoint, trajectory observability, and an AI-aware proxy. The authors say the set is not claimed to be complete or minimal.
- **What the security-relevant rows ask for.**
  - Tool mediation: classify calls as reversible, compensable or irreversible and require elevated authorization for the last (§IV.D).
  - Identity: SPIFFE and OAuth 2.0 Token Exchange as a base, extended with the agent's goal, model and skills, and policy that is per function and depends on what the agent has done (§IV.H).
  - Guardrails: platform-level constraints the agent cannot override. The authors state that classical MAC has O(1) decidable evaluation per system call and that no decidable policy language exists for natural-language content. They say current guardrail tools use model-based classifiers and so add stochasticity to what should be deterministic enforcement. Risk-based assessment and human-in-the-loop enforcement are named as necessary (§IV.I).
  - Failure detection: immutable audit ledgers the agent cannot modify, dry-run simulation and copy-on-write sandboxes (§IV.J, §IV.L).
- **Open agenda (§VII).** Eight problems: stochastic scheduling theory, evaluation methodology, semantic skill contracts, agent-aware information flow analysis, supply-chain security for AI-generated code, formal policy languages for natural-language guardrails, principled context-eviction theory, and agentic reinforcement learning.
- **Four lessons (§VI).** Standardize to leave the experimental phase; build on the prior layer and do not replace it; specify only what is genuinely new; the platform enforces what application code only requests.
- **A prototype (§V).** The authors' own open-source project, rossoctl, implements a subset of the primitives on Kubernetes: authorization (AuthBridge), SPIFFE/SPIRE identity and an MCP Gateway, as sidecars and custom resources. It targets cloud and datacenter deployments; personal and edge agents are out of scope. No measurement of it is given. The paper names AutoGen, LangGraph, OpenAI Swarm, Kagent and Openshell as other projects that each cover part of the primitives and says none yet gives the full platform layer.

## How

A conceptual derivation. For each classical abstraction, the authors ask what guarantee it gave, whether the problem recurs for agents and what must change (§IV). The status and horizon codes in Table I are the authors' own judgement and carry no stated method. The figures quoted in the gap discussions (for example 15 per cent degradation from model mismatch, 26 per cent of skills with a vulnerability, 45 per cent of AI-generated code failing security tests, 95 per cent of enterprise AI deployments failing) are taken from cited reports (references 18, 26, 46, 63), and the paper gives no check of them.

## Limits

The authors say the thirteen primitives are not complete or minimal, that dependencies among them are not worked out, and that the Agent-OS will take years. They name rossoctl as limited to cloud and datacenter deployments. They say agentic reinforcement learning is "in flux" with largely undefined platform primitives (§VII). They write that the challenge is a shortage of agreed abstractions with well-defined, platform-enforceable semantics, not of frameworks (§II.A). They acknowledge the help of Claude Sonnet 4.6 in drafting (§IX).

A careful reader adds the following.

- Nothing is measured or proved. The classification of each primitive as Open, Partial or Early is a claim by the authors; it is a map of the field and not a result.
- The platform is Kubernetes and its sidecars throughout. The paper does not examine the trusted base under the platform; it mentions kernel mechanisms such as the MMU and seccomp-BPF only as analogies and cites formal-methods work only in its open agenda (§III.A, §VII). Our reading: its enforcement points, a proxy and a control plane, are in effect assumed to be correct; the paper says only that application code cannot bypass them. Its argument that infrastructure enforces what agent code cannot is, on its own terms, about who enforces, not about how well.
- The paper gives no real-time analysis. Its remark that worst-case execution time is not computable concerns the agent's inference loop; it does not touch bounds on a kernel or a control loop.
- A few citations are loose. In the text, "AIOS [5]" points to the list's AgentOS paper, and the list gives AIOS as [1]. The agentic reinforcement learning paragraph cites a blog post titled "LLM wiki" (reference 62). The sentence in §IV.D that MCP standardizes via wrappers cites an IBM technical report (reference 27).
- rossoctl is the authors' own employer's project (references 27, 51 and 53 are IBM Research reports and repositories), and the comparisons with other projects are a sentence each.
- It is a preprint, and in our reading a position paper (the authors do not use the label), so it states a method and a direction for a community and not a finding.

## Against the wiki

- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md): **extends**. That page lists seven designs that put the limit in the OS layer. This source argues from the platform side that such a layer is needed and gives a checklist of thirteen primitives, and names AIOS, MemGPT-style memory managers and rossoctl, none of which the wiki has. Our reading: rossoctl is a Kubernetes control plane, a different place from the seL4, host-kernel, hypervisor and library placements in the table; it would be a new row of the "where it sits" column.
- [Quine](https://silentzero.ooo/wiki/sources/2026-ke-quine-realizing-llm.html.md): **related**. The paper cites Quine as an example for life-cycle management (reference 19, §II.A). The wiki records that Quine has no capability model.
- [AgentOS](https://silentzero.ooo/wiki/sources/2026-liu-agentos-application-silos.html.md): **related**. Cited as reference 5, which the text calls AIOS in one place and uses for the claim that agent messages can reprogram the receiver (§III.A).
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): **extends**. The paper's tool-mediation and identity primitives are the same job as the broker's, specified for a cloud substrate. Its open problems (fine-grained, context-dependent authorization; a decidable policy language for natural-language content) match the broker page's question of who writes the policies. It does not contradict the page: nothing in it is proved, and the authors do not claim a guarantee.
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md): **extends**. The paper counts injection through agent-to-agent messages as a gap with no byte-level analogue (§III.A, §IV.F) and proposes platform-level semantic inspection of messages (§IV.F). It reports no rates. The remark that current guardrail tools are model-based classifiers agrees with the page's state of heuristic defences, but the paper does not measure it.
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md): **extends** lightly. Agent-aware information flow analysis is item 4 of the open agenda (§VII); the paper does not mention FIDES or CaMeL, which the page covers.
- [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md): **related**. The paper names capability-based security as a precedent and says it is insufficient on declared interfaces alone (§III.A). It does not discuss object capabilities as the wiki does, where authority travels with the reference.
- [Model Context Protocol](https://silentzero.ooo/wiki/concepts/model-context-protocol.html.md): **extends**. The authors say MCP defines how agents communicate and not execution guarantees (§III, §IV.D) and place MCP gateways with a reversibility model at the mediation point. They cite no measurement.
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md): **related**. The paper says worst-case execution time is not computable for an agent loop (§III.A). The page covers WCET of kernel code; the two statements concern different things, and nothing in the paper changes the page.

## For Silent Zero

[The broker](https://silentzero.ooo/wiki/design/broker.html.md): no change of state. Our reading: the paper's reversibility classes for tool calls (reversible, compensable, irreversible, with elevated authorization for the last) give a vocabulary the broker page could use when it says what a grant covers; the paper itself says nothing of how a broker would be verified. Its argument that agent code cannot enforce its own limits matches the Silent Zero split between an untrusted agent and a trusted mediation layer (Section 3 of the paper). It is no evidence for the design, since it tests nothing.

[The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md) and [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): no change. The source's point that an agent loop has no computable worst-case execution time supports, as an argument and not a measurement, keeping the motor loop separate from the model. The source does not address that loop.

The Silent Zero paper (Section 5) says the first designs for the broker's job have appeared and none names real-time control as its goal; this source neither supports nor contradicts that. Our reading: its Table I contains no verified component, and verification appears as existing work cited in the open agenda and as an open problem (a language with decidable evaluation for natural-language output, §VII).

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md)
- [Model Context Protocol](https://silentzero.ooo/wiki/concepts/model-context-protocol.html.md)
- [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md)
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md)
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md)
- [AgentOS](https://silentzero.ooo/wiki/sources/2026-liu-agentos-application-silos.html.md)
- [Quine](https://silentzero.ooo/wiki/sources/2026-ke-quine-realizing-llm.html.md)
