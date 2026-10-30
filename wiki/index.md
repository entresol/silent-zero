---
type: index
updated: 2026-10-30
---

# zOS wiki

The catalogue of every page, with one line each. Read this first.

## zOS

- [[kernel]] · seL4 with MCS as the zOS kernel: proven (C-level correctness; MCS functional correctness on RISC-V), not stated for MCS (integrity, confidentiality), tested (HACMS), assumed (boot, IOMMU); no WCET bound on any 64-bit core yet. 11 sources.
- [[static-system]] · one description, one image: what Microkit checks, what is not proved, and the run-time swap in LionsOS, the kernel underneath. 5 sources.
- [[broker]] · the only component that hands out authority: capability patterns, CaMeL, why model-based defences fail; nothing proven yet. 9 sources.
- [[real-time-loops]] · the loops that move the motors: asynchronous chunks from slow models, observed timings, no proven bound yet. 6 sources.
- [[safety-path]] · Simplex in zOS: the agent proposes, the loop disposes; tested, not proven; the paper's 2001 date disputed by a 1994 origin. 3 sources.
- [[root-of-trust]] · the firmware below the kernel on Arm, RISC-V, PC and Raspberry Pi; OpenTitan, Caliptra, DICE; all *assumed* in the paper's terms. 12 sources.
- [[bootloader]] · where the zOS loader sits on each platform, signed and measured boot, proofs about boot code so far; the loader itself unproven. 13 sources.
- [[drivers]] · user-mode drivers, the first verified Ethernet driver, DMA and the IOMMU as assumed. 7 sources.

## Not yet covered

The zOS part *agents* has no page yet. Firmware on PCs (Intel ME, AMD PSP, FSP, open alternatives) and on Apple silicon is in the backlog. Also not yet covered: the seL4 roadmap and multicore, CHERI, DMA attacks and the IOMMU, the seams between proven parts, information-flow control for agents, the driver island, and competing agent operating systems.

## Systems

- [[sel4]] · the verified microkernel zOS builds on: proofs per architecture, cost, MCS, timing, HACMS. 8 sources.
- [[microkit]] · the build system for static seL4 systems: protection domains, channels, budgets, one image. 3 sources.
- [[lionsos]] · static OS from small components on seL4 and Microkit; first driver verified. 4 sources.
- [[coreboot]] · open firmware in stages with a fixed payload; verified and measured boot; closed vendor parts on x86. 3 sources.
- [[tf-a]] · Arm's reference firmware; BL31 stays resident at EL3 below the kernel. 2 sources.
- [[opensbi]] · RISC-V firmware in machine mode below the kernel. 1 source.
- [[raspberry-pi]] · the pib's board: closed ROM and EEPROM boot, secure-boot key in OTP on the Pi 4, seL4 verified without MCS. 3 sources.
- [[opentitan]] · open-source silicon root of trust, shipping in Chromebooks since March 2026. 2 sources.
- [[cva6]] · open 64-bit RISC-V core whose design lets latency bounds be proved; fence.t prototype. 5 sources.

## Concepts

- [[wcet-analysis]] · upper bounds on execution time, what they need, and where seL4 stands. 6 sources.
- [[functional-correctness]] · what seL4's refinement proof gives, what it assumes, where it holds. 4 sources.
- [[object-capabilities]] · references that both designate and authorise; permission versus authority; caretaker and membrane. 3 sources.
- [[confused-deputy]] · a program misusing one party's authority for another's request; capabilities as the remedy. 2 sources.
- [[prompt-injection]] · instructions hidden in data an agent reads; heuristic defences fail, defences around the model hold within limits. 2 sources.
- [[verified-boot]] · each stage checks the next against a key the attacker cannot change; proofs about boot code so far. 6 sources.
- [[measured-boot]] · each stage records what runs next; TPM and DICE; a verified DICE implementation. 4 sources.
- [[time-protection]] · closing timing channels between domains; prototypes on CVA6, proof for seL4 in progress. 3 sources.
- [[simplex]] · a simple safe controller guarding an untrusted one; tested with learned controllers. 1 source.
- [[action-chunking]] · slow robot models emitting action sequences for a fast loop; no bound on delay. 1 source.
- [[mixed-criticality]] · software of different criticality on one platform; processor time as a capability in seL4 MCS. 3 sources.

## Sources

