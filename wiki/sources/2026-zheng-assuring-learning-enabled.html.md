# a neuro-symbolic assurance agenda for learning-enabled CPS

> A research agenda for learning-enabled CPS: the learned side holds capability, a monitor and a safe controller hold authority; no results. position, full text.

Source · Zheng et al. 2026 · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/2026-zheng-assuring-learning-enabled.html

Xi Zheng, Ivan Ruchkin, Hong Jin Kang, Tevfik Bultan, Vijay Ganesh, Taylor T. Johnson, Ziyang Li, Lei Ma, Aloysius K. Mok, Daniel Neider, Ruzica Piskac, Nalini Venkatasubramanian, Simon Thompson and Sanjoy Baruah. "Assuring Learning-Enabled Cyber-Physical Systems with Foundation Models: A Neuro-Symbolic Agenda for Testing, Verification, and Runtime Assurance", arXiv 2610.39547v1 [cs.RO], 29 October 2026. A preprint, marked "manuscript submitted to ACM". [arXiv](https://arxiv.org/abs/2610.39547). The full text, 30 pages, was read; the reference list was read only for the works the text names.

## What it shows

The paper reports no experiment and no measurement. It is a research agenda, the authors cite Shonan seminar discussions (No. 235) as the origin of several of its points (§1, also §2.3, §3.3, §4.1, §4.3, §5, §6). Its claims are arguments.

- **The thesis.** Foundation models should not be the trusted core of a cyber-physical system (CPS). They are "constrained assistants" whose outputs are independently checked wherever correctness can be formally specified; trust comes from checkable evidence and not from a model's capability or confidence (abstract, §1, §7).
- **The stack.** A "Foundation Model Assurance Stack" (Figure 1) of three pillars, joined by shared artefacts (symbolic world models, domain-specific languages, assume–guarantee contracts, neural–symbolic interfaces): foundation models as assistive components (§2), conformance-based testing (§3) and verification (§4). A runtime assurance layer built on the Simplex architecture sits beneath them and puts their outputs to work during operation (§5).
- **Verify what is tractable.** Verification should aim at symbolic world models, interface guardrails, contracts, representation transformations and generated artefacts whose correctness or equivalence can be checked independently, not at the foundation model "in the abstract" (§4.1). This does not exclude verifying neural models; the authors cite existing neural-network verifiers as component-level targets and one closed-loop case study, an emergency-braking system (§4.1).
- **Propose, verify, refine.** A model proposes a program, specification or proof; a type checker, SMT solver, model checker, equivalence checker or proof assistant accepts or rejects it; failures return as feedback. The authors call the ideal output a certificate-producing artefact and point to translation validation and proof-carrying code as precedents. Trust then rests on the specification and the checker, "not in the stochastic generation process" (§4.3). They give one auto-formalisation system, ProofBridge, as an example of semantic alignment used to improve generation, not to certify it (§4.3).
- **Runtime layer.** A learned controller runs under a monitor; a verified safe controller, shielding or switching takes over when constraints are violated. The authors say the safe controller trades capability for analysability and need not match the advanced one (§5.1). They state that the loop "separates capability from authority" (§5.1). Shielding restricts or modifies single actions; switching hands control to the safe controller; the two may be combined (§5.1). Real-time reachability is named as a basis for switching decisions (§5.1).
- **Thresholds are not guarantees.** Intervention thresholds found by testing, such as for uncertainty or distance to a boundary, are "empirical operating evidence" and do not become formal guarantees (§3.4, §4.4, §5.2).
- **Four open challenges.** Turning informal intent into executable specifications; making the neural–symbolic–physical boundary trustworthy ("assurance-carrying interfaces"); composing different kinds of evidence into system claims without collapsing them into one confidence score; and lifecycle certification with continuous assurance cases (§6.1 to §6.4).
- **A staged path.** First tasks that have an explicit correctness oracle, then compositional system assurance, then certifiable closed-loop autonomy; only afterwards a wider reach towards direct verification of foundation-model components. Verifying unrestricted general-purpose models is called a valuable grand challenge but not a prerequisite for trustworthy deployment (§6.5, §7).

## How

A position paper by a fourteen-author group. It draws on the authors' own earlier work and on published systems for illustration: TARGET and SAFE for test generation from traffic rules and crash reports (§3.2), neuro-symbolic behaviour trees (§2.3), RusTReach and shields for runtime assurance (§5.1), and NeuroSymLand for a UAV landing pipeline (§4.2, §5.1). The paper gives no figures of its own for any of them, and this page does not repeat theirs.

## Limits

The authors say the following.

- The stack is a framework and an agenda. It is not a tested system. For general-purpose models, the objective that every model be intrinsically safe or fully verified remains technically remote and, for many open-ended tasks, difficult even to specify (§6).
- A symbolic abstraction is not correct merely because it is symbolic. A world model can omit a pedestrian or turn an uncertain relation into a certain one, and reasoning over it is then correct for a wrong world (§6.2). They call this the neural–symbolic–physical assurance gap.
- Local guarantees count only when their assumptions are discharged, and a failure at one boundary can invalidate guarantees elsewhere (§4.2, §6).
- Not every verified property can be monitored at runtime: some depend on latent state or on future behaviour, and some cost too much to evaluate within a CPS's timing (§4.4).
- Theories for composing probabilistic evidence, uncertainty propagation and incremental re-assurance are listed as open (§6.3).

A careful reader adds the following. This is inference.

- There is no result, no case study of the whole stack and no cost figure. Evidence that the stack works as a whole is absent; its parts rest on other papers, which this page has not read.
- The Simplex layer is described by role. The paper gives no concrete switching rule (§5.1 gives only a qualitative condition and names real-time reachability as a basis), no timing bound and no statement of what stops the learned side from interfering with the safe side. It does not discuss the operating system or hypervisor beneath the layer.
- Its mention of the safe controller as "verified" is a design aim. The text does not show a verified safe controller for a foundation-model system.
- The authors are advocates of the approach, and several cited examples are their own work.
- The paper is a preprint with template placeholders (conference name, year 2018, DOI) still in place.

## Against the wiki

- [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md): **confirms and extends.** It uses the same three parts (learned controller, monitor, safe controller) with foundation-model pipelines in the learned role, and adds shielding as a variant beside switching, which the concept page does not yet record. It names the point the page already lists, that the safe controller trades capability for analysability. It says nothing on the page's rule that the safe side owns its sensors, or on isolation by a kernel; its monitor reads "symbolic world-model elements" and uncertainty exposed by the neural side (§5.1). Our reading is that this is closer to the relaxed form of [Synergistic Simplex](https://silentzero.ooo/wiki/sources/2026-bansal-synergistic-simplex-cooperative.html.md) than to the strict form in [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md); the paper does not discuss the difference. For the pattern's origin it cites Sha 2001 and Bak et al. 2009 and gives no earlier date, so it neither confirms nor disputes the 1994 date on the page.
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): **confirms the stance, adds no proof.** "Capability from authority" and "constrain, do not verify the model" is the thesis the page rests on, now stated, in our reading independently, as an agenda. The page's table of what exists is unchanged, because the paper offers no demonstration and no proven safety controller. It also suggests that thresholds for the switch come from testing and are evidence, not proof. Our reading is that this bears on the open question of what the monitor detects.
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md): **confirms.** The page says only what a checker accepts counts. The paper generalises the same split, generator outside and small checker inside the trusted base, and names translation validation and proof-carrying code as precedents (§4.3). It does not give new measurements of proof generation.
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md): our reading is that the barrier shield in that preprint is one instance of the action-level shielding named in §5.1. This paper does not cite it.

## For Silent Zero

[The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): no change of state. The paper is an independent statement of the thesis that a learned component should hold capability while a smaller checked layer holds authority. It is a position, so it counts as a statement of experts and gives no evidence that the pattern works for an agent operating system. Its trust line (a model outside the trusted base, a small checker inside) also matches how [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md) is used. Its call to keep intervention thresholds apart from proofs is a point the paper's safety loop should state if it names thresholds. Nothing in Silent Zero is built, and the paper's agenda is not a design for Silent Zero.

## Related pages

- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md)
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md)
- [Synergistic Simplex](https://silentzero.ooo/wiki/sources/2026-bansal-synergistic-simplex-cooperative.html.md)
- [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md)
