---
type: system
status: reviewed
sources: [2026-google-opentitan-shipping-production, nd-caliptra, 2025-cnx-nuvoton-introduces-first, 2022-google-announcing-kataos-sparrow, 2023-amar-cheriot-complete-memory]
glossary: OpenTitan
updated: 2026-10-31
---

# OpenTitan

An open-source silicon root of trust, developed by Google with an open community over seven years and maintained by the non-profit lowRISC C.I.C. ([[2026-google-opentitan-shipping-production]]).

## State, October 2026

Shipping in commercially available Chromebooks since the announcement of 4 March 2026, as a part made by Nuvoton. It supports secure boot with post-quantum signatures (SLH-DSA) and ownership transfer. Deployment in Google's data centres was expected later in 2026, and a second generation with lattice-based PQC is in development ([[2026-google-opentitan-shipping-production]]).

In February 2025 Google announced the start of fabrication of the Nuvoton chip, the first production-ready OpenTitan part, with mass production planned from spring 2025 and Chromebooks and data centres later that year ([[2025-cnx-nuvoton-introduces-first]]). In 2022 Google's Sparrow project planned to pair [[kataos]] on seL4 with an OpenTitan root of trust on RISC-V ([[2022-google-announcing-kataos-sparrow]]).

## Evidence

Functional and code coverage above 90 per cent and more than 40,000 nightly tests, as stated by the project ([[2026-google-opentitan-shipping-production]]). No formal proof is claimed.

## Licence and code

Open source on GitHub, as stated in [[2026-google-opentitan-shipping-production]]; the licence is not named there.

## Related

The Ibex core maintained in the OpenTitan project is the base of CHERIoT-Ibex ([[2023-amar-cheriot-complete-memory]], §4); see [[cheriot]].

Caliptra provides a root of trust for measurement integrated into data-centre SoCs rather than as a separate chip ([[nd-caliptra]]); the OpenTitan announcement says OpenTitan IP is being reused for it ([[2026-google-opentitan-shipping-production]]).

## Open questions

- Which boards outside Chromebooks carry OpenTitan, and how a zOS board would get one. See [[root-of-trust]].
