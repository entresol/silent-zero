# RAVEL, rolling inference for flow-based VLAs

> RAVEL: rolling inference cuts the time to the first action by 2.6 to 2.9 times on one GPU; real-world dynamic tasks. measurement, full text.

Source · Chen et al. 2026 · LLM reviewed · updated 2026-11-22 · https://silentzero.ooo/wiki/sources/2026-chen-ravel-asynchronous-rolling.html

Yuhan Chen, Ke Yu, Pengfei Liu, Shuxun Wang, Yi Yang and Linchao Zhu (Zhejiang University, Nanyang Technological University). "RAVEL: Asynchronous Rolling Inference for Flow-Based Vision-Language-Action Models", arXiv 2609.34170v2 [cs.RO], 19 November 2026. A preprint. [arXiv](https://arxiv.org/abs/2609.34170). The main text and the appendix tables were read; the related work was skimmed.

## What it shows

- **The problem.** A flow-based vision-language-action (VLA) model has two delays before it can act: encoding the observation with the language model, and several denoising steps to produce a chunk. Synchronous inference waits for both (abstract, §1).
- **The method.** RAVEL is an asynchronous inference framework that changes the runtime and needs fine-tuning. It keeps a rolling buffer of partly denoised future actions, so the near-term action needs one more denoising step, and runs the slow encoding in parallel, reusing the latest context until it updates. A Fast Observation Pathway (FOP) feeds the action expert the current observation (abstract, §1, §3).
- **First-action latency.** Median time from observation to the first action on one RTX 4090: X-VLA 142.58 ms with full denoising against 54.97 ms rolling (2.59 times), π0.5 272.86 against 93.45 ms (2.92 times) (Table 1). Figure 1 is a schematic timeline with the labels 178.52 ms, 92.97 ms and "1.92x faster response"; it does not say which model or hardware it uses.
- **Simulation, synchronous.** On LIBERO and RoboTwin 2.0, where the simulator pauses during inference, RAVEL without FOP gets "comparable or slightly higher" success than the full-denoising baselines (§4.1); the plotted values are within about two points, and for one model on LIBERO the baseline is 0.1 point higher (our reading of Figure 3). These runs say nothing about latency benefits.
- **Simulation, dynamic.** On DOM, a dynamic benchmark from DynamicVLA, RAVEL reached 44.06 per cent overall success, 8.56 points above the best other method (CI & LAAS, 35.50), and 46.94 per cent with FOP (Table 2; 1,800 episodes). The authors ran the baselines locally: VLASH and FASTER were re-implemented by them and scored below the unmodified DynamicVLA base (18.78 and 23.78 against 26.06), and asynchrony is emulated in one process (appendix A.2).
- **Real robot.** Table-tennis return and conveyor-belt grasping, trained on 299 and 272 teleoperated trajectories, policy on an RTX 5090, 20 trials per method and task (§4.3). Success: RAVEL 75 and 95 per cent; RTC 0 and 0; VLASH 25 and 90; naive asynchronous 5 and 20; synchronous 0 and 0 (Table 3). Observation age, from receiving the source image to dispatching the action, median / 95th percentile: RAVEL 118 / 167 ms, synchronous 309 / 456, naive asynchronous 236 / 307, VLASH 244 / 331, RTC 465 / 641 (Table 3). The authors blame RTC's added update latency from vector-Jacobian products. On tennis-ball grasping the four methods lie at 40 to 45 per cent, and RAVEL has the lowest high-frequency oscillation and jerk (Table 4).

## How

First-action latency on one RTX 4090; the dynamic simulation on two RTX 4090 GPUs with simulator and policy on separate ones; real-world runs on an RTX 5090. Baselines differ by experiment: the base policy with full denoising on LIBERO and RoboTwin, DynamicVLA, CI & LAAS, VLASH and FASTER on DOM, synchronous, naive asynchronous, RTC and VLASH on the real robot. In the real-world runs synchronous, naive asynchronous and RTC use the task checkpoint as it is, while VLASH and RAVEL got further training steps on the same data (appendix B.2).

## Limits

The authors say (§5): it needs training aligned to streaming; the temporal-offset conditioning and FOP change the action expert, which differs between models; it is built for flow-based VLAs; its action latency cannot fall below one forward pass of the action expert; and the delay between a prediction and the physical execution remains and may reduce the benefit of FOP. Appendix B.3 says that observation age excludes physical execution and that smoothness metrics depend on motion speed, so slower motion scores better.

A careful reader adds:

- RTC scores 0 per cent on both dynamic tasks here but 40 per cent on tennis-ball grasping. The settings were chosen by the authors, so the zero says something about RTC under these settings, not about RTC in general.
- Success rates on the real robot compare a further-trained RAVEL with partly untrained-for-this baselines; with 20 trials per cell the intervals are wide.
- Latency is reported as medians and 95th percentiles on single consumer GPUs; neither is a worst case. Table 7 reports shares of actions over a 160 ms budget (2.52 and 11.39 per cent in the cases shown).
- It is a preprint.

## Against the wiki

- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md): **extends**. A second method, after FASTER, that shortens the time to the first action; it also reports observation age, a delay the page did not have.
- [FASTER, reaction time of flow VLAs](https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html.md): **extends**. RAVEL compares against FASTER on DOM, a benchmark from another paper; FASTER there scored below its own base policy under the authors' re-implementation, so the comparison says little about FASTER as its authors ran it.
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md): related. The RTC baseline did badly in the dynamic real-world tasks, under the authors' settings and with their explanation of RTC's update latency.

## For Silent Zero

[Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): no change of state. Our reading: the numbers show again that the learned side's delay differs by a factor of two to four between models and methods (Table 1: 1.9 times between the two models; observation age 118 to 465 ms between methods), and that its tail is reported only as a 95th percentile, not bounded; the loop below has to treat it as unbounded. [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): no change.

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md)
- [FASTER, reaction time of flow VLAs](https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html.md)
- [KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md)
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)
