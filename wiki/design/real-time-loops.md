---
type: design
status: reviewed
sources: [2025-black-real-time-execution, 2025-nesti-use-simplex-architecture, 2026-sel4-functional-correctness-proof, 2026-heiser-mcs-safety-os, 2022-wistoff-systematic-prevention-core, nd-sel4-microkit-user-manual, 2025-google-building-next-generation, nd-linux-real-time-preemption, 2026-jiang-futurertc-real-time, 2026-agarwal-multi-link-safety, 2024-wistoff-fence-t-s, 2026-lu-faster-rethinking-real, 2026-jager-context-dependent-runtime, 2026-chen-typego-os-runtime, 2026-li-formal-methods-harness, 2026-wang-real-time-robot, 2026-liu-learning-native-continuation, 2026-chen-ravel-asynchronous-rolling]
updated: 2026-11-22
---

# Real-time loops

The control loops at the bottom of zOS move the motors on a fixed period and have the last word over motion. Learned models above them are slower and deliver commands early, in chunks; the loops execute them on time or fall back (paper, Sections 2.4 and 4).

## What it must do

- Run on a fixed period with a bounded response time, whatever the agent does.
- Treat commands from the learned side as untrusted and possibly late.
- Get its processor time from a budget no other component can take. See [[mixed-criticality]].

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| Learned models are slower than the control loop (π0 at 50 Hz with 46 ms prefill on an RTX 4090; OpenVLA 321 ms on an A100) | measured | measurement | [[2025-black-real-time-execution]] |
| Asynchronous chunking (RTC) holds throughput under up to 200 ms extra delay; synchronous chunking degrades | measured on real robots | measurement; no bound on delay | [[2025-black-real-time-execution]] |
| Asynchronous chunking with predicted inputs (FutureRTC) loses 5.7 to 6.4 points of success from delays of 5 to 20 control steps (LIBERO) | measured in simulation and on one real robot; preprint, no bound on delay | measurement | [[2026-jiang-futurertc-real-time]] |
| Isolated safe domain with the learned controller in the loop at a 4 ms period | worst observed round trip 3,976 µs over 10,000 samples, 24 µs margin, no bound | measurement on a hypervisor not claimed to be verified | [[2025-nesti-use-simplex-architecture]] |
| Processor-time budgets enforced by the kernel | implemented in seL4 MCS | MCS functional-correctness proof on RISC-V; no theorem on temporal isolation | [[2026-sel4-functional-correctness-proof]], [[2026-heiser-mcs-safety-os]], [[kernel]] |
| Kernel WCET and schedulability | not yet | none | [[kernel]] |
| Fixed context-switch time with timing-channel protection | prototype on CVA6; also an OpenC910 prototype, padding length not given ([[2024-wistoff-fence-t-s]]) | measurement | [[2022-wistoff-systematic-prevention-core]] |
| Reaction to a sudden event through a chunking policy: a range set by inference latency and call interval, shortened by FASTER's first-action sampling | measured on two consumer GPUs and one real arm; preprint, single-latency model, no bound | measurement | [[2026-lu-faster-rethinking-real]] |
| Policies trained for a delay range: REMAC beats RTC on a real arm with 122 to 140 ms end-to-end delay; failure outside the trained maximum is stated as possible | measured on one arm, 30 trials per task; ICLR 2026 paper; no bound | measurement | [[2026-wang-real-time-robot]] |
| Rolling inference: median time to the first action 54.97 ms against 142.58 ms (X-VLA) and 93.45 against 272.86 ms (π0.5) on one RTX 4090 | measured; observation age 118 ms against 236 to 465 ms (medians) on a real arm, 20 trials per cell; preprint, no worst case | measurement | [[2026-chen-ravel-asynchronous-rolling]] |

One timing reference on an edge platform: the barrier filter ran at every 50 ms step and a flow update every fifth step, both on the CPU, while the policy ran once per ten-action chunk on the integrated GPU, at 177.3 ms (p50) after trimming, against 343 ms in the released configuration; the trimming lowered task success by 4.17 percentage points on the 300 mm escape condition. No bound is proven ([[2026-agarwal-multi-link-safety]], §III-D, §V-B).

Another: a Simplex decision module measured 0.0281 ms mean and 4.13 ms worst case over 81,749 cycles on a 35 W processor, against a 50 ms control period; no bound is proven, and the authors name timing analysis as future work ([[2026-jager-context-dependent-runtime]], §IV-E1, §V).

## The paper and its sources

- Section 2.4 says robot stacks separate a reasoning model that plans and calls tools from an action model that drives the motors, citing [[2025-google-building-next-generation]]. Confirmed for Google's stack, where the reasoning model calls a vision-language-action model for motor control; its thinking budget makes its latency a setting; our reading: a setting, not a bound.
- Section 2.4 says action models emit commands in chunks so a robot can hold a 50 Hz rate while the slower model thinks, citing [[2025-black-real-time-execution]]. Partly confirmed: the source shows that chunking alone pauses, and that holding the rate needs asynchronous execution.
- The paper calls the loop *verified* (abstract, Section 4) and in Section 4 calls the safety controller a candidate for proof. No source so far shows a control loop on seL4 with a proven deadline; the kernel's WCET is missing (see [[kernel]], [[safety-path]]).

- Section 6 names PREEMPT_RT as Linux's route to real time. [[nd-linux-real-time-preemption]] confirms that it makes the kernel largely preemptible; the chapters read state no latency bound, and warn that shared caches, memory and buses can disturb deterministic handling. See [[preempt-rt]].

- [[typego]] keeps the language model off the critical path with layered asynchronous loops in a Python runtime on a quadruped: planning overlapped with motion, a reflex layer and a scheduler. Its authors report 50 per cent lower per-step delay and about 200 ms and 50 ms of scheduling and reflex overhead; no proved bound, and isolation only as future work ([[2026-chen-typego-os-runtime]]). [[specos]] proposes control loops at 100 Hz and above on static topologies verified offline and planning at 3 to 10 Hz verified at run time; no implementation is reported ([[2026-li-formal-methods-harness]]).

## Open

- Fine-tuning answers (REMAC, Legato, RAVEL) train for a delay range or lower the delay's median; our reading is that none of the three bounds the delay (RAVEL reports a 95th percentile, REMAC's authors state both that a maximum delay must be specified and that their training bounds are not limits; [[2026-wang-real-time-robot]], [[2026-chen-ravel-asynchronous-rolling]]). The loop's rule for a late chunk stays undecided.

- [[2025-black-real-time-execution]] estimates delay from history and does not bound it. The loop must have a defined behaviour when the next chunk does not arrive: hold, slow, stop.
- The paper's condition for no interruption of streamed actions is that the next action arrives within one control period ([[2026-lu-faster-rethinking-real]], appendix D.2); our reading: otherwise the buffer can run dry. What the loop does then is undecided.
- Microkit provides no timers or sleep API ([[nd-sel4-microkit-user-manual]]); a periodic loop needs a timer driver of its own.
- On Arm, a Microkit component allowed to make secure monitor calls voids the kernel's WCET properties ([[nd-sel4-microkit-user-manual]]).
