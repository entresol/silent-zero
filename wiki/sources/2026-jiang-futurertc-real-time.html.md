# FutureRTC

> FutureRTC: an adapter that predicts the inputs of the next action chunk to tolerate inference delay; preprint. measurement, full text.

Source · Jiang et al. 2026 · LLM reviewed · updated 2026-11-05 · https://silentzero.ooo/wiki/sources/2026-jiang-futurertc-real-time.html

Hai Jiang, Yixian Zou, Binbin Liang, Boqian Liu, Fanman Meng and Shuaicheng Liu (Sichuan University, University of Electronic Science and Technology of China, University of Alberta). arXiv 2607.24008, version 1 of 27 July 2026, a preprint. [arXiv](https://arxiv.org/abs/2607.24008). Read in full; the numbers of the real-world figures are garbled in the text extraction and are not quoted here.

## What it shows

- **The problem.** Asynchronous execution of a vision-language-action policy computes the next action chunk while the current one runs. The chunk is then based on a stale observation, which shows as discontinuities at chunk boundaries (abstract; Introduction). See [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md).
- **The method.** FutureRTC is an adapter that leaves the policy unchanged. A state module corrects the rolled-forward robot state, and an observation module predicts the visual features at execution time from the stale observation, the committed actions and the corrected state, using the robot's motion as a physical prior. A consistency loss aligns the chunks produced from predicted inputs with those produced from the true inputs (abstract; method section).
- **Simulation.** On LIBERO with π0.5 and SmolVLA-450M and delays of 5 to 20 control steps, the authors report the highest success rate and the fewest execution steps at every delay and for both backbones. Success falls by 5.7 points (π0.5) and 6.4 points (SmolVLA) from 5 to 20 steps of delay (Table 1). On Kinetix, the benchmark of [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md), delays run from 0 to 4 steps (Figure 5); there the authors say the method trails several training-time methods at delays of 0 and 1 and takes fewer steps only from a delay of 2.
- **Cost.** The adapter adds 6.45 million parameters and 3.64 ms of inference latency to π0.5, and 5.19 million and 3.04 ms to SmolVLA (Experiments, ablation and appendix).
- **Real robot.** A dual-arm AgileX Cobot Magic with π0.5 at 30 Hz, a 99 ms forward pass, about 40 ms of network and 30 ms of processing, an end-to-end latency near 170 ms (a delay of about 5 steps), and a second setting with 150 ms added (Real-World Evaluation, setup). The authors report smoother trajectories, faster execution and higher success on three tasks.

## How

Training of the adapter samples the delay at random per step, so no retraining per delay is needed. Simulation uses LIBERO and Kinetix, the real-robot test uses three manipulation tasks (Stack Plates, Fold Towel, Hang Cups).

## Limits

The authors state three limits (Limitations). The observation module relies on the robot being the main source of change and may struggle in scenes dominated by other moving agents. It is built for flow-matching policies with latent-space prediction. More extreme delays are future work. A careful reader adds that the comparison runs against other chunking methods, not against any bound on the delay, and that the work is a preprint.

## Against the wiki

- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md): **extends** the state with a further method that tolerates delay by predicting the inputs, next to real-time chunking. The page's remark that no scheme bounds the delay still holds: the paper measures robustness over delays up to 20 steps in simulation and does not bound the delay.
- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): confirms that the model side is built to tolerate late chunks, with no guarantee.

## For Silent Zero

[Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): no change of state. Our reading: the paper makes the case for the Silent Zero split again. The learned part hides latency better, its guarantee stays statistical, and the loop below it must not rely on it.

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md)
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)
