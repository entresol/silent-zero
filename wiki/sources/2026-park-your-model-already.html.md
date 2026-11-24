# KNOWS, a safety filter steered by the policy's attention

> KNOWS: the policy’s own attention names the target; collisions with moving obstacles 70.8 to 26.9 % against the authors’ baseline, simulation only. measurement, full text.

Source · Park et al. 2026 · LLM reviewed · updated 2026-11-24 · https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html

Seongbin Park, Fan Zhang, Baharan Mirzasoleiman, Shahriar Talebi and Nader Sehatbakhsh (University of California, Los Angeles). "Your Model Already Knows: Attention-Guided Safety Filter for Vision-Language-Action Models", arXiv 2606.09749v1 [cs.RO], 8 June 2026. A preprint. [arXiv](https://arxiv.org/abs/2606.09749). Read in full, except the appendix equations and the references.

## What it shows

- **The idea.** Earlier barrier-function filters ask a vision-language model once, at the start of an episode, which object is the target; the answer goes stale when objects move. The authors read the target from a single attention head of a frozen π0.5 policy at every step, treat every other tracked object as an obstacle and feed them into a control-barrier program (§1, §3). They name the framework KNOWS. See [Control barrier functions](https://silentzero.ooo/wiki/concepts/control-barrier-functions.html.md).
- **The head.** They profiled four episodes of one suite and picked layer 12, head 3 for the agent camera (§3.3). Over 80 long-horizon episodes, attention density on the target in the early window predicted success with an AUC of 0.89, against 0.70 over the whole episode (§4.4, Figure 3). The authors call it an "inference-time correlate of task outcome".
- **Static scenes.** Against a baseline that fixes obstacles at the start, the text says KNOWS keeps success comparable to the baseline (§4.2). Our reading of Table 1: not on every cell. Its collision rate is higher in several, for example the long-horizon suite (45.5 against 32.0 per cent at level I; 39.5 against 14.0 at level II), and its safe-success lower in some (long-horizon level II 24.0 against 42.5, spatial level I 53.0 against 61.0).
- **Moving obstacles.** In Level III, a benchmark extension where an obstacle moves along a line over 30 control steps (1.5 s at 20 Hz), the collision rate over the four suites falls from 70.8 to 26.9 per cent on average (our arithmetic from Table 1), which the abstract calls outperforming "by 43%, on average"; the figure matches the difference in percentage points, not the relative drop of 62 per cent (our reading). Safe-success is higher in all four suites (Table 1).
- **Timing.** On a workstation with two RTX PRO 6000 GPUs the added work is 49.3 ms per step, which is the 50 ms of a 20 Hz loop (the listed parts sum to 50.0 ms): attention read 0.8 ms, segmentation 19.3 ms, depth and centroid 9.1 ms, target identification 9.4 ms, the program 11.4 ms. One policy call takes 243 ms per chunk and, with eight-step chunks, about 30 ms per step (Table 2, §4.3). The paper says the system holds the control rate and does not say how policy and wrapper overlap; the wrapper alone fills the budget, and the policy's 30 ms per step would come on top if they do not overlap (our reading).
- **Fallback.** If no safe action exists, the filter "falls back to an emergency stop" (§3.1).

## How

Simulation only: SafeLIBERO (from the VLSA paper, see [VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md)) with a third, dynamic level, four suites, 50 episodes per task, π0.5 as policy, a fine-tuned YOLOE for segmentation, no real robot. Baselines: the policy unfiltered, and a "naive" filter that the authors built to reflect that earlier design with ground-truth segmentation at the first step, never updated (§4.1).

## Limits

The authors say: only the end effector is guarded, so arm and elbow collisions occur; geometry and tracking are only as good as perception; the safety statement holds for a reduced model of the end effector and transfers to the arm "only modulo" the tracking error of a downstream controller they treat as a black box (§5). They say it should generalise to other transformer-based policies without architectural change, and expect its efficacy to depend on the quality of the backbone (§6). Our reading: the text reports no policy other than π0.5.

A careful reader adds:

- The main comparison is against the authors' own reconstruction of earlier work, not against the released system, and the baseline reads the first frame from ground truth.
- There is no proof here, only a conditional barrier argument and simulation; the authors write of "formal collision-avoidance guarantees" for inference-time filters in general (§1).
- The head was chosen from four episodes of one suite and tested on the same benchmark family.
- The attention signal is taken from the model that the filter is meant to guard. Our reading: a policy that fails in a way that also moves its attention would move the filter with it.

## Against the wiki

- [VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md): **extends and challenges**. It names that design's weakness with moving objects; its evidence is a reconstruction.
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md): related. Another filter for moving hazards; Agarwal runs the nominal action when infeasible, KNOWS stops.
- [RAVEL, rolling inference for flow-based VLAs](https://silentzero.ooo/wiki/sources/2026-chen-ravel-asynchronous-rolling.html.md): related. Policy latency (243 ms per chunk here) is again large against the loop.

## For Silent Zero

[The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): no change of state. Our reading: a filter whose obstacle set comes from the model's own attention does not satisfy the rule that the loop relies on nothing the learned side controls. [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): a table of per-step timings of a filter, workstation hardware, no bound.

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Control barrier functions](https://silentzero.ooo/wiki/concepts/control-barrier-functions.html.md)
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md)
- [RAVEL, rolling inference for flow-based VLAs](https://silentzero.ooo/wiki/sources/2026-chen-ravel-asynchronous-rolling.html.md)
- [VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md)
