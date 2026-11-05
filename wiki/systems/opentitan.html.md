# OpenTitan

> Open-source silicon root of trust, shipping in Chromebooks since March 2026.

System · LLM reviewed · updated 2026-10-31 · 5 sources · https://silentzero.ooo/wiki/systems/opentitan.html

An open-source silicon root of trust, developed by Google with an open community over seven years and maintained by the non-profit lowRISC C.I.C. ([OpenTitan shipping in production](https://silentzero.ooo/wiki/sources/2026-google-opentitan-shipping-production.html.md)).

## State, October 2026

Shipping in commercially available Chromebooks since the announcement of 4 March 2026, as a part made by Nuvoton. It supports secure boot with post-quantum signatures (SLH-DSA) and ownership transfer. Deployment in Google's data centres was expected later in 2026, and a second generation with lattice-based PQC is in development ([OpenTitan shipping in production](https://silentzero.ooo/wiki/sources/2026-google-opentitan-shipping-production.html.md)).

In February 2025 Google announced the start of fabrication of the Nuvoton chip, the first production-ready OpenTitan part, with mass production planned from spring 2025 and Chromebooks and data centres later that year ([Nuvoton's OpenTitan chip](https://silentzero.ooo/wiki/sources/2025-cnx-nuvoton-introduces-first.html.md)). In 2022 Google's Sparrow project planned to pair [KataOS](https://silentzero.ooo/wiki/systems/kataos.html.md) on seL4 with an OpenTitan root of trust on RISC-V ([Announcing KataOS and Sparrow](https://silentzero.ooo/wiki/sources/2022-google-announcing-kataos-sparrow.html.md)).

## Evidence

Functional and code coverage above 90 per cent and more than 40,000 nightly tests, as stated by the project ([OpenTitan shipping in production](https://silentzero.ooo/wiki/sources/2026-google-opentitan-shipping-production.html.md)). No formal proof is claimed.

## Licence and code

Open source on GitHub, as stated in [OpenTitan shipping in production](https://silentzero.ooo/wiki/sources/2026-google-opentitan-shipping-production.html.md); the licence is not named there.

## Related

The Ibex core maintained in the OpenTitan project is the base of CHERIoT-Ibex ([CHERIoT, complete memory safety for embedded devices](https://silentzero.ooo/wiki/sources/2023-amar-cheriot-complete-memory.html.md), §4); see [CHERIoT](https://silentzero.ooo/wiki/systems/cheriot.html.md).

Caliptra provides a root of trust for measurement integrated into data-centre SoCs rather than as a separate chip ([Caliptra](https://silentzero.ooo/wiki/sources/nd-caliptra.html.md)); the OpenTitan announcement says OpenTitan IP is being reused for it ([OpenTitan shipping in production](https://silentzero.ooo/wiki/sources/2026-google-opentitan-shipping-production.html.md)).

## Open questions

- Which boards outside Chromebooks carry OpenTitan, and how a Silent Zero board would get one. See [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md).

## Sources

- [Announcing KataOS and Sparrow](https://silentzero.ooo/wiki/sources/2022-google-announcing-kataos-sparrow.html.md)
- [Caliptra](https://silentzero.ooo/wiki/sources/nd-caliptra.html.md)
- [CHERIoT, complete memory safety for embedded devices](https://silentzero.ooo/wiki/sources/2023-amar-cheriot-complete-memory.html.md)
- [Nuvoton's OpenTitan chip](https://silentzero.ooo/wiki/sources/2025-cnx-nuvoton-introduces-first.html.md)
- [OpenTitan shipping in production](https://silentzero.ooo/wiki/sources/2026-google-opentitan-shipping-production.html.md)

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [CHERIoT](https://silentzero.ooo/wiki/systems/cheriot.html.md)
- [KataOS](https://silentzero.ooo/wiki/systems/kataos.html.md)
