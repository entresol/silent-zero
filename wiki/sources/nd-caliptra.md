---
type: source
id: nd-caliptra
status: reviewed
read: partial
kind: report
sources: [nd-caliptra]
updated: 2026-10-30
---

# Caliptra

The README of the Caliptra repository of the CHIPS Alliance, read on 30 October 2026. [Repository](https://github.com/chipsalliance/Caliptra). Only the README was read, not the specifications it links to.

## What it shows

- **What it is.** IP and firmware for a root-of-trust block integrated into a system-on-chip: the specification, silicon logic, ROM and firmware for a "Root of Trust for Measurement (RTM)". An integration gives the SoC identity, measured boot and attestation.
- **Target.** Data-centre SoCs: CPUs, GPUs, DPUs, TPUs.
- **Licence.** Apache 2.0 for all code written for Caliptra.
- **Origin and home.** Started at the Open Compute Project, which publishes the major specification revisions; source and documentation live at the CHIPS Alliance.
- **Versions.** Released as independently versioned components (RTL, ROM, first-mutable code, runtime firmware). Version 1.3 adds a post-quantum identity chain (ML-DSA-87) in runtime firmware alone, beside the existing ECDSA chain based on DICE. Releases 2.0 and 2.1 are listed with compatible configurations; 2.0 adds firmware signatures with ML-DSA and a Caliptra subsystem, 2.1 adds ML-KEM and OCP L.O.C.K. The 2.x ROM, first-mutable and runtime documents on the main branch are marked work in progress.

## How

A project README with links to specifications and a compatibility matrix.

## Limits

A careful reader adds: the README links a software CI dashboard and a CPU design-verification coverage dashboard, which the wiki has not read; it states what Caliptra provides, not what checking showed.

## Against the wiki

- [[opentitan]]: Caliptra plays a role for data-centre SoCs that OpenTitan plays as a discrete chip; [[2026-google-opentitan-shipping-production]] says OpenTitan IP is reused in Caliptra.
- [[measured-boot]]: an integrated root of trust for measurement, related to DICE ([[2021-tao-dice-formally-verified]]).

## For zOS

- [[root-of-trust]]: Caliptra is a measurement root inside the main SoC rather than a separate chip. Our reading: for zOS boards it matters only if a chip with Caliptra reaches the embedded market; the README names data-centre SoCs only.
