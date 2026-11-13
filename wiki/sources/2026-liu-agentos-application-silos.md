---
type: source
id: 2026-liu-agentos-application-silos
status: reviewed
read: partial
kind: design
sources: [2026-liu-agentos-application-silos]
updated: 2026-11-13
---

# Liu et al. 2026: AgentOS

Rui Liu, Tao Zhe, Dongjie Wang, Zijun Yao, Kunpeng Liu, Yanjie Fu, Huan Liu and Jian Pei. "AgentOS: From Application Silos to a Natural Language-Driven Data Ecosystem". [arXiv:2603.08938](https://arxiv.org/abs/2603.08938), version 2 of 11 March 2026. A vision paper framed for the data-mining community. Read in part: the abstract, the introduction, the architecture section and the section on risks in full; the section on data-mining methods was skimmed.

## What it shows

- **The proposal.** A "Personal Agent Operating System" that replaces the graphical desktop with a natural-language interface. Its core is an "Agent Kernel" that interprets intent, splits tasks and coordinates agents; applications become modular "Skills". The legacy kernel stays underneath, hidden (abstract, §1, §2).
- **Security.** The authors say that access-control lists, which either grant access or not, do not fit agents that need broad access, and call for a "Semantic Firewall" inside the Agent Kernel: input is checked for malicious intent, data from untrusted sources is marked as tainted and kept from triggering high-privilege actions (the authors say they were inspired by an experimental design called Aura), and outgoing actions are screened for leaks. The authors require strict sandboxes for high-risk operations and file-system snapshots to roll an erroneous action back (§4).

## How

An argument; there is no implementation or measurement in the text read.

## Limits

The security mechanisms are named, not specified or tested. The Semantic Firewall judges intent, which is the kind of model-based check that [[prompt-injection]] reports as defeated by adaptive attackers. Our reading, since the paper itself does not discuss attacks on the firewall. The paper uses "real-time" loosely, for example for the firewall and for rollback "in milliseconds", and gives no hard real-time guarantee; it makes no claim of formal verification.

## Against the wiki

- [[broker]]: another design above a conventional kernel, like [[2026-zou-agentkernel-trust-native]] and [[2026-sharma-agent-operating-systems]]. It differs from the second by relying on intent analysis, not on deny-by-default capability checks, as its main control; the first also keeps a model-based classifier beside capability narrowing, so there the difference is one of emphasis.
- [[agentos]]: unrelated to that system despite the name; the project there is an seL4-based platform.

## For zOS

Related work only. No `design/` page changes. The paper does not cite this source.
