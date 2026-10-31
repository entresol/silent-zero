---
type: system
status: reviewed
sources: [2026-google-opentitan-shipping-production, nd-caliptra]
glossary: OpenTitan
updated: 2026-10-30
---

# OpenTitan

An open-source silicon root of trust, developed by Google with an open community over seven years and maintained by the non-profit lowRISC C.I.C. ([[2026-google-opentitan-shipping-production]]).

## State, October 2026

Shipping in commercially available Chromebooks since the announcement of 4 March 2026, as a part made by Nuvoton. It supports secure boot with post-quantum signatures (SLH-DSA) and ownership transfer. Deployment in Google's data centres was expected later in 2026, and a second generation with lattice-based PQC is in development ([[2026-google-opentitan-shipping-production]]).

## Evidence

Functional and code coverage above 90 per cent and more than 40,000 nightly tests, as stated by the project ([[2026-google-opentitan-shipping-production]]). No formal proof is claimed.

## Licence and code

Open source on GitHub, as stated in [[2026-google-opentitan-shipping-production]]; the licence is not named there.

## Related

Caliptra provides a root of trust for measurement integrated into data-centre SoCs rather than as a separate chip ([[nd-caliptra]]); the OpenTitan announcement says OpenTitan IP is being reused for it ([[2026-google-opentitan-shipping-production]]).

## Open questions

- Which boards outside Chromebooks carry OpenTitan, and how a zOS board would get one. See [[root-of-trust]].
