---
type: concept
status: reviewed
sources: [2026-nasr-attacker-moves-second, 2025-debenedetti-defeating-prompt-injections, 2023-greshake-not-what-you, 2025-costa-securing-ai-agents, 2026-shen-mcp-38-comprehensive, 2026-wu-mosaic-knowledge-guided]
glossary: Prompt injection
updated: 2026-11-07
---

# Prompt injection

An attacker places instructions in data that a language-model agent reads, such as an email, a document or a web page, so that the agent acts on them instead of on its user's request. A jailbreak, by contrast, is the user working against the model designer's intent ([[2026-nasr-attacker-moves-second]], §5). The *indirect* variant, with the instructions placed in data the application retrieves rather than typed by its user, was analysed in 2023 in what its authors present as the first systematic treatment, with demonstrations against Bing Chat and applications built on GPT-4 ([[2023-greshake-not-what-you]]).

## Two kinds of defence

- Heuristic and model-based defences: prompts, training against known attacks, detectors in front of or behind the model, secret canaries. Twelve such defences against prompt injection and jailbreaks fell to adaptive attacks, fully or substantially and most above 90 per cent, after most had reported near zero ([[2026-nasr-attacker-moves-second]]).
- Defences around the model: CaMeL keeps untrusted data away from the part that plans, and checks every tool call against policies on where data came from and who may see it. It stopped AgentDojo's attacks within its threat model, at some cost in utility; its interpreter is not verified, and it leaves some side channels and attack classes open ([[2025-debenedetti-defeating-prompt-injections]]). FIDES tracks confidentiality and integrity labels through the planner and blocks consequential tool calls whose choice untrusted data influenced; with its policies it let none of AgentDojo's attacks through that it counts against them, controls explicit flows only, and lets attacks that change only the text shown to the user pass ([[2025-costa-securing-ai-agents]]). See [[information-flow-control]]. Nasr et al. skip such designs because their attacks would fail by construction, and note that they fit a limited set of tasks and reduce utility ([[2026-nasr-attacker-moves-second]], Appendix G.1).

## State, October 2026

No defence in the sources survives an adaptive attacker by evaluation alone; evaluations can only fail to break a defence ([[2026-nasr-attacker-moves-second]], §6). Defences around the model hold by construction within their threat model, and have not been tested adaptively ([[2025-debenedetti-defeating-prompt-injections]], [[2025-costa-securing-ai-agents]]). In 2023 effective mitigations were "currently lacking" ([[2023-greshake-not-what-you]], abstract). For the Model Context Protocol, a 2026 preprint lists 38 threat categories, among them the injection of instructions through tool descriptions and chains of benign tools; it states that five open-source scanners and proxies together cover at most 18 of them ([[2026-shen-mcp-38-comprehensive]]).

A July 2026 preprint adds an attack that carries no explicit malicious instruction: benign command-line steps of a coding agent that pass state to each other through files, environment variables and hooks. In the authors' 2,525 trials, built from 101 attack paths they constructed, it succeeded in 96.59 per cent. On Claude Code a capability policy (Progent) and an information-flow policy (CaMeL, run there as a monitor over the trace) did not lower the rate ([[2026-wu-mosaic-knowledge-guided]]).

## Open questions

- When the user asks the agent to follow instructions found in data, data becomes control; isolating the planner alone cannot stop it, and policies and capabilities have to carry the load ([[2025-debenedetti-defeating-prompt-injections]], §6.4).
- Sequences of individually allowed steps may add up to a harmful one ([[2025-debenedetti-defeating-prompt-injections]], §9.3).
- The zOS paper treats prompt injection as a [[confused-deputy]] problem (Section 2.4) and limits what capabilities do against it (Section 6). See [[broker]].
