---
type: concept
status: reviewed
sources: [2025-nesti-use-simplex-architecture, 2026-bansal-synergistic-simplex-cooperative, 2026-zheng-assuring-learning-enabled, 2026-jager-context-dependent-runtime]
glossary: Simplex architecture
updated: 2026-11-21
---

# Simplex architecture

A pattern for running a controller one cannot trust: a high-performance controller drives the system, a simple safe controller stands by, and a safety monitor decides when to switch to the safe one. It was first proposed to test new controllers safely on safety-critical systems and to update control software online, by Sha, Rajkumar and Gagliardi in 1994 and Seto et al. in 1998; it is now used to make learned controllers usable in such systems ([[2025-nesti-use-simplex-architecture]], §2.2).

## What makes it work

- The switching rule is specific to each system. For a pendulum it can keep the state inside an estimate of the region from which the safe controller can still recover; for a vehicle, a distance envelope with speed limits ([[2025-nesti-use-simplex-architecture]], §2.3, §4.2, §5.3).
- The safe side owns the sensors it relies on, and leaves out inputs it cannot trust; on the rover, camera images reach only the learned side ([[2025-nesti-use-simplex-architecture]], §5.2).
- A hypervisor or kernel must keep the unsafe side from interfering with the safe side, in memory and in time ([[2025-nesti-use-simplex-architecture]], §3).
- Alternating between controllers can destabilise the system unless a state machine governs the switch, with hysteresis or similar ([[2025-nesti-use-simplex-architecture]], §3).

## State, October 2026

Demonstrated with learned controllers on a pendulum and a rover, on a hypervisor not claimed to be verified, with tests rather than proofs ([[2025-nesti-use-simplex-architecture]]).

A 2026 variant, Synergistic Simplex, lets information flow both ways: the safety layer may ask the learned layer to replan within safe bounds, and may use a learned output that is independent of the function it protects, under conditions the authors derive on paper. In simulation of a car it cut stops where an undetected obstacle lay in a neighbouring lane, with no collisions; its assumptions include static obstacles and correct lane detection ([[2026-bansal-synergistic-simplex-cooperative]]).

A 2026 research agenda uses Simplex as the runtime layer for foundation-model-enabled cyber-physical systems and names shielding (modifying single actions) as a variant beside switching; there is no demonstration and no concrete switching rule (§5.1 gives only a qualitative condition and names real-time reachability as a basis) ([[2026-zheng-assuring-learning-enabled]], §5.1). The agenda's monitor reads symbolic world-model elements, interface states and uncertainty estimates that the learned side exposes (§5.1). Our reading: closer to the relaxed form of [[2026-bansal-synergistic-simplex-cooperative]] than to the strict form; the paper does not discuss the difference.

A 2026 preprint builds the switching rule from design-time artifacts, with several certified safe controllers and a switch between them. In simulation a one-step prediction kept a ground robot within its limit when the model was matched, but on hardware only a horizon of about 15 control periods did so in every configuration ([[2026-jager-context-dependent-runtime]], §IV-C, §IV-E1).

## Open questions

- The zOS paper dates the pattern to 2001 and cites Sha 2001; [[2025-nesti-use-simplex-architecture]] dates it to 1994.
- How a monitor handles a wrong command that leaves the safe region within one step; Nesti et al. name a one-step prediction and leave it out (§4.2). Jäger et al. found one step enough only with matched dynamics; with unmodelled dynamics they tuned the horizon by experiment ([[2026-jager-context-dependent-runtime]], §IV-D).
