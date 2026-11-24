# ToolFence

> ToolFence: a typed authorization blueprint from the user’s request, a deterministic monitor and a model judge for gaps; 0.20 % attack success on AgentDojo with Qwen3-max; preprint. measurement, partly read.

Source · Li et al. 2026 · LLM reviewed · updated 2026-11-19 · https://silentzero.ooo/wiki/sources/2026-li-toolfence-fine-grained.html

Yanjie Li, Xiangyu He, Xuelong Dai and Bin Xiao (Hong Kong Polytechnic University, Shandong University). "ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents", arXiv 2609.37196, 29 September 2026. A preprint. [arXiv](https://arxiv.org/abs/2609.37196). Read: the abstract, the design (§3), the experiments (§4) and the conclusion. The appendices (algorithm, baseline setup, prompts) were not read.

## What it shows

- **The idea.** The authors treat prompt injection as privilege escalation. Before the agent reads any external content, a separate model call turns the user's request into a typed authorization blueprint. For each tool it fixes the effect and, for each sensitive argument, where the value must come from: the request itself, the output of a named earlier tool, or an authenticated template. Only arguments that carry no authority are left to the agent (§3.2). A deterministic monitor, with no model call, checks every proposed call against the blueprint (§3.1 to §3.3).
- **A judge for the gaps.** When a call misses the blueprint, the controller builds a candidate capability and refuses it at once if a sensitive argument cannot be traced to the user or a declared source. Otherwise a model judge sees the capability's shape, without the argument values, and may grant it. A granted shape extends the running blueprint and is cached across sessions. If the judge refuses, the call falls back to one per-call judge verdict on the concrete call (§3.4, §3.5).
- **Results on AgentDojo.** Over 609 user-attack pairs from four suites and six attack strategies (AgentDojo has 629; the authors leave out 20 ambiguous pairs, §4.1), ToolFence reached an overall attack success rate of 0.20 per cent with Qwen3-max, against 0.42 per cent for CaMeL and 21.20 per cent with no defence, and 0.90 per cent with GPT-4o, against 1.28 per cent for CaMeL and 38.01 per cent with no defence (Table 1; intervals appear only in Figure 2). Clean utility was 38.90 per cent with Qwen3-max (no defence 42.70) and 82.70 with GPT-4o (no defence 84.20); CaMeL's was 32.67 and 70.50.
- **Within-tool attacks.** A tool filter alone left 9.18 per cent of within-tool attacks through on Qwen3-max, where an attack reuses an allowed tool with bad arguments. ToolFence left 0.80 per cent (Table 1, §4.2).
- **Ablation.** Blueprint and monitor alone gave 0.45 per cent attack success and 25.60 per cent utility under attack. The runtime grant raised utility to 30.40 per cent and, with caching and read auto-allow, to 32.45 per cent, at 0.20 per cent. A per-call judge instead of the blueprint gave 4.35 per cent (Table 2).
- **Cost.** The full system ran at 1.90 times the undefended runtime in the ablation, and judge calls fell by about 43 per cent with caching (Table 2, §4.3). In the timing comparison, on 50 clean tasks and 200 attacked pairs, the full system took 1.63 times as long as the undefended agent on Qwen3-max and 3.79 times on GPT-4o; CaMeL took about 11 to 13 times (§4.5, Figure 4).

## How

The evaluation uses AgentDojo's Workspace, Slack, Travel and Banking suites with Qwen3-max and GPT-4o (a third model, Mistral-small, is in an appendix table not read). Baselines are prompt-level and filtering defences, a tool filter, SecInfer and CaMeL, each with the original settings where available. Runs use fixed seeds and report means with 95 per cent bootstrap intervals (§4.1; Figure 2 states five seeds).

## Limits

The authors name three. Provenance constraints do not stop every manipulation inside an authorized path; in one Travel case the injection steered which of several authorized candidates the model chose (§4.4). A legitimate value found only in untrusted content, such as a URL in a file, is not allowed automatically, which costs utility, and handling such values permissively enlarges the attack surface; the authors suggest asking a person to confirm new sensitive targets (§4.4). A careful reader adds the following. The attacks are AgentDojo's fixed set, not adaptive attacks on this design, and the authors do not claim a formal guarantee. A model call writes the blueprint and a model judge decides grants, so the guarantee depends on those calls where the paper's own broker is meant to decide without a model. The baselines are the authors' runs, and the utility figures are low for Qwen3-max in every row, and the paper is a preprint.

## Against the wiki

- [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md): **extends** the comparison. On the authors' runs CaMeL had the lowest attack success among the baselines and the largest cost; ToolFence's attack success was lower on both models and its cost lower. Our reading: the authors make no claim of a guarantee by construction, which is what the wiki's CaMeL page records for CaMeL.
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): **extends** the open question on who writes the policies. Here a model compiles them from the user's request, and the grant path includes a model.
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md): **extends** the state of the defences around the model with a design that controls arguments as well as tools.
- [Causality laundering](https://silentzero.ooo/wiki/sources/2026-chinaei-causality-laundering-denial.html.md): related. The ToolFence design requires that an unauthorized call end in an explicit, recoverable denial with a diagnostic message (§3.1); that is the channel the other source describes. Our reading: the parts read do not test it; the appendices were not read.

## For Silent Zero

[The broker](https://silentzero.ooo/wiki/design/broker.html.md): no change of state. Our reading: fixing where each sensitive argument may come from fits the paper's wording that the broker binds an action to recipients, data and parameters (Section 5). The result suggests that binding to provenance can cut hijacked arguments at a moderate cost (1.63 to 3.79 times the runtime, §4.5). In ToolFence, a model builds and extends the authority, so it is a different design from a broker whose decisions are the guarantee (Section 3), and nothing in Silent Zero is built.

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md)
- [agent capabilities should follow task intent (IntentCap)](https://silentzero.ooo/wiki/sources/2026-zheng-llm-agent-capabilities.html.md)
- [CaMeLoT, a static check of an agent's plan on top of CaMeL](https://silentzero.ooo/wiki/sources/2026-nikolaou-camelot-camel-orchestrated.html.md)
- [Causality laundering](https://silentzero.ooo/wiki/sources/2026-chinaei-causality-laundering-denial.html.md)
- [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)
- [PACE, provenance-aware capability enforcement](https://silentzero.ooo/wiki/sources/2026-li-pace-provenance-aware.html.md)
