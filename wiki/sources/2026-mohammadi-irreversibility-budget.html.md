# the irreversibility budget

> A cumulative account of irreversible exposure, charged below the agents; fleets overdraw by up to 48 times without it. design, partly read.

Source · Mohammadi and Bindschaedler 2026 · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/2026-mohammadi-irreversibility-budget.html

Bardia Mohammadi and Laurent Bindschaedler (Max Planck Institute for Software Systems). "The Irreversibility Budget: Fleet-Level Risk Accounting and Admission Control for Agent Operating Systems", AgenticOS workshop at SOSP 2026, September 2026. [PDF](https://os-for-agent.github.io/papers/AgenticOS_SOSP_2026_paper_30.pdf). Read in part: abstract, introduction, background, resource model and the first part of the runtime; the evaluation only through its summary in the introduction.

## What it shows

- **The problem.** Controls check one effect at a time, so "a fleet of individually authorized agents can overdraw its principal's risk under a shared trigger while every local gate stays correct". The example is fifty procurement agents that each stay under their own cap and together commit a position nobody approved.
- **The proposal.** An "irreversibility budget": a cumulative account of residual value at risk that a trusted runtime keeps for each principal (an agent, a workflow, a tenant). The runtime charges each effect "the loss expected to survive recovery", below the agent, and denies the next effect when the balance would exceed the budget. Charges come from tool specifications and a trusted pricing service, "never from the model"; an effect the registry cannot identify is charged at the most expensive matching class. Reserve, confirm and cancel calls on ledgers up the path from agent to workflow to tenant keep a fleet from double-spending; a rising "risk pressure" tightens admission and escalates to a rate-limited authority.
- **Evidence.** A controlled simulation of the procurement fleet, a study of public agent traces and a ledger microbenchmark. Per-effect gates let the fleet overdraw its risk limit by 2.4 times on average and by up to 48 times at a thousand agents; the budget "holds every correctly charged run within that limit". "The ledger itself is cheap."

## How

A design with a simulation. The charges, correlations and the fleet are the authors' model.

## Limits

The authors name pricing as the weak point: when effect types are misdeclared, or a shared trigger correlates losses that the charges assumed independent, "realized loss can still exceed what the ledger accounted for". The trusted base is "wider than the ledger": the registry and its auditors, the tool wrappers, the pricing service and principal attribution. "Conservative, dependency-aware pricing remains the central open problem." Parts of the paper, among them the evaluation details, were not read.

## Against the wiki

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): **extends** with a limit on cumulative exposure across agents, which the paper's broker, as the paper describes it, does not have.
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md): **extends** ([Towards an Agent Operating System](https://silentzero.ooo/wiki/sources/2026-steinder-towards-agent-operating.html.md) likewise proposes classes of reversible, compensable and irreversible actions).

## For Silent Zero

Our reading: the paper's Section 5 binds each permitted action to recipients, data and parameters and defines revocation; it does not account for the sum of what many agents are allowed to do. For a robot the exposure is not money, and the paper's answer to harm in the physical world is the safety loop; the charge as a vector, which the authors mention, would have to cover it. The paper does not name this work. See [The broker](https://silentzero.ooo/wiki/design/broker.html.md).

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [Towards an Agent Operating System](https://silentzero.ooo/wiki/sources/2026-steinder-towards-agent-operating.html.md)
