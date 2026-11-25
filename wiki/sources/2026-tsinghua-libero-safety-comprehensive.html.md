# LIBERO-Safety, a benchmark for physical and semantic safety of VLA models

> LIBERO-Safety: five suites and 19,664 collision-free demonstrations; eight VLA policies fall sharply on out-of-distribution levels; a chunk-level barrier filter shown once on a real robot. measurement, partly read.

Source · Cui, Zhang et al. 2026 · LLM reviewed · updated 2026-11-25 · https://silentzero.ooo/wiki/sources/2026-tsinghua-libero-safety-comprehensive.html

Rongxu Cui, Zongzheng Zhang, Jingrui Pang, Haohan Chi, Jinbang Guo, Saining Zhang, Shaoxuan Xie, Xin Jin, Yao Mu, Jiaolong Yang, Guocai Yao, Xianyuan Zhan, Ya-Qin Zhang and Hao Zhao (Institute for AI Industry Research, Tsinghua University, Beijing Academy of Artificial Intelligence and others). "LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models", arXiv 2606.23686 [cs.RO]; the text read is v2 of 26 June 2026. A preprint; project page libero-safety.github.io. [arXiv](https://arxiv.org/abs/2606.23686). Read: the main text (§1 to §5), the appendices on a chunk-level barrier filter (D) and the limitations (E); the other appendices (training settings, suite details) not read, and no claim below rests on them.

## What it shows

- **A benchmark of five suites.** Four embodied physical-safety suites (affordance-aware grasping, human-robot interaction, tabletop spatial avoidance, free-space hand-object avoidance) and one semantic-reasoning suite. Each has three levels that differ by suite; roughly, L0 is nominal, L1 adds a perturbation or dynamics, L2 is out-of-distribution or paraphrased (§3.2). Scenes are generated from a parametric description language; the hand-object poses come from a hand model and a grasp generator.
- **A dataset.** 19,664 human-screened demonstrations over 40 tasks, made by a planner (CuRobo) from sparse human "keyposes": 500 candidates per L0 and L1 task, then screening. L2 tasks and the semantic suite are left out of training on purpose (§3.3, §3.4). The authors give 1.8 minutes of human effort per task against 7.4 for teleoperation (Table 2).
- **An evaluation.** Eight VLA models (OpenVLA, OpenVLA-OFT, π0, π0.5, UniVLA, VLA-JEPA, GR00T N1.5 and N1.6) fine-tuned on the dataset, and two embodied reasoning models run zero-shot, on eight A800 GPUs. Ten trials per task, three seeds; the success rate counts only goal completion with no constraint violation, and any violation ends the episode (§4.1).
- **Results, physical track (Table 3).** Success rates differ widely and fall at L2. π0.5 reaches 35.3 to 83.3 per cent at L2 across the four suites; OpenVLA ranges from 0.0 to 22.0 per cent, with three cells above 12.7; π0 is below 21 per cent at L2. The text says π0.5 has the highest "overall" success rate across all suites and difficulty levels; in the table OpenVLA-OFT is higher in three of the twelve cells: grasping L1 (79.3 against 59.3), spatial avoidance L0 (65.3 against 58.0) and hand-object avoidance L0 (61.3 against 55.3) (our reading of Table 3).
- **Results, semantic track (Table 4).** Refusal rates of hazardous instructions: RoboBrain2.0-7B 80, 40 and 20 per cent at L0, L1, L2; RynnBrain-CoP 56, 72 and 36 per cent.
- **Scaling and perturbation (Tables 5 and 6).** Ten times more demonstrations per task (50 to 500) raised π0.5's success from 48.9 to 51.3 per cent and cut its collision rate from 12.7 to 10.0 per cent; the planner used as a privileged baseline reached 87.0 and 0.0. Under perturbations of the tabletop suite at L0, success stayed between 56.3 and 60.7 per cent against 58.0, while a changed object layout raised the collision rate from 2.7 to 6.3 per cent. The text names two different suites for Table 5.
- **Failure analysis (§4.4).** In a qualitative analysis without counts, the authors report that task failures are frequently decoupled from safety violations: policies time out, hover or run into joint limits, or grasp a look-alike distractor, collision-free.
- **A deployment-time filter (appendix).** The authors add a barrier filter that works on a whole action chunk: a quadratic program over the chunk keeps it close to the policy's output and smooth, with a distance-based barrier and slack variables, applied at each chunk boundary. Evidence is one real-robot case, a π0 policy placing a bowl on a plate with a fragile bottle in the way: unfiltered, the robot tipped the bottle; filtered, it went around. No counts, no benchmark figures for the filter.

## How

Simulation, with the benchmark's own tasks and its own dataset, so models are trained and tested by the same authors on the same task family; the semantic track is a static image and an instruction, answered or refused (§4.1).

## Limits

The authors say: the simulator approximates contact, soft bodies and friction; simulated humans lack the unpredictability of real ones; the renderer misses lighting changes, reflections and motion blur. They plan hierarchical designs that bridge slow semantic risk assessment and fast motor control, and uncertainty-aware filters that trigger "verified safe fallback maneuvers" (appendix E; the paper does not say what verifies them).

A careful reader adds:

- The benchmark scores policies. It does not score an external filter, and the paper reports no benchmark results for the chunk-level filter (it says the barrier is defined in the benchmark; whether it was run there is not stated), so the safety of a filtered policy is not measured here.
- A violation ends the episode and counts as failure, so the success rate mixes unsafe and unsuccessful. The collision rate is a supplementary metric.
- The filter's constraint is soft, since slack variables are penalised, although the text says it enforces forward invariance over the chunk. Our reading: the guarantee holds only where the slack is zero. The filter acts once per chunk; a hazard that appears mid-chunk is seen at the next boundary (our reading, from the receding-horizon description).
- Collisions are those of the simulator's geometry; the paper reports no contact forces.

## Against the wiki

- [VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md): **extends**. The paper's Table 1 lists the SafeLIBERO benchmark of that source as static, physical-safety only; LIBERO-Safety adds dynamic scenes, human proxies and a semantic track.
- [Control barrier functions](https://silentzero.ooo/wiki/concepts/control-barrier-functions.html.md): **extends**. A fourth barrier filter for VLA policies, and the first here that works on a whole chunk; its evidence is a single demonstration.
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md): touches. The filter is tied to chunk boundaries.
- [KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md), [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md): no conflict; they evaluate filters on moving hazards, this paper does not.

## For Silent Zero

[The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): no change of state. Our reading: the benchmark could serve as a test bed for a filter that sits outside the policy, but nobody has run one on it. [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): no timing figure for the filter.

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md)
- [Control barrier functions](https://silentzero.ooo/wiki/concepts/control-barrier-functions.html.md)
- [KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md)
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md)
- [VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md)
