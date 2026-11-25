---
type: design
status: reviewed
sources: [2025-nesti-use-simplex-architecture, 2025-black-real-time-execution, 2018-klein-formally-verified-software, 2025-google-building-next-generation, 2026-bansal-synergistic-simplex-cooperative, 2026-agarwal-multi-link-safety, 2026-jager-context-dependent-runtime, 2026-zheng-assuring-learning-enabled, 2026-lu-faster-rethinking-real, 2025-hu-vlsa-vision-language, 2026-park-your-model-already, 2026-elisa-enabling-linux-safety, nd-sysgo-robotics-humanoids, nd-sysgo-safety-certification, 2026-nvidia-inside-halos-robotics, 2026-qnx-nvidia-deepen-collaboration, 2026-nvidia-announces-halos-robotics, 2026-abi-research-rtos-robotics-ranking, 2024-dickson-limitations-formal-verification, 2026-tsinghua-libero-safety-comprehensive, 2026-unverified-silent-failures-physical]
updated: 2026-11-25
---

# The safety path

In zOS the agent and its action model play the complex controller of a [[simplex]] architecture: powerful, unproven, isolated and lower in criticality. The safety controller and the switching logic play the simple one; they are small, run at the highest criticality and are candidates for proof. "The agent may suggest any motion. Only the loop moves the motor." (paper, Section 4).

## What it must do

- Decide, for one robot and one task, when the learned controller's command is safe to pass on.
- Hand over to a safe controller before the system leaves the region from which it can recover.
- Rely on nothing the learned side controls: not its inputs, not its timing.
- Stay useful: degrade before it stops.

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| Simplex as a pattern | traced to 1994 and 1998 by a recent paper; the paper's own source, Sha 2001, not read | secondary account | [[2025-nesti-use-simplex-architecture]] |
| Simplex with learned controllers on a pendulum and a rover, AI isolated by a hypervisor | demonstrated | tests on two systems; switching rule designed per system | [[2025-nesti-use-simplex-architecture]] |
| Safe side owns the sensors; camera input only on the learned side | demonstrated on the rover | test | [[2025-nesti-use-simplex-architecture]] |
| A separation kernel or safety RTOS keeps an untrusted AI side apart from the control loops that run on it | offered by vendors: SYSGO's PikeOS (certifications listed by the vendor) and QNX with NVIDIA's Halos on IGX Thor (early access; inspection for certification readiness under way, no robotics certificate claimed) | vendor statements and an analyst ranking; no proof of the kernel mentioned | [[nd-sysgo-robotics-humanoids]], [[nd-sysgo-safety-certification]], [[2026-nvidia-inside-halos-robotics]], [[2026-qnx-nvidia-deepen-collaboration]], [[2026-abi-research-rtos-robotics-ranking]] |
| A proven safety controller and switching logic | not found in the sources | none | — |

The 2026 Synergistic Simplex variant relaxes the rule for its safety layer: it may read a learned output, such as lane boundaries, when it is independent of the function protected; in one simulated scenario the strict form meant more stops (route completion 0.1 against 0.7), and the authors note that certification standards prohibit such use. Its evidence is a car in CARLA with static obstacles, ten runs per cell in CARLA, and proofs on paper ([[2026-bansal-synergistic-simplex-cooperative]]). Our reading: zOS keeps the strict form, since its loop owns its sensors and takes nothing from the model.

A robot model's vendor says its model-level safety filters "are not a substitute for the rigorous safety engineering required for physical systems" and asks for several layers, with emergency stops and collision avoidance outside the model ([[2025-google-building-next-generation]]). Related evidence that is not Simplex: a robot's protective stop caught an oscillating learned controller in an experiment ([[2025-black-real-time-execution]], §4.2), and HACMS showed a compromised component contained in flight ([[2018-klein-formally-verified-software]]).

A different pattern from Simplex switching is a filter on the commanded motion. One preprint shows a barrier-function shield between a frozen π0.5 policy and the arm, whose barrier program ran at 2.2 ms (p99) on a CPU and which cut collisions with moving hazards in simulation from 65.62 to 27.27 per cent, as a mean over six simulated conditions. It has no proof for the moving-hazard case, takes its hazard model from perception, and runs the nominal action when its program is infeasible. Our reading: it does not meet this page's rule that the loop owns its sensors, and changes no state ([[2026-agarwal-multi-link-safety]], §III-C, §V-A, §V-B).

