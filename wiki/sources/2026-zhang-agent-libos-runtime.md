---
type: source
id: 2026-zhang-agent-libos-runtime
status: reviewed
read: full
kind: design
sources: [2026-zhang-agent-libos-runtime]
updated: 2026-11-05
---

# Zhang 2026: Agent libOS

Yingqi Zhang (Tsinghua University). "Agent libOS: A Runtime Substrate for Capability-Controlled Self-Evolving LLM Agents". [arXiv:2606.03895](https://arxiv.org/abs/2606.03895), version 3 of 18 August 2026. A preprint. Read in full; the extraction garbled Table 3, so its baseline rows are not quoted.

## What it shows

- **The problem.** Agents now persist, learn skills, write their own tools, fork children and save checkpoints. If a runtime lets what an action looks like (its schema) stand for permission to do it, self-evolution becomes a path to more authority (§1).
- **The invariant.** What the model can ask for may change; what it may affect and where its information may flow may not change with it (§1, abstract); the invariant I1 states it for authority over existing resources (§2.4). Skills, generated tools, images, checkpoints and child processes change the action surface, and none grants authority over existing resources (§5, Table 1).
- **Three planes.** Operation admission is a conjunction that must all hold: a live process, a typed capability, the ceiling of the task's authority manifest, deterministic policy or a person's approval, a budget and a concrete primitive. Information-flow admission carries labels and source references along, resolves the recipient from a registry the host owns, checks its clearance, and for conditionally permitted high-sensitivity egress needs an exact one-shot release by a person. A third plane records evidence and never grants anything (§2.3, equations 4 to 6, §3).
- **Capabilities.** Typed by resource, with an effect of allow, ask or deny, expiry, use counts and delegation that may keep or narrow a grant but never widen it (§3.1).
- **Labels.** Joins are conservative: highest sensitivity, lowest integrity and trust. Under the default configuration, unlisted recipients count as untrusted with a normal sensitivity ceiling. A release does not change a label (§3.3, §3.4).
- **Crashes.** Effects outside the database follow prepare, dispatch, settle. After a crash an effect that may have run stays "unknown", is never replayed blindly, and is reconciled only through a reconciliation hook that the operation's contract installs. The authors call this a mediation property, not exactly-once execution (§4).
- **Evaluation.** On the authors' own suite of scripted plans the full runtime passes 33 of 33 task oracles and 33 of 33 safety checks, with 0 of 119 unauthorized effects and 0 of 119 false denials. Three simple baselines run the same plans, and three ablations remove one component at a time (§7.2). A real-model gate with one model configuration records 12 of 12 safe and 12 of 12 fully useful runs (§7.4). A paired study of 15 pairs compares loading skills on demand with exposing every tool schema at once; the outcome oracle passes 15 of 15 in both arms, but runs that are fully correct in outcome, route, probe and exit are 13 of 15 in both (§7.6). Recovery gates seed 100,000 effect rows, and the crash matrix passes 6 of 6 cases (§7.3).

## How

A Python library with a command line and a local operator GUI, SQLite or PostgreSQL storage and typed providers for files, shell, Git, JSON-RPC and MCP. Git is deliberately typed: no arbitrary arguments, URLs or credentials from the model (§6). The code is at github.com/yingqi-z20/Agent-libOS; the evaluated commit is named in the paper (§7). Every quantitative result is generated from hashed reports bound to one source revision (§7.1).

## Limits

What the author says. It is not a kernel sandbox: it runs in a conventional Python process on the host, and trusted runtime modules, MCP stdio servers and any authorized shell or native program can use host authority outside the typed boundary. Prompt injection stays possible: the design bounds mediated authority and flows, not what the model decides. Once a recipient has data, its handling lies outside the threat model. The MCP part is a client subset. The results describe one model configuration and are not rates for agents in general. The design claims no noninterference theorem and does not try to stop untrusted data from changing the agent's plan (§2.1, §7.7, §8.3, §9.1).

A careful reader adds:

- **The base is trusted.** The trusted base lists the runtime managers, the Python interpreter, the storage backend and the host operating system (§2.1). Nothing in it is verified.
- **Scripted plans.** The 33 of 33 and the 0 of 119 come from deterministic plans made by the authors; they show that the checks fire where the authors put them, and the paper says as much (§7.7).
- **Small live samples.** Twelve canonical and thirty paired real-model runs, one model, no adaptive attacker.

## Against the wiki

- [[broker]]: extends it with a worked design of the same job above a conventional host. The conjunction of capability, ceiling, approval and budget is close to what the broker must do; the host stays unverified.
- [[information-flow-control]]: extends it with high-water labels and a one-shot release in place of automatic declassification. It differs from [[2025-costa-securing-ai-agents]] and [[2025-debenedetti-defeating-prompt-injections]] by not trusting the plan (§8.3).
- [[object-capabilities]]: capabilities with attenuating delegation and revocation at the primitive, in a library and not in a kernel.
- [[model-context-protocol]]: it treats MCP as a client only, with servers and items registered by the host; a server's declared capabilities do not become authority for the process (§6.4).
- [[agent-operating-systems]]: one of the designs listed there.

## For zOS

Section 5 of the paper: "Agent libOS keeps an agent's authority fixed while its tools and skills grow, on top of a conventional host (Zhang 2026)." Confirmed, with one qualification: the guarantee is that growth of the action surface does not by itself expand authority over existing resources. A person may still grant more later, and fresh resources get handles (§2.4, I1). The paper's sentence that none of these systems names real-time control as its goal holds for this one; the text speaks of budgets and recovery, not deadlines. No `design/` page changes state.
