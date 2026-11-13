---
type: source
id: 2026-bansal-synergistic-simplex-cooperative
status: reviewed
read: partial
kind: test
sources: [2026-bansal-synergistic-simplex-cooperative]
updated: 2026-11-13
---

# Bansal et al. 2026: Synergistic Simplex

Ayoosh Bansal, Mikael Yeghiazaryan, Artyom Khachatryan, Tianyi Zhu, Hunmin Kim, Naira Hovakimyan and Lui Sha (UIUC, Caltech, Mercer University and others). "Synergistic Simplex: Cooperative Runtime Assurance for Safety-Critical Autonomous Systems". [arXiv:2605.08190](https://arxiv.org/abs/2605.08190), version 1 of 5 May 2026. Read in part: abstract, introduction, related work, the method's statement of the links and theorems 1 to 4, and the evaluation in full. The proofs of theorems 2 to 4 and the fault-probability derivations were skimmed, and this page makes no claim about their details.

## What it shows

- **The idea.** A [[simplex]] design keeps a verifiable safety layer beside an unverifiable ML layer. The authors let information flow both ways: from the safety layer to the ML layer (S2M), which asks the ML layer to replan within the safe bounds before the safety layer overrides, and from the ML layer to the safety layer (M2S), which lets the safety layer use an ML output such as lane boundaries (§III).
- **Claims of proof.** Under stated assumptions the S2M selection always returns an action in the safe set (Theorem 1). For M2S the authors derive conditions on a dependency graph of the autonomy stack under which using an ML output keeps the safety guarantee of their earlier Perception Simplex; the admissible class is an ML output independent of the protected function in both directions (Definition 2, Theorem 2); an "upstream use" is shown inadmissible (Theorem 4) and downstream use is left out of scope (§III-B). Our reading: the proofs are paper proofs on a model, since the text mentions no machine checking.
- **Evaluation.** In the CARLA simulator with a TransFuser++ driving model, an undetected static obstacle in the ego lane led to collisions in all 10 runs of the ML-only agent and none under the plain Perception Simplex or the M2S variant; neither safety variant completed the route (Table I, Experiment 1). With an undetected obstacle in a neighbouring lane, route completion was 0.1 under the plain safety layer and 0.7 with M2S, against 1.0 for the ML-only agent, whose time was 10.53 s against about 15 s for both safety variants (Experiment 2). S2M could not be tried in CARLA; in a separate nuPlan experiment 29 of 39 runs (74 per cent) finished, in the cases where the planner changed lane early enough; the authors say its effect depends on the planner's responsiveness, and there is no baseline without S2M (§VI-D).

## How

Faults are injected by replaying recorded nominal ML actions into scenarios with obstacles, so every architecture sees the same fault. Ten runs per configuration, 60 in CARLA; LiDAR at 2 Hz; a traffic-free "Parked Obstacle" scenario in daylight and clear weather (§V).

## Limits

What the authors say: obstacles are static, sensors do not fail, and lane detection is correct in the scenarios; outside the formal region neither design gives a guarantee. The two links were not tested in one stack; joint evaluation is future work. Faults were injected at decision level, not produced by perception (§IV-B, §IV-C, §V-D, §V).

A careful reader adds: the system is an autonomous car, not a robot arm, and the guarantee rests on assumptions about the safety layer's own correctness (assumptions 1 to 3, and for the plain Perception Simplex also 7, which the authors drop for the new design). The evidence is small: ten runs per cell, simulation only.

## Against the wiki

- [[simplex]]: extends it. The concept page records a one-way pattern with learned controllers on a pendulum and a rover ([[2025-nesti-use-simplex-architecture]]); this source adds a variant in which the safe side may read ML output under proved conditions. It credits Sha with pioneering Simplex for control systems; its reference list gives 2001 (IEEE Software).
- [[safety-path]]: the design page lists "rely on nothing the learned side controls". This source relaxes that principle for the safety layer, under conditions, and so is a point against reading the principle as absolute. Our reading: zOS keeps the strict form, because its safety loop owns its sensors and takes no output from the model.

## For zOS

[[safety-path]]: no state changes. The source is a counterpoint, not a contradiction: it shows that the strict form costs performance in one simulated scenario (route completion 0.1 against 0.7). The authors add that safety certification standards, as they put it, prohibit the safety layer from using unverifiable ML output (Introduction), which is the more basic reason for the strict form.
