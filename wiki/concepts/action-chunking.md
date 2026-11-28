---
type: concept
status: reviewed
sources: [2025-black-real-time-execution, 2025-google-building-next-generation, 2026-jiang-futurertc-real-time, 2026-lu-faster-rethinking-real, 2026-wang-real-time-robot, 2026-liu-learning-native-continuation, 2026-chen-ravel-asynchronous-rolling, 2026-agouzoul-understanding-asynchronous-inference]
glossary: Action chunking
updated: 2026-11-28
---

# Action chunking

A learned robot policy emits a sequence of future actions for each call, a *chunk*, and the robot executes several of them before the next call. This keeps motion consistent over time, but it costs reactivity, and switching between chunks can cause pauses or jumps; on its own it "does not fully address the latency problem" ([[2025-black-real-time-execution]], abstract, §1, §2).

## State, October 2026

Real-time chunking (RTC) computes the next chunk while the current one runs and makes it consistent with the actions that will execute in the meantime. With π0.5 at 50 Hz and model latencies around 100 ms, it held task throughput under up to 200 ms of extra delay, where synchronous chunking degraded ([[2025-black-real-time-execution]]). FutureRTC, a 2026 preprint, takes another route: an adapter predicts the observation and state at the moment the chunk will run, so the policy plans from them instead of from stale inputs. On the LIBERO benchmark it lost 5.7 to 6.4 percentage points of success between delays of 5 and 20 control steps, and on a real dual-arm robot it was tested at delays near 5 and 10 steps ([[2026-jiang-futurertc-real-time]]).

Three 2026 papers fine-tune the policy for asynchronous execution; RAVEL also changes the runtime, and Legato still guides each chunk by the previous one at inference. REMAC adds a second failure to the discontinuity between chunks: the first actions executed come from an earlier chunk and fit an older observation. It fine-tunes the policy with masked chunks so that it takes the delay as an input, and on a real arm at 15 Hz with an end-to-end delay of about 122 to 140 ms it beat RTC on its tasks; its authors say a maximum delay must be specified in advance and also that the training bounds are not limits; the 55 to 64 ms of extra latency it attributes to RTC is a statement, not shown as a measurement ([[2026-wang-real-time-robot]]). Legato argues that RTC's inference-time inpainting leads to spurious switching between grasp goals and arms, and trains the continuation into the policy; on five dual-arm tasks it finished faster than RTC, by about 10 per cent in the authors' summary and by 14 to 23 per cent in their Table I (our arithmetic), with its own runs of RTC ([[2026-liu-learning-native-continuation]]). RAVEL keeps a rolling buffer of partly denoised actions and cut the median time to the first action by a factor of 2.6 to 2.9 on one GPU; on its two dynamic real-world tasks (20 trials each) RTC reached 0 per cent success under the authors' settings ([[2026-chen-ravel-asynchronous-rolling]]). REMAC and Legato appeared at ICLR and RSS 2026 and RAVEL is a preprint; all three are measurements on research platforms, and none bounds the delay.

One preprint compares RTC's two variants with VLASH and a per-step correction head (A2C2) under controlled conditions on two benchmarks, in simulation, with delays up to 15 steps on small policies and up to 20 on SmolVLA. The inference-time variant of RTC was competitive at low delay and fell towards the naive baseline at long chunks and high delay; A2C2 led at high delay on both benchmarks and IT-RTC at the lowest delays on LIBERO; the rankings differed between the two benchmarks, and the paper's VLASH result on LIBERO used privileged future states ([[2026-agouzoul-understanding-asynchronous-inference]], §4, §5).

## What it does not do

It does not bound the delay. The scheme works while the inference delay stays within the chunk's slack, estimated from past delays. Such policies are often used above a faster loop that turns their actions into motor signals ([[2025-black-real-time-execution]], Algorithm 1, §5). Asynchronous execution also leaves the reaction delay; it follows the time to first action and the interval between calls, and a flow policy that finishes its first action in one denoising step shortens it; measured on two GPUs and two models ([[2026-lu-faster-rethinking-real]], §2, §3.3, §4.1, Table 2).

## Above the chunks

A reasoning model can sit above the action model and call it as a tool; in Google's Gemini Robotics-ER 1.5 that model's thinking budget trades latency against accuracy ([[2025-google-building-next-generation]]).

## Open questions

- Whether the claims against RTC (mode switching, extra latency) hold outside the authors' set-ups; the three papers compare against RTC on tasks of their own choosing.

- What the lower loop must do when a chunk arrives late or not at all. See [[real-time-loops]].
