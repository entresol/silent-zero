---
type: source
id: 2026-peters-gill-can-camels
status: reviewed
read: full
kind: test
sources: [2026-peters-gill-can-camels, 2025-debenedetti-defeating-prompt-injections]
updated: 2026-11-10
---

# Peters-Gill et al. 2026: Can CaMeLs Talk?

James Peters-Gill, Avi Semler, Henning Bartsch, Ilia Shumailov and Christian Schroeder de Witt. "Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks". [arXiv:2610.05640](https://arxiv.org/abs/2610.05640), version 1 of 5 October 2026, cs.MA. A preprint. Read in full, the appendices only in part (the example trajectory and the result tables).

## What it shows

- **The setting.** Hierarchical systems in which a parent agent calls child agents as if they were tools, and the child treats its parent as its user. The authors call this the agent-as-tool pattern (§II.A). They define control-flow integrity for such systems: execution stays inside a plan fixed by the user's instruction and other trusted information (§II.B, Definition 3). CaMeL, which plans in a trusted model and keeps untrusted data in a separate one ([[2025-debenedetti-defeating-prompt-injections]]), satisfies it for a single agent.
- **CaMeL does not compose.** Securing each agent with CaMeL does not secure the system. The parent puts a value derived from untrusted data into the natural-language instruction for a child; the child's planner reads it as trusted input and changes its plan. The authors name this boundary laundering. Their example has an orchestrator, an SQL agent and a notification agent, all under CaMeL with the trivial policy and one frontier model as planner and quarantined model. An injected request in the database adds an email call to the notification agent's plan (§III.A, Figures 1 to 3).
- **A general statement.** Every system in the tree-shaped agent-as-tool setting that has more than one agent and a tool with untrusted return values violates system-level control-flow integrity, even if each agent satisfies it, under one assumption: for any two tools of an agent, agent calls included, some instruction calls the second with arguments that depend on the first's result. The proof is a short case analysis (§III.C).
- **Single-agent CaMeL still helps.** In one small demonstration, an attack from the OMNI-Leak setup that needs one agent's plan hijacked failed against CaMeL agents in the authors' orchestrator topology: 0 per cent success in 5 trials, benign accuracy 100 per cent (§III.B).
- **The fix: multi-CaMeL.** The call to a child gets two arguments, a trusted message and a dictionary of values the child's planner cannot see and reads at run time through a `get_variable` tool. The interpreter enforces that the message depends on no tool output and carries provenance across the boundary. Untrusted data can still choose among branches the plan already holds (the authors call this branch steering) but cannot add paths (§IV).
- **Security result.** On MultiAgentDojo, the authors' split of AgentDojo's tools among two to four sub-agents per suite behind an orchestrator, with 949 injected task instances per model and configuration and five backend models, the attack success rate averaged over the models was 12.9 per cent without CaMeL (model-side defences only), 0.2 per cent with CaMeL on each agent and 0.0 per cent with multi-CaMeL (Table III). The per-model rates without CaMeL ranged from 0.0 to 36.1 per cent. All residual successes under single-agent CaMeL were boundary laundering (§V.B, §V.C). The evaluation used the trivial policy, so it tests plan integrity and not data-flow policies. The constructed attack of §III.A is a single demonstration, not one of these rates.
- **Utility result.** On AssetOpsBench (112 tasks after the authors excluded 29 they judge unsatisfiable as specified), single-agent CaMeL cost 21.6 points of task success on average against no CaMeL, and multi-CaMeL 3.2 points more on average across the five models; across the two strongest models the extra cost was 0.85 points. The confidence intervals of the two CaMeL settings overlap for every model (§V.A). All tools needed full return schemas in their descriptions, because the planner writes the parsing code before it sees the output (§V).

## How

New code on top of the CaMeL and AgentDojo implementations, five models from several vendors accessed through a router, and two benchmarks, one of them the authors' own. Their code and benchmark are announced as released (§VIII). The authors used language models as coding and editing assistants and say they inspected the output (§IX).

## Limits

What the authors say themselves:

- Only trees: each agent has one parent. Directed graphs, cycles, asynchronous and peer-to-peer designs are left open (§VI.A).
- The noninterference-style property of the LLMbda calculus rules out some behaviour that control-flow integrity permits, branch steering among them; the authors leave the formal relation between the two open (§VI.B).
- Multi-CaMeL inherits the CaMeL interpreter's gaps: implicit dependencies on branches not taken can be missed. It has no retry loop and so not that leak. Confinement against covert channels is open (§VI.B).
- Zero success on one model without any defence "should not be interpreted" as robustness, since it may reflect the attacks the benchmark contains and not immunity to stronger adaptive attacks, and large-scale adaptive red teaming found non-zero success against all frontier models tested (Table III note).
- Most benign failures come from fixing the plan before seeing data, and some from a sub-agent silently returning data for a nearby scope that the parent's plan does not check (§V.C).

A careful reader adds: the headline security gain is a drop from 0.2 to 0.0 per cent of 949 attempts per model, on a benchmark built by the authors; AgentDojo's attacks are not adaptive, which the paper does not state for this benchmark; the stronger evidence is the construction of the counterexample and the case analysis, not the percentages. The utility figures come from one LLM-judged benchmark. It is a preprint.

## Against the wiki

- [[prompt-injection]]: extends. The defences around the model are tested there only for one agent; this source shows by a worked attack that the guarantee needs the call between agents to be controlled too.
- [[broker]]: extends the CaMeL row. It does not contradict the figures of the original paper; it adds a case that paper's threat model, one agent, did not cover.
- [[information-flow-control]]: the source places its property next to a noninterference property and says control-flow integrity is the weaker one (§VI.B). It does not say anything about FIDES.

## For zOS

The zOS paper has several untrusted agents, each in its own protection domain (Section 3), and starts with one; as far as this wiki has read, it does not discuss agents that call agents, so nothing in it is contradicted. Our reading: if zOS lets one agent delegate to another, the instruction a delegating agent writes for its helper is a channel on which untrusted data can become trusted. The capabilities the broker grants would still bound what the helper can reach, and would not stop it from being steered within them. The part affected is [[broker]]; its state does not change. Candidates for the pool, named by this source and not yet in it: Naik et al. on OMNI-Leak, Garby, Gordon and Sands on the LLMbda calculus, and Foerster et al. on CaMeL for computer-use agents.
