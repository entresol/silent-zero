# multi-link safety filtering for VLA policies

> A barrier-function shield between a frozen VLA and the arm; collisions with moving hazards 65.62 to 27.27 % in simulation. measurement, full text.

Source · Agarwal and Raghunathan 2026 · LLM reviewed · updated 2026-11-20 · https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html

Yatharth Agarwal and Vijay Raghunathan (School of Electrical and Computer Engineering, Purdue University). "Multi-Link Safety Filtering for VLA Policies Around Moving Hazards", arXiv 2609.40007v1 [cs.RO], 30 September 2026. A preprint. [arXiv](https://arxiv.org/abs/2609.40007). Read: the full text; the reference list was read only for the works the text names.

## What it shows

- **The problem.** With moving hazards, the π0.5 policy completes 62.93 per cent of episodes but disturbs the hazard in 65.62 per cent (introduction; Table Ia, unshielded mean). Task success alone does not show that a policy is safe in clutter.
- **The shield.** A training-free runtime filter between a pretrained vision-language-action (VLA) policy and the robot. It guards five ellipsoids (gripper, wrist, three overlapping forearm ellipsoids) against one keep-out ellipsoid around the hazard, in a single control-barrier quadratic program that minimises the change to the policy's command (§III-A, §III-B). The elbow and upper arm carry no guarded ellipsoid (§III-B).
- **Tracking.** The hazard ellipsoid is fitted once at reset from RGB-D images, after a vision-language model names the hazard and an open-vocabulary detector locates it. Sparse optical flow then moves only the ellipsoid's centre, every five control steps; shape and orientation stay as fitted (§III-C).
- **Main result.** Over six simulated hazard-motion conditions, 624 episodes each, collision fell from 65.62 to 27.27 per cent and safe-success (task done without collision) rose from 29.35 to 50.43 per cent. Task success, 62.93 unshielded and 61.38 shielded, showed neither a significant change nor equivalence within the authors' margin of 3 percentage points (§V-A, Table Ia).
- **Against other filters.** AEGIS, the end-effector filter this work builds on, collided in 35.74 per cent of moving episodes. That differs significantly from the shield. The safe-success difference (44.90 against 50.43) does not. OSCBF, a torque-level filter, collided in 48.96 per cent and reached 41.88 safe-success, both significantly worse than the shield (§V-A). On static SafeLIBERO the shield collided in 27.00 per cent against 30.75 for AEGIS and 83.44 unshielded (Table Ib). The authors say the OSCBF gap does not show that torque-level filtering protects less, because the robot envelopes differ; with the hazard in a bounding sphere OSCBF collided in 25.80 per cent of 300 mm escape episodes, not significantly different from the shield.
- **Arm coverage.** On static scenes, guarding wrist and forearm besides the end effector lowered collision from 31.31 to 25.19 per cent, with no significant change in task or safe-success. Safe failures, episodes that avoid the hazard but miss the task, rose from 1.50 to 21.94 per cent against the unshielded policy (§VI-A, Table Ib). With exact hazard geometry and motion, which is not deployable, collision under multi-link coverage was 14.44 per cent, against 21.94 per cent under end-effector coverage (§VI-A).
- **Severity.** Unshielded episodes displaced the hazard by 147.7 mm at the median; surviving disturbances under multi-link coverage were 32.5 mm (§VI-A). Of the unshielded policy's flagged episodes 82.05 per cent carry a recorded contact, against 48.29 per cent under the shield (§IV).
- **Where protection is lost.** On the 300 mm escape condition with the original caption, collision was 45.99 per cent unshielded, 30.29 with the estimate frozen at reset, 22.44 with the full system and 18.43 with exact geometry and true motion (Table III; its note says the upper and lower blocks compare at system level, not tracking only). The authors conclude that image-based perception keeps most of the protection available with exact information (§VI-B). Re-detecting the hazard on a fixed cadence collided as often as the frozen estimate (30.13 per cent), because refits are accepted only within 50 mm of the last position and at least one refresh was accepted in only 184 of 624 episodes (§VI-B).
- **Update rate.** Strides of 1, 2, 5, 10 and 20 control steps gave collision between 22.76 and 24.84 per cent; strides 40 and 80 gave 28.37 and 29.97, near the frozen 30.29 (§VI-C). Stride 5 is deployed.
- **A grounding failure.** The aggregate hides one: in six of 624 episodes the same plausible but wrong phrase made the filter guard a different object (§VI-B).
- **Edge cost.** On a laptop processor (Intel Core Ultra X7 358H, with iGPU and NPU), the five-ellipsoid barrier took 2.0 ms at the median and 2.2 ms at the 99th percentile on the CPU; the optical-flow update 3.1 and 3.6 ms (Table IIb). A policy call took 343 ms on the iGPU in the released configuration and 177.3 ms after trimming the vision-language prefix (968 to 576 positions) and halving the integration steps from ten to five, with unchanged weights (§III-D, §V-B). On the CPU it took 7,844.2 ms, on the NPU 446.2 ms (Table IIa). With synchronous calls each chunk boundary stalls for the call's duration, 177.3 ms at the median (§V-B).
- **Cost of that trim.** On the 300 mm escape condition, the shielded system's collision stayed at 22.92 against 22.44 per cent, but task success fell by 4.17 and safe-success by 3.53 percentage points, both significant (§V-B).
- **Hardware.** On a physical SO-101 arm, four tasks with four episodes each, the arm touched the hazard in 3 of 16 shielded and 11 of 16 unshielded episodes, and completed the placement in 11 shielded and 13 unshielded ones (§V-B).

## How

Simulation in MuJoCo with the Franka Panda of the LIBERO suites and the public π0.5 LIBERO checkpoint. A new moving-hazard benchmark reuses SafeLIBERO scenes with six conditions: stationary, a 25 mm orbit, a 300 mm shuttle and one-way escapes of 50, 150 and 300 mm, all at 50 mm/s (§IV). Static results cover 32 scenes with 1,600 episodes per configuration. A collision is flagged when the hazard's position shifts by more than 1 mm in total at any control step, which need not involve contact, so contacts are also recorded (§IV). Comparisons are paired by scene, with a permutation test and Holm–Bonferroni correction. AEGIS and OSCBF run from their authors' code, adapted to the same policy and episodes. The hazard namer is Qwen3-VL and the detector Grounding DINO. The barrier is solved with OSQP at a nominal 20 Hz (§IV).

## Limits

The authors state the following.

- The guarantee scope is narrow. The barrier conditions preserve the modelled safe set only under a fixed hazard, exact state and geometry, and feasible continuous-time execution. The deployed system relaxes several of these (geometry from RGB-D, sample-and-hold, approximated link motion, a hazard pose updated periodically), and the authors treat collision reduction as an empirical result, not an invariance guarantee for the moving-hazard loop (§III-C).
- If the program is infeasible, the current implementation executes and logs the nominal action, with no certified fallback (§III-C).
- Centre transport assumes the hazard translates without large rotation or change of visible shape, and keeps its reset height (§III-C).
- The scope is task-irrelevant hazards; tasks that need contact call for other constraints (§II).
- The policy does not see the shield's corrections within a chunk, which can limit recovery when avoidance needs replanning (§VII).
- The hardware budget is small, the hazard is hand-carried, and the counts come without paired tests (§V-B).
- Reported rates are from simulation (§IV).

A careful reader adds the following.

- The baselines are adapted from the authors' code, with different robot envelopes, and the authors call the comparison one of practical standing (§V).
- The benchmark and the moving conditions are the authors' own, with commanded trajectories at one speed. The ablations and the policy-configuration comparison use the 300 mm escape condition, while the coverage comparison and placement sweep use the static benchmark (§IV, §VI-A, §VI-C); one policy checkpoint was used. No adaptive adversary is tested.
- The shield's hazard model comes from a language model and a detector at reset, so the protection depends on learned perception, not only on the barrier arithmetic. The paper shows one named wrong-object failure.
- The edge figures are from one laptop; energy is a platform total above idle (§IV).
- The paper is a preprint.

## Against the wiki

- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): **extends**, not contradicts. This is a different kind of runtime check from [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md): a filter that edits each command so that a geometric constraint holds, instead of switching to a separate safe controller. Our reading: it shows such a filter can run in milliseconds on a CPU beside a policy, but its hazard model comes from learned perception and it falls back to the nominal action when infeasible. The wiki page records a strict rule: the loop owns its sensors and takes nothing from the model. This design does not meet it.
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md): **extends**. The policy call takes 177.3 ms on the iGPU, while the shield takes 2.2 ms (p99) per step on the CPU. That is one more measured figure for the delay a lower loop must tolerate; the paper reports that, when calls are issued synchronously, each chunk boundary stalls for the call's duration, 177.3 ms at p50 (§V-B); it does not say its deployed loop is synchronous.
- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): **extends** with the cadences on one edge platform: barrier at every 50 ms step, flow every fifth step, policy once per ten-action chunk (§III-D). It gives timings, not a proven bound.
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md): related. Both treat a slow policy above a faster step; our reading: the paper does not mention real-time or asynchronous chunking.
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md) and [The broker](https://silentzero.ooo/wiki/design/broker.html.md): no connection, apart from the general pattern of a deterministic check beside an untrusted model.

## For Silent Zero

[The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): no change of state. Our reading: the source is evidence that a constraint-based filter of commanded motion is cheap in compute beside a policy, which bears on the open question of what the loop must check. It does not supply a proof, and its own guarantee scope (§III-C) is weaker than what the paper's safety loop would need to claim. [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): no change of state; a new timing reference only. Nothing in Silent Zero is built.

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md)
- [Control barrier functions](https://silentzero.ooo/wiki/concepts/control-barrier-functions.html.md)
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md)
- [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md)
- [a neuro-symbolic assurance agenda for learning-enabled CPS](https://silentzero.ooo/wiki/sources/2026-zheng-assuring-learning-enabled.html.md)
- [FASTER, reaction time of flow VLAs](https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html.md)
- [KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md)
- [LIBERO-Safety, a benchmark for physical and semantic safety of VLA models](https://silentzero.ooo/wiki/sources/2026-tsinghua-libero-safety-comprehensive.html.md)
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)
- [VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md)
