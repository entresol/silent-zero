# FASTER, reaction time of flow VLAs

> FASTER: a flow policy that samples its first action in one step to shorten reaction time; measured on two consumer GPUs and one real arm. measurement, partly read.

Source · Lu et al. 2026 · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html

Yuxiang Lu, Zhe Liu, Xianzhe Fan, Zhenya Yang, Jinghua Hou, Junyi Li, Kaixin Ding and Hengshuang Zhao (The University of Hong Kong; ACE Robotics). "FASTER: Rethinking Real-Time Flow VLAs", arXiv 2603.19199v3 [cs.RO], 16 May 2026. A preprint. [arXiv](https://arxiv.org/abs/2603.19199). Read: the main text and appendices B, C, D.1, D.2, E.1, E.3, E.4, F, G and H. Not read: appendix A (related work), D.3 (algorithms), most of E.2, Table 5 and the references. No claim on this page rests on the unread parts.

## What it shows

- **Reaction time besides smoothness.** Asynchronous inference methods such as real-time chunking (RTC) fix pauses between chunks and smooth the motion, but the authors say they overlook how fast a robot reacts to a sudden event (introduction, §2). They model reaction time as uniformly distributed between the inference latency and the latency plus the inference interval. In expectation, going from synchronous to asynchronous inference saves only half the inference latency, a gain §2 calls "potentially limited" (§2, Table 1). This rests on a simplified model, see Limits.
- **A new metric.** Time to First Action (TTFA) is the time until the robot can start to move. Reaction depends on it, because the robot does not need the whole chunk to begin (§2).
- **The method.** Flow-based policies normally denoise all actions of a chunk with the same schedule, so no action can be sent before the last denoising step. In a pilot study on π0.5 fine-tuned on the authors' tasks, the first one to ten actions of a chunk showed straighter denoising paths and smaller estimate changes (§3.2, Figure 3). FASTER, with a Horizon-Aware Schedule, finishes near-term actions earlier, so the first action needs one denoising step. Fine-tuning mixes the new and the constant schedule, and a streaming client-server interface sends actions as they are finished (§3.3). With the first action ready, the remaining sampling can stop early once the execution horizon is done, which allows a shorter execution horizon (§3.3).
- **Latency figures.** At 30 Hz control, on an RTX 4090 and an RTX 4060, TTFA for π0.5 fell from 80.0 to 62.1 ms and from 303.3 to 238.6 ms. For X-VLA it fell from 113.7 to 44.8 ms and from 399.5 to 129.2 ms (Table 2). Expected reaction time on the RTX 4060 fell from 470.0 to 371.9 ms for π0.5 and from 599.5 to 229.2 ms for X-VLA, against the asynchronous baseline (Table 2). The "tenfold" in the abstract and Figure 1 concerns the sampling of the first action (76.7 ms down to 7.8 ms in the figure). The end-to-end TTFA gain is 1.27 to 3.09 times. Our reading: this is because the vision-language prefill (22.4 ms in Figure 1) is unchanged, which §3.3 supports, since it gives TTFA going from ΔtVLM + NΔtAE to ΔtVLM + ΔtAE. Figure 1's hardware is not named, and 22.4 + 76.7 = 99.1 ms does not match Table 2's 80.0 ms for π0.5 on the RTX 4090.
- **Probability of a faster reaction.** For π0.5 the chance that a sampled reaction is faster than the asynchronous baseline's was 0.66 on the RTX 4090 and 0.77 on the RTX 4060. For X-VLA it was 1.00, since FASTER's upper bound lies below the baseline's lower bound (§4.1, Table 3; appendix F.1 gives 111.5 against 113.7 ms and 329.2 against 399.5 ms).
- **Real robot, dynamic task.** A table-tennis task on a 6-DoF Piper arm (AgileX Cobot Magic), fine-tuned on about 14 minutes of teleoperated data, about 15 trials per method (our inference; appendix E.1 says 15 trials for Table Tennis) (§4.2, appendix E). The scores below are for π0.5; X-VLA results exist (Figure 11, appendix F.2), where the authors say FASTER is "better or comparable" and naive asynchronous inference "often" fails. Completion scores on the RTX 4090: synchronous 0.00, naive asynchronous 0.20, Training-time RTC 0.53, FASTER 0.80. On the RTX 4060: 0.00, 0.20, 0.30, 0.47 (Figure 5, Table 8; the 96 per cent bootstrap intervals overlap for some pairs, for example FASTER and Training-time RTC on the RTX 4060). On that card inference ran at about 3 Hz (§4.2). The real-robot delay d and execution horizon s in Table 6 are slightly larger than the Table 2 minimums (table tennis, FASTER: s = 4 against 5 on the RTX 4090; s = 10 against 11 and d = 8 against 10 on the RTX 4060), so the real-robot gain is smaller than Table 2 suggests.
- **Slower tasks.** Pick Beverage and Fold Towel with π0.5: scores for FASTER were 0.957 and 0.963, against 0.950 and 0.888 for Training-time RTC. Durations were close to Training-time RTC's, 12.0 against 11.9 s and 20.5 against 20.7 s. Synchronous inference was slowest (Figure 6, Table 9; 35 and 10 trials). The authors call these results better or comparable.
- **Cost in simulation.** On LIBERO the average success for π0.5 moved from 96.9 to 96.5 per cent with FASTER, for X-VLA from 98.0 to 97.1. On CALVIN ABC to D the average chain length moved from 4.313 to 4.292 for π0.5 and from 4.151 to 4.093 for X-VLA (appendix F.3, Table 10). Per suite, X-VLA with FASTER fell on LIBERO-10 from 96.8 to 93.0 and at CALVIN step 5 from 70.2 to 64.5 (Table 10); the X-VLA baseline is marked ∗ (the authors' cluster, official checkpoints), and X-VLA used α = 0.7. A high mixing probability p (0.7 and 1.0) is much worse (Table 13: average length 3.206 and 3.112 against 4.093 at p = 0.5), so the slight cost depends on the mixed schedule (§3.3, appendix F.4). The authors say FASTER may slightly affect long-horizon accuracy. On the Kinetix benchmark, with a policy that is "a simple 4-layer MLP rather than a VLA model" (appendix E.2), the table gives a solve rate: 0.869 for FASTER at d = 1, s = 4 against 0.492 to 0.813 for baselines at d = 4 (appendix F.3, Table 11).

## How

FASTER changes how a flow policy is fine-tuned and sampled and leaves its architecture alone. It was applied to π0.5 and X-VLA. Latency was measured on an RTX 4090 and an RTX 4060 with the robot control frequency set to 30 Hz and the execution horizon at its minimum (§4.1). Real-robot tests ran on the AgileX platform with the policy on a server; simulation used LIBERO, CALVIN and Kinetix. The method follows RTC, with the overlapping actions as a prefix condition (§2).

## Limits

The authors state the following (appendix G, §2 and the real-world sections).

- It applies to flow or diffusion policies with iterative sampling. The speed-up depends on implementation and hardware; in JAX the runtime was not always proportional to the number of iterations.
- It is an inference-scheduling method. It does not repair perception failures, language grounding errors or wrong actions of the base policy.
- The reaction analysis lumps sensing, communication, pre-processing, inference and dispatch into one constant latency. Real latency can vary with scheduling, network jitter, memory contention and OS overhead.
- The schedule trades some accuracy for responsiveness, especially for tasks needing precise long-horizon coordination.
- A more reactive robot can make failures more severe. The authors do not recommend deployment in safety-critical or unsupervised human-facing settings without risk assessment, safety monitors and physical safeguards (appendix H).
- The experiments were in controlled research settings.

A careful reader adds the following (inference).

- The real-robot counts are small: 15 trials on the table-tennis task and 10 on Fold Towel, with wide intervals for some of the pairs.
- The study compares FASTER with Training-time RTC; the table-tennis scores are the authors' own task and scoring. There is no test against a worst-case delay, only a mean-latency model.
- Reaction time is modelled from inference latency and call interval, and Table 4 times run from the start of inference; camera capture and actuator response are not measured. The time to stop a motion is not measured either, and that remains an inference.
- Faster first actions come from a one-step estimate of near-term actions. The paper gives no bound on how far such an action can stray from the full sampling, only task scores and open-loop error maps (appendix F).

## Against the wiki

- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md): **extends**. The page says chunking costs reactivity and that RTC fixes pauses; this source adds that the reaction delay stays and is set by TTFA and the execution horizon (§2, Table 1). Its model gives a range for reaction time and assumes one constant latency, so it yields no bound.
- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): **extends**. A lower loop that takes chunks from a slow model should expect the first action after TTFA, then more actions streaming in. Appendix D.2 gives only a sufficient condition: the robot is not interrupted as long as the next action arrives within one control period. Our reading: when it does not, the buffer can run dry; the paper supplies no rule for what to do then.
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md): **extends**, no conflict. This source builds on RTC and its training-time variant and measures a gap RTC leaves, reaction latency. It reports synchronous execution as the worst on its tasks, in line with the earlier page.
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md): related. The shield there runs at a fixed step beside a policy call of 177.3 ms; this source shows ways to shorten the time to the first action of such a policy. Our reading: neither paper treats the other's problem.

## For Silent Zero

[Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): no change of state. Our reading: the source models reaction time as a range uniform between the inference latency and the latency plus the call interval, under a constant-latency assumption, and says real latency may vary (appendix G). Our reading: the range can have a long upper end, so the Silent Zero loop cannot count on a learned side to react to a sudden event within a known time; reflexes belong in the loop below. It is measurement on commodity GPUs and no proof. [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): no change; the authors themselves ask for safety monitors and physical safeguards around such policies. Nothing in Silent Zero is built.

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md)
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md)
- [RAVEL, rolling inference for flow-based VLAs](https://silentzero.ooo/wiki/sources/2026-chen-ravel-asynchronous-rolling.html.md)
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)
- [REMAC, masked action chunking](https://silentzero.ooo/wiki/sources/2026-wang-real-time-robot.html.md)
