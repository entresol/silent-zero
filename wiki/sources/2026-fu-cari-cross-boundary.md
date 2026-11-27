---
type: source
id: 2026-fu-cari-cross-boundary
status: drafted
read: partial
kind: test
sources: [2026-fu-cari-cross-boundary]
updated: 2026-11-27
---

# CARI: cross-boundary adversarial runtime injection in coding-agent workflows

Jie Fu, Shuang Wu, Ashish Kundu, Wendy Hui Wang and Yuan Hong; arXiv 2610.38799, v1 of 28 October 2026, in the format of IEEE Transactions on Dependable and Secure Computing. A preprint; the page does not say it has been accepted anywhere. [arxiv.org/abs/2610.38799](https://arxiv.org/abs/2610.38799). Read in part: abstract, introduction, threat model, set-up, the results on models, placement, product agents and prompt-level defences, and the discussion; not the appendices.

## What it shows

- **A new injection path.** A component the victim's coding agent must talk to (a backend, a test harness, a CI job, a deployment service) may report its own state but has no authority over the victim's files, credentials or shell. The authors let such a component put instructions into the runtime feedback it returns, so that the agent turns diagnostic advice into actions on its own side (abstract, §1, §3.2). They call it direct runtime injection, against the usual case in which poisoned content is placed first and read later.
- **High success in the authors' harness.** Ten attacks, four programming languages, five models, 15 trials per attack, language and model: 2,845 of 3,000 successes, 94.8 per cent (abstract). Per model the rate runs from 86.3 per cent (GPT-5.4-mini) to 99.0 per cent (Gemini 2.5 Flash) (§5).
- **Placement matters.** With the payload byte-identical, success on GPT-5.4-mini was 8.9 per cent as a static artifact, 35.6 per cent in a runtime log and 93.3 per cent as a diagnostic that appears when the agent runs its task; on Claude Sonnet 4.5 it was 2.2, 57.8 and 97.8 per cent (§5, 15 trials per cell).
- **Product agents lower it, not remove it.** On the Python target, GPT-5.4-mini in Codex reached 61.3 per cent (84.7 per cent in the authors' harness) and Claude Sonnet 4.5 in Claude Code 58.7 per cent (98.0 per cent). Two attacks, file permissions and a fake SSH key, fell to 0 per cent on both products; the authors say the data do not separate resistance to the behaviour from resistance to the wording of those payloads (§5.4).
- **Prompt-level defences trade safety for use.** A generic warning left success at 94.7 per cent (Claude Sonnet 4.5) and 66.0 per cent (GPT-5.4-mini) and kept benign tasks at 100 and 88.7 per cent. An explicit security policy cut success to 6.0 and 11.3 per cent, and benign tasks completed fell to 60.7 and 20.7 per cent (§7, Table 8; two models, 15 trials per condition).
- **The authors' pointer.** Runtime decisions should consider where feedback comes from and what actions it may influence; they name capability scoping, provenance tracking and execution isolation as directions and do not test them (§8.2).

## How

A Todo application written four times (Python, Go, Java, Rust) with a backend, a frontend client and tests. The attacker controls the backend's responses; the victim agent acts for a separate integration role and repairs a failing integration test. Five models (GPT-5.4-mini, Claude Sonnet 4.5, Gemini 2.5 Flash, Qwen3-coder, Codestral-2508) ran in the mini-swe-agent harness with no step limit; Codex and Claude Code ran with default settings, which allow shell and network access to local mock services without approval (§5.1).

## Limits

The authors say themselves that the application is a controlled one, and that success rates need not carry over to production systems with their own access controls and agent configuration (§8.1). They tested only system-prompt defences and none of the stronger ones they list (§8.2). A careful reader adds: the numbers come from synthetic backends the authors wrote, with synthetic credentials; each product agent was tested with one model; and the page rests on the parts read, not on the appendices.

## Against the wiki

- [[prompt-injection]]: **extends**. A source of injection the page does not yet name: the live component's feedback, with authority to report and none to act. Its prompt-level results agree with the page's finding that defences inside the model do not hold.
- [[confused-deputy]]: **extends**. Our reading: the coding agent is the deputy that holds the victim's authority and acts on a peer's request; the paper does not use the term.
- [[broker]]: **confirms**, no change of state. Our reading: the case supports enforcing authority outside the model; the paper does not test such a defence.

## For zOS

[[broker]]: no change. The paper does not touch a claim of the zOS paper; it adds an attack setting, and its own defences are the kind the broker avoids.
