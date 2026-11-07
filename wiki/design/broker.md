---
type: design
status: reviewed
sources: [1988-hardy-confused-deputy-or, 2006-miller-robust-composition-towards, 2025-debenedetti-defeating-prompt-injections, 2026-nasr-attacker-moves-second, 2018-klein-formally-verified-software, nd-sel4-verified-configurations, 2026-sel4-functional-correctness-proof, nd-sel4-microkit-user-manual, 2026-heiser-mcs-safety-os, 2026-bower-cohesix-research-operating, 2025-costa-securing-ai-agents, 2023-greshake-not-what-you, 2022-google-announcing-kataos-sparrow, 2026-zou-agentkernel-trust-native, 2026-shen-mcp-38-comprehensive, 2026-sharma-agent-operating-systems, 2026-wu-mosaic-knowledge-guided]
updated: 2026-11-07
---

# The broker

The only component in zOS that hands out authority. It grants capabilities that are attenuated, time-limited and revocable, and it words every request a human sees, so the agent never does. It runs isolated and still belongs to the trusted base, because its decisions are the guarantee. It will be *tested* first, with *proven* as the target (paper, Section 3).

## What it must do

- Bind each permitted action to recipients, data and parameters, enforce that at every tool call, and define revocation for actions under way (paper, Section 5).
- Word approval requests in a form the agent cannot imitate (paper, Section 5).
- Our reading: grant the least authority that serves a person's intent, and never decide on the strength of a model's judgement of untrusted text.

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| Passing names lets a deputy misuse another's authority; passing capabilities prevents it | established since 1988 | argument from practice | [[1988-hardy-confused-deputy-or]] |
| Attenuation and revocation built from small forwarding programs (caretaker, membrane) | established patterns | design, informal argument | [[2006-miller-robust-composition-towards]] |
| Kernel-level authority confinement and integrity | proven for seL4's verified configurations without MCS; not stated for MCS, which Microkit always uses | proof | [[2018-klein-formally-verified-software]], [[nd-sel4-verified-configurations]], [[nd-sel4-microkit-user-manual]] |
| Heuristic and model-based defences fail against adaptive attackers | 12 of 12 broken fully or substantially, most above 90 % | test | [[2026-nasr-attacker-moves-second]] |
| Capability and policy checks around the model stop known injection attacks | 0 successful attacks within the threat model on AgentDojo; 77 % utility vs 84 % | guarantee by construction under an unverified interpreter; tested with static attacks only | [[2025-debenedetti-defeating-prompt-injections]] |
| A passive server runs on its caller's budget | in seL4 MCS and Microkit | design; MCS functional-correctness proof on RISC-V | [[2026-heiser-mcs-safety-os]], [[nd-sel4-microkit-user-manual]], [[2026-sel4-functional-correctness-proof]] |
| Information-flow labels keep untrusted data from choosing consequential tool calls (FIDES) | no AgentDojo attack counted against its policies succeeded; explicit flows only | noninterference for integrity stated as a proposition without proof; unverified planner; static attacks | [[2025-costa-securing-ai-agents]] |
| Defences over tool calls (Progent, CaMeL) stop attacks made of composed benign commands that share OS state | no: both left the success rate at 96.63 % in the authors' setup on Claude Code | test; one agent (Claude Code), authors' own policies, CaMeL as an adapted trace monitor, 101 constructed exploit paths, preprint | [[2026-wu-mosaic-knowledge-guided]] |
| A proven broker | none in the sources | none | — |

## The paper and its sources

- Section 2.4 cites [[1988-hardy-confused-deputy-or]] for the confused deputy, [[2026-nasr-attacker-moves-second]] for the twelve broken defences and [[2006-miller-robust-composition-towards]] for passing authority as capabilities. All three confirmed; Nasr et al. say the defences were broken "either fully or substantially". The step from confused deputy to prompt injection is the paper's own analogy; [[2023-greshake-not-what-you]], cited for the phenomenon, confirms the phenomenon and does not use the term. Section 6 limits the analogy: capabilities bound how far a deceived agent reaches.
- Table 1 cites [[2025-debenedetti-defeating-prompt-injections]]: "77 % of tasks with provable security versus 84 % undefended". The figure is confirmed. Our reading: "provable" in CaMeL means a formally stated property that holds by construction under a correct interpreter and correct policies; nothing is formally proven, so "secure by design" would be the accurate wording. The same row names FIDES ([[2025-costa-securing-ai-agents]]), which enforces information flow rather than capabilities; the figures in the row are CaMeL's.
- Section 6 cites [[2025-costa-securing-ai-agents]] for adding information-flow control to capabilities. Confirmed for what information-flow control does; the pairing with capabilities is the paper's step. FIDES leaves implicit flows open, which fits the paper's point that data leaks through allowed channels. See [[information-flow-control]].