- [[2026-sillitoe-resurrecting-sel4-wcet]] · seL4's WCET analysis runs again on RV64 MCS, with placeholder values; sound CVA6 latencies expected Q1 2027. progress, full text.
- [[nd-trustworthy-wcet-worst-case]] · the archived project page: the sound ARM11 analysis and why it stopped. report, full text.
- [[2009-klein-sel4-formal-verification]] · the first proof that seL4's C code implements its specification; assumptions, cost, bugs found. proof, full text.
- [[2018-klein-formally-verified-software]] · HACMS: security by architecture on seL4, a helicopter's mission computer under attack in flight. test, full text.
- [[nd-sel4-verified-configurations]] · which properties are proved on which architecture; boot and IOMMU outside every proof. report, full text.
- [[2026-sel4-functional-correctness-proof]] · MCS functional correctness proved on RISC-V, June 2026; Arm next. report, full text.
- [[2026-heiser-mcs-safety-os]] · mixed criticality on seL4: scheduling contexts, WCET, MCS dates, LionsOS. survey, slides only.
- [[2026-trustworthy-guaranteeing-timeliness-mcs]] · the project to get from budgets to provable deadlines on RISC-V. progress, full text.
- [[nd-sel4-microkit-user-manual]] · Microkit 2.3.0: the static model, its rules for real time, build-time checks, what is not enforced. report, main chapters (board notes and API skimmed).
- [[2026-trustworthy-lionsos]] · LionsOS 0.4.0: composable components, static with a run-time swap, verification under way. report, full text (introduction page).
- [[2022-parker-sel4-device-driver]] · the seL4 device driver framework: user-level drivers, lock-free queues, performance claims. measurement, slides only.
- [[2026-tyler-smt-based-deductive]] · a LionsOS Ethernet driver proved with SMT-based verification: four properties, three bugs, 11.5 person-weeks. proof, full text.
- [[2022-wistoff-systematic-prevention-core]] · fence.t on CVA6: resetting all non-architectural state closes on-core timing channels at under 1 % cost. measurement, full text.
- [[2026-trustworthy-where-are-we]] · time protection for seL4: proof approach revised, one-way channels on RISC-V. progress, slides and abstract.
- [[2025-nesti-use-simplex-architecture]] · Simplex with learned controllers on a pendulum and a rover, isolated by a hypervisor. test, full text.
- [[2025-black-real-time-execution]] · real-time chunking keeps task throughput under up to 200 ms of extra delay, where synchronous chunking pauses. measurement, full text.
- [[2026-google-opentitan-shipping-production]] · OpenTitan ships in Chromebooks, March 2026. report, full text.
- [[1988-hardy-confused-deputy-or]] · the compiler that overwrote the billing file: why capabilities bundle naming and permission. position, full text.
- [[2006-miller-robust-composition-towards]] · object capabilities, permission versus authority, revocable grants, revocation across machines. design, chapters 1–3, 8, 9, 11, 12.
- [[2025-debenedetti-defeating-prompt-injections]] · CaMeL: capabilities and policies around an untrusted model; 77 % utility, no successful attacks within its threat model. test, main text and appendices D, E, I.
- [[2026-nasr-attacker-moves-second]] · adaptive attacks break 12 prompt-injection and jailbreak defences, most above 90 %. test, full text.
- [[nd-coreboot-architecture]] · coreboot's stages from bootblock to a payload fixed at build time. report, full text.
- [[nd-coreboot-vboot]] · verified boot rooted in write-protected flash, A/B slots, automatic recovery. report, full text.
- [[nd-coreboot-measured-boot]] · TPM measurements, a software-rooted first measurement, vendor hardware roots behind it. report, full text.
- [[nd-chromeos-verified-boot]] · Chromium OS's design: against the opportunistic attacker, the owner keeps control, rollback a weakness. design, full text.
- [[nd-tfa-firmware-design]] · Arm's boot stages BL1 to BL33; BL31 resident at EL3. report, cold boot and runtime services.
- [[nd-opensbi]] · the SBI reference firmware for RISC-V machine mode. report, README.
- [[nd-uboot-verified-boot]] · signed FIT images; the public key must be unchangeable. report, full text.
- [[nd-raspberrypi-boot]] · ROM and EEPROM bootloader on Pi 4 and 5; secure-boot key hash in the Pi 4's OTP. report, boot chapters.
- [[nd-sel4-x64-platform]] · seL4 on PCs boots through a Multiboot loader. report, full text.
- [[nd-caliptra]] · open root of trust for measurement inside data-centre SoCs. report, README.
- [[2018-cook-model-checking-boot]] · 783 lines of AWS boot code proved memory safe by bounded model checking. proof, full text.
- [[2020-straznickas-verified-first-stage]] · a RISC-V measurement root in Coq that signs what it loads; theorem stated, not fully proved. progress, full text.
- [[2021-tao-dice-formally-verified]] · DICE, verify-and-measure boot, verified at the level of generated C; on an STM32. proof, full text.
- [[2022-zhang-pa-boot-formally]] · processor authentication for multi-chip secure boot, proved in Isabelle/HOL. proof, main sections.
