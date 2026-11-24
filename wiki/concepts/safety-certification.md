---
type: concept
status: reviewed
sources: [nd-sel4-proofs-certification, nd-sysgo-safety-certification, 2026-nvidia-announces-halos-robotics, 2026-nvidia-inside-halos-robotics, 2024-dickson-limitations-formal-verification, 2026-elisa-enabling-linux-safety]
short: Assessing a system against a safety standard
updated: 2026-11-24
---

# Safety certification

Certification is "a process to assess a system against a pre-existing standard", with verification typically a key component among other requirements ([[nd-sel4-proofs-certification]]). A proof of code and a certificate for a product are different things: our reading is that the proof is evidence and the certificate is the result of an assessment against a standard. The sources name IEC 61508 (listed for industrial automation), ISO 13849, ISO 26262 (road vehicles) and DO-178C (airborne software). In NVIDIA's account the final system certificate comes from a third-party certification agency.

## State, November 2026

- **A certified separation kernel exists as a product.** SYSGO lists PikeOS 5.1.3 for DO-178C DAL A, ISO 26262-6 ASIL D, IEC 61508 SIL 3 and others, pre-certified by TÜV SÜD; it gives no scopes ([[nd-sysgo-safety-certification]], [[pikeos]]).
- **A robot stack is on the way to certification.** TÜV Rheinland is inspecting NVIDIA's Halos for Robotics for certification readiness, and TÜV SÜD has inspected the Thor chip and Halos Core for the automotive standard ISO 26262. NVIDIA's lab issues an inspection certificate that a partner takes to a certification body for the final system certificate. No robotics certificate is claimed in the sources ([[2026-nvidia-announces-halos-robotics]], [[2026-nvidia-inside-halos-robotics]], [[nvidia-halos]]).
- **seL4 has proofs and no certificate named.** The seL4 Foundation argues that its proofs go beyond what Common Criteria EAL 7 and ISO 26262 ASIL-D require and fit DO-178C Level A evidence. Its page names no certificate or certified product and does not mention IEC 61508. It says Isabelle/HOL has, to its knowledge, not been qualified for DO-178C ([[nd-sel4-proofs-certification]], [[sel4]]).
- **A limit on proofs about the world.** An essay argues that proofs about AI systems in the physical world will stay approximate; it expects formal verification to help through proofs about approximate models ([[2024-dickson-limitations-formal-verification]]).

- **An open Linux effort aims at certification.** The Linux Foundation's ELISA project says it wants to give companies shared elements, processes and tools to develop and certify Linux-based safety systems; its February 2026 release names no standard and no certified result ([[2026-elisa-enabling-linux-safety]], [[elisa]]).

## Related

[[functional-correctness]], [[mixed-criticality]], [[safety-path]], [[nvidia-halos]], [[pikeos]], [[qnx]], [[elisa]].

## Open questions

- How a proof becomes evidence that a certification body accepts for a robot: the seL4 page argues the strength of the proofs standard by standard but states no accepted case for IEC 61508 or ISO 13849.
- Whether any seL4-based product holds a safety certificate; none appears in the wiki's sources.
- How a small open-source project would carry a certificate; none of the sources discusses it.
