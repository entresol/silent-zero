---
type: source
id: 2026-unverified-silent-failures-physical
status: reviewed
read: partial
kind: survey
sources: [2026-unverified-silent-failures-physical]
updated: 2026-11-25
---

# Or 2026: Silent failures in physical AI, a literature review of runtime action authorization

Barak Or (STATE16, a company the author founded and leads; the text lists teaching posts at other institutions "solely for biographical context" and says they did not sponsor or endorse the paper). "Silent Failures in Physical AI: A Literature Review of Runtime Action Authorization for Autonomous Systems", arXiv 2606.00090 [cs.RO], v1 of 23 May 2026. A single-author preprint. [arXiv](https://arxiv.org/abs/2606.00090). Read: the abstract, §1 to §3, the evaluation requirements (§8, in part), the limitations (§11), the assurance implications (§10) and the conclusion; the literature map, the empirical-milestone table and the simulator section only skimmed. No claim below rests on the skimmed parts.

## What it shows

- **A definition.** A silent failure is a case in which an autonomous system acts with high apparent confidence on an incorrect, incomplete or physically invalid picture of the world, so that the system keeps running and no crash reveals it. The paper formalises it: a runtime layer decides "authorize, modify, block, fallback or escalate" for each proposed action from the observation history, a state estimate, active constraints and evidence about the state's validity (§1, §2, equations 1 to 4).
- **A formal claim.** Equation 3 says that the policy's likelihood of an action does not imply that the action is authorized. The paper calls it its minimal formal claim and says the formalisation is intentionally minimal; it introduces no benchmark and no empirical evaluation of a guardrail (§11). Our reading: it states the problem and proves nothing.
- **A taxonomy.** Seven guardrail functions: semantic validity, state validity, physical feasibility, spatial and operational validity, temporal validity, fallback authority, auditability (Table 1). The author argues that safe control, runtime assurance, shielding, uncertainty estimation and benchmarks each cover part of this, and that no single stream of the literature surveyed covers all (§1, §4).
- **Evaluation requirements.** Guardrails should be judged by the quality of their interventions, not by task success alone; the paper lists metric families and a minimal record of an "authorization event" with fields for evidence, decision, fallback, timing and audit trace (§8, §10, Tables 4, 5, 7).
- **Boundary conditions it names.** A runtime layer cannot guarantee safety when observability is poor, constraints are incomplete, the fallback is underspecified or the environment is adversarial. Guarantees from barrier filters or runtime assurance weaken when state estimates are stale, the dynamics model is wrong, or the action representation the policy exposes differs from the one assumed in the safety proof. A correct block that arrives after commitment is insufficient, and a fallback is not automatically safe. The layer should not replace certified control, verified hardware limits, operator training, incident response or regulatory compliance (§11).

## How

A literature review with a "focused review strategy" (our reading: not a systematic one): sources from arXiv, OpenReview, IEEE, ACM and proceedings, chosen for relevance to the path from model output to hardware command, with standards, certification and general AI ethics excluded unless they bear on that path (§4.1). The author names the risk that adjacent work is under-represented and says the incidents from road vehicles used as examples are analogues, not evidence about vision-language-action models (§11).

## Limits

The author says: the formalisation is minimal; the paper offers no benchmark and no evaluation of a guardrail; guardrails are one layer among several; the selection is curated. A careful reader adds:

- One author, one company, a preprint without review. Our reading: the paper also states a case for an independent authorization layer, which fits the author's business, though the text declares no product.
- Its synthesis depends on the literature it chose; the paper does not show that a gap exists beyond the author's reading of eleven streams.
- The text read does not discuss a verified kernel, capabilities or [[simplex]] as such, although a reference list entry cites the Simplex architecture.

## Against the wiki

- [[safety-path]]: **confirms and extends**. The paper asks for a layer independent of the learned model that checks state validity, feasibility, timing and fallback before a command reaches the hardware, which, in our reading, is the split of [[simplex]] (the text does not discuss Simplex); its list of conditions under which such a layer's guarantees weaken matches the wiki's open points on perception and on the learned side's influence on safety margins.
- [[control-barrier-functions]]: **confirms**. The paper names the same weakness: barrier guarantees depend on state estimates and models that the filter does not control.
- [[broker]]: touches. The paper's "semantic validity" and "spatial and operational validity" include task permissions and policy engines; its audit-trace requirement is not discussed on the broker page.

## For zOS

[[safety-path]]: no change of state. Our reading: the authorization-event record is a candidate checklist for what zOS's loop and broker log, and its seven functions show which checks fall to the safety loop (state, feasibility, timing, fallback) and which to the broker (intent, permissions). That split is ours, not the paper's.
