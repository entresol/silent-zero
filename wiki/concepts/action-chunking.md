---
type: concept
status: reviewed
sources: [2025-black-real-time-execution]
updated: 2026-10-29
---

# Action chunking

A learned robot policy emits a sequence of future actions for each call, a *chunk*, and the robot executes several of them before the next call. This keeps motion consistent over time, but it costs reactivity, and switching between chunks can cause pauses or jumps; on its own it "does not fully address the latency problem" ([[2025-black-real-time-execution]], abstract, §1, §2).

## State, October 2026

Real-time chunking (RTC) computes the next chunk while the current one runs and makes it consistent with the actions that will execute in the meantime. With π0.5 at 50 Hz and model latencies around 100 ms, it held task throughput under up to 200 ms of extra delay, where synchronous chunking degraded ([[2025-black-real-time-execution]]).

## What it does not do

It does not bound the delay. The scheme works while the inference delay stays within the chunk's slack, estimated from past delays. Such policies are often used above a faster loop that turns their actions into motor signals ([[2025-black-real-time-execution]], Algorithm 1, §5).

## Open questions

- What the lower loop must do when a chunk arrives late or not at all. See [[real-time-loops]].
