# ISA 1.0 released

> CHERIoT ISA 1.0, November 2025: stable since December 2024, two implementations, first chips from the fab; the RISC-V CHERI base “tentatively Y”. report, full text.

Source · CHERIoT 2025 · LLM reviewed · updated 2026-11-23 · https://silentzero.ooo/wiki/sources/2025-cheriot-cheriot-isa-1.html

"CHERIoT 1.0 Released!", a post on the CHERIoT Platform site, dated 3 November 2025 by its address (the page text carries no date and no author name). [Post](https://cheriot.org/sail/specification/release/2025/11/03/cheriot-1.0.html). Read in full from a saved copy of the page.

## What it shows

- **The release.** Version 1.0 of the CHERIoT specification is out: the ISA, the language extensions, the compilation model and relocations. The post gives the last ISA change as December 2024 and calls the release stable enough to support in hardware for a long time.
- **Two implementations.** CHERIoT Ibex 1.0 and CHERIoT Kudu follow the specification; Kudu had no official release yet. The post says that together they show the ISA scales from three-stage single-issue to six-stage dual-issue pipelines, about the range of Arm's M profile.
- **Silicon.** The author's company, SCI, had the first of its ICENI chips with the Ibex-based core on the way back from the fab and planned mass production for the new year. The post does not speak for other companies and expects 2026 to be "exciting".
- **The RISC-V base.** RISC-V International is standardising a CHERI base, "tentatively named Y". Its composition is under discussion. CHERIoT 2.0 is to be source-compatible with 1.0 on top of that base. The `ct.` prefix is reserved for CHERIoT's own instructions, and 1.x releases may change assembler mnemonics but not the ISA.
- **Plans beyond.** The post lists plans and ideas, some firmer than others (it plans Zfinx and Zdinx and aims to add both bounds encodings; the rest it is exploring or considering): floating point in integer registers (Zfinx, Zdinx), two alternative bounds encodings, two integer sub-registers per capability, a thread ID register as compartment identifier, and a constant-time programming model after the BLACKOUT research.

## How

A release announcement by the project. It reports no measurement, no hardware figure and no proof.

## Limits

A careful reader adds:

- Stability, scaling across pipelines and the silicon schedule are the project's own statements. The post gives no data for any of them.
- It says nothing on verification of the ISA, the cores or the RTOS; the wiki has no source that reports one ([CHERIoT](https://silentzero.ooo/wiki/systems/cheriot.html.md)).
- The post is silent on timing, WCET and on any real-time guarantee.
- The date of the post comes from its address and was not confirmed elsewhere.

## Against the wiki

- [CHERIoT](https://silentzero.ooo/wiki/systems/cheriot.html.md): **extends**. The page described two cores as published in 2023; the post names the 1.0 specification and two implementations, and an ISA that stopped changing in December 2024.
- [CHERI standardisation status](https://silentzero.ooo/wiki/sources/2026-kurd-cheri-standardisation-status.html.md): both speak of a RISC-V CHERI standard under way. This post names the base "Y"; the slides give the stage of the work.

## For Silent Zero

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md): a stable embedded CHERI ISA exists and by this source's account the first chips were back from the fab and mass production was planned for 2026. The ISA is microcontroller-class, built on RV32E by the post's account. It says nothing about a CHERIoT-class design on application cores or on the 64-bit boards Silent Zero targets, although the post says the Y base is meant as a common subset that includes application cores. It says nothing about proofs.

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [CHERIoT](https://silentzero.ooo/wiki/systems/cheriot.html.md)
- [CHERI standardisation status](https://silentzero.ooo/wiki/sources/2026-kurd-cheri-standardisation-status.html.md)
