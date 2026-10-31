---
type: concept
status: reviewed
sources: [2025-nesti-use-simplex-architecture]
glossary: Simplex architecture
updated: 2026-10-29
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

## Open questions

- The zOS paper dates the pattern to 2001 and cites Sha 2001; [[2025-nesti-use-simplex-architecture]] dates it to 1994.
- How a monitor handles a wrong command that leaves the safe region within one step; Nesti et al. name a one-step prediction and leave it out (§4.2).
