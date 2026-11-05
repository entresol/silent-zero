---
type: concept
status: reviewed
sources: [2025-black-real-time-execution, 2025-google-building-next-generation, 2026-jiang-futurertc-real-time]
glossary: Action chunking
updated: 2026-11-05
---

# Action chunking

A learned robot policy emits a sequence of future actions for each call, a *chunk*, and the robot executes several of them before the next call. This keeps motion consistent over time, but it costs reactivity, and switching between chunks can cause pauses or jumps; on its own it "does not fully address the latency problem" ([[2025-black-real-time-execution]], abstract, §1, §2).

## State, October 2026

Real-time chunking (RTC) computes the next chunk while the current one runs and makes it consistent with the actions that will execute in the meantime. With π0.5 at 50 Hz and model latencies around 100 ms, it held task throughput under up to 200 ms of extra delay, where synchronous chunking degraded ([[2025-black-real-time-execution]]). FutureRTC, a 2026 preprint, takes another route: an adapter predicts the observation and state at the moment the chunk will run, so the policy plans from them instead of from stale inputs. On the LIBERO benchmark it lost 5.7 to 6.4 percentage points of success between delays of 5 and 20 control steps, and on a real dual-arm robot it was tested at delays near 5 and 10 steps ([[2026-jiang-futurertc-real-time]]).

## What it does not do

It does not bound the delay. The scheme works while the inference delay stays within the chunk's slack, estimated from past delays. Such policies are often used above a faster loop that turns their actions into motor signals ([[2025-black-real-time-execution]], Algorithm 1, §5).

## Above the chunks

A reasoning model can sit above the action model and call it as a tool; in Google's Gemini Robotics-ER 1.5 that model's thinking budget trades latency against accuracy ([[2025-google-building-next-generation]]).

## Open questions

- What the lower loop must do when a chunk arrives late or not at all. See [[real-time-loops]].
