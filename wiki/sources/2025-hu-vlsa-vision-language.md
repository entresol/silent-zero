---
type: source
id: 2025-hu-vlsa-vision-language
status: reviewed
read: full
kind: measurement
sources: [2025-hu-vlsa-vision-language]
updated: 2026-11-24
---

# Hu et al. 2025: VLSA and AEGIS, a barrier-function layer for VLA policies

Songqiao Hu, Zeyi Liu, Shuang Liu, Jun Cen, Zihan Meng, Shihefeng Wang, Xiang Li and Xiao He (Tsinghua University, TetraBOT, DAMO Academy). "VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer", arXiv 2512.11891 [cs.RO], first posted in December 2025; the text read is v2 of 2 July 2026. A preprint. [arXiv](https://arxiv.org/abs/2512.11891). Read in full, except the references.

## What it shows

- **The architecture.** A safety-constraint layer behind the action output of an existing vision-language-action (VLA) model. A vision-language model names the single most critical non-robot obstacle from the instruction and one camera image, an open-set detector localises it, and the obstacle and the end effector are each enclosed in an ellipsoid. A control-barrier quadratic program then changes the policy's action as little as possible; when no risk is found, the output equals the policy's (§IV-A to §IV-C). See [[control-barrier-functions]].
- **The guarantee.** Theorem 1 says the end effector will not collide with the obstacle, assuming accurate safety assessment, precise point-cloud filtering and ellipsoids that enclose obstacle and end effector. The proof follows from forward invariance of the safe set under the barrier condition (§IV-C).
- **The benchmark.** SafeLIBERO: 16 tasks from four LIBERO suites, two safety levels each (obstacle near the target, obstacle in the path), 50 randomised episodes per scenario, 32 scenarios and 1,600 episodes (§V-A).
- **The results.** The base policy is π0.5, on a Franka Panda in Robosuite at 20 Hz, with GLM-4.5V for the assessment. The collision avoidance rate (CAR) rose from 18.7 to 77.9 per cent in the translation-only action space and from 17.1 to 68.9 per cent in the full action space; task success rose from 50.9 to 68.1 and from 57.8 to 67.5 per cent. OpenVLA-OFT, the second baseline, reached a CAR of 15.1 and 5.7 per cent (Table I); the table's own full-action rows for it (8.3, 19.5, 11.5, 6.0) average 11.3, so the printed 5.7 does not match (our arithmetic). The abstract says "over 50%" for obstacle avoidance and "nearly 10%" for task success; the table's gains are 59.2 and 51.8 points of CAR, and 17.2 and 9.7 points of task success (our arithmetic).
- **Cost.** The layer took 0.356 ms per step on an RTX 4090 setup, 1.86 per cent of the cycle and about 1/47 of the policy's inference time (§V-B, Fig. 10). The paper calls this the safety-constraint layer's time and does not say whether it includes the vision-language model and the detector.
- **Real robot.** A Franka Panda with π0.5-DROID, zero-shot, policy at 15 Hz and a low-level controller at 1 kHz, two tasks with two safety levels each. The authors say the unfiltered policy collided with the obstacles and the filtered one performed consistently with the simulation; the results are in a supplementary video and no counts are given (§VI).

## How

Simulation in LIBERO and Robosuite plus one small real-robot demonstration. The barrier function is the signed distance between two ellipsoids; the program has one linear constraint (§V-B). The comparison is against the unfiltered π0.5 and against OpenVLA-OFT, not against another safety filter.

## Limits

The authors say: residual collisions come from the perception pipeline (wrong obstacle, wrong localisation, aggressive point-cloud filtering) and from unconstrained arm links, since only the end effector is guarded; a safe action can push the system into states the policy rarely saw, so it may fail the task afterwards; highly dynamic obstacles and whole-body avoidance are left as future work (§V-C, §VII).

A careful reader adds:

- The theorem's premises are the weak point. The residual collisions (CAR 68.9 to 77.9 per cent) have two causes the authors name, perception errors and unguarded arm links, and the table does not separate them. The guarantee is conditional on perception, which nobody proves.
- The obstacle comes from a vision-language model and a detector. Our reading: a wrong answer from them removes the guarantee for that episode, so this does not match the safety path's rule that the loop relies on nothing the learned side controls. How often they run is not stated in the text read; a later paper says such filters run them once, at the start of an episode ([[2026-park-your-model-already]], §1).
- All simulation results come from one base policy and one benchmark made by the same authors.

## Against the wiki

- [[2026-agarwal-multi-link-safety]]: **extends**. That preprint builds on AEGIS and reports it collided in 35.74 per cent of moving-hazard episodes; this source covers the static case.
- [[2026-park-your-model-already]]: **extends**. Park et al. build a baseline "reflecting the design" of this source and argue that its obstacle choice goes stale when objects move.
- [[safety-path]] and [[control-barrier-functions]]: confirm that barrier filters exist for VLA policies, with the guarantee conditional on perception.

## For zOS

[[safety-path]]: no change of state, one more row of evidence for a filter on commanded motion. [[real-time-loops]]: the layer's computation is small against the policy's; a bound is not shown.
