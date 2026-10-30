---
type: concept
status: reviewed
sources: [2026-nasr-attacker-moves-second, 2025-debenedetti-defeating-prompt-injections]
updated: 2026-10-29
---

# Prompt injection

An attacker places instructions in data that a language-model agent reads, such as an email, a document or a web page, so that the agent acts on them instead of on its user's request. A jailbreak, by contrast, is the user working against the model designer's intent ([[2026-nasr-attacker-moves-second]], §5).

## Two kinds of defence

- Heuristic and model-based defences: prompts, training against known attacks, detectors in front of or behind the model, secret canaries. Twelve such defences against prompt injection and jailbreaks fell to adaptive attacks, fully or substantially and most above 90 per cent, after most had reported near zero ([[2026-nasr-attacker-moves-second]]).
- Defences around the model: CaMeL keeps untrusted data away from the part that plans, and checks every tool call against policies on where data came from and who may see it. It stopped AgentDojo's attacks within its threat model, at some cost in utility; its interpreter is not verified, and it leaves some side channels and attack classes open ([[2025-debenedetti-defeating-prompt-injections]]). Nasr et al. skip such designs because their attacks would fail by construction, and note that they fit a limited set of tasks and reduce utility ([[2026-nasr-attacker-moves-second]], Appendix G.1).

## State, October 2026

No defence in the sources survives an adaptive attacker by evaluation alone; evaluations can only fail to break a defence ([[2026-nasr-attacker-moves-second]], §6). Defences around the model hold by construction within their threat model, and have not been tested adaptively ([[2025-debenedetti-defeating-prompt-injections]]).

## Open questions

- When the user asks the agent to follow instructions found in data, data becomes control; isolating the planner alone cannot stop it, and policies and capabilities have to carry the load ([[2025-debenedetti-defeating-prompt-injections]], §6.4).
- Sequences of individually allowed steps may add up to a harmful one ([[2025-debenedetti-defeating-prompt-injections]], §9.3).
- The zOS paper treats prompt injection as a [[confused-deputy]] problem (Section 2.4) and limits what capabilities do against it (Section 6). See [[broker]].
