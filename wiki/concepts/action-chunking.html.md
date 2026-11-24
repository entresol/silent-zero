# Action chunking

> Slow robot models emitting action sequences for a fast loop; RTC and three 2026 policy-side answers; no bound on delay.

Concept · LLM reviewed · updated 2026-11-22 · 7 sources · https://silentzero.ooo/wiki/concepts/action-chunking.html

A learned robot policy emits a sequence of future actions for each call, a *chunk*, and the robot executes several of them before the next call. This keeps motion consistent over time, but it costs reactivity, and switching between chunks can cause pauses or jumps; on its own it "does not fully address the latency problem" ([Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md), abstract, §1, §2).

## State, October 2026

Real-time chunking (RTC) computes the next chunk while the current one runs and makes it consistent with the actions that will execute in the meantime. With π0.5 at 50 Hz and model latencies around 100 ms, it held task throughput under up to 200 ms of extra delay, where synchronous chunking degraded ([Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)). FutureRTC, a 2026 preprint, takes another route: an adapter predicts the observation and state at the moment the chunk will run, so the policy plans from them instead of from stale inputs. On the LIBERO benchmark it lost 5.7 to 6.4 percentage points of success between delays of 5 and 20 control steps, and on a real dual-arm robot it was tested at delays near 5 and 10 steps ([FutureRTC](https://silentzero.ooo/wiki/sources/2026-jiang-futurertc-real-time.html.md)).

Three 2026 papers fine-tune the policy for asynchronous execution; RAVEL also changes the runtime, and Legato still guides each chunk by the previous one at inference. REMAC adds a second failure to the discontinuity between chunks: the first actions executed come from an earlier chunk and fit an older observation. It fine-tunes the policy with masked chunks so that it takes the delay as an input, and on a real arm at 15 Hz with an end-to-end delay of about 122 to 140 ms it beat RTC on its tasks; its authors say a maximum delay must be specified in advance and also that the training bounds are not limits; the 55 to 64 ms of extra latency it attributes to RTC is a statement, not shown as a measurement ([REMAC, masked action chunking](https://silentzero.ooo/wiki/sources/2026-wang-real-time-robot.html.md)). Legato argues that RTC's inference-time inpainting leads to spurious switching between grasp goals and arms, and trains the continuation into the policy; on five dual-arm tasks it finished faster than RTC, by about 10 per cent in the authors' summary and by 14 to 23 per cent in their Table I (our arithmetic), with its own runs of RTC ([Legato, native continuation for chunked policies](https://silentzero.ooo/wiki/sources/2026-liu-learning-native-continuation.html.md)). RAVEL keeps a rolling buffer of partly denoised actions and cut the median time to the first action by a factor of 2.6 to 2.9 on one GPU; on its two dynamic real-world tasks (20 trials each) RTC reached 0 per cent success under the authors' settings ([RAVEL, rolling inference for flow-based VLAs](https://silentzero.ooo/wiki/sources/2026-chen-ravel-asynchronous-rolling.html.md)). REMAC and Legato appeared at ICLR and RSS 2026 and RAVEL is a preprint; all three are measurements on research platforms, and none bounds the delay.

## What it does not do

It does not bound the delay. The scheme works while the inference delay stays within the chunk's slack, estimated from past delays. Such policies are often used above a faster loop that turns their actions into motor signals ([Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md), Algorithm 1, §5). Asynchronous execution also leaves the reaction delay; it follows the time to first action and the interval between calls, and a flow policy that finishes its first action in one denoising step shortens it; measured on two GPUs and two models ([FASTER, reaction time of flow VLAs](https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html.md), §2, §3.3, §4.1, Table 2).

## Above the chunks

A reasoning model can sit above the action model and call it as a tool; in Google's Gemini Robotics-ER 1.5 that model's thinking budget trades latency against accuracy ([Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md)).

## Open questions

- Whether the claims against RTC (mode switching, extra latency) hold outside the authors' set-ups; the three papers compare against RTC on tasks of their own choosing.

- What the lower loop must do when a chunk arrives late or not at all. See [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md).

## Sources

- [FASTER, reaction time of flow VLAs](https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html.md)
- [FutureRTC](https://silentzero.ooo/wiki/sources/2026-jiang-futurertc-real-time.html.md)
- [Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md)
- [Legato, native continuation for chunked policies](https://silentzero.ooo/wiki/sources/2026-liu-learning-native-continuation.html.md)
- [RAVEL, rolling inference for flow-based VLAs](https://silentzero.ooo/wiki/sources/2026-chen-ravel-asynchronous-rolling.html.md)
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)
- [REMAC, masked action chunking](https://silentzero.ooo/wiki/sources/2026-wang-real-time-robot.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [Control barrier functions](https://silentzero.ooo/wiki/concepts/control-barrier-functions.html.md)
- [TypeGo](https://silentzero.ooo/wiki/systems/typego.html.md)
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md)
