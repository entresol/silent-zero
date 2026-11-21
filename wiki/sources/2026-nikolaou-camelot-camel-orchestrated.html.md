# CaMeLoT, a static check of an agent's plan on top of CaMeL

> CaMeLoT: a static temporal check of the agent’s plan before execution, on top of CaMeL; coverage and agreement with CaMeL, no attack-success figures. test, full text.

Source · Nikolaou et al. 2026 · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/2026-nikolaou-camelot-camel-orchestrated.html

Elia Nikolaou, Magnus Wiik Eckhoff, Robert Flood, Gudmund Grov, Vasileios Mavroeidis and David Aspinall (University of Edinburgh; Norwegian Defence Research Establishment and University of Oslo). "CaMeLoT: CaMeL orchestrated with Temporal logic for static verification and liveness", arXiv 2609.18674v1 [cs.CR], 16 September 2026. A preprint. [arXiv](https://arxiv.org/abs/2609.18674). I read the full text and the reference list only for the works the text names.

## What it shows

CaMeL ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)) has a privileged model write a plan as restricted Python, and checks each tool call at run time against policies on where its arguments came from. The authors add a layer that checks the whole plan, before any tool or model call, against temporal-logic policies (§1, §3).

- **The mechanism.** The plan's syntax tree is turned into a finite-state machine whose states are program points. It is labelled with the tool called, the provenance and taint of each argument, and history flags such as "approval already requested". Loops become a nondeterministic choice between another round and exit. Branch conditions are left out and also become nondeterministic choices. The nuXmv model checker verifies Computation Tree Logic (CTL) formulas over this model (§3, §3.2, §6). If a formula fails, the counterexample trace is turned into text and the privileged model is asked to repair the plan, until the plan passes or a repair budget runs out (§3, §4).
- **What it can state.** Rules that span a whole run, which per-call policies cannot express naturally: order ("confirm the host before isolating it"), approval before a strong action, "a created ticket is eventually resolved or escalated", "isolation must happen", "no isolation directly after a scan" (Table 4, §1).
- **Overlap with CaMeL, Experiment 1 (§5.1).** Mirroring CaMeL's own AgentDojo policies, CTL covers 22 of 28 security policies in full, one in part and five not at all. Of the confidentiality policies, which depend on who may read a value, it covers 16 in full and 9 not at all (Table 1). The authors leave confidentiality to CaMeL's run-time checks; §5.1 says confidentiality properties "are not handled directly by CaMeLoT; they overlap only when the output of a function call is public", and Table 1 counts policies, not reader sets. On the 97 AgentDojo user tasks with Claude Haiku 4.5, run without any injected attack, the two systems agree on block or pass in 59 of 75 plans that were not failures under both; they disagree in 16 (9 pass only under CaMeLoT, 7 only under CaMeL). Another 22 tasks fail under both because the plan misses the task (Table 3). The authors name run-time facts such as reader sets as the main cause of the disagreements.
- **Beyond CaMeL, Experiment 2 (§5.2).** In a simulated security-operations workflow with seven CTL rules, CaMeLoT rejected all seven hand-made unsafe variants of a fixed safe plan. A CaMeL-style baseline the authors wrote, which tracks taint only, rejected one, the taint case (Table 5). With plans written by Claude Haiku 4.5 from four prompts built to give a bad plan, CaMeLoT rejected all four and the baseline none (Table 6). The authors say the rules were chosen to exceed CaMeL, so they expect it to miss most.
- **Properties from the user's prompt, Experiment 3 (§5.3).** A model proposes "typed obligations" from a fixed set of ten forms (Table 7); trusted code checks tool names and atoms and compiles them to CTL, so the model never writes CTL. On the 97 AgentDojo tasks, the exact set of state-changing tools was recovered in 85 (87.6 per cent), a set that also credits correct conditional steps in 88 (90.7 per cent); every proposal was in the vocabulary and survived grounding (Table 9). When four models were asked to write CTL directly, one (GPT-4.1 nano) produced a clean suite on only 12 of 97 tasks and even the best run had one invalid formula; the typed route gave 97 of 97 clean (Table 10); the direct runs ranged from 12 to 96 of 97, the margin over Haiku 4.5 being one task and over Sonnet 4.5 three (94 of 97). Our reading: since trusted code compiles the formulas, the comparison is close to by-construction, and the typed route was run with Haiku only. In 20 controlled cases, the extracted formulas rejected every violating plan, accepted every correct plan, and matched handwritten CTL (Table 11).
- **Cost claim.** Checking before running means no model or tool call is spent on a plan that fails (abstract, §6). The text gives no measured token or time figure; the paper's claim that checking is "significantly less expensive" than running a workflow is stated without a measurement (§6).

## How

The authors forked CaMeL's public code and kept its interpreter and run-time policies; accepted plans go to CaMeL unchanged (§4). Provenance is a ladder trusted < user < untrusted < qllm, a derived value takes the highest of its inputs, and any value whose provenance is untrusted, conditional or not decidable before execution counts as tainted (§3.2, §4). Policies are written as CTL with Sigma-style metadata, and a policy is selected when its tools or propositions appear "in the generated plan or in the corresponding domain configuration" (§4). Plan generation and prompt extraction use Claude Haiku 4.5 (§5.1 to §5.3); only the direct-CTL comparison in Table 10 also uses GPT-4.1 nano, GPT-4.1 mini and Sonnet 4.5. The authors say the plan-level experiments use fixed, hand-written plans to remove planner variability (§5.2, §5.3).

