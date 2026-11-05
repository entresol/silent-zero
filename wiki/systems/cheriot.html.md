# CHERIoT

> CHERI capabilities on small RISC-V cores with its own RTOS: memory safety in hardware, measured, not proven; CHERI for RISC-V “being standardised” in 2026.

System · LLM reviewed · updated 2026-11-02 · 2 sources · https://silentzero.ooo/wiki/systems/cheriot.html

A 32-bit RISC-V adaptation of the CHERI capability architecture for embedded devices, co-designed with its own real-time OS. Every memory access needs a capability, a pointer that carries bounds and permissions and cannot be forged; hardware revocation adds temporal safety, so that compartments from mutually distrusting suppliers can share one core and one heap ([CHERIoT, complete memory safety for embedded devices](https://silentzero.ooo/wiki/sources/2023-amar-cheriot-complete-memory.html.md)).

## State, as published in 2023

Two cores implement it, a Flute-based prototype and CHERIoT-Ibex, derived from the Ibex core of the OpenTitan project. Measured in synthesis for 28 nm, the full CHERIoT-Ibex needs a little under 10 per cent more gates than Ibex with a 16-entry PMP; CoreMark loses 21 per cent on Ibex and 6 per cent on Flute, on Flute largely from compiler bugs, by the authors' belief. An IoT application ran on an FPGA at 20 MHz with 17.5 per cent CPU load ([CHERIoT, complete memory safety for embedded devices](https://silentzero.ooo/wiki/sources/2023-amar-cheriot-complete-memory.html.md)). Later developments are not yet covered here.

## What it is, and what it is not

- Isolation without an MMU, aimed at deterministic latency; no WCET analysis is reported.
- Guarantees argued from the design, with SMT checks of some properties of the capability encoding; our reading: no proof of the cores or of the RTOS switcher is reported.
- Our reading: a different route from seL4's, protection checked by the processor on every access, rather than a proven kernel managing page tables.

## Licence and code

The paper links the RTOS source on GitHub (`microsoft/CHERIoT-RTOS`); its licence is not named in the source.

## Related

[Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md), [RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md), [OpenTitan](https://silentzero.ooo/wiki/systems/opentitan.html.md) (the Ibex core's home).

## Open questions

- Whether CHERIoT hardware, or CHERI for RISC-V generally, is standardised and available. A talk of March 2026 calls it "being standardised" and lists the criteria, a Sail specification, simulation and a test suite among them, without a ratification or a date ([CHERI is being standardised](https://silentzero.ooo/wiki/sources/2026-moore-cheri-is-being.html.md)).
- Whether a Silent Zero board could use capability hardware below seL4, and what that would add to the kernel's proofs.

## Sources

- [CHERI is being standardised](https://silentzero.ooo/wiki/sources/2026-moore-cheri-is-being.html.md)
- [CHERIoT, complete memory safety for embedded devices](https://silentzero.ooo/wiki/sources/2023-amar-cheriot-complete-memory.html.md)

## Related pages

- [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md)
- [RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md)
- [OpenTitan](https://silentzero.ooo/wiki/systems/opentitan.html.md)
