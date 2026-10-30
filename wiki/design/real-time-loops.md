---
type: design
status: reviewed
sources: [2025-black-real-time-execution, 2025-nesti-use-simplex-architecture, 2026-sel4-functional-correctness-proof, 2026-heiser-mcs-safety-os, 2022-wistoff-systematic-prevention-core, nd-sel4-microkit-user-manual]
updated: 2026-10-29
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
| Isolated safe domain with the learned controller in the loop at a 4 ms period | worst observed round trip 3,976 µs over 10,000 samples, 24 µs margin, no bound | measurement on a hypervisor not claimed to be verified | [[2025-nesti-use-simplex-architecture]] |
| Processor-time budgets enforced by the kernel | implemented in seL4 MCS | MCS functional-correctness proof on RISC-V; no theorem on temporal isolation | [[2026-sel4-functional-correctness-proof]], [[2026-heiser-mcs-safety-os]], [[kernel]] |
| Kernel WCET and schedulability | not yet | none | [[kernel]] |
| Fixed context-switch time with timing-channel protection | prototype on CVA6 | measurement | [[2022-wistoff-systematic-prevention-core]] |

## The paper and its sources

- Section 2.4 says action models emit commands in chunks so a robot can hold a 50 Hz rate while the slower model thinks, citing [[2025-black-real-time-execution]]. Partly confirmed: the source shows that chunking alone pauses, and that holding the rate needs asynchronous execution.
- The paper calls the loop *verified* (abstract, Section 4) and in Section 4 calls the safety controller a candidate for proof. No source so far shows a control loop on seL4 with a proven deadline; the kernel's WCET is missing (see [[kernel]], [[safety-path]]).

## Open

- [[2025-black-real-time-execution]] estimates delay from history and does not bound it. The loop must have a defined behaviour when the next chunk does not arrive: hold, slow, stop.
- Microkit provides no timers or sleep API ([[nd-sel4-microkit-user-manual]]); a periodic loop needs a timer driver of its own.
- On Arm, a Microkit component allowed to make secure monitor calls voids the kernel's WCET properties ([[nd-sel4-microkit-user-manual]]).
