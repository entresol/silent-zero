---
type: source
id: 2026-heiser-mcs-safety-os
status: reviewed
read: partial
kind: survey
sources: [2026-heiser-mcs-safety-os]
updated: 2026-10-29
---

# Heiser 2026: MCS safety, an OS perspective

Gernot Heiser (UNSW Sydney). Award talk at RTAS 2026, May 2026 (venue and date from the publication list on [[2026-trustworthy-guaranteeing-timeliness-mcs]]). [Abstract and slides](https://trustworthy.systems/publications/papers/Heiser_26:rtas.abstract). There is no paper; the wiki has read the slides. A talk says more than its slides, so this page counts as a partial reading.

## What it shows

- **The requirement.** In a mixed-criticality system, certifying a critical component must not depend on the behaviour of less critical ones, so the OS must prevent any interference, in space and in time. See [[mixed-criticality]].
- **Time as a capability.** In seL4 MCS a thread no longer has a time slice but a capability to a scheduling-context object with a period T and a budget C ≤ T; a thread without a scheduling context cannot run. A passive server runs on its client's scheduling context, so the client is charged for the server's time. Budget overruns raise timeout exceptions, a policy-free mechanism; the slides list emergency budget, rollback, lowering a client's priority and, "if you must", priority inheritance as possible reactions, and mention a pending RFC for budget thresholds. The mechanism is from Lyons et al. (EuroSys 2018), cited on the slides and not yet covered here.
- **IPC cost.** A table from Mi et al. (EuroSys 2019, not yet covered here) gives round-trip cross-address-space IPC on 64-bit Intel Skylake: 986 cycles for seL4, 2,717 for Fiasco.OC and 8,157 for Google's Zircon, against 790 cycles of mandatory hardware cost.
- **Proof limits named.** Initialisation code is not verified, MMU and caches are modelled abstractly, and multicore verification is in progress.
- **WCET.** The original analysis used Chronos on Armv6 and Armv7 (32-bit) before MCS. Chronos became unmaintained and Arm stopped publishing latencies, so the analysis "bit-rotted". It has been revived with Heptane for 64-bit RISC-V and MCS, with latencies to come from the Verilog design. See [[wcet-analysis]].
- **Status of MCS, as of May 2026.** The slides give "mid-'27" for the end of the functional verification of seL4-MCS and September 2027 for a formal schedulability framework; the stated aim is "provable timeliness".
- **LionsOS.** The second half of the talk presents LionsOS: a static architecture with fine-grained components, single-threaded event handlers and lock-free single-producer, single-consumer queues. For a networking system on an i.MX8M the slides give about 400 lines for the network driver and under 1,000 lines for the shared networking system, against 3,000 and about one million lines in Linux. Verification of components with SMT solvers is "demonstrated on NIC driver"; composing the proofs is named as the challenge.

## How

Slides of an overview talk. The claims summarise the group's work and cite their sources on the slides; the LionsOS performance plots on the slides do not state their origin.

## Limits

The slides do not give methods or measurement conditions beyond what is quoted above.

A careful reader adds:

- **The MCS date is older than the proof.** "Mid-'27" was said in May 2026; the seL4 Foundation announced the proof on RISC-V on 29 June 2026 ([[2026-sel4-functional-correctness-proof]]). The slides do not say whether "mid-'27" referred to all architectures.
- **The IPC table is secondhand.** It comes from Mi et al. 2019, and the slides do not give the seL4 version or configuration measured.

## Against the wiki

- [[sel4]], [[kernel]]: **extends** them with scheduling contexts and the dates for MCS as of May 2026.
- [[wcet-analysis]]: **extends** the history. The slides name Armv6 and Armv7 for the original analysis; see the note there.
- [[mixed-criticality]]: created with this source.

## For zOS

- [[kernel]]: the paper cites this talk for "time as a protected resource" (Sections 3 and 4). The slides support it: processor time is handed out through capabilities with budgets the kernel enforces.
- Our reading: the passive-server model, where a server runs on its client's budget, bears on the broker. A broker that serves agents would be charged to the agent that calls it, not to the safety path. Whether zOS's broker should be a passive server is a design question for the static system.
- The schedulability framework due September 2027 is the step from budgets to deadlines. The paper's "a CPU budget is still no end-to-end guarantee" (Section 4) matches.
