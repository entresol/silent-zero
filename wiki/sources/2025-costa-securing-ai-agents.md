---
type: source
id: 2025-costa-securing-ai-agents
status: reviewed
read: full
kind: test
sources: [2025-costa-securing-ai-agents]
updated: 2026-10-31
---

# Costa et al. 2025: Securing AI agents with information-flow control

Manuel Costa, Boris Köpf, Aashish Kolluri, Andrew Paverd, Mark Russinovich, Ahmed Salem, Shruti Tople, Lukas Wutschitz and Santiago Zanella-Béguelin (Microsoft). [arXiv:2505.23643](https://arxiv.org/abs/2505.23643), version 2 of 3 September 2025. Read in full, appendices skimmed.

## What it shows

- **A formal model of planners.** The planner is the part of an agent that orchestrates calls to the model and to tools. The authors model it, attach confidentiality and integrity labels to all data, and characterise what dynamic taint tracking can enforce (§1, §3–§5).
- **Two policies with stated guarantees.** One keeps the decision to take a consequential action from being influenced by untrusted data: noninterference for integrity, stated as a proposition whose formalisation the authors forgo as "straightforward" (§4.4). Arguments of an allowed call may still come from untrusted data (§5.1). The other keeps the agent from creating illicit information flows, but only for explicit flows. The authors call this "explicit secrecy" and a "pragmatic compromise": confidential data may still influence control flow, and implicit flows are not prevented (§1, §4).
- **FIDES**, a planner that tracks labels, enforces the policies deterministically before tool calls, and adds two primitives: tool results are hidden in variables when they would taint the context, and a quarantined model can inspect such a variable with constrained decoding and return a typed value (§1, §5).
- **A taxonomy of tasks** that shows which tasks each planner design can complete securely (§6).
- **Results on AgentDojo** (§8): of 949 attacks, with gpt-4o, the basic planner without policy checks let 163 succeed; FIDES with policy checks, 1, and none once two injection tasks the authors do not count as attacks on their policies are left out (Table 1). With reasoning models (o1, o3, o4-mini), FIDES completes on average about 16 per cent more tasks than a basic planner under the same policies, about 24 per cent with a tuned prompt (§1, §8.2). The introduction says that without policy checks all planners fall to practical prompt injections (§1); in Table 1, though, the strict Variable Passing planner lets no counted attack through even without them, which §8.1 acknowledges.

## How

The planners run on AgentDojo with five models, OpenAI's and grok-3, using generic per-tool policies rather than policies fitted to the benchmark; §7.1 speaks of two policies, §8.1 of three (§7, §8.1). Which data fields count as untrusted was taken from the benchmark: every field that at least one AgentDojo injection targets (§7.1). Task completion is measured without attacks; attacks are AgentDojo's own, not adapted to FIDES.

## Limits

What the authors say themselves: only explicit flows are controlled; policies are enforced at tool calls, so text-to-text attacks that only change the answer shown to the user get through (§8.1); FIDES "is still far from achieving ideal utility" on the data-independent task classes DI and DIQ, because the model misuses the inspection primitive or falls back to expanding variables (§8.2). The agent's configuration, system message, tool descriptions and models are trusted (§2).

A careful reader adds:

- **No adaptive attacker.** The attacks are AgentDojo's; nothing was designed against FIDES. Within its policies the guarantee holds by construction, as the authors argue it, so adaptivity matters less for integrity than for utility.
- **The planner is trusted code.** The guarantees assume that FIDES's label tracking and policy engine are implemented correctly, and that tool wrappers label their outputs correctly (§4.1); no proof of the implementation is reported.
- **The zero comes from the policies.** With policy checks, the basic and Variable Passing planners also reach zero counted attacks (Table 1); what FIDES adds is completed tasks.
- **Percentages of what.** Finding 4 calls a related 8.2 per cent "absolute utility"; whether the 16 and 24 per cent are percentage points or relative gains, the text does not say.

## Against the wiki

- [[prompt-injection]]: extends it with a second defence around the model, alongside CaMeL, and with a formal account of what it guarantees.
- [[information-flow-control]]: created with this source.
- [[broker]]: our reading: a candidate mechanism for the broker's checks at tool calls.
- [[object-capabilities]]: our reading: FIDES's labels, like CaMeL's, track information flow and convey no authority.

## For zOS

The paper cites this source twice. Table 1 (Section 5) lists "CaMeL, FIDES" under agent authority as "Capability and information-flow enforcement for agents"; FIDES is information-flow enforcement, and the figure in that row (77 versus 84 per cent) is CaMeL's, not this paper's. Section 6 says capability systems for agents "add information-flow control, which tracks where data comes from and where it may go". Confirmed for what information-flow control does for agents; pairing it with capabilities is the paper's step, as this source discusses no capability system. Our reading: FIDES controls explicit flows only, in line with the paper's preceding sentence that data can leak through channels an agent is allowed to use. No `design/` page changes state.
