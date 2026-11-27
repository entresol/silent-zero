# Intel FSP binaries (repository README)

> Intel’s repository of FSP binaries, seventeen platform directories; the binaries’ licence not stated. report, full text.

Source · LLM reviewed · updated 2026-11-27 · https://silentzero.ooo/wiki/sources/nd-intel-fsp-binaries.html

The README of Intel's GitHub repository of Firmware Support Package binaries; undated. [github.com/intel/FSP](https://github.com/intel/FSP). The pool holds a snapshot of 2 November 2026. Read in full; it is a short page.

## What it shows

- **What the repository is.** A repository of FSP binaries posted by Intel, one directory per project, each with the FSP specification version it follows. It links Intel's FSP home page, a configuration editor from the EDK2 project, a wiki and a support page.
- **Coverage.** Seventeen directories, covering Core parts from Skylake to Raptor Lake, Atom and Pentium/Celeron parts (Braswell, Apollo Lake, Denverton, Elkhart Lake) and Xeon parts (Cooper Lake, Ice Lake-SP and -D, Sapphire Rapids). Most follow specification v2.0 to v2.3; Braswell and Skylake follow v1.1. Older projects are in a legacy branch.
- **Third-party parts.** The README lists three third-party components inside the Intel software, EDK2 and EDK2-Platforms (BSD-2-Clause-Patent) and OpenSSL (Apache 2.0), each with its own licence file. It states that such software may be governed by separate licence terms.

## How

A project index. The page gives no source code, no hash, no signature information and no statement on the licence of the binaries themselves.

## Limits

The page does not say what the binaries do, whether they are signed, or how Intel patches them; "memory and silicon initialisation" is our reading from [coreboot: Intel FSP documentation](https://silentzero.ooo/wiki/sources/nd-coreboot-intel-fsp.html.md). It gives no release dates, so the state of any platform's binary is not dated here. A careful reader adds that the README lists specification versions (v2.2, v2.3) beyond those, 1.0 to 2.1, that coreboot's documentation links, and that the licence of the binaries is the point that matters for the project, and this page does not answer it.

## Against the wiki

- [Intel Firmware Support Package (FSP)](https://silentzero.ooo/wiki/systems/intel-fsp.html.md): **extends**. The page now has Intel's own distribution point; coreboot's documentation described the component only from the integrator's side.
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md): no change.

## For Silent Zero

[Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md): no change of state. Our reading: for the PC profile the binaries are code a Silent Zero loader would have to accept or avoid, and Intel publishes them as binaries.

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
- [Intel Firmware Support Package (FSP)](https://silentzero.ooo/wiki/systems/intel-fsp.html.md)
- [coreboot: Intel FSP documentation](https://silentzero.ooo/wiki/sources/nd-coreboot-intel-fsp.html.md)