Two further preprints belong to this family, summarised on [[control-barrier-functions]]. AEGIS puts a barrier program behind a π0.5 policy without retraining it; its theorem needs accurate perception and enclosing ellipsoids, and on its benchmark the collision avoidance rate rose from 18.7 to 77.9 per cent (translation-only actions), so collisions remain; the obstacle comes from a vision-language model and a detector ([[2025-hu-vlsa-vision-language]], Theorem 1, Table I). KNOWS takes the target from the policy's own attention at every step and stops when no safe action exists; with moving obstacles its collision rate fell from 70.8 to 26.9 per cent on average against its authors' own reconstruction of the earlier design, in simulation ([[2026-park-your-model-already]], §3.1, Table 1). Our reading: neither meets the rule that the loop relies on nothing the learned side controls, and neither changes a state.

A single-author literature review argues, in our reading, for the same split from the other side (it does not discuss Simplex): an authorization layer independent of the learned model that checks state validity, feasibility, timing and fallback before a command reaches the hardware, and records the decision. It measures nothing and, in our reading, proves nothing; it says such a layer's guarantees weaken with stale state estimates or a wrong model; it is a preprint by the head of a company ([[2026-unverified-silent-failures-physical]], §1, §11). A benchmark with a dataset of 19,664 collision-free demonstrations scores eight VLA policies on physical safety and two reasoning models on semantic safety; it does not score an external filter, so it could serve as a test bed that nobody has used for that yet (our reading; [[2026-tsinghua-libero-safety-comprehensive]]).

A 2026 preprint derives the switching rule of a Simplex by contraction and reachability analysis for a path-tracking robot with an uncertified high-performance controller on the other side (a behavioural-cloning network in one hardware test). The proof covers the model; the hardware safety margin rests on a tuned prediction horizon, tested on one ground robot ([[2026-jager-context-dependent-runtime]], §IV). Our reading: a second kind of evidence for the switch; it changes no state.

A 2026 research agenda by fourteen authors states what is, in our reading, the same thesis independently: a learned component holds capability, and a monitor with shielding or switching plus a safe controller holds authority. It says thresholds found by testing are empirical evidence, not formal guarantees; it is a position, with no results ([[2026-zheng-assuring-learning-enabled]], §3.4, §5). The authors of FASTER ask for safety monitors and physical safeguards around faster-reacting policies ([[2026-lu-faster-rethinking-real]], appendix H).

Commercial neighbours that, in our reading, build the same split from parts their vendors call certified: [[pikeos]] runs an untrusted ROS 2 and Linux partition "physically separated in memory and CPU time" from control loops on a certified kernel, and [[nvidia-halos]] pairs AI compute with a safety island and, in one configuration, a [[qnx]] virtual machine for safety-critical functions, with a decision logic running as a state machine on the island ([[nd-sysgo-robotics-humanoids]], [[2026-nvidia-inside-halos-robotics]]). Their evidence is the vendors' own statements and, for Halos, inspection for certification readiness; none states a proof of the kernel or of the decision logic. The standards they name (IEC 61508, ISO 13849, ISO 26262) are the yardstick of [[safety-certification]].

## The paper and its sources

- Section 6 names the alternative of hardened Linux with a separate safety controller for the motors and cites the ELISA project. [[2026-elisa-enabling-linux-safety]] shows that the project exists and aims at certifying Linux-based safety systems; it names no certificate (see [[elisa]]).
- Section 4 cites Sha 2001 and dates the pattern "twenty-five years ago"; Table 1 says "Established since 2001", and the Epilogue "the Simplex pattern from 2001". [[2025-nesti-use-simplex-architecture]] traces Simplex to Sha, Rajkumar and Gagliardi 1994. Our reading: the pattern is older than the paper says. Sha 2001 itself is not covered here; for the design of zOS the pattern matters, not its first source.
- Section 4's "Most of the engineering lies in deciding what it can reliably detect, for one robot and one task" matches Nesti et al.: the switching rule "requires to be designed for each use case".
- The abstract and Section 4 speak of a "verified loop", while Section 4 also calls the safety controller and switching logic "candidates for proof". Our reading: the paper should keep one of the two; the sources support only the second.

## Open

- The sources show the pattern working in tests. None proves a safety controller or its switching logic against a model of the plant.
- A single bad command can leave the safe region before the monitor reacts; a one-step prediction guards against it and was left out in [[2025-nesti-use-simplex-architecture]] (§4.2).
- Safety margins can rest on properties of the learned side, as the rover's lateral zones rested on the network's output bound ([[2025-nesti-use-simplex-architecture]], §5.4).
- Whether a proof of a safety path can count as evidence for a certification body; the sources name the standards and the certified products but no such case ([[safety-certification]]). Our reading: nothing in the split requires the safety side to be zOS's own kernel; the sources do not discuss a certified vendor partition beside an authority layer of zOS.
