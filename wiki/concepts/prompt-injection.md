---
type: concept
status: reviewed
sources: [2026-nasr-attacker-moves-second, 2025-debenedetti-defeating-prompt-injections, 2023-greshake-not-what-you, 2025-costa-securing-ai-agents, 2026-shen-mcp-38-comprehensive, 2026-narisetty-adaptive-evaluation-out, 2026-maloyan-breaking-protocol-security, 2026-huang-model-context-protocol]
glossary: Prompt injection
updated: 2026-11-05
---

# Prompt injection

An attacker places instructions in data that a language-model agent reads, such as an email, a document or a web page, so that the agent acts on them instead of on its user's request. A jailbreak, by contrast, is the user working against the model designer's intent ([[2026-nasr-attacker-moves-second]], §5). The *indirect* variant, with the instructions placed in data the application retrieves rather than typed by its user, was analysed in 2023 in what its authors present as the first systematic treatment, with demonstrations against Bing Chat and applications built on GPT-4 ([[2023-greshake-not-what-you]]).

## Two kinds of defence

- Heuristic and model-based defences: prompts, training against known attacks, detectors in front of or behind the model, secret canaries. Twelve such defences against prompt injection and jailbreaks fell to adaptive attacks, fully or substantially and most above 90 per cent, after most had reported near zero ([[2026-nasr-attacker-moves-second]]).
- Defences around the model: CaMeL keeps untrusted data away from the part that plans, and checks every tool call against policies on where data came from and who may see it. It stopped AgentDojo's attacks within its threat model, at some cost in utility; its interpreter is not verified, and it leaves some side channels and attack classes open ([[2025-debenedetti-defeating-prompt-injections]]). FIDES tracks confidentiality and integrity labels through the planner and blocks consequential tool calls whose choice untrusted data influenced; with its policies it let none of AgentDojo's attacks through that it counts against them, controls explicit flows only, and lets attacks that change only the text shown to the user pass ([[2025-costa-securing-ai-agents]]). See [[information-flow-control]]. Nasr et al. skip such designs because their attacks would fail by construction, and note that they fit a limited set of tasks and reduce utility ([[2026-nasr-attacker-moves-second]], Appendix G.1).

## State, October 2026

No defence in the sources survives an adaptive attacker by evaluation alone; evaluations can only fail to break a defence ([[2026-nasr-attacker-moves-second]], §6). Defences around the model hold by construction within their threat model, and CaMeL and FIDES have not been tested adaptively ([[2025-debenedetti-defeating-prompt-injections]], [[2025-costa-securing-ai-agents]]). A June 2026 preprint ran one such defence, Progent, against a hand-made adaptive attack on a weak open-weight model; attack success stayed low, at 2.6 per cent; the authors call it one small data point that is consistent with, and does not establish, the idea that such defences are harder to attack than detectors ([[2026-narisetty-adaptive-evaluation-out]]). It also names the open weak spots: who assigns the labels, tasks that must act on untrusted content, and side channels. In 2023 effective mitigations were "currently lacking" ([[2023-greshake-not-what-you]], abstract). For the Model Context Protocol, a 2026 preprint lists 38 threat categories, among them the injection of instructions through tool descriptions and chains of benign tools; it states that five open-source scanners and proxies together cover at most 18 of them, though its own table does not match that ([[2026-shen-mcp-38-comprehensive]]). Two further preprints measure it: in the authors' own harness attack success rose from 26.4 to 52.8 per cent when equivalent tools were reached through MCP ([[2026-maloyan-breaking-protocol-security]]), and of seven MCP clients tested with poisoned tool descriptions one failed all four attacks, while for file reading and remote scripts those that held did so largely through the model's refusal ([[2026-huang-model-context-protocol]]). See [[model-context-protocol]].

## Open questions

- When the user asks the agent to follow instructions found in data, data becomes control; isolating the planner alone cannot stop it, and policies and capabilities have to carry the load ([[2025-debenedetti-defeating-prompt-injections]], §6.4).
- Sequences of individually allowed steps may add up to a harmful one ([[2025-debenedetti-defeating-prompt-injections]], §9.3).
- The zOS paper treats prompt injection as a [[confused-deputy]] problem (Section 2.4) and limits what capabilities do against it (Section 6). See [[broker]].
