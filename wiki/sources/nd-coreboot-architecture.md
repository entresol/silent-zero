---
type: source
id: nd-coreboot-architecture
status: reviewed
read: full
kind: report
sources: [nd-coreboot-architecture]
updated: 2026-10-30
---

# coreboot: architecture and boot stages

A page of the coreboot documentation (version 26.09), undated, read on 30 October 2026. [Page](https://doc.coreboot.org/getting_started/architecture.html).

## What it shows

- **Stages.** coreboot is built from separate binaries, its stages, stored in its own file system (CBFS); each stage loads the next. In order: bootblock, verstage (with verified boot), romstage, postcar, ramstage, payload.
- **Bootblock.** The first stage after CPU reset, written in assembly. It prepares a C environment by using the CPU cache as RAM, and on x86 it applies microcode updates, sets up a timer and switches from 16-bit real mode to 32-bit protected mode.
- **Verstage** "is where the root-of-trust starts". The page assumes it "cannot be overwritten in-field (together with the public key)"; it verifies each file before it is loaded from CBFS, which allows trusted firmware updates with a fail-safe recovery mode.
- **Romstage** initialises DRAM; **postcar** leaves cache-as-RAM; **ramstage** initialises PCI, on-chip devices, the TPM if verstage has not, optionally graphics, and the CPU including SMM. It writes the tables the next stage reads (ACPI, SMBIOS, coreboot tables, device-tree updates on Arm) and locks down the hardware: write protection of the boot medium, security registers, SMM.
- **Payload.** The software that runs after coreboot. It lives in CBFS, "and there's no possibility to choose it at runtime".

## How

Developer documentation; it describes the design and makes no measurements.

## Limits

A careful reader adds: the page describes the open part of the chain. What runs before the bootblock, such as microcode and vendor firmware on x86, is mentioned only as the microcode updates the bootblock applies.

## Against the wiki

- [[coreboot]]: created with this source.

## For zOS

- [[bootloader]]: a zOS loader on a PC could sit where the payload sits. Our reading: a payload fixed in CBFS matches the paper's "no menu" (Section 3), since nothing is chosen at run time; coreboot itself has a fail-safe recovery mode, so the paper's "no fallback" does not carry over.
- [[root-of-trust]]: this page calls the verstage the start of the root of trust; the bootblock runs before it, and [[nd-coreboot-vboot]] places the root in the whole read-only part of the flash, bootblock included.
