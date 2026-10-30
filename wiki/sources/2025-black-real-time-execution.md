---
type: source
id: 2025-black-real-time-execution
status: reviewed
read: full
kind: measurement
sources: [2025-black-real-time-execution]
updated: 2026-10-29
---

# Black, Galliker and Levine 2025: Real-Time Execution of Action Chunking Flow Policies

Kevin Black, Manuel Y. Galliker and Sergey Levine (Physical Intelligence, UC Berkeley). NeurIPS 2025; read in arXiv version 2 of 5 December 2025. [arXiv](https://arxiv.org/abs/2506.07339).

## What it shows

- **The problem.** Large robot models are slower than the control loop. The 3-billion-parameter π0 spends 46 ms, with an RTX 4090, on the KV-cache prefill alone, before any denoising step, at a target rate of 50 Hz (20 ms per step); an optimised 7B OpenVLA takes 321 ms on an A100 (§2). *Action chunking*, where the model emits a sequence of actions per call, "does not fully address the latency problem, leading to pauses or out-of-distribution jerky movements at chunk boundaries" (abstract). See [[action-chunking]].
- **The method.** Real-time chunking (RTC) generates the next chunk while the current one executes. It freezes the actions that will run during inference and fills in the rest consistently with the previous chunk, by guided inpainting with soft weights (§3). It needs no retraining and works with diffusion and flow policies (abstract).
- **Simulation.** Across 12 dynamic tasks in the Kinetix simulator, RTC is the most robust method as inference delay grows (Figure 5).
- **Real robots.** RTC kept its task throughput on two 6-DoF arms with π0.5 at 50 Hz, even with up to 200 ms of extra injected delay. Model latency was 97 ms for RTC, plus 10 to 20 ms of network. Synchronous chunking, which pauses while the next chunk is computed, degraded linearly. Temporal ensembling oscillated so much at +100 and +200 ms that the robot's protective stop triggered (§4.2). The evaluation covers 480 episodes, 28 hours of robot time.
- **Match lighting.** In the most precision-sensitive task, RTC achieved a markedly higher score (§4.2, Figure 1).

## How

An inference-time algorithm, evaluated in simulation with 2,048 rollouts per data point and on six real bimanual tasks with ten trials per task and method. The model runs remotely over a LAN, and the robots use position control (§4.2).

## Limits

The authors state (§6): RTC adds "significant computational overhead"; it applies only to diffusion and flow policies; legged locomotion is simulated, not tested on real robots.

A careful reader adds:

- **"Real-time" here is not hard real time.** The authors define a system as real-time if it is "guaranteed to produce a response ... within a fixed time constraint" (§2), but the guarantee holds only while the inference delay stays within the chunk's slack, and the delay is estimated from past delays (Algorithm 1). Nothing bounds it.
- **A lower loop does the actual control.** The real robots use position control (§4.2). The authors note that such policies are "often used in conjunction with" a faster loop, such as a PID controller, call this cascade control and leave its analysis to future work (§5).

## Against the wiki

- [[action-chunking]]: created with this source.

## For zOS

- [[real-time-loops]]: the paper (Section 2.4) says action models emit commands in chunks so a robot can hold a 50 Hz control rate while the slower model thinks, citing this source. Partly confirmed: π0.5 runs at 50 Hz with about 100 ms of model latency, but chunking alone pauses while the model thinks; holding the rate needs asynchronous execution such as RTC. Our reading: the paper's sentence credits chunking with what RTC adds.
- Our reading: this is strong evidence for the paper's split. The learned model cannot meet the loop's deadline and does not try; it delivers chunks early, and a lower loop executes them on time. zOS puts the guarantee into that lower loop and treats chunk arrival as untrusted and possibly late. The protective stop that caught the oscillations is the kind of safety function zOS wants on the motion path, verified.
