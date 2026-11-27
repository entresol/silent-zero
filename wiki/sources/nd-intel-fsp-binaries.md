---
type: source
id: nd-intel-fsp-binaries
status: drafted
read: full
kind: report
sources: [nd-intel-fsp-binaries]
updated: 2026-11-27
---

# Intel FSP binaries (repository README)

The README of Intel's GitHub repository of Firmware Support Package binaries; undated. [github.com/intel/FSP](https://github.com/intel/FSP). The pool holds a snapshot of 2 November 2026. Read in full; it is a short page.

## What it shows

- **What the repository is.** A repository of FSP binaries posted by Intel, one directory per project, each with the FSP specification version it follows. It links Intel's FSP home page, a configuration editor from the EDK2 project, a wiki and a support page.
- **Coverage.** Seventeen directories, from Skylake and Braswell to Raptor Lake and the Sapphire Rapids and Ice Lake Xeon families. Most follow specification v2.0 to v2.3; Braswell and Skylake follow v1.1. Older projects are in a legacy branch.
- **Third-party parts.** The README lists three third-party components inside the Intel software, EDK2 and EDK2-Platforms (BSD-2-Clause-Patent) and OpenSSL (Apache 2.0), each with its own licence file. It states that such software may be governed by separate licence terms.

## How

A project index. The page gives no source code, no hash, no signature information and no statement on the licence of the binaries themselves.

## Limits

The page does not say what the binaries do, whether they are signed, or how Intel patches them; "memory and silicon initialisation" is our reading from [[nd-coreboot-intel-fsp]]. It gives no release dates, so the state of any platform's binary is not dated here. A careful reader adds that the licence of the binaries is the point that matters for the project, and this page does not answer it.

## Against the wiki

- [[intel-fsp]]: **extends**. The page now has Intel's own distribution point; coreboot's documentation described the component only from the integrator's side.
- [[coreboot]]: no change.

## For zOS

[[root-of-trust]]: no change of state. Our reading: for the PC profile the binaries are code a zOS loader would have to accept or avoid, and Intel publishes them as binaries.
