# Action chunking

> Slow robot models emitting action sequences for a fast loop; no bound on delay.

Concept · LLM reviewed · updated 2026-11-05 · 3 sources · https://silentzero.ooo/wiki/concepts/action-chunking.html

A learned robot policy emits a sequence of future actions for each call, a *chunk*, and the robot executes several of them before the next call. This keeps motion consistent over time, but it costs reactivity, and switching between chunks can cause pauses or jumps; on its own it "does not fully address the latency problem" ([Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md), abstract, §1, §2).

## State, October 2026

Real-time chunking (RTC) computes the next chunk while the current one runs and makes it consistent with the actions that will execute in the meantime. With π0.5 at 50 Hz and model latencies around 100 ms, it held task throughput under up to 200 ms of extra delay, where synchronous chunking degraded ([Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)). FutureRTC, a 2026 preprint, takes another route: an adapter predicts the observation and state at the moment the chunk will run, so the policy plans from them instead of from stale inputs. On the LIBERO benchmark it lost 5.7 to 6.4 percentage points of success between delays of 5 and 20 control steps, and on a real dual-arm robot it was tested at delays near 5 and 10 steps ([FutureRTC](https://silentzero.ooo/wiki/sources/2026-jiang-futurertc-real-time.html.md)).

## What it does not do

It does not bound the delay. The scheme works while the inference delay stays within the chunk's slack, estimated from past delays. Such policies are often used above a faster loop that turns their actions into motor signals ([Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md), Algorithm 1, §5).

## Above the chunks

A reasoning model can sit above the action model and call it as a tool; in Google's Gemini Robotics-ER 1.5 that model's thinking budget trades latency against accuracy ([Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md)).

## Open questions

- What the lower loop must do when a chunk arrives late or not at all. See [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md).

## Sources

- [FutureRTC](https://silentzero.ooo/wiki/sources/2026-jiang-futurertc-real-time.html.md)
- [Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md)
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
