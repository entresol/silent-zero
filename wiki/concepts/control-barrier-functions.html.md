# Control barrier functions

> A filter that keeps a robot’s commanded motion inside a safe set; three VLA filters, guarantees conditional on perception.

Concept · LLM reviewed · updated 2026-11-24 · 3 sources · https://silentzero.ooo/wiki/concepts/control-barrier-functions.html

A control barrier function (CBF) turns "stay away from the obstacle" into a condition on a robot's commanded motion. The safe states form the set where a function h(x) is at least zero. A quadratic program picks the control closest to the policy's nominal command that still satisfies the condition that h may fall no faster than a rate set by a design function (ḣ ≥ −α(h)). If the robot starts inside the set, the condition keeps it there ([VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md), §III, §IV-C). Used as a safety filter between a learned policy and the arm, it leaves the policy's action untouched when no risk is near and corrects it otherwise.

## State, November 2026

Three preprints in the wiki put a CBF filter behind a frozen vision-language-action policy, all in simulation first:

- AEGIS builds the obstacle from a vision-language model and a detector (a later paper describes such filters as running them once per episode); its theorem holds if perception is accurate and the ellipsoids enclose the obstacle ([VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md)).
- KNOWS reads the target from the policy's attention at every step and tracks obstacles; its collision rate with moving obstacles is lower than a once-per-episode baseline's ([KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md)).
- A multi-link variant guards wrist and forearm and tracks a moving hazard by optical flow ([multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md)).

In each, the guarantee is conditional on a geometry that perception supplies, and each reports collisions that remain. None proves the filter, its perception or the controller below it. When no safe action exists the systems differ: one executes the nominal action, one stops ([multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md), [KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md)).

## Related

[The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md), [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md), [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md), [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md).

## Open questions

- Whether a barrier filter can be made independent of the learned side's perception, so that it fits the safety path's rule that the loop owns its sensors.
- Whether a filter's guarantee can be stated against a model of the plant, with the tracking error of the controller below included.

## Sources

- [KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md)
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md)
- [VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md)
- [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md)
