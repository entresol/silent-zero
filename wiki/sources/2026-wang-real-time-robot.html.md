# REMAC, masked action chunking

> REMAC: masked fine-tuning so a chunking policy copes with delay; beats RTC on one real arm; needs a maximum delay fixed in advance. measurement, full text.

Source · Wang et al. 2026 · LLM reviewed · updated 2026-11-22 · https://silentzero.ooo/wiki/sources/2026-wang-real-time-robot.html

Haoxuan Wang, Gengyu Zhang, Yan Yan, Yuzhang Shang, Ramana Rao Kompella and Gaowen Liu (University of Illinois Chicago, University of Central Florida, Cisco Research). "Real-Time Robot Execution with Masked Action Chunking", arXiv 2601.20130v1 [cs.RO], 27 January 2026; the PDF is marked as published at ICLR 2026. [arXiv](https://arxiv.org/abs/2601.20130).

## What it shows

- **A second failure of asynchronous chunking.** Asynchronous inference lets the next chunk be computed while the current one runs. Earlier work blamed failures on inter-chunk discontinuity. The authors add intra-chunk inconsistency: with an inference delay of d steps, the first d actions executed come from the previous chunk and were chosen for an older observation (§3).
- **The method.** REMAC fine-tunes a pretrained flow policy so that it knows the delay d. It masks the first d actions in the loss (prefix masking), mixes the pretrained policy's own predictions into the training input on a schedule (self-conditioned curriculum), and adds a residual term; a prefix-preserved sampling step keeps the executed actions as a prior (§4). It uses LoRA adapters of at most 1.5 per cent of the model's parameters, which are merged into the backbone afterwards, so that no inference time is added (§4.3, model adaptation).
- **Simulation.** On 12 Kinetix tasks, with delays d of 0 to 4 and a prediction horizon of 8, REMAC beat naive asynchronous execution, bidirectional decoding and RTC in solve rate under all delay settings and had shorter average execution time (Figure 2); the text says the gains are especially pronounced at larger delays.
- **Real robot.** A Franka Research 3 arm with π0, prediction horizon 50, control at 15 Hz (period about 67 ms), execution horizon 8. The model ran on a server over a LAN. Pure model time was 76 to 80 ms, network 34 to 40 ms, processing and disk writing 10 to 20 ms: an end-to-end delay of roughly 122 to 140 ms, d = 2 or 3. On three grasp-and-place tasks, average completion progress for REMAC was 0.903, 0.943 and 0.812 (easy, medium, hard), against 0.823, 0.848 and 0.753 for RTC and 0.805, 0.718 and 0.670 for synchronous inference (Table 3; 30 trials per task and method). The baseline description says RTC adds 55 to 64 ms of inference latency on this setup; no measurement of it is shown in the text read, and the authors give it as a cause of RTC's weaker score.
- **More delay.** With 75 ms and 150 ms of injected delay, REMAC stayed ahead on the hard task; the paper notes that naive asynchronous execution does comparatively better at larger delays and that RTC degrades significantly, which the authors attribute to longer execution horizons at larger delays and adverse effects of RTC's test-time adjustments (Figure 4, grasp-hard task only).
- **Wrong delay values.** In simulation the true delay was fixed and the policy was given wrong values: off by one in two thirds of the calls, and in 10 per cent of the calls the largest valid value (appendix F, Table 7). The authors call the degradation of both graceful and say REMAC under corrupted delays still beats RTC under accurate ones. At d = 4 REMAC scores 0.757 under noise and spikes against 0.575 for RTC; at d = 0 REMAC falls from 0.877 to 0.820 while RTC falls from 0.817 to 0.814, so REMAC's margin there is 0.006. A real-robot test with the delay input drawn from d−1 to d+2 cost one or two more failures in ten trials; the authors call these a timeout artifact from pauses after overestimated delays (appendix F).

## How

REMAC changes training, not the network. Evaluation used the Kinetix benchmark in the protocol of the RTC paper and one real arm, against synchronous, naive asynchronous, temporal-ensembling and RTC baselines. The bidirectional-decoding baseline is left out of the real-world runs as too slow.

## Limits

The authors say (appendix G):

- The method needs a maximum inference delay specified in advance; if the real delay exceeds it, "unexpected failure may occur". The paper is not consistent here: §4.3 and appendix E say the training bounds qmax and qmin are "not limits" on the delays the model can handle but settings for the strength of the masking, and that the chosen qmax = 4 should not be read as limiting the range.
- The masked fine-tuning may need a substantial amount of data.

A careful reader adds:

- The real-robot results are 30 trials per cell on three tasks of one arm and one policy; no confidence intervals are given in the text read.
- The delay is estimated on the client as the maximum of the latest measured delays (§3, deployment framework; appendix F says it follows RTC). That is an estimate from history, not a bound.
- The 55 to 64 ms of RTC latency is a statement in the baseline description and the authors' explanation of RTC's weaker real-world score, so part of REMAC's advantage there comes from RTC's added delay, not only from the method. At about 67 ms a step it is about one step of delay.
- Our arithmetic: with d = ⌊δ/Δt⌋ and Δt about 67 ms (§3), a delay of 122 to 140 ms gives d = 1 or 2, while the experiments say d = 2 or 3; the text does not explain the difference, and §3 says observation latency is left out of d.
- Real-world adaptation used 200 trajectories, the data need the authors name as a limit.
- The paper's own definition leaves out observation latency and sub-step delays (§3), so its d is not the delay from sensor to motor.

## Against the wiki

- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md): **extends**. The page says RTC fixes pauses and that the delay is not bounded; this source adds a second failure mode, trains the policy to take the delay as an input, and states the same limit in its own words: a fixed maximum delay.
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md): **extends**, no conflict. This paper states that RTC adds 55 to 64 ms of latency in its setup and finds RTC behind REMAC on its tasks; it does not repeat the earlier paper's measurements.
- [FASTER, reaction time of flow VLAs](https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html.md): related. Both treat what a robot does with a late chunk and neither gives a bound.

## For Silent Zero

[Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): no change of state. Our reading: the authors say failure outside the trained delay may occur, though the paper does not test it and also says the bounds are not limits; that is a further reason why the loop below must define what it does when a chunk is late. [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): no change. It is measurement on one arm; nothing is proven.

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md)
- [FASTER, reaction time of flow VLAs](https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html.md)
- [Legato, native continuation for chunked policies](https://silentzero.ooo/wiki/sources/2026-liu-learning-native-continuation.html.md)
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)
