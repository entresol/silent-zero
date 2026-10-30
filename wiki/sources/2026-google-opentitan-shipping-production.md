---
type: source
id: 2026-google-opentitan-shipping-production
status: reviewed
read: full
kind: report
sources: [2026-google-opentitan-shipping-production]
updated: 2026-10-29
---

# Google 2026: OpenTitan shipping in production

Cyrus Stoller and Miguel Osorio (OpenTitan), Google Open Source Blog, 4 March 2026. [Post](https://opensource.googleblog.com/2026/03/opentitan-shipping-in-production.html).

## What it shows

- **Shipping.** OpenTitan "is now shipping in commercially available Chromebooks". The first part is made by Nuvoton.
- **What it is.** The post calls OpenTitan the first open-source silicon root of trust. Google built it over seven years with the open-source community, and the non-profit lowRISC C.I.C. maintains it. It can be bought from a partner or manufactured independently.
- **Features named.** Secure boot with post-quantum signatures (SLH-DSA), which the post calls a first for a commercially available open-source root of trust; ownership transfer, which the post says "helps to move away from co-signing" so that owners control their own update schedule.
- **Quality claims.** Functional and code coverage above 90 per cent for the IP blocks and the top-level design (Earl Grey), with more than 40,000 tests run nightly.
- **Next.** Deployment in Google's data centres "expected to land later this year"; a second generation with lattice-based PQC (ML-DSA, ML-KEM); reuse of OpenTitan IP in Caliptra.

## How

A vendor announcement. It names no Chromebook models, no volumes and no independent evaluation.

## Limits

A careful reader adds:

- **The vendor's own word.** The quality figures are Google's and lowRISC's; the post links to documentation and names no audit.
- **"Verified" means testing here.** The post speaks of design verification and test coverage, in the hardware industry's sense. It does not claim formal proof.
- **A root of trust for Chromebooks.** How OpenTitan would sit in a zOS board, and which boards carry it, the post does not say.

## Against the wiki

- [[opentitan]]: created with this source.

## For zOS

- [[root-of-trust]]: the paper says OpenTitan has shipped in production Chromebooks since March 2026 (In brief, Sections 3 and 5). Confirmed as announced on 4 March 2026. The paper places the hardware and root-of-trust layer in the trusted base as *assumed* (Section 3); the post's coverage figures are the vendor's design-verification claims and do not cover the fabricated chip, so they do not change that state.
