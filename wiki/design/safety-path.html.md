# The safety path

> Simplex in Silent Zero: the agent proposes, the loop disposes; tested, not proven; the paper’s 2001 date disputed by a 1994 origin; certified real-time kernels sell the same split as products; two more barrier filters, guarantees conditional on perception.

Design · LLM reviewed · updated 2026-11-25 · 21 sources · https://silentzero.ooo/wiki/design/safety-path.html

In Silent Zero the agent and its action model play the complex controller of a [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md) architecture: powerful, unproven, isolated and lower in criticality. The safety controller and the switching logic play the simple one; they are small, run at the highest criticality and are candidates for proof. "The agent may suggest any motion. Only the loop moves the motor." (paper, Section 4).

## What it must do

- Decide, for one robot and one task, when the learned controller's command is safe to pass on.
- Hand over to a safe controller before the system leaves the region from which it can recover.
- Rely on nothing the learned side controls: not its inputs, not its timing.
- Stay useful: degrade before it stops.

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| Simplex as a pattern | traced to 1994 and 1998 by a recent paper; the paper's own source, Sha 2001, not read | secondary account | [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) |
| Simplex with learned controllers on a pendulum and a rover, AI isolated by a hypervisor | demonstrated | tests on two systems; switching rule designed per system | [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) |
| Safe side owns the sensors; camera input only on the learned side | demonstrated on the rover | test | [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) |
| A separation kernel or safety RTOS keeps an untrusted AI side apart from the control loops that run on it | offered by vendors: SYSGO's PikeOS (certifications listed by the vendor) and QNX with NVIDIA's Halos on IGX Thor (early access; inspection for certification readiness under way, no robotics certificate claimed) | vendor statements and an analyst ranking; no proof of the kernel mentioned | [SYSGO: PikeOS for robotics and humanoids](https://silentzero.ooo/wiki/sources/nd-sysgo-robotics-humanoids.html.md), [SYSGO: PikeOS safety certification](https://silentzero.ooo/wiki/sources/nd-sysgo-safety-certification.html.md), [Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md), [QNX and NVIDIA deepen their collaboration](https://silentzero.ooo/wiki/sources/2026-qnx-nvidia-deepen-collaboration.html.md), [ranking of real-time operating systems for robotics safety](https://silentzero.ooo/wiki/sources/2026-abi-research-rtos-robotics-ranking.html.md) |
| A proven safety controller and switching logic | not found in the sources | none | — |

The 2026 Synergistic Simplex variant relaxes the rule for its safety layer: it may read a learned output, such as lane boundaries, when it is independent of the function protected; in one simulated scenario the strict form meant more stops (route completion 0.1 against 0.7), and the authors note that certification standards prohibit such use. Its evidence is a car in CARLA with static obstacles, ten runs per cell in CARLA, and proofs on paper ([Synergistic Simplex](https://silentzero.ooo/wiki/sources/2026-bansal-synergistic-simplex-cooperative.html.md)). Our reading: Silent Zero keeps the strict form, since its loop owns its sensors and takes nothing from the model.

A robot model's vendor says its model-level safety filters "are not a substitute for the rigorous safety engineering required for physical systems" and asks for several layers, with emergency stops and collision avoidance outside the model ([Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md)). Related evidence that is not Simplex: a robot's protective stop caught an oscillating learned controller in an experiment ([Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md), §4.2), and HACMS showed a compromised component contained in flight ([Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)).

A different pattern from Simplex switching is a filter on the commanded motion. One preprint shows a barrier-function shield between a frozen π0.5 policy and the arm, whose barrier program ran at 2.2 ms (p99) on a CPU and which cut collisions with moving hazards in simulation from 65.62 to 27.27 per cent, as a mean over six simulated conditions. It has no proof for the moving-hazard case, takes its hazard model from perception, and runs the nominal action when its program is infeasible. Our reading: it does not meet this page's rule that the loop owns its sensors, and changes no state ([multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md), §III-C, §V-A, §V-B).

Two further preprints belong to this family, summarised on [Control barrier functions](https://silentzero.ooo/wiki/concepts/control-barrier-functions.html.md). AEGIS puts a barrier program behind a π0.5 policy without retraining it; its theorem needs accurate perception and enclosing ellipsoids, and on its benchmark the collision avoidance rate rose from 18.7 to 77.9 per cent (translation-only actions), so collisions remain; the obstacle comes from a vision-language model and a detector ([VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md), Theorem 1, Table I). KNOWS takes the target from the policy's own attention at every step and stops when no safe action exists; with moving obstacles its collision rate fell from 70.8 to 26.9 per cent on average against its authors' own reconstruction of the earlier design, in simulation ([KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md), §3.1, Table 1). Our reading: neither meets the rule that the loop relies on nothing the learned side controls, and neither changes a state.

A single-author literature review argues, in our reading, for the same split from the other side (it does not discuss Simplex): an authorization layer independent of the learned model that checks state validity, feasibility, timing and fallback before a command reaches the hardware, and records the decision. It measures nothing and, in our reading, proves nothing; it says such a layer's guarantees weaken with stale state estimates or a wrong model; it is a preprint by the head of a company ([Silent failures in physical AI, a literature review of runtime action authorization](https://silentzero.ooo/wiki/sources/2026-unverified-silent-failures-physical.html.md), §1, §11). A benchmark with a dataset of 19,664 collision-free demonstrations scores eight VLA policies on physical safety and two reasoning models on semantic safety; it does not score an external filter, so it could serve as a test bed that nobody has used for that yet (our reading; [LIBERO-Safety, a benchmark for physical and semantic safety of VLA models](https://silentzero.ooo/wiki/sources/2026-tsinghua-libero-safety-comprehensive.html.md)).

A 2026 preprint derives the switching rule of a Simplex by contraction and reachability analysis for a path-tracking robot with an uncertified high-performance controller on the other side (a behavioural-cloning network in one hardware test). The proof covers the model; the hardware safety margin rests on a tuned prediction horizon, tested on one ground robot ([context-dependent regions of attraction for a multi-candidate Simplex](https://silentzero.ooo/wiki/sources/2026-jager-context-dependent-runtime.html.md), §IV). Our reading: a second kind of evidence for the switch; it changes no state.

A 2026 research agenda by fourteen authors states what is, in our reading, the same thesis independently: a learned component holds capability, and a monitor with shielding or switching plus a safe controller holds authority. It says thresholds found by testing are empirical evidence, not formal guarantees; it is a position, with no results ([a neuro-symbolic assurance agenda for learning-enabled CPS](https://silentzero.ooo/wiki/sources/2026-zheng-assuring-learning-enabled.html.md), §3.4, §5). The authors of FASTER ask for safety monitors and physical safeguards around faster-reacting policies ([FASTER, reaction time of flow VLAs](https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html.md), appendix H).

Commercial neighbours that, in our reading, build the same split from parts their vendors call certified: [PikeOS](https://silentzero.ooo/wiki/systems/pikeos.html.md) runs an untrusted ROS 2 and Linux partition "physically separated in memory and CPU time" from control loops on a certified kernel, and [NVIDIA Halos for Robotics](https://silentzero.ooo/wiki/systems/nvidia-halos.html.md) pairs AI compute with a safety island and, in one configuration, a [QNX](https://silentzero.ooo/wiki/systems/qnx.html.md) virtual machine for safety-critical functions, with a decision logic running as a state machine on the island ([SYSGO: PikeOS for robotics and humanoids](https://silentzero.ooo/wiki/sources/nd-sysgo-robotics-humanoids.html.md), [Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md)). Their evidence is the vendors' own statements and, for Halos, inspection for certification readiness; none states a proof of the kernel or of the decision logic. The standards they name (IEC 61508, ISO 13849, ISO 26262) are the yardstick of [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md).

## The paper and its sources

- Section 6 names the alternative of hardened Linux with a separate safety controller for the motors and cites the ELISA project. [NVIDIA joins as a premier member](https://silentzero.ooo/wiki/sources/2026-elisa-enabling-linux-safety.html.md) shows that the project exists and aims at certifying Linux-based safety systems; it names no certificate (see [ELISA](https://silentzero.ooo/wiki/systems/elisa.html.md)).
- Section 4 cites Sha 2001 and dates the pattern "twenty-five years ago"; Table 1 says "Established since 2001", and the Epilogue "the Simplex pattern from 2001". [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) traces Simplex to Sha, Rajkumar and Gagliardi 1994. Our reading: the pattern is older than the paper says. Sha 2001 itself is not covered here; for the design of Silent Zero the pattern matters, not its first source.
- Section 4's "Most of the engineering lies in deciding what it can reliably detect, for one robot and one task" matches Nesti et al.: the switching rule "requires to be designed for each use case".
- The abstract and Section 4 speak of a "verified loop", while Section 4 also calls the safety controller and switching logic "candidates for proof". Our reading: the paper should keep one of the two; the sources support only the second.

## Open

- The sources show the pattern working in tests. None proves a safety controller or its switching logic against a model of the plant.
- A single bad command can leave the safe region before the monitor reacts; a one-step prediction guards against it and was left out in [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) (§4.2).
- Safety margins can rest on properties of the learned side, as the rover's lateral zones rested on the network's output bound ([The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md), §5.4).
- Whether a proof of a safety path can count as evidence for a certification body; the sources name the standards and the certified products but no such case ([Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md)). Our reading: nothing in the split requires the safety side to be Silent Zero's own kernel; the sources do not discuss a certified vendor partition beside an authority layer of Silent Zero.

## Sources

- [a neuro-symbolic assurance agenda for learning-enabled CPS](https://silentzero.ooo/wiki/sources/2026-zheng-assuring-learning-enabled.html.md)
- [context-dependent regions of attraction for a multi-candidate Simplex](https://silentzero.ooo/wiki/sources/2026-jager-context-dependent-runtime.html.md)
- [FASTER, reaction time of flow VLAs](https://silentzero.ooo/wiki/sources/2026-lu-faster-rethinking-real.html.md)
- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)
- [Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md)
- [Halos for Robotics, the announcement](https://silentzero.ooo/wiki/sources/2026-nvidia-announces-halos-robotics.html.md)
- [Inside Halos for Robotics](https://silentzero.ooo/wiki/sources/2026-nvidia-inside-halos-robotics.html.md)
- [KNOWS, a safety filter steered by the policy's attention](https://silentzero.ooo/wiki/sources/2026-park-your-model-already.html.md)
- [LIBERO-Safety, a benchmark for physical and semantic safety of VLA models](https://silentzero.ooo/wiki/sources/2026-tsinghua-libero-safety-comprehensive.html.md)
- [limitations on formal verification for AI safety](https://silentzero.ooo/wiki/sources/2024-dickson-limitations-formal-verification.html.md)
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md)
- [NVIDIA joins as a premier member](https://silentzero.ooo/wiki/sources/2026-elisa-enabling-linux-safety.html.md)
- [QNX and NVIDIA deepen their collaboration](https://silentzero.ooo/wiki/sources/2026-qnx-nvidia-deepen-collaboration.html.md)
- [ranking of real-time operating systems for robotics safety](https://silentzero.ooo/wiki/sources/2026-abi-research-rtos-robotics-ranking.html.md)
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)
- [Silent failures in physical AI, a literature review of runtime action authorization](https://silentzero.ooo/wiki/sources/2026-unverified-silent-failures-physical.html.md)
- [Synergistic Simplex](https://silentzero.ooo/wiki/sources/2026-bansal-synergistic-simplex-cooperative.html.md)
- [SYSGO: PikeOS for robotics and humanoids](https://silentzero.ooo/wiki/sources/nd-sysgo-robotics-humanoids.html.md)
- [SYSGO: PikeOS safety certification](https://silentzero.ooo/wiki/sources/nd-sysgo-safety-certification.html.md)
- [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md)
- [VLSA and AEGIS, a barrier-function layer for VLA policies](https://silentzero.ooo/wiki/sources/2025-hu-vlsa-vision-language.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [Control barrier functions](https://silentzero.ooo/wiki/concepts/control-barrier-functions.html.md)
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [Safety certification](https://silentzero.ooo/wiki/concepts/safety-certification.html.md)
- [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md)
- [ELISA](https://silentzero.ooo/wiki/systems/elisa.html.md)
- [NVIDIA Halos for Robotics](https://silentzero.ooo/wiki/systems/nvidia-halos.html.md)
- [PikeOS](https://silentzero.ooo/wiki/systems/pikeos.html.md)
- [QNX](https://silentzero.ooo/wiki/systems/qnx.html.md)
- [SpecOS](https://silentzero.ooo/wiki/systems/specos.html.md)
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md)
- [AutoReal, LLM-driven theorem proving on seL4](https://silentzero.ooo/wiki/sources/2026-unverified-autoreal-sel4-proof.html.md)
- [credible compilation against verification](https://silentzero.ooo/wiki/sources/2026-rinard-quantitative-comparison-credible.html.md)
- [fence.t.s for out-of-order cores](https://silentzero.ooo/wiki/sources/2024-wistoff-fence-t-s.html.md)
- [Formal methods as the harness for AIOS (SpecOS)](https://silentzero.ooo/wiki/sources/2026-li-formal-methods-harness.html.md)
- [Legato, native continuation for chunked policies](https://silentzero.ooo/wiki/sources/2026-liu-learning-native-continuation.html.md)
- [RAVEL, rolling inference for flow-based VLAs](https://silentzero.ooo/wiki/sources/2026-chen-ravel-asynchronous-rolling.html.md)
- [REMAC, masked action chunking](https://silentzero.ooo/wiki/sources/2026-wang-real-time-robot.html.md)
- [the Axon compiler](https://silentzero.ooo/wiki/sources/2026-rinard-testing-credible-compilation.html.md)
- [Towards an Agent Operating System](https://silentzero.ooo/wiki/sources/2026-steinder-towards-agent-operating.html.md)
