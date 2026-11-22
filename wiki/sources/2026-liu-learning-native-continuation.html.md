# Legato, native continuation for chunked policies

> Legato: continuation between chunks trained into the policy; 14 to 23 % faster than RTC on five dual-arm tasks, in its own runs. measurement, partly read.

Source · Liu et al. 2026 · LLM reviewed · updated 2026-11-22 · https://silentzero.ooo/wiki/sources/2026-liu-learning-native-continuation.html

Yufeng Liu, Hang Yu, Juntu Zhao, Bocheng Li, Di Zhang, Mingzhu Li, Wenxuan Wu, Yingdong Hu, Junyuan Xie, Junliang Guo, Dequan Wang and Yang Gao (Shanghai Jiao Tong University, Spirit AI, Tsinghua University and others). "Learning Native Continuation for Action Chunking Flow Policies", Robotics: Science and Systems 2026, Sydney, 13 to 17 July 2026. [Paper](https://roboticsproceedings.org/rss22/p058.pdf). The 11-page PDF ends at the references; the appendix the paper refers to for task, metric and trial details is not part of it, so the page reads `partial`, and no claim here rests on the missing part.

## What it shows

- **The claim about RTC.** Real-time chunking (RTC) applies its continuation only at inference time, by inpainting. The authors say it "alleviates" discontinuities but, being external to the policy, leads to "spurious multimodal switching" across chunk boundaries: the policy alternates between competing grasp goals or arms from chunk to chunk, shown as hesitation and slower tasks (abstract, §I, Figure 6).
- **The method.** Legato is a training-time method for chunked flow policies. Denoising starts from a schedule-shaped mixture of known actions and noise; the learned velocity field is reshaped so that training and inference agree under guidance applied before every denoising step (§III). Guidance against the previous chunk is still applied at inference. Randomised schedule parameters in training let one policy handle several inference delays and set how smooth the motion is (§III).
- **Real robot.** A dual-arm robot, five tasks (stack bowls, pour, put items in a box, fold a towel, open a drawer), a cutoff of 120 s, both methods fine-tuned from the same π0.5 checkpoint on the same data (§IV-A). In Table I Legato has the shorter completion time on all five tasks, by 14 to 23 per cent (our arithmetic from the table: for example 75.73 against 95.07 s on pour, 20.00 against 25.93 s on the towel), and a lower NSPARC, a smoothness metric, on all five (by 9 to 42 per cent). The abstract summarises this as "approximately 10%" improvements in smoothness and completion time. Task scores are slightly higher; most differences lie within about one standard error (for example drawer 9.50 against 9.20, pour 9.72 against 9.34, both a little outside it) (Table I).
- **Against training-time RTC.** On the pour task Legato beat the authors' own implementation of a training-time RTC: 75.73 against 81.73 s, NSPARC 1.65 against 2.46 (§IV-C, Table II).
- **Other models and delays.** On the pour task Legato also outperformed RTC with π0 and GR00T N1.6 (§IV-D4, Table V), and in the Kinetix simulator when the delay was above zero, shown in a plot (§IV-E). A schedule ablation shows a trade-off between overlap consistency and smoothness (Figure 7).

## How

Controlled comparison: same checkpoint, datasets, hyperparameters and training steps for RTC and Legato, both run by the authors. Metrics are task score, completion time, NSPARC, NLDLJ (a jerk measure) and the error between the overlapping parts of consecutive chunks (§IV-A). Trial counts are not in the PDF.

## Limits

The authors say: the number of denoising steps is fixed at training time, which limits changing it at inference (§V). The model condition row makes Legato unstable at one denoising step and worse at three; they use a heuristic rescaling and recommend a variant without the row for variable step counts (§IV-D6, Table VII, §IV-F). If the randomised delay range in training does not include zero, the policy is out of distribution and fails almost completely, and fixing the delay in training hurts other delays (§IV-E). Excessive guidance training can impair reactivity, and smaller strides reduce whole-trajectory smoothness (§IV-D1, §IV-F). The NLDLJ gains do not reach significance on all tasks, which the authors explain by NLDLJ being dominated by motion outside the overlap (§IV-B).

A careful reader adds:

- All real-world results come from one lab's dual-arm platform; π0.5 was tested on all five tasks, π0 and GR00T N1.6 on pour only.
- The delay in deployment is the maximum of recent delays (§IV), an estimate from history.
- The cause given for RTC's weaker result is supported by an analytic argument and trace examples, not by a count of switches in the text read. The text says overlap RMSE falls "across tasks"; on the drawer task it falls from 12.11 to 11.74, within the errors.
- The comparison with RTC is on the authors' tasks and with their own runs of RTC.

## Against the wiki

- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md): **extends**. The page gives RTC's measured result; this source claims a residual flaw (mode switching) and a fine-tuning remedy, on its own tasks.
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md): **challenged on one point by a rival method**. The Legato authors credit RTC with alleviating boundary discontinuities and claim a remaining weakness; they dispute none of Black et al.'s measurements.
- [REMAC, masked action chunking](https://silentzero.ooo/wiki/sources/2026-wang-real-time-robot.html.md): related. Another training-time answer to the same problem with a different diagnosis.

## For Silent Zero

[Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): no change of state. Our reading: the failure when the delay range in training excludes the delays met in use (§IV-E) is one more reason for the lower loop to define what happens when a chunk is late or off-model; the authors' remedy fixes a range chosen in advance. [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md): no change.

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md)
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)
- [REMAC, masked action chunking](https://silentzero.ooo/wiki/sources/2026-wang-real-time-robot.html.md)
