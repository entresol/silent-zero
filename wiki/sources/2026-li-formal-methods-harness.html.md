# Formal methods as the harness for AIOS (SpecOS)

> SpecOS: relational state, lambdas, intents held back until a two-phase check passes. design, full text.

Source · Li et al. 2026 · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/2026-li-formal-methods-harness.html

Mingyu Li, Zhanbo Wang and Yiping Weng (Institute of Software, Chinese Academy of Sciences). "Formal Methods as the Harness for AIOS", AgenticOS workshop at SOSP 2026, September 2026, paper of three pages, a design sketch. [PDF](https://os-for-agent.github.io/papers/AgenticOS_SOSP_2026_paper_3.pdf). Read in full.

## What it shows

- **The problem it names.** AI-generated operating systems "outpace human review"; existing verified kernels (seL4, CertiKOS, Hyperkernel) "are tailored for static, human-curated codebases". SpecOS is meant to verify AI-generated components "continuously", before they run.
- **Three primitives.** System state as relational tables, so that invariants are decidable constraints over finite relations and updates are transactions (ACID). Logic as pure, memory-safe functional lambdas with a declared effect signature, whose output is a closed type of "Intent" rather than raw commands; intents are buffered and only then "materialize" them "into the physical world" after the whole graph of lambdas passes global verification and the transaction commits. Two-phase verification: bounded model checking of each lambda for a behavioural summary (effects, output types, resource bounds), then a check of the composed graph against "expert-curated" invariants in a decidable language such as Datalog, which the authors say takes polynomial time.
- **Layers by frequency.** Control loops at 100 Hz and above use static topologies verified offline; planning and AI-generated tasks at 3 to 10 Hz are verified at run time before their intents are carried out.
- **Under it.** A formally verified microkernel, "e.g., seL4 or HongMeng", isolates unverified drivers; the two-phase verification is aimed only at the fast-changing, AI-generated parts.
- **A case.** Replacing the ROS 2 control plane for robots; a table lists qualitative differences (centralised state against distributed local state, atomic rollback, intent buffering, pre-deployment verification).

## How

A design sketch. The paper reports no implementation, no measurement and no proof; its claim that continuous verification can be embedded "without sacrificing real-time performance" comes without numbers.

## Limits

The authors note that semantic verification of general code is undecidable, and the design rests on lambdas that are loop-bounded and confined to finite relational domains. The root of trust is the expert-written invariants. No implementation is reported.

## Against the wiki

- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md): **extends** ([SpecOS](https://silentzero.ooo/wiki/systems/specos.html.md)).
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): **extends** with a design that holds AI-generated actions back until a check passes and separates fast loops from slow planning.
- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): **extends** with a proposed split of control at 100 Hz and above from planning at 3 to 10 Hz.

## For Silent Zero

Our reading: the one design on paper that touches all three parts Silent Zero has, a verified kernel, a gate on what the AI side may do and a control loop apart from planning. It differs in what it verifies: generated code and its composition, where Silent Zero's broker grants authority and its safety loop is a small fixed function. It has no implementation to compare. The paper does not name it. See [SpecOS](https://silentzero.ooo/wiki/systems/specos.html.md).

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [SpecOS](https://silentzero.ooo/wiki/systems/specos.html.md)
