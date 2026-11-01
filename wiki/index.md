---
type: index
updated: 2026-11-01
---

# zOS wiki

The catalogue of every page, with one line each. Read this first.

## zOS

- [[kernel]] · seL4 with MCS as the zOS kernel: proven (C-level correctness; MCS functional correctness on RISC-V), not stated for MCS (integrity, confidentiality), tested (HACMS), assumed (boot, IOMMU); no WCET bound on any 64-bit core yet. 12 sources.
- [[static-system]] · one description, one image: what Microkit checks, what is not proved, and the run-time swap in LionsOS, the kernel underneath. 5 sources.
- [[broker]] · the only component that hands out authority: capability patterns, CaMeL and FIDES, why model-based defences fail; nothing proven yet. 13 sources.
- [[real-time-loops]] · the loops that move the motors: asynchronous chunks from slow models, observed timings, no proven bound yet. 7 sources.
- [[safety-path]] · Simplex in zOS: the agent proposes, the loop disposes; tested, not proven; the paper's 2001 date disputed by a 1994 origin. 4 sources.
- [[root-of-trust]] · the firmware below the kernel on Arm, RISC-V, PC and Raspberry Pi; OpenTitan, Caliptra, DICE; all *assumed* in the paper's terms. 12 sources.
- [[bootloader]] · where the zOS loader sits on each platform, signed and measured boot, proofs about boot code so far; the loader itself unproven. 16 sources.
- [[drivers]] · user-mode drivers, the first verified Ethernet driver, DMA and the IOMMU as assumed. 8 sources.

## Not yet covered

The zOS part *agents* has no page yet. Firmware on PCs (Intel ME, AMD PSP, FSP, open alternatives) and on Apple silicon is in the backlog. Also not yet covered: the seL4 roadmap and multicore, the standardisation of CHERI for RISC-V, DMA attacks and the IOMMU, the seams between proven parts, the driver island, and most competing agent operating systems.

## Systems

- [[sel4]] · the verified microkernel zOS builds on: proofs per architecture and platform, cost, MCS, timing, HACMS. 11 sources.
- [[microkit]] · the build system for static seL4 systems: protection domains, channels, budgets, one image. 3 sources.
- [[lionsos]] · static OS from small components on seL4 and Microkit; first driver verified. 5 sources.
- [[coreboot]] · open firmware in stages with a fixed payload; verified and measured boot; closed vendor parts on x86. 3 sources.
- [[tf-a]] · Arm's reference firmware; BL31 stays resident at EL3 below the kernel. 2 sources.
- [[opensbi]] · RISC-V firmware in machine mode below the kernel. 3 sources.
- [[raspberry-pi]] · the pib's board: closed ROM and EEPROM boot, secure-boot key in OTP on the Pi 4, seL4 verified without MCS. 4 sources.
- [[opentitan]] · open-source silicon root of trust, shipping in Chromebooks since March 2026. 5 sources.
- [[agentos]] · seL4-based I/O platform for agents: device-owning domains, Linux and FreeBSD guests under QEMU; agent services not yet booted. 1 source.
- [[verus]] · verifier for Rust code with SMT solving; case studies, no kernel. 1 source.
- [[cohesix]] · seL4-based control layer for edge AI fleets: a Queen decides what hosts' models may do; landing page only. 1 source.
- [[kataos]] · Google's seL4 and Rust OS for machine-learning devices, 2022; OpenTitan in its Sparrow plan. 1 source.
- [[cheriot]] · CHERI capabilities on small RISC-V cores with its own RTOS: memory safety in hardware, measured, not proven. 1 source.
- [[cva6]] · open 64-bit RISC-V core whose design lets latency bounds be proved; fence.t prototype. 6 sources.
- [[sifive-hifive]] · SiFive and its boards: the discontinued HiFive Unleashed with seL4's MCS proof, the HiFive Premier P550 one can buy. 5 sources.

## Concepts

