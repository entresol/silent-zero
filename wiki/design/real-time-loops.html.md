# Real-time loops

> The loops that move the motors: asynchronous chunks from slow models, policies trained for a delay range, observed timings, per-step costs of two barrier filters, no proven bound yet.

Design · LLM reviewed · updated 2026-11-24 · 20 sources · https://silentzero.ooo/wiki/design/real-time-loops.html

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
| Fixed context-switch time with timing-channel protection | prototype on CVA6; also an OpenC910 prototype, padding length not given ([fence.t.s for out-of-order cores](https://silentzero.ooo/wiki/sources/2024-wistoff-fence-t-s.html.md)) | measurement | [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md) |
| Reaction to a sudden event through a chunking policy: a range set by inference latency and call interval, shortened by FASTER's first-action sampling | measured on two consumer GPUs and one real arm; preprint, single-latency model, no bound | measurement | [FASTER, reaction time of flow VLAs](https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html.md) |
| Policies trained for a delay range: REMAC beats RTC on a real arm with 122 to 140 ms end-to-end delay; failure outside the trained maximum is stated as possible | measured on one arm, 30 trials per task; ICLR 2026 paper; no bound | measurement | [REMAC, masked action chunking](https://silentzero.ooo/wiki/sources/2026-wang-real-time-robot.html.md) |
| Rolling inference: median time to the first action 54.97 ms against 142.58 ms (X-VLA) and 93.45 against 272.86 ms (π0.5) on one RTX 4090 | measured; observation age 118 ms against 236 to 465 ms (medians) on a real arm, 20 trials per cell; preprint, no worst case | measurement | [RAVEL, rolling inference for flow-based VLAs](https://silentzero.ooo/wiki/sources/2026-chen-ravel-asynchronous-rolling.html.md) |

One timing reference on an edge platform: the barrier filter ran at every 50 ms step and a flow update every fifth step, both on the CPU, while the policy ran once per ten-action chunk on the integrated GPU, at 177.3 ms (p50) after trimming, against 343 ms in the released configuration; the trimming lowered task success by 4.17 percentage points on the 300 mm escape condition. No bound is proven ([multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md), §III-D, §V-B).

Another: a Simplex decision module measured 0.0281 ms mean and 4.13 ms worst case over 81,749 cycles on a 35 W processor, against a 50 ms control period; no bound is proven, and the authors name timing analysis as future work ([context-dependent regions of attraction for a multi-candidate Simplex](https://silentzero.ooo/wiki/sources/2026-jager-context-dependent-runtime.html.md), §IV-E1, §V).

Two barrier filters give per-step costs. AEGIS's constraint layer took 0.356 ms per step on an RTX 4090 setup, about 1/47 of the policy's inference time, in a 20 Hz loop; the paper does not say whether this includes its vision-language model and detector ([VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md), §V-B). KNOWS's wrapper took 49.3 ms per step (segmentation 19.3 ms, program 11.4 ms; the listed parts sum to 50.0 ms) against the 50 ms of a 20 Hz loop, while one policy call took 243 ms per chunk, about 30 ms per step with eight-step chunks. The paper does not say how policy and wrapper overlap, and wrapper plus policy share would exceed 50 ms if they did not; the authors call perception the only term near the budget, on a workstation with two RTX PRO 6000 GPUs ([KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md), §4.3, Table 2). Means only, no worst case, no bound; see [Control barrier functions](https://silentzero.ooo/wiki/concepts/control-barrier-functions.html.md).

## The paper and its sources

- Section 2.4 says robot stacks separate a reasoning model that plans and calls tools from an action model that drives the motors, citing [Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md). Confirmed for Google's stack, where the reasoning model calls a vision-language-action model for motor control; its thinking budget makes its latency a setting; our reading: a setting, not a bound.
- Section 2.4 says action models emit commands in chunks so a robot can hold a 50 Hz rate while the slower model thinks, citing [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md). Partly confirmed: the source shows that chunking alone pauses, and that holding the rate needs asynchronous execution.
- The paper calls the loop *verified* (abstract, Section 4) and in Section 4 calls the safety controller a candidate for proof. No source so far shows a control loop on seL4 with a proven deadline; the kernel's WCET is missing (see [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md), [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)).

- Section 6 names PREEMPT_RT as Linux's route to real time. [Linux kernel documentation: real-time preemption](https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html.md) confirms that it makes the kernel largely preemptible; the chapters read state no latency bound, and warn that shared caches, memory and buses can disturb deterministic handling. See [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md).

- [TypeGo](https://silentzero.ooo/wiki/systems/typego.html.md) keeps the language model off the critical path with layered asynchronous loops in a Python runtime on a quadruped: planning overlapped with motion, a reflex layer and a scheduler. Its authors report 50 per cent lower per-step delay and about 200 ms and 50 ms of scheduling and reflex overhead; no proved bound, and isolation only as future work ([TypeGo, an OS runtime for embodied agents](https://silentzero.ooo/wiki/sources/2026-chen-typego-os-runtime.html.md)). [SpecOS](https://silentzero.ooo/wiki/systems/specos.html.md) proposes control loops at 100 Hz and above on static topologies verified offline and planning at 3 to 10 Hz verified at run time; no implementation is reported ([Formal methods as the harness for AIOS (SpecOS)](https://silentzero.ooo/wiki/sources/2026-li-formal-methods-harness.html.md)).

## Open

- Fine-tuning answers (REMAC, Legato, RAVEL) train for a delay range or lower the delay's median; our reading is that none of the three bounds the delay (RAVEL reports a 95th percentile, REMAC's authors state both that a maximum delay must be specified and that their training bounds are not limits; [REMAC, masked action chunking](https://silentzero.ooo/wiki/sources/2026-wang-real-time-robot.html.md), [RAVEL, rolling inference for flow-based VLAs](https://silentzero.ooo/wiki/sources/2026-chen-ravel-asynchronous-rolling.html.md)). The loop's rule for a late chunk stays undecided.

- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md) estimates delay from history and does not bound it. The loop must have a defined behaviour when the next chunk does not arrive: hold, slow, stop.
- The paper's condition for no interruption of streamed actions is that the next action arrives within one control period ([FASTER, reaction time of flow VLAs](https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html.md), appendix D.2); our reading: otherwise the buffer can run dry. What the loop does then is undecided.
- Microkit provides no timers or sleep API ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)); a periodic loop needs a timer driver of its own.
- On Arm, a Microkit component allowed to make secure monitor calls voids the kernel's WCET properties ([seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)).

## Sources

- [context-dependent regions of attraction for a multi-candidate Simplex](https://silentzero.ooo/wiki/sources/2026-jager-context-dependent-runtime.html.md)
- [FASTER, reaction time of flow VLAs](https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html.md)
- [fence.t.s for out-of-order cores](https://silentzero.ooo/wiki/sources/2024-wistoff-fence-t-s.html.md)
- [Formal methods as the harness for AIOS (SpecOS)](https://silentzero.ooo/wiki/sources/2026-li-formal-methods-harness.html.md)
- [FutureRTC](https://silentzero.ooo/wiki/sources/2026-jiang-futurertc-real-time.html.md)
- [Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md)
- [KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md)
- [Legato, native continuation for chunked policies](https://silentzero.ooo/wiki/sources/2026-liu-learning-native-continuation.html.md)
- [Linux kernel documentation: real-time preemption](https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html.md)
- [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md)
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md)
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md)
- [RAVEL, rolling inference for flow-based VLAs](https://silentzero.ooo/wiki/sources/2026-chen-ravel-asynchronous-rolling.html.md)
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)
- [REMAC, masked action chunking](https://silentzero.ooo/wiki/sources/2026-wang-real-time-robot.html.md)
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md)
- [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md)
- [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md)
- [TypeGo, an OS runtime for embodied agents](https://silentzero.ooo/wiki/sources/2026-chen-typego-os-runtime.html.md)
- [VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md)

## Related pages

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [Control barrier functions](https://silentzero.ooo/wiki/concepts/control-barrier-functions.html.md)
- [Memory-safe code](https://silentzero.ooo/wiki/concepts/memory-safe-code.html.md)
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md)
- [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md)
- [SpecOS](https://silentzero.ooo/wiki/systems/specos.html.md)
- [TypeGo](https://silentzero.ooo/wiki/systems/typego.html.md)
- [ARSENAL](https://silentzero.ooo/wiki/sources/2026-lide-arsenal-assured-robotics.html.md)
- [Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md)
- [LIBERO-Safety, a benchmark for physical and semantic safety of VLA models](https://silentzero.ooo/wiki/sources/2026-tsinghua-libero-safety-comprehensive.html.md)
- [Towards an Agent Operating System](https://silentzero.ooo/wiki/sources/2026-steinder-towards-agent-operating.html.md)
