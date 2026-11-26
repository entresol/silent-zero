---
type: source
id: 2026-yu-safe-night-vla
status: reviewed
read: full
kind: measurement
sources: [2026-yu-safe-night-vla]
updated: 2026-11-26
---

# Yu et al. 2026: Safe-Night VLA, thermal perception and a barrier filter on a Franka arm

Dian Yu, Qingchuan Zhou, Bingkun Huang, Majid Khadiv and Zewen Yang. "Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation", arXiv 2603.05754 [cs.RO], first posted 5 March 2026 (date and venue, IROS 2026, from the arXiv listing); the text read is v3 of 20 October 2026. [arXiv](https://arxiv.org/abs/2603.05754). Read in full, except the reference list.

## What it shows

- **The system.** A GR00T-N1.5-3B policy with a frozen vision-language backbone, fine-tuned for 5,000 steps on 600 teleoperated demonstrations, takes three camera views: RGB, a low-cost long-wave infrared (thermal) camera shown to the encoder as pseudo-colour, and depth (§III, §IV-A). Its output is a Cartesian end-effector displacement plus a gripper command (§III-C).
- **The filter.** At each control step a quadratic program finds the joint displacement that best tracks the policy's Cartesian request, with a damping term, subject to a barrier condition on the distance between collision spheres on the arm links and the environment, and to joint limits (Eq. 1a to 1c). See [[control-barrier-functions]]. In the experiments the constraints are a box boundary, the tabletop and a wall; the authors say they impose the wall (§IV-D) and describe the others as modelled constraints.
- **The results.** Success over 50 trials per cell (Table II). Hot/cold bottle, normal light, with the filter: RGB-only 42, RGB plus thermal (RGB-T, no depth) 86, full model 82 per cent; without the filter 32, 78 and 72. Buried object, normal light, with the filter: 16, 66 and 78 per cent; without 14, 60 and 74. In dim light the full model (thermal, depth and filter) reaches 64 and 72 per cent on the two tasks. In the mirror task the filter raised the full model's rejection of the reflected target from 4 to 15 of 20 trials in normal light and from 5 to 17 of 20 in dim light, and the RGB-T variant's from 12 to 19 of 20 (§V-A). These mirror counts are a first-step, open-loop score, and the paper does not say how a filtered proposal is scored, since it also counts a proposal that violates the wall constraint as a failed trial. The authors read the filter's effect as removing out-of-distribution motion, such as backward moves toward the modelled wall.
- **The attention check.** In 10 episodes of the bottle task, the attention mass on the hot object (the encoder's saliency combined with the action head's cross-attention) rose from 16.8 to 53.5 per cent when thermal input was on instead of masked. The authors call the study preliminary and exploratory and say it does not show thermodynamic reasoning (§V-C).

## How

A Franka Panda, a RealSense depth camera and a Topdon thermal camera. Dim light is simulated by darkening the RGB stream only. The mirror task is scored on the first predicted displacement, open loop, and a proposal that violates the wall constraint counts as a failed trial (§IV-D, §V-A).

## Limits

The authors name five limits (§III-B, §III-C, §V-B, §VI). The tasks are diagnostic, chosen to expose what RGB-only policies miss, and one base model is used. The filter's guarantee depends on the modelled safe set, accurate state estimates and correct geometry, and it does not handle unmodelled dynamic obstacles. The filter may block similar infeasible actions again and again, because the policy often keeps proposing similar actions instead of retrying; being stopped and colliding can then end in the same task failure. The thermal channel is uncalibrated pseudo-colour, and a cold target near ambient temperature is hard to find.

A careful reader adds:

- Each table cell is 50 trials from one trained model, with no variance reported (our reading).
- The filter's cost is not reported, and neither is a collision count with and without it; the evidence for the filter is task success, which mixes it with perception.
- The paper states no theorem. "Safety guarantee" is the authors' heading for the barrier condition and its stated conditions.
- Our reading: the constraint geometry here is fixed by the experimenters, not read from a camera by a learned model, unlike the filters in [[2025-hu-vlsa-vision-language]] and [[2026-park-your-model-already]]. That fits the safety path's rule that the loop relies on nothing the learned side controls, but only because the scene is static and modelled.

## Against the wiki

- [[control-barrier-functions]]: **extends**. A fifth paper with a filter behind a learned policy whose vision-language backbone is frozen, in joint space with link spheres; its constraints are modelled, not perceived.
- [[2025-hu-vlsa-vision-language]], [[2026-park-your-model-already]]: **confirm** the pattern; none reports a proof of the filter.

## For zOS

[[safety-path]]: no change of state. One more instance of a filter outside the policy, whose weakness is the one already named: the filter can stop the arm but not make the policy succeed.
