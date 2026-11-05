# Real-time loops

> The loops that move the motors: asynchronous chunks from slow models, observed timings, no proven bound yet.

Design · LLM reviewed · updated 2026-11-05 · 9 sources · https://silentzero.ooo/wiki/design/real-time-loops.html

The control loops at the bottom of Silent Zero move the motors on a fixed period and have the last word over motion. Learned models above them are slower and deliver commands early, in chunks; the loops execute them on time or fall back (paper, Sections 2.4 and 4).

## What it must do

- Run on a fixed period with a bounded response time, whatever the agent does.
- Treat commands from the learned side as untrusted and possibly late.
- Get its processor time from a budget no other component can take. See [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md).

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| Learned models are slower than the control loop (π0 at 50 Hz with 46 ms prefill on an RTX 4090; OpenVLA 321 ms on an A100) | measured | measurement | [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md) |
| Asynchronous chunking (RTC) holds throughput under up to 200 ms extra delay; synchronous chunking degrades | measured on real robots | measurement; no bound on delay | [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md) |
| Asynchronous chunking with predicted inputs (FutureRTC) loses 5.7 to 6.4 points of success from delays of 5 to 20 control steps (LIBERO) | measured in simulation and on one real robot; preprint, no bound on delay | measurement | [FutureRTC](https://silentzero.ooo/wiki/sources/2026-jiang-futurertc-real-time.html.md) |
| Isolated safe domain with the learned controller in the loop at a 4 ms period | worst observed round trip 3,976 µs over 10,000 samples, 24 µs margin, no bound | measurement on a hypervisor not claimed to be verified | [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) |
| Processor-time budgets enforced by the kernel | implemented in seL4 MCS | MCS functional-correctness proof on RISC-V; no theorem on temporal isolation | [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md), [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md), [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md) |
| Kernel WCET and schedulability | not yet | none | [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md) |
| Fixed context-switch time with timing-channel protection | prototype on CVA6 | measurement | [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md) |

## The paper and its sources

- Section 2.4 says robot stacks separate a reasoning model that plans and calls tools from an action model that drives the motors, citing [Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md). Confirmed for Google's stack, where the reasoning model calls a vision-language-action model for motor control; its thinking budget makes its latency a setting; our reading: a setting, not a bound.
- Section 2.4 says action models emit commands in chunks so a robot can hold a 50 Hz rate while the slower model thinks, citing [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md). Partly confirmed: the source shows that chunking alone pauses, and that holding the rate needs asynchronous execution.
- The paper calls the loop *verified* (abstract, Section 4) and in Section 4 calls the safety controller a candidate for proof. No source so far shows a control loop on seL4 with a proven deadline; the kernel's WCET is missing (see [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md), [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)).

- Section 6 names PREEMPT_RT as Linux's route to real time. [Linux kernel documentation: real-time preemption](https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html.md) confirms that it makes the kernel largely preemptible; the chapters read state no latency bound, and warn that shared caches, memory and buses can disturb deterministic handling. See [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md).

## Open

- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md) estimates delay from history and does not bound it. The loop must have a defined behaviour when the next chunk does not arrive: hold, slow, stop.
- Microkit provides no timers or sleep API ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)); a periodic loop needs a timer driver of its own.
- On Arm, a Microkit component allowed to make secure monitor calls voids the kernel's WCET properties ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)).

## Sources

- [FutureRTC](https://silentzero.ooo/wiki/sources/2026-jiang-futurertc-real-time.html.md)
- [Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md)
- [Linux kernel documentation: real-time preemption](https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html.md)
- [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md)
- [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md)

## Related pages

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md)
- [Memory-safe code](https://silentzero.ooo/wiki/concepts/memory-safe-code.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md)
- [Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md)
