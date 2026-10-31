---
type: source
id: 2022-google-announcing-kataos-sparrow
status: reviewed
read: full
kind: report
sources: [2022-google-announcing-kataos-sparrow]
updated: 2026-10-31
---

# Google 2022: Announcing KataOS and Sparrow

Sam, Scott and June, AmbiML developers at Google; Google Open Source Blog, 14 October 2022. [Post](https://opensource.googleblog.com/2022/10/announcing-kataos-and-sparrow.html). Read from the page as saved on 23 October 2026.

## What it shows

- **Goal.** The team sets out to build a provably secure platform for embedded devices that run machine-learning applications and collect data such as images and voice recordings; the post calls it an ongoing project "with plenty left to do".
- **KataOS** builds on seL4, chosen because it "puts security front and center", and uses the CAmkES framework for statically defined, analysable components. It is written "almost entirely in Rust".
- **What was released:** most core pieces on GitHub, among them Rust frameworks such as the `sel4-sys` crate for seL4 system calls, an alternative root server in Rust for dynamic system-wide memory management, and kernel modifications to seL4 that reclaim the root server's memory. Simulation and GDB debugging came through Antmicro's Renode.
- **Not released:** KataOS can load and run third-party applications built outside CAmkES, internally; the components for that were not on GitHub, which the post hopes to publish "in the near future".
- **Sparrow**, a reference implementation, is to combine KataOS with a root of trust built with OpenTitan on RISC-V; the first release targeted 64-bit Arm in QEMU simulation. The aim is to open-source all of Sparrow, hardware and software.

## How

A project announcement: goals, a list of released components and plans. No measurements.

## Limits

A careful reader adds:

- **Strong wording.** The post says seL4 is "mathematically proven secure, with guaranteed confidentiality, integrity, and availability", and that it is "logically impossible" for applications to breach the kernel's hardware security protections and that the system components are "verifiably secure". Our reading: seL4's proofs hold for its verified configurations and under their assumptions ([[nd-sel4-verified-configurations]]); the post names no proof for the Rust root server, the kernel modifications or the CAmkES components, and none for availability.
- **Modified kernel.** Memory reclamation needed changes to seL4; whether they are covered by its proofs, the post does not say.
- **An announcement from 2022.** What became of KataOS and Sparrow later is not in this source.

## Against the wiki

- [[kataos]]: created with this source.
- [[sel4]]: an early system on seL4 aimed at machine-learning devices; Rust above a verified C kernel.
- [[opentitan]]: Sparrow planned OpenTitan as its root of trust, more than two years before fabrication of the Nuvoton chip began.

## For zOS

Section 5 of the paper: "Google's KataOS paired seL4 with Rust for machine-learning devices (Google 2022)". Confirmed. No `design/` page changes state. Our reading: KataOS is the closest earlier attempt at a verified base for devices that run models, and it chose a dynamic root server, where zOS chooses a static system.