## Limits

The authors state the following.

- Run-time facts such as reader sets, computed capabilities and tool-specific trust stay with CaMeL. A plan accepted statically may still be rejected at run time (§4, §6).
- Over-tainting may block safe plans; because values and reader sets are not modelled, it may also block too little. The authors call this a trade-off and the cost "bounded" (§6).
- The model is deliberately coarse. It carries taint only, conditions are dropped, and tool calls are black boxes; they say some properties a finer model could check will be out of reach, and name pre- and post-conditions on tool calls as future work (§6).
- Loop abstraction may block safe plans but, in their words, keeps potential violations (§3.2).
- The comparison runs on the AgentDojo suites without prompt injections, with repair switched off except for unsupported operations (§5.1). Experiments 2 and 3 use fixed plans; the end-to-end part of Experiment 2 has four tests (Table 6).
- The SOC workflow is simplified and built by the authors; they call for specialised SOC policy benchmarks (§5.2, §6).

A careful reader adds the following, as inference.

- No attack success rate is measured for CaMeLoT. The figures are about coverage, agreement with CaMeL and whether violating plans are caught; whether the layer changes what an adversary can do in AgentDojo is not tested, and no adaptive attacker appears.
- The seven SOC rules, the unsafe plans and the baseline are the authors', so "7 of 7 against 1 of 7" shows that CTL can state these rules. It does not show that CaMeL could not be extended to check them.
- A plan check does not see what the tools do. Whether a run follows its plan rests on CaMeL's interpreter; nothing in this paper proves that the finite-state model is a sound abstraction of that interpreter, or that nuXmv or the plan-to-model translation is free of errors.
- §3.2 states only that trusted values map to trusted and `untrusted` or `qllm` values to tainted. §4 says values from the user are trusted (CaMeL's Sources), and Listing 3 uses `is_trusted`; how `user` provenance maps to the propositions is left open.
- One model family (Claude Haiku 4.5) generated all plans and extractions; the direct-CTL comparison uses four models, but the typed pipeline is shown with Haiku only (Table 10).
- The paper is a preprint.

## Against the wiki

- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md): **extends**. The wiki lists CaMeL as the main defence around the model. This source adds a pre-execution layer on the plan, with CaMeL's run-time checks kept behind it. It reports no attack-success numbers, so it adds nothing to the state of evidence there. The state-passing attack of [MOSAIC](https://silentzero.ooo/wiki/sources/2026-wu-mosaic-knowledge-guided.html.md) hides in benign steps a plan check sees only as tool calls; our reading is that this layer would not address it, since tool calls are black boxes here.
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md): **extends**. The taint is a static, conservative copy of CaMeL's provenance (the lattice in §3.2); reader sets (§3, §4, §5.1), and so confidentiality, are not handled directly.
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): **extends**; nothing contradicted. The wiki asks who writes CaMeL's policies and from what. Here the security rules are written by hand in CTL, and rules that follow from the user's request are derived by a model that can only fill typed forms, with trusted code checking them. The broker page's concern about harmful sequences of individually allowed steps is the kind of rule CTL can state, but, our reading, only over the plan and not over the state tools share.
- [Can CaMeLs Talk?](https://silentzero.ooo/wiki/sources/2026-peters-gill-can-camels.html.md): related. It shows CaMeL's plan integrity can break when agents call agents; this source works inside single-agent CaMeL and does not mention that case.
- [ToolFence](https://silentzero.ooo/wiki/sources/2026-li-toolfence-fine-grained.html.md): related. Both build a check from the user's request before tools run. ToolFence compiles an authorisation blueprint and monitors calls; CaMeLoT checks the whole plan's order and obligations.
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md): loosely related; **no change**. This is model checking of a small abstraction. Nothing is proved of the system itself. It gives one more data point on model-written specifications: typed forms checked by trusted code beat free generation of formulas in the authors' test (Table 10); compare the specification step in [OSVBench](https://silentzero.ooo/wiki/sources/2025-li-osvbench-benchmarking-llms.html.md), a different task.

## For Silent Zero

[The broker](https://silentzero.ooo/wiki/design/broker.html.md): no change of state. Our reading: the source is evidence that a broker could check, before granting authority, that a plan contains an approval step before a strong action, and could send the failing trace back for repair. The checks that matter most to the broker (who may read what, which tool does what) stay at run time in this design, and the verifier and the plan-to-model translation would be part of what must be trusted. Nothing in Silent Zero is built.

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md)
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md)
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [Can CaMeLs Talk?](https://silentzero.ooo/wiki/sources/2026-peters-gill-can-camels.html.md)
- [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)
- [MOSAIC](https://silentzero.ooo/wiki/sources/2026-wu-mosaic-knowledge-guided.html.md)
- [OSVBench](https://silentzero.ooo/wiki/sources/2025-li-osvbench-benchmarking-llms.html.md)
- [ToolFence](https://silentzero.ooo/wiki/sources/2026-li-toolfence-fine-grained.html.md)
