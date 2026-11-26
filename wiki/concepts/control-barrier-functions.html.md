# Control barrier functions

> A filter that keeps a robot’s commanded motion inside a safe set; five VLA filters, guarantees conditional on perception or on modelled geometry.

Concept · LLM reviewed · updated 2026-11-26 · 6 sources · https://silentzero.ooo/wiki/concepts/control-barrier-functions.html

A control barrier function (CBF) turns "stay away from the obstacle" into a condition on a robot's commanded motion. The safe states form the set where a function h(x) is at least zero. A quadratic program picks the control closest to the policy's nominal command that still satisfies the condition that h may fall no faster than a rate set by a design function (ḣ ≥ −α(h)). If the robot starts inside the set, the condition keeps it there ([VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md), §III, §IV-C). Used as a safety filter between a learned policy and the arm, it leaves the policy's action untouched when no risk is near and corrects it otherwise.

## State, November 2026

Five papers in the wiki put a CBF filter behind a frozen vision-language-action policy; three were evaluated in simulation first:

- AEGIS builds the obstacle from a vision-language model and a detector (a later paper describes such filters as running them once per episode); its theorem holds if perception is accurate and the ellipsoids enclose the obstacle ([VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md)).
- KNOWS reads the target from the policy's attention at every step and tracks obstacles; its collision rate with moving obstacles is lower than a once-per-episode baseline's ([KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md)).
- A multi-link variant guards wrist and forearm and tracks a moving hazard by optical flow ([multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md)).
- A benchmark paper adds a variant that filters a whole action chunk at each chunk boundary, with a distance-based barrier and soft constraints; its evidence is one real-robot demonstration, and the benchmark itself scores policies, not filters ([LIBERO-Safety, a benchmark for physical and semantic safety of VLA models](https://silentzero.ooo/wiki/sources/2026-tsinghua-libero-safety-comprehensive.html.md), appendix).
- A thermal-perception policy with a joint-space filter on a Franka arm: the barrier is on link spheres against a box, the tabletop and a wall that the authors modelled, not perceived; the paper states no theorem and reports success rates, not collision counts, with the filter raising mirror rejection of the full model from 4 to 15 of 20 trials in normal light, scored on the first predicted step ([Safe-Night VLA, thermal perception and a barrier filter on a Franka arm](https://silentzero.ooo/wiki/sources/2026-yu-safe-night-vla.html.md), Table II).

In the first three, the guarantee is conditional on a geometry that perception supplies, and each reports collisions that remain; the chunk-level filter reports neither a guarantee beyond the statement that its constraint enforces forward invariance nor collision counts. None proves the filter, its perception or the controller below it. The thermal-perception paper adds that a blocked policy often keeps proposing similar actions, so being stopped and colliding can end in the same task failure ([Safe-Night VLA, thermal perception and a barrier filter on a Franka arm](https://silentzero.ooo/wiki/sources/2026-yu-safe-night-vla.html.md), §V-B). A literature review names the same weakness: the guarantees weaken when state estimates are stale, the dynamics model is wrong or the action representation differs from the one the proof assumes ([Silent failures in physical AI, a literature review of runtime action authorization](https://silentzero.ooo/wiki/sources/2026-unverified-silent-failures-physical.html.md), §11). When no safe action exists the systems differ: one executes the nominal action, one stops ([multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md), [KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md)).

## Related

[The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md), [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md), [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md), [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md).

## Open questions

- Whether a barrier filter can be made independent of the learned side's perception, so that it fits the safety path's rule that the loop owns its sensors.
- Whether a filter's guarantee can be stated against a model of the plant, with the tracking error of the controller below included.

## Sources

- [KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md)
- [LIBERO-Safety, a benchmark for physical and semantic safety of VLA models](https://silentzero.ooo/wiki/sources/2026-tsinghua-libero-safety-comprehensive.html.md)
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md)
- [Safe-Night VLA, thermal perception and a barrier filter on a Franka arm](https://silentzero.ooo/wiki/sources/2026-yu-safe-night-vla.html.md)
- [Silent failures in physical AI, a literature review of runtime action authorization](https://silentzero.ooo/wiki/sources/2026-unverified-silent-failures-physical.html.md)
- [VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md)
- [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md)
