# Rings

The order in which the pool's sources are worked into the wiki. The wiki needs a critical mass before it answers questions better than the pool does, so it grows from the centre outwards: first the sources the paper's design rests on, then what extends, competes with or attacks that design, then the history and the setting. Read `CLAUDE.md` in this directory first.

The rings are a guide to the order, not a gate. The run works through them in order, and within a ring from top to bottom; when one is done, it continues with the next. The team may reorder them at any time. Sources the daily run adds to the pool are worked in on the day they arrive, whatever their ring.

When a source is worked in, mark it `[x]` here in the same pull request. A source that turns out to belong to another ring moves there, and `log.md` says why.

## Ring 1 · the load-bearing sources

One group per part of the zOS design. These sources carry what the paper claims as proven or tested, or they name the threat the design answers. After this ring every `zos/` page exists.

### kernel

- [x] 2009-klein-sel4-formal-verification
- [x] nd-sel4-verified-configurations
- [x] 2026-sel4-functional-correctness-proof
- [x] 2026-heiser-mcs-safety-os
- [x] 2026-trustworthy-guaranteeing-timeliness-mcs
- [x] 2018-klein-formally-verified-software

### static system

- [x] nd-sel4-microkit-user-manual
- [x] 2026-trustworthy-lionsos

### drivers

- [x] 2022-parker-sel4-device-driver
- [x] 2026-tyler-smt-based-deductive

### broker

- [x] 2025-debenedetti-defeating-prompt-injections
- [x] 1988-hardy-confused-deputy-or
- [x] 2006-miller-robust-composition-towards
- [x] 2026-nasr-attacker-moves-second

### safety path

- [x] 2025-nesti-use-simplex-architecture

### real-time loops

- [x] 2025-black-real-time-execution

### timing isolation

- [x] 2022-wistoff-systematic-prevention-core
- [x] 2026-trustworthy-where-are-we

### root of trust

- [x] 2026-google-opentitan-shipping-production

## Ring 2 · neighbours, rivals, attacks

Work that extends the design, competes with it or attacks its assumptions: other agent operating systems, prompt injection and MCP, AI-generated proofs, CHERI, verified drivers, real-time policies and safety filters, hardened Linux. The order within this ring is still rough.

- [x] 2023-amar-cheriot-complete-memory
- [x] 2026-anthropic-project-glasswing-securing
- [x] 2026-anthropic-project-glasswing-initial
- [x] 2026-bower-cohesix-research-operating
- [x] 2025-cnx-nuvoton-introduces-first
- [x] 2025-costa-securing-ai-agents
- [x] 2025-darpa-ai-cyber-challenge
- [x] 2022-google-announcing-kataos-sparrow
- [x] 2025-google-building-next-generation
- [x] 2023-greshake-not-what-you
- [x] 2026-he-neuro-symbolic-proof
- [x] 2025-heiser-fast-secure-adaptable
- [x] 2026-hubbard-agentos-operating-system
- [x] 2024-lattuada-verus-practical-foundation
- [ ] 2026-lide-arsenal-assured-robotics
- [ ] nd-linux-landlock-unprivileged-access
- [ ] nd-linux-real-time-preemption
- [ ] 2019-markettos-thunderclap-exploring-vulnerabilities
- [ ] 2026-moore-cheri-is-being
- [ ] nd-sel4-sel4-roadmap
- [ ] 2024-trail-leftoverlocals-listening-llm
- [ ] nd-trustworthy-proof-statistics
- [ ] 2025-vander-rust-android-move
- [ ] 2025-yang-autoverus-automated-proof
- [ ] 2026-zhang-agent-libos-runtime
- [ ] 2026-zhao-agenticos-intent-oriented
- [ ] 2026-ke-quine-realizing-llm
- [ ] 2026-narisetty-adaptive-evaluation-out
- [ ] 2026-maloyan-breaking-protocol-security
- [ ] 2026-huang-model-context-protocol
- [ ] 2026-he-neuro-symbolic-proof-osdi
- [ ] 2024-zhang-selene-pioneering-automated
- [ ] 2025-li-osvbench-benchmarking-llms
- [ ] 2025-tu-agentic-verification-software
- [ ] 2025-zhao-verifying-device-drivers
- [ ] 2026-sison-two-interfaces-sel4
- [ ] 2024-wistoff-fence-t-s
- [ ] 2026-lu-faster-rethinking-real
- [ ] 2026-wang-real-time-robot
- [ ] 2026-liu-learning-native-continuation
- [ ] 2026-sel4-sel4-16-0
- [ ] 2026-kurd-cheri-standardisation-status
- [ ] 2025-cheriot-cheriot-isa-1
- [ ] 2026-owasp-owasp-mcp-top
- [ ] 2026-elisa-enabling-linux-safety
- [ ] 2025-hu-vlsa-vision-language
- [ ] 2026-park-your-model-already
- [ ] 2026-tsinghua-libero-safety-comprehensive
- [ ] 2026-unverified-silent-failures-physical
- [ ] 2026-unverified-autoreal-seL4-proof

