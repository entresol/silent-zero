---
type: source
id: 2023-amar-cheriot-complete-memory
status: reviewed
read: full
kind: measurement
sources: [2023-amar-cheriot-complete-memory]
updated: 2026-10-31
---

# Amar et al. 2023: CHERIoT, complete memory safety for embedded devices

Saar Amar, David Chisnall, Tony Chen, Nathaniel Wesley Filardo, Ben Laurie, Kunyan Liu, Robert Norton, Simon W. Moore, Yucong Tao, Robert N. M. Watson and Hongyan Xia (Microsoft, Google, University of Cambridge, Arm). Proc. MICRO '23, Toronto. [Paper](https://www.microsoft.com/en-us/research/publication/cheriot-complete-memory-safety-for-embedded-devices/). Read from the authors' PDF (13 pages).

## What it shows

- **The claim.** A 32-bit adaptation of the CHERI capability architecture, co-designed with a new ("green-field") real-time OS, gives "complete and deterministic" memory safety between compartments: spatial and temporal, for heap, stack and globals, while keeping C/C++ source compatibility (abstract, §1, §6). The authors define eight things one compartment must not be able to do to another's objects, among them using freed memory or keeping a pointer passed for a single call (§2.3).
- **Real time as a design rule.** No hardware operation has nondeterministic latency, and the design avoids MMUs and caches on hot paths (§2, §2.1). Sentry capabilities state which code runs with interrupts disabled, so a compartment can be allowed to call one function with interrupts off without being able to switch them off at will (§3.1.2).
- **Small trusted code.** The RTOS primitives that enforce compartment calls, returns and preemptive multitasking total "a little over 300 hand-written instructions"; the heap allocator is a separate compartment (§2.3, §2.6). Compartments are statically linked into one image (§2.6).
- **Temporal safety in hardware.** Each 8-byte heap granule has a revocation bit, 1.56 per cent of heap SRAM. A load filter in the pipeline invalidates every capability that points to freed memory as it is loaded, and a background revoker sweeps memory in spare load-store cycles (§3.3).
- **Capabilities in 64 bits.** A new encoding fits 12 permissions into 6 bits and keeps 9 bits of bounds precision, which cuts average internal fragmentation to about 0.19 per cent; some properties of the encoding were checked with Sail's SMT backend, not elaborated (§3.2).
- **Area and power** (CHERIoT-Ibex, TSMC 28 nm, Table 2): the plain RV32E core has 26,988 gates; with a 16-entry PMP 55,905; with capabilities, load filter and background revoker 61,422, a little under 10 per cent above the PMP variant. Power estimates are called preliminary, with "a potentially large margin of error" (§7.1).
- **Speed** (CoreMark per MHz, Table 3): capabilities cost 5.73 per cent on the Flute core and 13.18 per cent on Ibex; with the load filter, Ibex loses 21.28 per cent, Flute nothing more. The authors believe that much of the Flute overhead comes from two known compiler bugs, "but some is unavoidable" (§7.2, §7.2.1).
- **An end-to-end application:** a compartmentalised network stack (FreeRTOS TCP/IP, mbedTLS, MQTT), and JavaScript bytecode fetched from Azure IoT Hub and run in a separate interpreter compartment, on CHERIoT-Ibex at 20 MHz on an FPGA, used 17.5 per cent of the CPU averaged over a minute (§7.2.3).

## How

Two cores implement the ISA: a prototype on the Flute five-stage pipeline and CHERIoT-Ibex, derived from the Ibex core maintained in the OpenTitan project (§4). Area and power come from synthesis for 28 nm; performance from CoreMark, an allocation microbenchmark and the IoT application.

## Limits

What the authors say themselves: power figures are pre-silicon estimates; the compiler had two unfixed bugs that inflate the performance and code-size numbers, which should be treated as "worst-case" (§7.1, §7.2). Memory safety enforced by RTOS and architecture covers the cross-compartment case; inside a compartment it depends on the compiler (§2.3). Representable range is smaller than in other CHERI encodings, which some C pointer arithmetic could trip; they found no case in their corpus (§3.2.3). Multicore systems would need the revoker to snoop all cores' memory traffic (§3.3.3). Rust support is planned (§8).

A careful reader adds:

- **Measured, not proven.** The guarantees follow from the design and are argued in the paper; apart from SMT checks of the encoding, no proof of the ISA, the cores or the switcher is reported here.
- **No silicon in this paper.** Every figure is from synthesis, simulation or an FPGA board.
- **The allocator and switcher are trusted.** The paper calls the allocator and scheduler "partially-trusted" compartments and the switcher trusted (§1); the guarantees rest on them.

## Against the wiki

- [[object-capabilities]]: extends it with capabilities enforced by the processor on every memory access, beside seL4's kernel capabilities.
- [[time-protection]], [[wcet-analysis]]: the design aims at deterministic latency, but the paper reports no WCET analysis.
- [[cheriot]]: created with this source.

## For zOS

The paper's Table 1 (Section 5) cites this source: "CHERIoT pairs CHERI with a clean-slate embedded OS". Confirmed; the authors call it a "green-field, security-centric RTOS". The same row says standardisation for RISC-V is under way, citing another source not yet covered. No `design/` page changes state. Our reading: CHERIoT is evidence for a different route to the same goal, isolation without an MMU and with real time in mind, enforced in hardware rather than proven in a kernel.
