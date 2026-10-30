---
type: source
id: 2025-debenedetti-defeating-prompt-injections
status: reviewed
read: partial
kind: test
sources: [2025-debenedetti-defeating-prompt-injections]
updated: 2026-10-29
---

# Debenedetti et al. 2025: Defeating Prompt Injections by Design (CaMeL)

Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes, Nicholas Carlini, Daniel Fabian, Christoph Kern, Chongyang Shi, Andreas Terzis and Florian Tramèr (Google, Google DeepMind, ETH Zürich). Preprint; read in arXiv version 2 of 24 June 2025. [arXiv](https://arxiv.org/abs/2503.18813). The main text (§1 to §11) and appendices D, E and I (strict mode, the policies used, a worked side channel) were read; the other appendices hold result tables, prompts and transcripts.

## What it shows

- **A system layer around an untrusted model.** CaMeL ("CApabilities for MachinE Learning") separates a *privileged* LLM, which sees only the user's request and writes a program in restricted Python, from a *quarantined* LLM, which parses untrusted data into a fixed schema and has no tools. A custom interpreter runs the program, tracks for every value where it came from and who may read it, and checks security policies before every tool call (§5). Its "capabilities" are these tags of provenance and allowed readers; the authors use the word in "the standard security definition" (§1, footnote 2; §5.3).
- **A formal security definition.** The authors state what security means as a game, PI-SEC: the adversary wins if the agent takes an action outside the set allowed for the user's prompt (§4). They claim "guarantees that no policy violation can take place" (§1).
- **Why both flows matter.** Isolating the planner protects the control flow, but injected data can still change a tool's arguments, much as SQL injection changes a query's parameters while its structure stays intact (§2). The capabilities and policies close that gap.
- **The headline figure.** "77% of tasks with provable security (compared to 84% with an undefended system) in AgentDojo" (abstract). The abstract names no model; per model and suite the drop varies widely (Table 2).
- **Attacks in AgentDojo.** Without policies, CaMeL cut successful attacks for every model tested, for Gemini 2.5 Pro from 300 to 0 of 949 (§6.2.1). The attacks that still counted as successful, for some models, were outside the threat model: one where the user asks the agent to act on instructions in a document, and one that merely shows an injected recommendation (§6.2.1, §6.2.2). With Claude 3.5 Sonnet, CaMeL had 0 successful attacks, the next best defence 8 (§6.3).
- **Costs.** CaMeL needs about 2.8 times the input and 2.7 times the output tokens of native tool calling for the median task, measured with Claude 3.5 Sonnet under attack; no other defence compared needs as many (§6.5). Utility drops mainly where tasks need the planner to act on data it cannot see, and where tool outputs are poorly documented (§6.1.2).
- **Policies and approvals.** Policies are short rules per tool, for example: send money only if the recipient came from the user or can read every part of the transaction; share a file only with an address that came directly from the user (Appendix E). In the implementation the CaMeL engine defines them; users, tool providers or automatic derivation are envisaged later (§5.2, §10). When a policy blocks a call, a real deployment would ask the user to confirm (§5.4). Without attack, policies were triggered in 33.87 per cent of tasks in NORMAL mode and 53.23 per cent in STRICT mode, with large differences between suites (Appendix D, Table 8).

## How

The authors built CaMeL with a custom interpreter and Python policies and evaluated it on the AgentDojo benchmark. They used eight current models, AgentDojo's built-in attacks and three other defences for comparison; the baselines, failure analysis and overheads use Claude 3.5 Sonnet (§6).

## Limits

The authors state:

- Out of scope: text-to-text attacks that change no data or control flow, such as a misleading summary or phishing shown to the user; and full autonomy without human confirmation (§3.1).
- Side channels: private data can leak through loops and exceptions; STRICT mode closes the cases shown, but the adversary "might still be able to raise arbitrary exceptions by manipulating the data accessed by tools". The timing example does not work in the current interpreter, which lacks a time module, and the authors "do not exclude that other timing side-channels could be present" (§7).
- When the user asks the agent to follow instructions found in data, data flow becomes control flow; this task "is not stoppable simply by using the isolation" and needs policies and capabilities (§6.4).
- Attacks in the spirit of return-oriented programming may work: "an attacker might be able to create a malicious control flow by approximating it with the smaller control flow blocks that are allowed by the security policy" (§9.3).
- Users must codify and maintain policies, and approval prompts risk user fatigue (§9.2, §9.3). "No, prompt injection attacks are not fully solved." (§9.3)
- Verifying the interpreter and its enforcement of policies is future work (§10).

A careful reader adds:

- **Adaptive attacks.** The security evaluation uses AgentDojo's own attacks. The authors argue that adaptive prompts hurt heuristic defences (§6.3, citing US-AISI 2025); they do not run adaptive attacks against CaMeL itself. [[2026-nasr-attacker-moves-second]] skips CaMeL because its attacks would fail by construction.

## Against the wiki

- [[2026-nasr-attacker-moves-second]]: **complements** it; see there for why CaMeL was left out and for the caveat on utility.
- [[prompt-injection]]: CaMeL is the main defence around the model.
- [[object-capabilities]]: CaMeL's capabilities are labels for information flow, related to but distinct from object capabilities.

## For zOS

- [[broker]]: the paper's Table 1 cites "CaMeL solves 77 % of tasks with provable security versus 84 % undefended". Confirmed as the abstract states it. Our reading: "provable" here means a stated security property (PI-SEC) that holds by construction if the interpreter and policies are correct; the interpreter is not verified, and the security testing used static attacks.
- Our reading: CaMeL is the closest existing design to what the paper's broker must do above the kernel: bind each action to recipients and data, check at every tool call, ask a person when policy says no. Its limits name the broker's open problems: who writes the policies, how approvals avoid fatigue, how to stop harmful sequences of individually allowed steps, and what the agent may do with instructions found in data.
