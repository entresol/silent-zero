---
type: source
id: 2026-fu-cari-cross-boundary
status: reviewed
read: partial
kind: test
sources: [2026-fu-cari-cross-boundary]
updated: 2026-11-27
---

# CARI: cross-boundary adversarial runtime injection in coding-agent workflows

Jie Fu, Shuang Wu, Ashish Kundu, Wendy Hui Wang and Yuan Hong; arXiv 2610.38799, v1 of 28 October 2026, in the format of IEEE Transactions on Dependable and Secure Computing. A preprint; the page does not say it has been accepted anywhere. [arxiv.org/abs/2610.38799](https://arxiv.org/abs/2610.38799). Read in part: abstract, introduction, threat model, set-up, the results on models, placement, product agents and prompt-level defences, and the discussion; not the appendices.

## What it shows

- **A new injection path.** A component the victim's coding agent must talk to (a backend, a test harness, a CI job, a deployment service) may report its own state but has no authority over the victim's files, credentials or shell. The authors let such a component put instructions into the runtime feedback it returns, so that the agent turns diagnostic advice into actions on its own side (abstract, §1, §3.2). They call it direct runtime injection, against the usual case in which poisoned content is placed first and read later.
- **High success in the authors' harness.** Ten attacks, four programming languages, five models, 15 trials per attack, language and model: 2,845 of 3,000 successes, 94.8 per cent (abstract). Per model the rate runs from 86.3 per cent (GPT-5.4-mini) to 99.0 per cent (Gemini 2.5 Flash) (§5.2).
- **Placement matters.** The payload was byte-identical and the task told the agent to read the artifact or log in every condition. Success on GPT-5.4-mini was 8.9 per cent as a static artifact, 35.6 per cent in a runtime log and 93.3 per cent as a diagnostic that appears when the agent runs its task; on Claude Sonnet 4.5 it was 2.2, 57.8 and 97.8 per cent. Three actions, 15 trials each, 45 per condition and model, in the authors' harness only (§5.3).
- **Product agents lower it, not remove it.** On the Python target, GPT-5.4-mini in Codex reached 61.3 per cent (84.7 per cent in the authors' harness) and Claude Sonnet 4.5 in Claude Code 58.7 per cent (98.0 per cent). Two attacks, file permissions and a fake SSH key, fell to 0 per cent on both products; the authors say this first leaves open whether the products resist the behaviour or the wording of those payloads (§5.5; one target, ten attacks, and the products' settings are the closest available permission configuration, §5.1). Their follow-up with less explicit wording raised success again, for local-account collection from 13.3 to 73.3 per cent on Codex and from 0 to 40.0 per cent on Claude Code, and for file permissions from 0 to 46.7 and 40.0 per cent; the authors conclude that part of the resistance depends on the wording (§5.6, Table 6).
- **Prompt-level defences trade safety for use.** A generic warning left success at 94.7 per cent (Claude Sonnet 4.5) and 66.0 per cent (GPT-5.4-mini) and kept benign tasks at 100 and 88.7 per cent. An attack-aware policy, written with knowledge of the attack classes, cut success to 6.0 and 11.3 per cent, and benign tasks completed fell to 60.7 and 20.7 per cent; for the retry-loop attack alone it gave 0 per cent success at 100 per cent benign completion (§7.2, Table 8; two models, 15 trials per condition, non-adaptive attacks, so the figures are a best case).
- **The authors' pointer.** Runtime decisions should consider where feedback comes from and what actions it may influence; among six directions (detection, instruction hierarchy, capability scoping, provenance tracking, runtime action monitoring, execution isolation) they say provenance alone is insufficient and point to provenance- and boundary-aware mediation of security-sensitive actions; they do not test it (§8.2).

## How

A Todo application written four times (Python, Go, Java, Rust) with a backend, a frontend client and tests. The attacker controls the backend's responses; the victim agent acts for a separate integration role and repairs a failing integration test. Five models (GPT-5.4-mini, Claude Sonnet 4.5, Gemini 2.5 Flash, Qwen3-coder, Codestral-2508) ran in the mini-swe-agent harness with no step limit; Codex and Claude Code ran with default settings, which allow shell and network access to local mock services without approval (§5.1).

## Limits

The authors say themselves that the application is a controlled one, and that success rates need not carry over to production systems with their own access controls and agent configuration (§8.1). They tested only system-prompt defences and none of the stronger ones they list (§8.2). A careful reader adds: the numbers come from synthetic backends the authors wrote, with synthetic credentials; each product agent was tested with one model; and the page rests on the parts read, not on the appendices.

## Against the wiki

- [[prompt-injection]]: **extends**. A source of injection the page does not yet name: the live component's feedback, with authority to report and none to act. Our reading: the results fit the page's point that prompt-level rules are a weak defence: a generic warning gave limited protection (94.7 and 66.0 per cent success), and the attack-aware policy suppressed attacks while refusing many legitimate tasks. The attacks were not adaptive.
- [[confused-deputy]]: **extends**. Our reading: the coding agent is the deputy that holds the victim's authority and acts on a peer's request; the paper does not use the term.
- [[broker]]: **confirms**, no change of state. Our reading: the case supports enforcing authority outside the model; the paper does not test such a defence.

## For zOS

[[broker]]: no change. The paper does not touch a claim of the zOS paper; it adds an attack setting. Our reading: the defences it tests are prompt rules, which the broker does not rely on; the direction it names, mediating actions by the origin of the feedback, is close to the broker's job but is not tested.
