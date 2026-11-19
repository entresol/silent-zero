# Causality laundering

> Causality laundering: a denied tool call leaks what exists; a monitor that records denials; three constructed scenarios, single author. design, partly read.

Source · Chinaei 2026 · LLM reviewed · updated 2026-11-19 · https://silentzero.ooo/wiki/sources/2026-chinaei-causality-laundering-denial.html

Mohammad Hossein Chinaei (independent researcher). "Causality Laundering: Denial-Feedback Leakage in Tool-Calling LLM Agents", arXiv 2604.04035, 5 April 2026. A single-author preprint. [arXiv](https://arxiv.org/abs/2604.04035). Read: the abstract, the introduction, the threat model (§2), the definition and first variants of the attack (§3.1 to §3.5), the related work, the limitations (§7.6), the discussion of the theorem's scope and the counterfactual rule (§9.1, §9.2). The layered design (§4 and §5) and the three scenarios of §7 were read in outline.

## What it shows

- **A leak through a refusal.** An enforcement layer that denies a tool call can still leak. The agent learns from the denial that a protected thing exists, that it is protected, or, if the denial carries a reason, what category it belongs to, and a later benign-looking call passes that on. The author calls this causality laundering. His example is a denied read of a sensitive file, followed by an email that says only that the file exists (§1, §3.1).
- **Why other defences miss it, by the author's account.** Flat taint tracking and dependency graphs over successful calls follow what flowed or succeeded, and a denial produced no data for them to follow. Counterfactual attribution defences re-run an agent with and without suspected inputs, and their targets are attacker content in tool results, not denials (§3.2). The author names FIDES and PCAS as the closest prior systems and says neither represents denied actions as events (§8).
- **A definition and variants.** Four conditions define the attack: a denied action, a later side effect, no successful data path between them, and a later action that would have differed without the denial (Definition 2, §3.3). The author describes it as a storage channel in Lampson's sense (§3.4). The paper names three variants: one probe that leaks one fact, many probes whose allow and deny results are put together, and a denied result encoded through an allowed intermediate tool before it is sent (§3.5).
- **The proposed monitor.** The Agentic Reference Monitor sits as a proxy on every tool call and result. It keeps a provenance graph that includes denied actions, links a denial to the next call by a counterfactual edge, and decides by deterministic rules over an integrity lattice of five trust levels, without asking a model. Its decisions go to a hash-chained audit log (§2.3, §2.4, §4).
- **Evidence.** In three constructed scenarios the graph-aware engine blocked the final action in each and a minimal flat-provenance baseline missed all three, with policy evaluation under 1 ms (median of 100 runs, §7). The prototype has 45 unit tests (§7).

## How

The monitor is described as an MCP proxy in front of one agent. The attacker controls only content the agent reads and cannot change the agent, the monitor or the system prompt; malicious users and multi-agent settings are out of scope (§2.2, §2.5). The security goals are stated as three properties, mediated integrity, a tamper-evident audit and defence in depth (§2.4).

## Limits

The author's own list (§7.6, §9.1) is long. The scenarios are hand-built and not a benchmark such as AgentDojo, and no model ran in the loop. The flat baseline is a minimal mechanism of the author's, not a reimplementation of FIDES or another full system. The theorem on mediated integrity holds only if every tool call goes through the proxy, which the author calls an operational assumption that code cannot guarantee, and it does not show completeness against all implicit-flow or denial-feedback attacks. The counterfactual rule links a denial to the next tool call, a deliberate over-approximation: it can flag a benign call that follows a denial and can miss delayed or multi-step chains, and no false-positive rate is reported (§3.7, §9.2, §7.6). It is sufficient for the probe-then-leak pattern and not necessary for every denial leak, and the field-level protection depends on trust overrides the integrator supplies. A careful reader adds that this is one preprint by one author, and that the claim that the channel exists rests on the argument and on one cited result that agents infer hidden monitoring from blocking feedback ([15] in the paper, not checked here).

## Against the wiki

- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md): **extends** it. The page lists defences around the model by what they block. This source names a channel through the defence's own answers.
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): **extends** the open questions. The page records what the broker must grant and how evidence stands, and says nothing about what the broker tells an agent when it refuses. Our reading: the denial is an output of the broker to the agent, so its content is part of what the broker discloses.
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md): **extends** it. The author says label tracking such as FIDES follows what flowed through successful calls and, in his reading, does not follow what an agent infers from a refusal; the author adds that ARM does not claim full non-interference for implicit flows such as timing channels, and says its counterfactual edges mitigate a class of inference-based attacks (§2.5).
- [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md): no contradiction. The CaMeL page does not discuss what a blocked call reveals, and the ARM author calls the two approaches complementary (§8).

## For Silent Zero

[The broker](https://silentzero.ooo/wiki/design/broker.html.md): no change of state. Our reading: the paper says the agent "never holds more authority than a person granted" (Abstract) and has the broker log every grant (Section 6), and it does not say what a refusal discloses. In a capability system an agent that holds no capability to an object has no name for it to probe, which would remove the file-exists example; that is our design intent, not a result of this source, and whether the broker's own replies to requests for authority carry the same leak is open. Nothing in Silent Zero is built.

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md)
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md)
- [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)
- [ToolFence](https://silentzero.ooo/wiki/sources/2026-li-toolfence-fine-grained.html.md)
