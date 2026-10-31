---
type: design
status: reviewed
sources: [1988-hardy-confused-deputy-or, 2006-miller-robust-composition-towards, 2025-debenedetti-defeating-prompt-injections, 2026-nasr-attacker-moves-second, 2018-klein-formally-verified-software, nd-sel4-verified-configurations, 2026-sel4-functional-correctness-proof, nd-sel4-microkit-user-manual, 2026-heiser-mcs-safety-os, 2026-bower-cohesix-research-operating]
updated: 2026-10-31
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
| A proven broker | none in the sources | none | — |

## The paper and its sources

- Section 2.4 cites [[1988-hardy-confused-deputy-or]] for the confused deputy, [[2026-nasr-attacker-moves-second]] for the twelve broken defences and [[2006-miller-robust-composition-towards]] for passing authority as capabilities. All three confirmed; Nasr et al. say the defences were broken "either fully or substantially". The step from confused deputy to prompt injection is the paper's own analogy; Greshake et al. 2023, not yet covered here, is cited for the phenomenon. Section 6 limits the analogy: capabilities bound how far a deceived agent reaches.
- Table 1 cites [[2025-debenedetti-defeating-prompt-injections]]: "77 % of tasks with provable security versus 84 % undefended". The figure is confirmed. Our reading: "provable" in CaMeL means a formally stated property that holds by construction under a correct interpreter and correct policies; nothing is formally proven, so "secure by design" would be the accurate wording.

## Related

- [[cohesix]] is a neighbouring design on seL4: models and agents stay on the host, and target-side role, ticket, lifecycle and bounds checks decide what is accepted ([[2026-bower-cohesix-research-operating]], landing page only).

## Open

- The integrity proof the broker relies on is not stated for MCS, and Microkit always uses MCS. Until it is, the kernel's guarantee under the broker is functional correctness only. See [[kernel]].
- CaMeL's policies are defined by its engine; users, tool providers or automatic derivation are envisaged later ([[2025-debenedetti-defeating-prompt-injections]], §5.2, §10). For zOS: who writes them, and from what?
- Blocked calls go to a person, and too many approvals breed fatigue ([[2025-debenedetti-defeating-prompt-injections]], §9.2). In CaMeL's STRICT mode policies fired in about half the tasks run without attack, with wide differences between task suites (Appendix D). The paper adds that requests must be worded so the agent cannot imitate them, which needs a trusted path to a screen.
- When a task is to act on instructions found in data, isolating the planner alone cannot help; policies and capabilities must carry the load ([[2025-debenedetti-defeating-prompt-injections]], §6.4).
- Sequences of individually allowed calls may add up to a harmful one, as return-oriented programming chains allowed code fragments ([[2025-debenedetti-defeating-prompt-injections]], §9.3).
- CaMeL leaks through loops and exceptions unless restricted, with a residual exception path; its authors do not exclude timing channels ([[2025-debenedetti-defeating-prompt-injections]], §7). In zOS the same holds one level down; see [[time-protection]].
- Revoking authority over a lost connection fails unsafe; a grant should lapse by itself when the broker cannot reach it ([[2006-miller-robust-composition-towards]], §11.5.3).
- In Microkit a called server must finish in bounded time, unenforced ([[nd-sel4-microkit-user-manual]]); the broker has to meet that.
