# The broker

> The only component that hands out authority: capability patterns, CaMeL and FIDES, why model-based defences fail; nothing proven yet.

Design · LLM reviewed · updated 2026-11-05 · 15 sources · https://silentzero.ooo/wiki/design/broker.html

The only component in Silent Zero that hands out authority. It grants capabilities that are attenuated, time-limited and revocable, and it words every request a human sees, so the agent never does. It runs isolated and still belongs to the trusted base, because its decisions are the guarantee. It will be *tested* first, with *proven* as the target (paper, Section 3).

## What it must do

- Bind each permitted action to recipients, data and parameters, enforce that at every tool call, and define revocation for actions under way (paper, Section 5).
- Word approval requests in a form the agent cannot imitate (paper, Section 5).
- Our reading: grant the least authority that serves a person's intent, and never decide on the strength of a model's judgement of untrusted text.

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| Passing names lets a deputy misuse another's authority; passing capabilities prevents it | established since 1988 | argument from practice | [The Confused Deputy](https://silentzero.ooo/wiki/sources/1988-hardy-confused-deputy-or.html.md) |
| Attenuation and revocation built from small forwarding programs (caretaker, membrane) | established patterns | design, informal argument | [Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md) |
| Kernel-level authority confinement and integrity | proven for seL4's verified configurations without MCS; not stated for MCS, which Microkit always uses | proof | [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md), [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md), [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md) |
| Heuristic and model-based defences fail against adaptive attackers | 12 of 12 broken fully or substantially, most above 90 % | test | [The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md) |
| Capability and policy checks around the model stop known injection attacks | 0 successful attacks within the threat model on AgentDojo; 77 % utility vs 84 % | guarantee by construction under an unverified interpreter; tested with static attacks only | [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md) |
| A passive server runs on its caller's budget | in seL4 MCS and Microkit | design; MCS functional-correctness proof on RISC-V | [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md), [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md), [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md) |
| Information-flow labels keep untrusted data from choosing consequential tool calls (FIDES) | no AgentDojo attack counted against its policies succeeded; explicit flows only | noninterference for integrity stated as a proposition without proof; unverified planner; static attacks | [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md) |
| A proven broker | none in the sources | none | — |

## The paper and its sources

- Section 2.4 cites [The Confused Deputy](https://silentzero.ooo/wiki/sources/1988-hardy-confused-deputy-or.html.md) for the confused deputy, [The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md) for the twelve broken defences and [Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md) for passing authority as capabilities. All three confirmed; Nasr et al. say the defences were broken "either fully or substantially". The step from confused deputy to prompt injection is the paper's own analogy; [Indirect prompt injection](https://silentzero.ooo/wiki/sources/2023-greshake-not-what-you.html.md), cited for the phenomenon, confirms the phenomenon and does not use the term. Section 6 limits the analogy: capabilities bound how far a deceived agent reaches.
- Table 1 cites [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md): "77 % of tasks with provable security versus 84 % undefended". The figure is confirmed. Our reading: "provable" in CaMeL means a formally stated property that holds by construction under a correct interpreter and correct policies; nothing is formally proven, so "secure by design" would be the accurate wording. The same row names FIDES ([Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md)), which enforces information flow rather than capabilities; the figures in the row are CaMeL's.
- Section 6 cites [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md) for adding information-flow control to capabilities. Confirmed for what information-flow control does; the pairing with capabilities is the paper's step. FIDES leaves implicit flows open, which fits the paper's point that data leaks through allowed channels. See [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md).

## Related

- [KataOS](https://silentzero.ooo/wiki/systems/kataos.html.md) put seL4 under machine-learning devices in 2022, with a dynamic root server rather than a static system ([Announcing KataOS and Sparrow](https://silentzero.ooo/wiki/sources/2022-google-announcing-kataos-sparrow.html.md)).
- [Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md) is a neighbouring design on seL4: models and agents stay on the host, and target-side role, ticket, lifecycle and bounds checks decide what is accepted ([Cohesix, a research operating system for edge AI](https://silentzero.ooo/wiki/sources/2026-bower-cohesix-research-operating.html.md), landing page only).

- [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md) is a design for the same job on a conventional host kernel: an external monitor outside the model, delegation that can only narrow a child's capabilities, and information-flow labels on memory. Its model-based classifier and eBPF enforcement rest on the host operating system, which the authors assume enforces them correctly, and they defer proofs of their invariants (design paper, partly read). Our reading: the host is not a verified kernel.
- [MCP-38](https://silentzero.ooo/wiki/sources/2026-shen-mcp-38-comprehensive.html.md) catalogues 38 threats to systems built on the Model Context Protocol, many of them ways in which text persuades a model, the rest classical flaws. Our reading: for the first kind the broker need not recognise the text, since it grants only declared authority, which limits reach but not leakage through allowed channels; the paper offers no evidence on that and the broker is not built.

## Open

- The integrity proof the broker relies on is not stated for MCS, and Microkit always uses MCS. Until it is, the kernel's guarantee under the broker is functional correctness only. See [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md).
- CaMeL's policies are defined by its engine; users, tool providers or automatic derivation are envisaged later ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), §5.2, §10). For Silent Zero: who writes them, and from what?
- Blocked calls go to a person, and too many approvals breed fatigue ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), §9.2). In CaMeL's STRICT mode policies fired in about half the tasks run without attack, with wide differences between task suites (Appendix D). The paper adds that requests must be worded so the agent cannot imitate them, which needs a trusted path to a screen.
- When a task is to act on instructions found in data, isolating the planner alone cannot help; policies and capabilities must carry the load ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), §6.4).
- Sequences of individually allowed calls may add up to a harmful one, as return-oriented programming chains allowed code fragments ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), §9.3).
- CaMeL leaks through loops and exceptions unless restricted, with a residual exception path; its authors do not exclude timing channels ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), §7). In Silent Zero the same holds one level down; see [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md).
- Revoking authority over a lost connection fails unsafe; a grant should lapse by itself when the broker cannot reach it ([Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md), §11.5.3).
- In Microkit a called server must finish in bounded time, unenforced ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)); the broker has to meet that.

## Sources

- [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md)
- [Announcing KataOS and Sparrow](https://silentzero.ooo/wiki/sources/2022-google-announcing-kataos-sparrow.html.md)
- [Cohesix, a research operating system for edge AI](https://silentzero.ooo/wiki/sources/2026-bower-cohesix-research-operating.html.md)
- [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)
- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)
- [Indirect prompt injection](https://silentzero.ooo/wiki/sources/2023-greshake-not-what-you.html.md)
- [MCP-38](https://silentzero.ooo/wiki/sources/2026-shen-mcp-38-comprehensive.html.md)
- [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)
- [Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md)
- [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md)
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md)
- [The Confused Deputy](https://silentzero.ooo/wiki/sources/1988-hardy-confused-deputy-or.html.md)

## Related pages

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [Confused deputy](https://silentzero.ooo/wiki/concepts/confused-deputy.html.md)
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md)
- [Memory-safe code](https://silentzero.ooo/wiki/concepts/memory-safe-code.html.md)
- [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md)
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md)
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md)
- [Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md)
- [KataOS](https://silentzero.ooo/wiki/systems/kataos.html.md)
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md)
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md)
- [LeftoverLocals](https://silentzero.ooo/wiki/sources/2024-trail-leftoverlocals-listening-llm.html.md)
- [Linux kernel documentation: Landlock](https://silentzero.ooo/wiki/sources/nd-linux-landlock-unprivileged-access.html.md)
