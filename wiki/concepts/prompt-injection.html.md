# Prompt injection

> Instructions hidden in data an agent reads; heuristic defences fail, defences around the model hold within limits; benign command chains through shared state beat two of them; CaMeL does not carry over between agents; argument-level authorization and refusals as a leak; MCP measured.

Concept · LLM reviewed · updated 2026-11-19 · 12 sources · https://silentzero.ooo/wiki/concepts/prompt-injection.html

An attacker places instructions in data that a language-model agent reads, such as an email, a document or a web page, so that the agent acts on them instead of on its user's request. A jailbreak, by contrast, is the user working against the model designer's intent ([The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md), §5). The *indirect* variant, with the instructions placed in data the application retrieves rather than typed by its user, was analysed in 2023 in what its authors present as the first systematic treatment, with demonstrations against Bing Chat and applications built on GPT-4 ([Indirect prompt injection](https://silentzero.ooo/wiki/sources/2023-greshake-not-what-you.html.md)).

## Two kinds of defence

- Heuristic and model-based defences: prompts, training against known attacks, detectors in front of or behind the model, secret canaries. Twelve such defences against prompt injection and jailbreaks fell to adaptive attacks, fully or substantially and most above 90 per cent, after most had reported near zero ([The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md)).
- Defences around the model: CaMeL keeps untrusted data away from the part that plans, and checks every tool call against policies on where data came from and who may see it. It stopped AgentDojo's attacks within its threat model, at some cost in utility; its interpreter is not verified, and it leaves some side channels and attack classes open ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)). FIDES tracks confidentiality and integrity labels through the planner and blocks consequential tool calls whose choice untrusted data influenced; with its policies it let none of AgentDojo's attacks through that it counts against them, controls explicit flows only, and lets attacks that change only the text shown to the user pass ([Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md)). See [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md). Nasr et al. skip such designs because their attacks would fail by construction, and note that they fit a limited set of tasks and reduce utility ([The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md), Appendix G.1).

## State, October 2026

No defence in the sources survives an adaptive attacker by evaluation alone; evaluations can only fail to break a defence ([The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md), §6). Defences around the model hold by construction within their threat model, and CaMeL and FIDES have not been tested adaptively ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md)). A June 2026 preprint ran one such defence, Progent, against a hand-made adaptive attack on a weak open-weight model; attack success stayed low, at 2.6 per cent; the authors call it one small data point that is consistent with, and does not establish, the idea that such defences are harder to attack than detectors ([adaptive evaluation of out-of-band defenses](https://silentzero.ooo/wiki/sources/2026-narisetty-adaptive-evaluation-out.html.md)). It also names the open weak spots: who assigns the labels, tasks that must act on untrusted content, and side channels. In 2023 effective mitigations were "currently lacking" ([Indirect prompt injection](https://silentzero.ooo/wiki/sources/2023-greshake-not-what-you.html.md), abstract). For the Model Context Protocol, a 2026 preprint lists 38 threat categories, among them the injection of instructions through tool descriptions and chains of benign tools; it states that five open-source scanners and proxies together cover at most 18 of them, though its own table does not match that ([MCP-38](https://silentzero.ooo/wiki/sources/2026-shen-mcp-38-comprehensive.html.md)). Two further preprints measure it: in the authors' own harness attack success rose from 26.4 to 52.8 per cent when equivalent tools were reached through MCP ([breaking the protocol](https://silentzero.ooo/wiki/sources/2026-maloyan-breaking-protocol-security.html.md)), and of seven MCP clients tested with poisoned tool descriptions one failed all four attacks, while for file reading and remote scripts those that held did so largely through the model's refusal ([MCP threat modelling and tool poisoning](https://silentzero.ooo/wiki/sources/2026-huang-model-context-protocol.html.md)). See [Model Context Protocol](https://silentzero.ooo/wiki/concepts/model-context-protocol.html.md).

A July 2026 preprint adds an attack that carries no explicit malicious instruction: benign command-line steps of a coding agent that pass state to each other through files, environment variables and hooks. In the authors' 2,525 trials, built from 101 attack paths they constructed, it succeeded in 96.59 per cent. On Claude Code a capability policy (Progent) and an information-flow policy (CaMeL, run there as a monitor over the trace) did not lower the rate ([MOSAIC](https://silentzero.ooo/wiki/sources/2026-wu-mosaic-knowledge-guided.html.md)).

An October 2026 preprint shows that the guarantee of CaMeL does not carry over to agents that call other agents. Untrusted data that one agent hands to another in the instruction text is read there as trusted, and changes the second agent's plan. The authors built such an attack. On their own multi-agent benchmark, averaged over five models, attack success was 12.9 per cent without CaMeL, 0.2 per cent with CaMeL on each agent and 0.0 per cent with a protocol that keeps data apart from instructions ([Can CaMeLs Talk?](https://silentzero.ooo/wiki/sources/2026-peters-gill-can-camels.html.md)).

Two further preprints bear on the defences around the model. ToolFence compiles a typed authorization blueprint from the user's request, with a model call that sees only the request and the tool schemas, and checks every tool call against it with a deterministic monitor; a model judge may grant capabilities the blueprint missed, seeing their shape and not the argument values. On AgentDojo it reached 0.20 per cent attack success with Qwen3-max against 0.42 per cent for CaMeL, with a lower runtime cost, against AgentDojo's fixed attacks; the authors claim no formal guarantee ([ToolFence](https://silentzero.ooo/wiki/sources/2026-li-toolfence-fine-grained.html.md)). A single-author preprint argues that a denied tool call is itself a channel, since the agent can infer from the refusal what exists and pass it on, and proposes a monitor that records denials; its evidence is three constructed scenarios ([Causality laundering](https://silentzero.ooo/wiki/sources/2026-chinaei-causality-laundering-denial.html.md)).

## Open questions

- When the user asks the agent to follow instructions found in data, data becomes control; isolating the planner alone cannot stop it, and policies and capabilities have to carry the load ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), §6.4).
- Sequences of individually allowed steps may add up to a harmful one ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), §9.3).
- The Silent Zero paper treats prompt injection as a [Confused deputy](https://silentzero.ooo/wiki/concepts/confused-deputy.html.md) problem (Section 2.4) and limits what capabilities do against it (Section 6). See [The broker](https://silentzero.ooo/wiki/design/broker.html.md).

## Sources

- [adaptive evaluation of out-of-band defenses](https://silentzero.ooo/wiki/sources/2026-narisetty-adaptive-evaluation-out.html.md)
- [breaking the protocol](https://silentzero.ooo/wiki/sources/2026-maloyan-breaking-protocol-security.html.md)
- [Can CaMeLs Talk?](https://silentzero.ooo/wiki/sources/2026-peters-gill-can-camels.html.md)
- [Causality laundering](https://silentzero.ooo/wiki/sources/2026-chinaei-causality-laundering-denial.html.md)
- [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)
- [Indirect prompt injection](https://silentzero.ooo/wiki/sources/2023-greshake-not-what-you.html.md)
- [MCP threat modelling and tool poisoning](https://silentzero.ooo/wiki/sources/2026-huang-model-context-protocol.html.md)
- [MCP-38](https://silentzero.ooo/wiki/sources/2026-shen-mcp-38-comprehensive.html.md)
- [MOSAIC](https://silentzero.ooo/wiki/sources/2026-wu-mosaic-knowledge-guided.html.md)
- [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md)
- [The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md)
- [ToolFence](https://silentzero.ooo/wiki/sources/2026-li-toolfence-fine-grained.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Confused deputy](https://silentzero.ooo/wiki/concepts/confused-deputy.html.md)
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md)
- [Model Context Protocol](https://silentzero.ooo/wiki/concepts/model-context-protocol.html.md)
- [Agent Operating Systems](https://silentzero.ooo/wiki/sources/2026-sharma-agent-operating-systems.html.md)
- [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md)
- [AgentOS](https://silentzero.ooo/wiki/sources/2026-liu-agentos-application-silos.html.md)
- [LeftoverLocals](https://silentzero.ooo/wiki/sources/2024-trail-leftoverlocals-listening-llm.html.md)
- [Quine](https://silentzero.ooo/wiki/sources/2026-ke-quine-realizing-llm.html.md)