### firmware and boot, core · worked in on 2026-10-30

The sources that carry the paper's firmware, bootloader and root-of-trust layers.

- [x] nd-coreboot-architecture
- [x] nd-coreboot-vboot
- [x] nd-coreboot-measured-boot
- [x] nd-tfa-firmware-design
- [x] nd-opensbi
- [x] nd-uboot-verified-boot
- [x] nd-raspberrypi-boot
- [x] nd-sel4-x64-platform
- [x] nd-chromeos-verified-boot
- [x] nd-caliptra
- [x] 2018-cook-model-checking-boot
- [x] 2020-straznickas-verified-first-stage
- [x] 2021-tao-dice-formally-verified
- [x] 2022-zhang-pa-boot-formally

### firmware and boot, periphery

Vendor firmware, distributions and other platforms; for the daily run once the team opens it.

- [ ] nd-coreboot-payloads
- [ ] nd-coreboot-amd-psp
- [ ] nd-coreboot-intel-fsp
- [ ] nd-intel-fsp-binaries
- [ ] nd-amd-opensil
- [ ] nd-me-cleaner
- [ ] nd-heads
- [ ] nd-linuxboot
- [ ] nd-oreboot
- [ ] nd-dasharo-overview
- [ ] nd-apple-boot-apple-silicon
- [ ] nd-apple-startup-disk-policy
- [ ] nd-asahi-m1n1
- [ ] 2023-tcg-pc-client-firmware-profile

## Ring 3 · history and setting

Foundations, history of the field, regulation, the robot. Needed for concept pages and context, not for the state of a `design/` page.

- [ ] nd-openbios (moved from ring 2 on 2026-10-30: Open Firmware, last release 2013, history)
- [ ] 2001-sha-using-simplicity-control (moved from ring 1 on 2026-10-29: the pattern goes back to 1994 and is history for the bare minimum; no open copy)
- [ ] 1966-dennis-programming-semantics-multiprogrammed
- [ ] 1972-anderson-computer-security-technology
- [ ] 1982-lamport-byzantine-generals-problem
- [ ] 1991-torvalds-posting-comp-os
- [ ] 1993-liedtke-improving-ipc-kernel
- [ ] 1999-dibona-open-sources-voices
- [ ] 2016-heiser-l4-microkernels-lessons
- [ ] 2016-w3c-25-years-ago
- [ ] 2017-tanenbaum-open-letter-intel
- [ ] 2012-felt-android-permissions-user
- [ ] 2017-fonseca-empirical-study-correctness
- [ ] nd-apple-xnu-kernel-source
- [ ] 2025-anthropic-donating-model-context
- [ ] 2025-leemhuis-zahlen-bitte-linux
- [ ] 2023-eu-machinery-regulation-2023-1230
- [ ] 2025-iso-iso-10218-2025
- [ ] nd-tinkerforge-servo-bricklet-2
- [ ] 2026-pib-pib-backend-software

## Outside the pool

Systems and sources the wiki will need that the pool lacks. They go into the pool first, as any new source does; this list only keeps them in view.

- Blackham et al. 2011 (RTSS): seL4 WCET on ARM11, named in `log.md` on 2026-10-25.
- Lyons et al. 2018 (EuroSys): scheduling-context capabilities, the mechanism behind MCS.
- Mi et al. 2019 (EuroSys), SkyBridge: the IPC comparison of seL4, Fiasco.OC and Zircon.
- Sewell et al. 2011 (integrity), Murray et al. 2013 (information flow), Sewell et al. 2013 (binary verification), Sewell et al. 2016 (loop bounds for WCET): the proofs beyond functional correctness.
- Åman Pohjola et al. 2023 (PLOS), Pancake; Ryzhyk et al. 2009 (EuroSys), Dingo; Murphy et al. 2025 (PLOS), device specifications from Verilog: the driver line.
- Greshake et al. 2023 is in the pool (ring 2) but the paper's confused-deputy argument for agents leans on it; candidate to move into ring 1.
- Sha, Rajkumar and Gagliardi 1994 (ISSAT) and Seto et al. 1998 (ACC): the origin of Simplex as cited by Nesti et al. 2025; the paper dates Simplex to Sha 2001.
- Fuchsia and Zircon: a capability-based system by a large vendor that shipped and lost its backing; for [[sel4]]'s neighbours and the static system. Research of 2026-10-28.

## Done before the rings

- [x] 2026-sillitoe-resurrecting-sel4-wcet
- [x] nd-trustworthy-wcet-worst-case
