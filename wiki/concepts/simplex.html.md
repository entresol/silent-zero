# Simplex architecture

> A simple safe controller guarding an untrusted one; tested with learned controllers.

Concept · LLM reviewed · updated 2026-11-21 · 4 sources · https://silentzero.ooo/wiki/concepts/simplex.html

A pattern for running a controller one cannot trust: a high-performance controller drives the system, a simple safe controller stands by, and a safety monitor decides when to switch to the safe one. It was first proposed to test new controllers safely on safety-critical systems and to update control software online, by Sha, Rajkumar and Gagliardi in 1994 and Seto et al. in 1998; it is now used to make learned controllers usable in such systems ([The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md), §2.2).

## What makes it work

- The switching rule is specific to each system. For a pendulum it can keep the state inside an estimate of the region from which the safe controller can still recover; for a vehicle, a distance envelope with speed limits ([The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md), §2.3, §4.2, §5.3).
- The safe side owns the sensors it relies on, and leaves out inputs it cannot trust; on the rover, camera images reach only the learned side ([The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md), §5.2).
- A hypervisor or kernel must keep the unsafe side from interfering with the safe side, in memory and in time ([The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md), §3).
- Alternating between controllers can destabilise the system unless a state machine governs the switch, with hysteresis or similar ([The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md), §3).

## State, October 2026

Demonstrated with learned controllers on a pendulum and a rover, on a hypervisor not claimed to be verified, with tests rather than proofs ([The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md)).

A 2026 variant, Synergistic Simplex, lets information flow both ways: the safety layer may ask the learned layer to replan within safe bounds, and may use a learned output that is independent of the function it protects, under conditions the authors derive on paper. In simulation of a car it cut stops where an undetected obstacle lay in a neighbouring lane, with no collisions; its assumptions include static obstacles and correct lane detection ([Synergistic Simplex](https://silentzero.ooo/wiki/sources/2026-bansal-synergistic-simplex-cooperative.html.md)).

A 2026 research agenda uses Simplex as the runtime layer for foundation-model-enabled cyber-physical systems and names shielding (modifying single actions) as a variant beside switching; there is no demonstration and no concrete switching rule (§5.1 gives only a qualitative condition and names real-time reachability as a basis) ([a neuro-symbolic assurance agenda for learning-enabled CPS](https://silentzero.ooo/wiki/sources/2026-zheng-assuring-learning-enabled.html.md), §5.1). The agenda's monitor reads symbolic world-model elements, interface states and uncertainty estimates that the learned side exposes (§5.1). Our reading: closer to the relaxed form of [Synergistic Simplex](https://silentzero.ooo/wiki/sources/2026-bansal-synergistic-simplex-cooperative.html.md) than to the strict form; the paper does not discuss the difference.

A 2026 preprint builds the switching rule from design-time artifacts, with several certified safe controllers and a switch between them. In simulation a one-step prediction kept a ground robot within its limit when the model was matched, but on hardware only a horizon of about 15 control periods did so in every configuration ([context-dependent regions of attraction for a multi-candidate Simplex](https://silentzero.ooo/wiki/sources/2026-jager-context-dependent-runtime.html.md), §IV-C, §IV-E1).

## Open questions

- The Silent Zero paper dates the pattern to 2001 and cites Sha 2001; [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) dates it to 1994.
- How a monitor handles a wrong command that leaves the safe region within one step; Nesti et al. name a one-step prediction and leave it out (§4.2). Jäger et al. found one step enough only with matched dynamics; with unmodelled dynamics they tuned the horizon by experiment ([context-dependent regions of attraction for a multi-candidate Simplex](https://silentzero.ooo/wiki/sources/2026-jager-context-dependent-runtime.html.md), §IV-D).

## Sources

- [a neuro-symbolic assurance agenda for learning-enabled CPS](https://silentzero.ooo/wiki/sources/2026-zheng-assuring-learning-enabled.html.md)
- [context-dependent regions of attraction for a multi-candidate Simplex](https://silentzero.ooo/wiki/sources/2026-jager-context-dependent-runtime.html.md)
- [Synergistic Simplex](https://silentzero.ooo/wiki/sources/2026-bansal-synergistic-simplex-cooperative.html.md)
- [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md)

## Related pages

- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md)
- [credible compilation against verification](https://silentzero.ooo/wiki/sources/2026-rinard-quantitative-comparison-credible.html.md)
- [multi-link safety filtering for VLA policies](https://silentzero.ooo/wiki/sources/2026-agarwal-multi-link-safety.html.md)
- [the Axon compiler](https://silentzero.ooo/wiki/sources/2026-rinard-testing-credible-compilation.html.md)
