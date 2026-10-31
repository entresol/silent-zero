---
type: source
id: 2023-greshake-not-what-you
status: reviewed
read: full
kind: test
sources: [2023-greshake-not-what-you]
updated: 2026-10-31
---

# Greshake et al. 2023: Indirect prompt injection

Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz and Mario Fritz (Saarland University, sequire technology, CISPA). "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection". Proc. AISec '23; read from [arXiv:2302.12173](https://arxiv.org/abs/2302.12173), version 2 of 5 May 2023, with its appendix of prompts skimmed.

## What it shows

- **The concept.** Applications that retrieve data for a language model blur the line between data and instructions. An attacker who places a prompt in data likely to be retrieved, such as a web page or an email, can steer the model without access to it: *indirect* prompt injection. The authors liken retrieved prompts to "arbitrary code" (abstract, §1).
- **A taxonomy** of injection methods and threats from a security perspective: information gathering and data theft, fraud, intrusion including persistence, remote control and API calls, malware including injections spreading as worms, manipulated content, and availability (§3).
- **Demonstrations.** The authors attack synthetic applications built on OpenAI models (text-davinci-003 via LangChain, and GPT-4), Bing Chat in the Edge sidebar, with injections in local HTML files, and GitHub Copilot, where the code-completion attack proved "very sensitive to context" (§4.1.3, §4.2.4). Among the attacks are extracting a user's name, phishing links, spreading an injection by email, persistence through a memory, remote control by fetching new instructions, and code-completion manipulation (§4).
- **Little effort.** The prompts "often" worked "on the very first attempt", and the authors left their typos in to show it (§5.2).
- **No effective mitigation yet.** The authors tested no defences and call effective mitigations "currently lacking" (abstract). Filtering retrieved inputs, they argue, runs into a dilemma: a less general model may not fall for the trap but may miss complex or encoded injections; a supervising model might miss disinformation and manipulation; interpretability-based outlier detection is named as promising (§5.6).

## How

Attacks were run on synthetic applications with mock functions and prepared content, and on Bing Chat through local pages, never by injecting public sources (§4, §5.1). Results are qualitative demonstrations.

## Limits

What the authors say themselves: no attack success rates; quantifying them in interactive sessions is left to future work. Attacks on products the authors had no access to, such as Microsoft 365 Copilot and ChatGPT plugins, were not tested. In-the-wild feasibility is supported by anecdotes (§5.2). The vulnerabilities were disclosed to OpenAI and Microsoft (§5.1).

A careful reader adds:

- **Models of early 2023.** The demonstrations are on text-davinci-003, GPT-4 and Bing Chat of that time; later models and defences are measured elsewhere ([[2026-nasr-attacker-moves-second]], [[2025-debenedetti-defeating-prompt-injections]]).
- **Agents as outlook.** The paper studies LLM-integrated applications "as a first step" toward agents (§5.3); the agent case is argued, not tested.

## Against the wiki

- [[prompt-injection]]: the origin of the indirect variant; the authors present their taxonomy as the first systematic analysis.
- [[confused-deputy]]: our reading: likening retrieved prompts to arbitrary code is the paper's security analogy; it does not use the term confused deputy.
- [[broker]]: confirms the phenomenon the paper cites it for.

## For zOS

Section 2.4 of the paper: "Indirect prompt injection follows the same pattern, with instructions hidden in data steering an agent that acts with its user's rights (Greshake et al. 2023)." Confirmed for the phenomenon: hidden instructions in retrieved data steer the model, and in the demonstrations it acts through the application's functions on the user's behalf. Linking it to the confused deputy is the paper's own step. No `design/` page changes state.
