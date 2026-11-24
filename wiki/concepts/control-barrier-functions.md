---
type: concept
status: reviewed
sources: [2025-hu-vlsa-vision-language, 2026-park-your-model-already, 2026-agarwal-multi-link-safety]
short: Filter keeping a robot inside safe states
updated: 2026-11-24
---

# Control barrier functions

A control barrier function (CBF) turns "stay away from the obstacle" into a condition on a robot's commanded motion. The safe states form the set where a function h(x) is at least zero. A quadratic program picks the control closest to the policy's nominal command that still satisfies the condition that h may fall no faster than a rate set by a design function (ḣ ≥ −α(h)). If the robot starts inside the set, the condition keeps it there ([[2025-hu-vlsa-vision-language]], §III, §IV-C). Used as a safety filter between a learned policy and the arm, it leaves the policy's action untouched when no risk is near and corrects it otherwise.

## State, November 2026

Three preprints in the wiki put a CBF filter behind a frozen vision-language-action policy, all in simulation first:

- AEGIS builds the obstacle from a vision-language model and a detector (a later paper describes such filters as running them once per episode); its theorem holds if perception is accurate and the ellipsoids enclose the obstacle ([[2025-hu-vlsa-vision-language]]).
- KNOWS reads the target from the policy's attention at every step and tracks obstacles; its collision rate with moving obstacles is lower than a once-per-episode baseline's ([[2026-park-your-model-already]]).
- A multi-link variant guards wrist and forearm and tracks a moving hazard by optical flow ([[2026-agarwal-multi-link-safety]]).

In each, the guarantee is conditional on a geometry that perception supplies, and each reports collisions that remain. None proves the filter, its perception or the controller below it. When no safe action exists the systems differ: one executes the nominal action, one stops ([[2026-agarwal-multi-link-safety]], [[2026-park-your-model-already]]).

## Related

[[safety-path]], [[simplex]], [[action-chunking]], [[real-time-loops]].

## Open questions

- Whether a barrier filter can be made independent of the learned side's perception, so that it fits the safety path's rule that the loop owns its sensors.
- Whether a filter's guarantee can be stated against a model of the plant, with the tracking error of the controller below included.
