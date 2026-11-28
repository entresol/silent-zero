---
type: source
id: 2026-agouzoul-understanding-asynchronous-inference
status: reviewed
read: partial
kind: measurement
sources: [2026-agouzoul-understanding-asynchronous-inference]
updated: 2026-11-28
---

# Agouzoul 2026: asynchronous inference methods for VLAs, compared

Ayoub Agouzoul (École polytechnique; Systems Group, ETH Zürich). "Understanding Asynchronous Inference Methods for Vision-Language-Action Models", arXiv 2605.08168v1 [cs.RO], 4 May 2026. A preprint. [arXiv](https://arxiv.org/abs/2605.08168). Read: the main text, sections 1 to 8. Not read: the appendices (method details, hyperparameters, per-environment plots, FLOP derivations) and the references. The claims below rest on the main text only.

## What it shows

- **Four methods, one test bench.** Under controlled conditions, the paper compares inference-time inpainting (IT-RTC, the real-time chunking of [[2025-black-real-time-execution]]), training-time delay simulation (TT-RTC), VLASH, which conditions the policy on a rolled-forward robot state, and A2C2, a small head that corrects each stale action at every control step (§1, §2.2). Until now they had different code bases, base policies and protocols; the author builds two unified code bases, one per benchmark (§3.1).
- **Delays beyond four steps.** Earlier work on asynchronous chunking has primarily evaluated delays up to d = 4 control steps, which is 80 ms at 50 Hz. The paper maps deployments to delay for π0 at 50 Hz, with latency estimates taken from another paper (Table 1): a local RTX 4090 gives d = 1, a Jetson Thor d = 2, a B100 edge server over 4G d = 3 and a slow cloud server (B100, 4G, slow cloud) d = 13 (§2.3). It sweeps delays up to 15 (Kinetix) and 20 (LIBERO).
- **Kinetix, small MLP policies, 10 environments.** At chunk length 16, A2C2 stayed above 90 per cent solve rate up to d = 8, where the naive baseline fell below 40 per cent. IT-RTC barely improved on naive at high delay with chunk length 30; TT-RTC with a wide training maximum overtook it (§4.1, Figures 1 and 2). TT-RTC was largely insensitive to the training maximum of the delay, VLASH was not: a wider range helped at high delay and cost accuracy at low delay (§4.2).
- **LIBERO, SmolVLA, chunk length 50.** The ranking changed. At d = 0 IT-RTC led (about 75 per cent success), then A2C2 (about 70), and VLASH and TT-RTC lay between 57 and 61. The naive baseline fell from about 61 to about 10 to 12 per cent at d = 20; IT-RTC from about 75 to about 20; TT-RTC from about 57 or 60 to about 33 or 25, depending on its training maximum. A2C2 led from d = 4 and slipped to about 58 at d = 20, while VLASH with wide training ranges stayed near 55 to 56 (§5, Figure 4; the numbers are the authors' readings of the figure).
- **Cost.** On LIBERO the vision-encoder prefill is 89.8 per cent of a chunk's computation, so IT-RTC's tripled denoising loop brings a chunk's cost to 1.20 times the naive cost; A2C2 with 50 residual calls per chunk brings it to 1.75 times (§6, computation, not latency). Measured on one RTX 3090 for one observation: naive 405.2 ms per chunk, TT-RTC 402.7, IT-RTC 469.7 (+15.9 per cent), A2C2 in series 412.4 (+1.8 per cent; one base call plus one residual call of 7.27 ms, not the 50 calls behind the 1.75 times) (Table 2, 100 timed runs).
- **The authors' advice.** IT-RTC as a drop-in if retraining is impossible and delay is low; TT-RTC if fine-tuning is possible and chunks are short (on LIBERO with chunk length 50 it degraded substantially); A2C2 for long chunks; VLASH if an accurate forward state model exists and an expected delay range can be fixed at fine-tuning (§8).

## How

Policies were evaluated in simulation. Kinetix uses an MLP-Mixer of about 310,000 parameters, trained from PPO experts' data, and 2,048 parallel rollouts per setting. LIBERO uses SmolVLA fine-tuned from a public checkpoint, 40 tasks, 10 rollouts per task and setting. Delay is simulated by feeding the policy the observation from d steps earlier; for A2C2 observations stay current and staleness is simulated on the actions (§3.2). Kinetix runs and LIBERO training used H100 GPUs, LIBERO evaluation RTX 3090 GPUs.

## Limits

The authors state these (§3.2, §7).

- VLASH on LIBERO uses ground-truth future states from the demonstrations, an advantage a deployed system would not have; its LIBERO results are, in the authors' words, to be read as an upper bound; a privileged variant on Kinetix tracked the standard one closely, which the authors call not conclusive (§5).
- Delay is a fixed integer; real delay varies with scheduling and network jitter.
- Hyperparameters come from the original papers and were not retuned.
- Time to solve was not reliable in simulation, and no physical robot was used; the authors say robots will be required for firm conclusions about energy, time to solve and overall efficiency (§7).

A careful reader adds the following (inference).

- Both benchmarks are simulations, and the Kinetix and LIBERO rankings differ; no single ranking carries over. The paper's absolute LIBERO success rates (below 80 per cent even at d = 0) belong to this SmolVLA checkpoint.
- It reports means of success, with confidence intervals only on Kinetix; the LIBERO figures have no intervals in the main text.
- The paper does not bound delay. It sweeps fixed delays, so a late chunk beyond the sweep is untested.

## Against the wiki

- [[action-chunking]]: **extends**. The page lists RTC, FutureRTC and three fine-tuning answers, each against RTC; this source compares RTC's two variants with two more methods under one protocol, and finds the inference-time one, among the four methods, weak at long chunks and high delay in its settings; on LIBERO it falls close to the naive baseline beyond d = 8.
- [[2025-black-real-time-execution]]: **extends**, no conflict. That paper measured RTC on real robots with π0.5 up to 200 ms of extra delay; this one ran it in simulation, on LIBERO in a reimplementation and on Kinetix in an extended original framework, with other policies. The two do not test the same thing.
- [[2026-jiang-futurertc-real-time]], [[2026-wang-real-time-robot]]: related. FutureRTC also sweeps delays of 5 to 20 steps on LIBERO, with SmolVLA among its policies, and adds a real robot; REMAC's simulation covers delays of 0 to 4 steps, and its real arm ran at an end-to-end delay of about 122 to 140 ms.
- [[real-time-loops]]: **extends**, see below.

## For zOS

[[real-time-loops]]: no change of state. Our reading: the source adds to the open question of what the lower loop does with late chunks. Whatever method the learned side uses, its output is a chunk that was computed from an observation d steps old, and most methods lose success at high delay, some only slightly (wide-range VLASH, which has privileged states, and TT-RTC on Kinetix stay nearly flat). The loop below cannot assume the chunk is fresh, which fits the paper's view that an agent's proposals are untrusted and a small loop has the last word. Nothing in zOS is built on this source.
