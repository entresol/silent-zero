---
type: source
id: nd-sysgo-safety-certification
status: reviewed
read: full
kind: report
sources: [nd-sysgo-safety-certification]
updated: 2026-11-21
---

# SYSGO: PikeOS safety certification

SYSGO. "Safety Certification", a page of the vendor's website, undated, read on 21 November 2026. [Page](https://sysgo.com/safety-certification). Read in full; it is short. A vendor statement.

## What it shows

- **The list.** "PikeOS 5.1.3 Safety Certification": DO-178C DAL A, ECSS Cat. A, EN 50716 SIL 4, ISO 26262-6 ASIL D and IEC 61508 SIL 3. "PikeOS is available pre-certified by TÜV SÜD." Higher levels "on several architectures are available on request".
- **How it supports a project.** Certification kits whose artefacts carry a unique ID, end-to-end traceability from architecture to source code, support for hardware debuggers and for full MC/DC code coverage, and senior engineers who accompany a project.
- **Domains.** Avionics and defence (DO-178C), space, railway (EN 50716), automotive (ISO 26262), industrial automation (IEC 61508), and medical (IEC 62304).

## How

A page with a list and short paragraphs. No certificate numbers, dates, scopes or reports.

## Limits

The page does not say which hardware, which configuration or which version of the product the certificate covers beyond "5.1.3", or when it was issued. Our reading: "pre-certified" describes a component certified against these standards, which a robot maker still has to build into a system whose own certification is separate.

## Against the wiki

- [[safety-certification]]: **creates** the first concrete example of what a certified separation kernel states about itself.
- [[safety-path]]: **extends**, together with [[nd-sysgo-robotics-humanoids]].

## For zOS

It shows what a buyer can already get from a certified kernel, and sets the yardstick for any statement of zOS on certification. See [[pikeos]].
