---
type: system
status: reviewed
sources: [2023-amar-cheriot-complete-memory, 2026-moore-cheri-is-being, 2025-cheriot-cheriot-isa-1, 2026-kurd-cheri-standardisation-status]
short: CHERI capabilities on small RISC-V cores
updated: 2026-11-23
---

# CHERIoT

A 32-bit RISC-V adaptation of the CHERI capability architecture for embedded devices, co-designed with its own real-time OS. Every memory access needs a capability, a pointer that carries bounds and permissions and cannot be forged; hardware revocation adds temporal safety, so that compartments from mutually distrusting suppliers can share one core and one heap ([[2023-amar-cheriot-complete-memory]]).

## State, as published in 2023

Two cores implement it, a Flute-based prototype and CHERIoT-Ibex, derived from the Ibex core of the OpenTitan project. Measured in synthesis for 28 nm, the full CHERIoT-Ibex needs a little under 10 per cent more gates than Ibex with a 16-entry PMP; CoreMark loses 21 per cent on Ibex and 6 per cent on Flute, on Flute largely from compiler bugs, by the authors' belief. An IoT application ran on an FPGA at 20 MHz with 17.5 per cent CPU load ([[2023-amar-cheriot-complete-memory]]).

## State in November 2025: ISA 1.0

The project released version 1.0 of the specification on 3 November 2025 by the post's address. It gives December 2024 as the last ISA change, names CHERIoT Ibex 1.0 and CHERIoT Kudu as implementations (Kudu without an official release yet), and says the first chips with the Ibex-based core were returning from the fab, with mass production planned for 2026. All of this is the project's own account, without data. Version 2.0 is meant to be source-compatible with 1.0 on top of the RISC-V CHERI base, which the post calls "tentatively named Y" ([[2025-cheriot-cheriot-isa-1]]).

## What it is, and what it is not

- Isolation without an MMU, aimed at deterministic latency; no WCET analysis is reported.
- Guarantees argued from the design, with SMT checks of some properties of the capability encoding; our reading: no proof of the cores or of the RTOS switcher is reported.
- Our reading: a different route from seL4's, protection checked by the processor on every access, rather than a proven kernel managing page tables.

## Licence and code

The paper links the RTOS source on GitHub (`microsoft/CHERIoT-RTOS`); its licence is not named in the source.

## Related

[[object-capabilities]], [[risc-v]], [[opentitan]] (the Ibex core's home).

## Open questions

- Whether CHERI for RISC-V is ratified. A talk of March 2026 calls it "being standardised" ([[2026-moore-cheri-is-being]]). Slides of 6 April 2026 put the specification in architecture review before its freeze, with ratification intended for the second quarter and thought more likely in the third, and call that timetable out of date ([[2026-kurd-cheri-standardisation-status]]). The pool holds nothing later, so the state after April is not known here.
- Whether CHERIoT silicon is available beyond the one company's plan for 2026.
- Whether a zOS board could use capability hardware below seL4, and what that would add to the kernel's proofs.
