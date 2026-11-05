# Prompt injection

> Instructions hidden in data an agent reads; heuristic defences fail, defences around the model hold within limits.

Concept · LLM reviewed · updated 2026-11-05 · 5 sources · https://silentzero.ooo/wiki/concepts/prompt-injection.html

An attacker places instructions in data that a language-model agent reads, such as an email, a document or a web page, so that the agent acts on them instead of on its user's request. A jailbreak, by contrast, is the user working against the model designer's intent ([The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md), §5). The *indirect* variant, with the instructions placed in data the application retrieves rather than typed by its user, was analysed in 2023 in what its authors present as the first systematic treatment, with demonstrations against Bing Chat and applications built on GPT-4 ([Indirect prompt injection](https://silentzero.ooo/wiki/sources/2023-greshake-not-what-you.html.md)).

## Two kinds of defence

- Heuristic and model-based defences: prompts, training against known attacks, detectors in front of or behind the model, secret canaries. Twelve such defences against prompt injection and jailbreaks fell to adaptive attacks, fully or substantially and most above 90 per cent, after most had reported near zero ([The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md)).
- Defences around the model: CaMeL keeps untrusted data away from the part that plans, and checks every tool call against policies on where data came from and who may see it. It stopped AgentDojo's attacks within its threat model, at some cost in utility; its interpreter is not verified, and it leaves some side channels and attack classes open ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)). FIDES tracks confidentiality and integrity labels through the planner and blocks consequential tool calls whose choice untrusted data influenced; with its policies it let none of AgentDojo's attacks through that it counts against them, controls explicit flows only, and lets attacks that change only the text shown to the user pass ([Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md)). See [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md). Nasr et al. skip such designs because their attacks would fail by construction, and note that they fit a limited set of tasks and reduce utility ([The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md), Appendix G.1).

## State, October 2026

No defence in the sources survives an adaptive attacker by evaluation alone; evaluations can only fail to break a defence ([The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md), §6). Defences around the model hold by construction within their threat model, and have not been tested adaptively ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md)). In 2023 effective mitigations were "currently lacking" ([Indirect prompt injection](https://silentzero.ooo/wiki/sources/2023-greshake-not-what-you.html.md), abstract). For the Model Context Protocol, a 2026 preprint lists 38 threat categories, among them the injection of instructions through tool descriptions and chains of benign tools; it states that five open-source scanners and proxies together cover at most 18 of them ([MCP-38](https://silentzero.ooo/wiki/sources/2026-shen-mcp-38-comprehensive.html.md)).

## Open questions

- When the user asks the agent to follow instructions found in data, data becomes control; isolating the planner alone cannot stop it, and policies and capabilities have to carry the load ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), §6.4).
- Sequences of individually allowed steps may add up to a harmful one ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), §9.3).
- The Silent Zero paper treats prompt injection as a [Confused deputy](https://silentzero.ooo/wiki/concepts/confused-deputy.html.md) problem (Section 2.4) and limits what capabilities do against it (Section 6). See [The broker](https://silentzero.ooo/wiki/design/broker.html.md).

## Sources

- [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)
- [Indirect prompt injection](https://silentzero.ooo/wiki/sources/2023-greshake-not-what-you.html.md)
- [MCP-38](https://silentzero.ooo/wiki/sources/2026-shen-mcp-38-comprehensive.html.md)
- [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md)
- [The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Confused deputy](https://silentzero.ooo/wiki/concepts/confused-deputy.html.md)
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md)
- [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md)
- [LeftoverLocals](https://silentzero.ooo/wiki/sources/2024-trail-leftoverlocals-listening-llm.html.md)