- [[risc-v]] · the open instruction set: what is open (the ISA) and what need not be (cores, chips, boards); privilege levels and the SBI. 11 sources.
- [[wcet-analysis]] · upper bounds on execution time, what they need, and where seL4 stands. 6 sources.
- [[functional-correctness]] · what seL4's refinement proof gives, what it assumes, where it holds. 4 sources.
- [[object-capabilities]] · references that both designate and authorise; permission versus authority; caretaker and membrane. 5 sources.
- [[confused-deputy]] · a program misusing one party's authority for another's request; capabilities as the remedy. 3 sources.
- [[prompt-injection]] · instructions hidden in data an agent reads; heuristic defences fail, defences around the model hold within limits. 4 sources.
- [[verified-boot]] · each stage checks the next against a key the attacker cannot change; proofs about boot code so far. 6 sources.
- [[measured-boot]] · each stage records what runs next; TPM and DICE; a verified DICE implementation. 4 sources.
- [[time-protection]] · closing timing channels between domains; prototypes on CVA6, proof for seL4 in progress. 3 sources.
- [[simplex]] · a simple safe controller guarding an untrusted one; tested with learned controllers. 1 source.
- [[action-chunking]] · slow robot models emitting action sequences for a fast loop; no bound on delay. 2 sources.
- [[ai-vulnerability-discovery]] · AI models finding software flaws at scale: DARPA's challenge and Anthropic's figures, the bottleneck moving to patching. 3 sources.
- [[information-flow-control]] · labels for where data came from and who may see it; FIDES and CaMeL for agents; explicit flows only. 2 sources.
- [[proof-automation]] · machines proposing proof steps, Isabelle checking them; 77.6 % of a seL4 benchmark sample; Verus as a faster verifier. 3 sources.
- [[mixed-criticality]] · software of different criticality on one platform; processor time as a capability in seL4 MCS. 3 sources.

## Sources

- [[2011-waterman-risc-v-instruction]] · the first RISC-V manual, Berkeley, May 2011: an open ISA for research and teaching. design, introduction only.
- [[2014-asanovic-instruction-sets-free]] · why instruction sets should be free, and why RISC-V. position, full text.
- [[2024-riscv-unprivileged-isa-manual]] · the ratified ISA: base ISAs, standard extensions, harts. design, introduction only.
- [[2024-riscv-privileged-isa-manual]] · privilege levels M, S, U and the SBI. design, introduction only.
- [[nd-riscv-international-about]] · who keeps the RISC-V standard: a Swiss non-profit; royalty-free ISA, no implementations. report, full text.
- [[nd-sifive-risc-v-history]] · SiFive's account of RISC-V and of itself. report, full text.
- [[nd-sifive-hifive-unleashed]] · the HiFive Unleashed, discontinued: FU540, U54 cores and a monitor core. report, full text.
- [[2024-sifive-hifive-premier-p550]] · the HiFive Premier P550, announced in Nuremberg, April 2024. report, full text.
- [[nd-sel4-supported-platforms]] · the boards seL4 runs on; boot chain of the P550. report, RISC-V and board pages.
- [[2025-heiser-fast-secure-adaptable]] · LionsOS design and benchmarks: a full gigabit on one Arm core where Linux plateaus at about 500 Mb/s; no worst-case figures. measurement, full text.
- [[2024-lattuada-verus-practical-foundation]] · Verus: 3 to 61 times faster than other verifiers on list benchmarks; a page table at 13.3 lines of proof per line of code. measurement, full text.
- [[2026-hubbard-agentos-operating-system]] · agentOS README: guests under QEMU proven by test, agent services not in the image. report, README as saved.
- [[2026-sel4-release-17]] · seL4 17.0.0: C-level proof on every 64-bit platform, MCS on `hifive` only; an icache fix. report, CAVEATS and 17.0.0 notes.
- [[2026-anthropic-project-glasswing-securing]] · an unreleased model finds thousands of high-severity flaws; the company's own claim, April 2026. report, full text.
- [[2026-anthropic-project-glasswing-initial]] · over ten thousand partner findings; of 1,752 open-source findings assessed, 62.4 % confirmed high or critical. report, full text.
- [[2026-bower-cohesix-research-operating]] · Cohesix: Queen and Workers on seL4, AI proposes and the target decides. report, landing page only.
- [[2023-amar-cheriot-complete-memory]] · CHERIoT: CHERI on 32-bit RISC-V with its own RTOS; under 10 % more gates than a PMP core, 21 % CoreMark cost on Ibex. measurement, full text.
- [[2025-cnx-nuvoton-introduces-first]] · fabrication of the first production OpenTitan chip, by Nuvoton, February 2025. report, full text.
- [[2025-costa-securing-ai-agents]] · FIDES: information-flow labels in the agent's planner; noninterference for integrity, explicit flows only. test, full text.
- [[2025-darpa-ai-cyber-challenge]] · AIxCC final: 54 of 63 planted flaws found, 43 patched, 18 real ones, about $152 a task. report, full text.
- [[2022-google-announcing-kataos-sparrow]] · KataOS on seL4 in Rust for ML devices; Sparrow with OpenTitan planned. report, full text.
- [[2025-google-building-next-generation]] · Gemini Robotics-ER 1.5: a reasoning model that calls an action model; safety filters no substitute for engineering. report, full text.
- [[2023-greshake-not-what-you]] · indirect prompt injection: instructions in retrieved data steer LLM applications; demonstrations, no rates. test, full text.
- [[2026-he-neuro-symbolic-proof]] · step-wise proof search with a small model proves 77.6 % of a seL4 benchmark sample, about 20 % of long proofs. measurement, full text.
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
