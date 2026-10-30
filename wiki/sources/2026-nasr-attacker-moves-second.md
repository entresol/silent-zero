---
type: source
id: 2026-nasr-attacker-moves-second
status: reviewed
read: full
kind: test
sources: [2026-nasr-attacker-moves-second]
updated: 2026-10-29
---

# Nasr et al. 2026: The Attacker Moves Second

Milad Nasr, Nicholas Carlini, Chawin Sitawarin, Sander V. Schulhoff, Florian Tramèr and nine co-authors (OpenAI, Anthropic, Google DeepMind, HackAPrompt, ETH Zürich and others). The zOS paper's reference list gives USENIX Security 2026; the wiki read arXiv version 1 of 10 October 2025, marked "under review". [arXiv](https://arxiv.org/abs/2510.09023).

## What it shows

- **Twelve defences broken.** Against jailbreaks and prompt injections, the authors attack 12 recent defences of four kinds: prompting, training against attacks, filtering models, and secret-knowledge checks. They break them "either fully or substantially" (§1), for most with attack success rates above 90 per cent, where "the majority of defenses originally reported near-zero" (abstract, Figure 1). The twelve include jailbreak defences (RPO, Circuit Breakers) and commercial detectors (Model Armor, Protect AI).
- **Examples.** Spotlighting and prompt sandwiching above 95 per cent on AgentDojo with search; MetaSecAlign 96 per cent where its paper reported 2; Circuit Breakers 100 per cent with RL; the detectors Protect AI, PromptGuard and Model Armor above 90 per cent with Gemini 2.5 Pro as the base model, PIGuard 71; MELON 76 per cent on Llama 3.3 70B without knowledge of the defence, 95 with (§5).
- **Humans still win.** An online red-teaming competition with over 500 participants succeeded against every scenario tested; on a subset, search succeeded 69 per cent of the time and humans collectively 100 (§4, §6, Lesson 3).
- **The method.** One adaptive loop instantiated four ways: gradients, reinforcement learning, search with an LLM as mutator, and human red-teaming (§4). If a defence fails against any adaptive instance, "it cannot be considered robust".
- **The lesson.** Static benchmarks and weak attacks give "a false sense of security"; an evaluation can only fail to show a defence is broken, never show it robust (§6, Lessons 1 and 2).

## How

Each defence was evaluated with the benchmarks of its original paper (HarmBench, AgentDojo, OpenPromptInject and others), so results are not comparable across defences (§5). Attackers were given large compute budgets on purpose: the question was whether a defence works, not how hard it is to break (§3).

## Limits

The authors state:

- The goal is not a full comparison of defences (§5).
- Automated attacks are less reliable than image-based attacks such as PGD (Lesson 2) and are outperformed by humans (Lesson 3); model-based judges used to score attacks can themselves be fooled (Lesson 4).
- They skip "plan-then-execute" defences such as Tool Filter, CaMeL and IPIGuard, "because the attack is guaranteed to fail in most of the selected scenarios as the planning phase is done independently of the triggers". Such defences are "not a panacea as they are applicable to a limited set of tasks and hence, noticeably reduce the utility"; evaluating them needs scenarios where control flow depends on data (Appendix G.1).

A careful reader adds:

- **Version.** The wiki read the October 2025 preprint; the published version may differ.
- **Shared authors.** Carlini, Tramèr, Shumailov, Hayes and Terzis are authors of both this paper and [[2025-debenedetti-defeating-prompt-injections]]; the two are not independent evidence on system-level defences.

## Against the wiki

- [[2025-debenedetti-defeating-prompt-injections]]: **complements** it. CaMeL is one of the plan-then-execute designs this paper skips, with the authors' own reason and their caveat on utility.
- [[prompt-injection]]: created with this source.

## For zOS

- [[broker]]: the paper (Section 2.4) says adaptive attacks broke 12 published defences, most with success rates above 90 per cent. Confirmed, with two notes: the source says "either fully or substantially", and not all twelve are published papers. This is the evidence behind the paper's thesis that zOS does not try to make the agent trustworthy.
- Our reading: any broker that relies on a model to judge whether a request is benign is a defence of the kind broken here. The broker's decisions must not depend on a model's judgement of untrusted text.