## Related

- [[kataos]] put seL4 under machine-learning devices in 2022, with a dynamic root server rather than a static system ([[2022-google-announcing-kataos-sparrow]]).
- [[cohesix]] is a neighbouring design on seL4: models and agents stay on the host, and target-side role, ticket, lifecycle and bounds checks decide what is accepted ([[2026-bower-cohesix-research-operating]], landing page only).

- [[2026-zou-agentkernel-trust-native]] is a design for the same job on a conventional host kernel: an external monitor outside the model, delegation that can only narrow a child's capabilities, and information-flow labels on memory. Its model-based classifier and eBPF enforcement rest on the host operating system, which the authors assume enforces them correctly, and they defer proofs of their invariants (design paper, partly read). Our reading: the host is not a verified kernel.
- [[2026-shen-mcp-38-comprehensive]] catalogues 38 threats to systems built on the Model Context Protocol, many of them ways in which text persuades a model, the rest classical flaws. Our reading: for the first kind the broker need not recognise the text, since it grants only declared authority, which limits reach but not leakage through allowed channels; the paper offers no evidence on that and the broker is not built.
- [[2026-sharma-agent-operating-systems]] proposes an agent operating system as a control plane over Linux or Windows: model output is a proposal, tool calls pass deny-by-default capability checks, and a registry admits tools found at run time. It is a design without implementation, measurements or proofs, and it names no real-time goal. It lists sequences of individually allowed actions as a gap: per-action enforcement is "necessary but not sufficient" and stateful evaluation may be needed (§8.2), which is the open question on sequences below.
- [[2026-wu-mosaic-knowledge-guided]] measures attacks that carry no explicit malicious instruction: benign command-line steps that pass state to each other through files, environment and hooks. Progent and CaMeL, run as hooks over an agent's tool calls, left their success rate unchanged at 96.63 per cent in the authors' setup on Claude Code. They explain it by the state passing between commands and not through tool-call arguments (CaMeL ran there as an adapted trace monitor). Our reading: a broker that checks tool calls cannot be the whole guarantee; what the agent's domain shares with other components must be bounded below it, by the capabilities it holds. See [[static-system]].

## Open

- The integrity proof the broker relies on is not stated for MCS, and Microkit always uses MCS. Until it is, the kernel's guarantee under the broker is functional correctness only. See [[kernel]].
- CaMeL's policies are defined by its engine; users, tool providers or automatic derivation are envisaged later ([[2025-debenedetti-defeating-prompt-injections]], §5.2, §10). For zOS: who writes them, and from what?
- Blocked calls go to a person, and too many approvals breed fatigue ([[2025-debenedetti-defeating-prompt-injections]], §9.2). In CaMeL's STRICT mode policies fired in about half the tasks run without attack, with wide differences between task suites (Appendix D). The paper adds that requests must be worded so the agent cannot imitate them, which needs a trusted path to a screen.
- When a task is to act on instructions found in data, isolating the planner alone cannot help; policies and capabilities must carry the load ([[2025-debenedetti-defeating-prompt-injections]], §6.4).
- Sequences of individually allowed calls may add up to a harmful one, as return-oriented programming chains allowed code fragments ([[2025-debenedetti-defeating-prompt-injections]], §9.3). A 2026 preprint reports such chains through shared system state succeeding against deployed coding agents in the authors' constructed attacks ([[2026-wu-mosaic-knowledge-guided]]); whether zOS leaves an agent any such state is open.
- CaMeL leaks through loops and exceptions unless restricted, with a residual exception path; its authors do not exclude timing channels ([[2025-debenedetti-defeating-prompt-injections]], §7). In zOS the same holds one level down; see [[time-protection]].
- Revoking authority over a lost connection fails unsafe; a grant should lapse by itself when the broker cannot reach it ([[2006-miller-robust-composition-towards]], §11.5.3).
- In Microkit a called server must finish in bounded time, unenforced ([[nd-sel4-microkit-user-manual]]); the broker has to meet that.
