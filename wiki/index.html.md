# Silent Zero wiki

> What the sources behind the Silent Zero paper show, page by page: designs, concepts, systems and sources, each with what is proven, tested or assumed.

This wiki gathers what the sources behind the paper show. It has a page for each source, each concept, each system the paper builds on and each part of the design: 74 sources, 17 concepts, 17 systems and 8 parts of the design so far. Every page says what is proven, tested or assumed, and on which source that rests.

## How this wiki is made

A language model writes the wiki and keeps it up to date from the sources in the project's research pool, after Andrej Karpathy's idea of a wiki that a language model maintains. A daily run adds new sources and works older ones in.

- **Draft.** Written, not yet reviewed, or held back for a stated reason.
- **LLM reviewed.** A second, independent pass found every figure and every quotation in its source and read the page's claims against the sources. This is the state of most pages.
- **Human curated.** Someone on the team has also compared the page with its sources.

A page can still be wrong or misleading in detail. If you find a mistake, please [open an issue](https://github.com/entresol/silent-zero/issues). Wiki rules are noted [here](https://github.com/entresol/silent-zero/blob/main/wiki/CLAUDE.md), changes are followed [here](https://github.com/entresol/silent-zero/blob/main/wiki/log.md).


## Design

- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md) · seL4 with MCS as the Silent Zero kernel: proven (C-level correctness; MCS functional correctness on RISC-V), not stated for MCS (integrity, confidentiality), tested (HACMS), assumed (boot, IOMMU); no WCET bound on any 64-bit core yet; the roadmap dates MCS on AArch64 to Q3 2027. 15 sources.
- [The static system](https://silentzero.ooo/wiki/design/static-system.html.md) · one description, one image: what Microkit checks, what is not proved, and the run-time swap in LionsOS, the kernel underneath. 6 sources.
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md) · the only component that hands out authority: capability patterns, CaMeL and FIDES, why model-based defences fail; nothing proven yet. 15 sources.
- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md) · the loops that move the motors: asynchronous chunks from slow models, observed timings, no proven bound yet. 9 sources.
- [The safety path](https://silentzero.ooo/wiki/design/safety-path.html.md) · Simplex in Silent Zero: the agent proposes, the loop disposes; tested, not proven; the paper's 2001 date disputed by a 1994 origin. 4 sources.
- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md) · the firmware below the kernel on Arm, RISC-V, PC and Raspberry Pi; OpenTitan, Caliptra, DICE; all *assumed* in the paper's terms. 13 sources.
- [The bootloader](https://silentzero.ooo/wiki/design/bootloader.html.md) · where the Silent Zero loader sits on each platform, signed and measured boot, proofs about boot code so far; the loader itself unproven. 16 sources.
- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md) · user-mode drivers, the first verified Ethernet driver, DMA and the IOMMU as assumed, attacked in 2019 although enabled. 10 sources.

## Systems

- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md) · the verified microkernel Silent Zero builds on: proofs per architecture and platform, cost, MCS, timing, HACMS. 13 sources.
- [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md) · the build system for static seL4 systems: protection domains, channels, budgets, one image. 4 sources.
- [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md) · static OS from small components on seL4 and Microkit; first driver verified. 5 sources.
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md) · open firmware in stages with a fixed payload; verified and measured boot; closed vendor parts on x86. 3 sources.
- [Trusted Firmware-A](https://silentzero.ooo/wiki/systems/tf-a.html.md) · Arm's reference firmware; BL31 stays resident at EL3 below the kernel. 2 sources.
- [OpenSBI](https://silentzero.ooo/wiki/systems/opensbi.html.md) · RISC-V firmware in machine mode below the kernel. 3 sources.
- [Raspberry Pi](https://silentzero.ooo/wiki/systems/raspberry-pi.html.md) · the pib's board: closed ROM and EEPROM boot, secure-boot key in OTP on the Pi 4, seL4 verified without MCS. 4 sources.
- [OpenTitan](https://silentzero.ooo/wiki/systems/opentitan.html.md) · open-source silicon root of trust, shipping in Chromebooks since March 2026. 5 sources.
- [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md) · seL4-based I/O platform for agents: device-owning domains, Linux and FreeBSD guests under QEMU; agent services not yet booted. 1 source.
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md) · verifier for Rust code with SMT solving; case studies, no kernel; AutoVerus writes proofs for it. 2 sources.
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md) · Linux sandbox a process applies to itself: filesystem, network, capability and namespace rules; part of the hardened-Linux route. 1 source.
- [PREEMPT_RT](https://silentzero.ooo/wiki/systems/preempt-rt.html.md) · the Linux real-time configuration: preemptible kernel, threaded interrupts; no latency bound stated. 1 source.
- [Cohesix](https://silentzero.ooo/wiki/systems/cohesix.html.md) · seL4-based control layer for edge AI fleets: a Queen decides what hosts' models may do; landing page only. 1 source.
- [KataOS](https://silentzero.ooo/wiki/systems/kataos.html.md) · Google's seL4 and Rust OS for machine-learning devices, 2022; OpenTitan in its Sparrow plan. 1 source.
- [CHERIoT](https://silentzero.ooo/wiki/systems/cheriot.html.md) · CHERI capabilities on small RISC-V cores with its own RTOS: memory safety in hardware, measured, not proven; CHERI for RISC-V "being standardised" in 2026. 2 sources.
- [CVA6](https://silentzero.ooo/wiki/systems/cva6.html.md) · open 64-bit RISC-V core whose design lets latency bounds be proved; fence.t prototype. 6 sources.
- [SiFive and the HiFive boards](https://silentzero.ooo/wiki/systems/sifive-hifive.html.md) · SiFive and its boards: the discontinued HiFive Unleashed with seL4's MCS proof, the HiFive Premier P550 one can buy. 5 sources.

## Concepts

- [RISC-V](https://silentzero.ooo/wiki/concepts/risc-v.html.md) · the open instruction set: what is open (the ISA) and what need not be (cores, chips, boards); privilege levels and the SBI. 11 sources.
- [IOMMU](https://silentzero.ooo/wiki/concepts/iommu.html.md) · the memory management unit for devices: what it limits, and the 2019 attacks that worked although it was on. 1 source.
- [WCET analysis](https://silentzero.ooo/wiki/concepts/wcet-analysis.html.md) · upper bounds on execution time, what they need, and where seL4 stands. 6 sources.
- [Functional correctness](https://silentzero.ooo/wiki/concepts/functional-correctness.html.md) · what seL4's refinement proof gives, what it assumes, where it holds. 4 sources.
- [Object capabilities](https://silentzero.ooo/wiki/concepts/object-capabilities.html.md) · references that both designate and authorise; permission versus authority; caretaker and membrane. 5 sources.
- [Confused deputy](https://silentzero.ooo/wiki/concepts/confused-deputy.html.md) · a program misusing one party's authority for another's request; capabilities as the remedy. 3 sources.
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md) · instructions hidden in data an agent reads; heuristic defences fail, defences around the model hold within limits. 5 sources.
- [Verified boot](https://silentzero.ooo/wiki/concepts/verified-boot.html.md) · each stage checks the next against a key the attacker cannot change; proofs about boot code so far. 6 sources.
- [Measured boot](https://silentzero.ooo/wiki/concepts/measured-boot.html.md) · each stage records what runs next; TPM and DICE; a verified DICE implementation. 4 sources.
- [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md) · closing timing channels between domains; prototypes on CVA6, proof for seL4 in progress. 3 sources.
- [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md) · a simple safe controller guarding an untrusted one; tested with learned controllers. 1 source.
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md) · slow robot models emitting action sequences for a fast loop; no bound on delay. 3 sources.
- [AI vulnerability discovery](https://silentzero.ooo/wiki/concepts/ai-vulnerability-discovery.html.md) · AI models finding software flaws at scale: DARPA's challenge and Anthropic's figures, the bottleneck moving to patching. 3 sources.
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md) · labels for where data came from and who may see it; FIDES and CaMeL for agents; explicit flows only. 2 sources.
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md) · machines proposing proof steps, Isabelle checking them; 77.6 % of a seL4 benchmark sample; Verus as a faster verifier. PROMISE as a second method; AutoVerus for Rust. 5 sources.
- [Memory-safe code](https://silentzero.ooo/wiki/concepts/memory-safe-code.html.md) · new code in Rust instead of C: Android's memory-safety flaws below 20 % in 2025; the hardening rival to a verified base. 2 sources.
- [Mixed criticality](https://silentzero.ooo/wiki/concepts/mixed-criticality.html.md) · software of different criticality on one platform; processor time as a capability in seL4 MCS. 3 sources.

## Sources

- [The RISC-V Instruction Set Manual, Version 1.0](https://silentzero.ooo/wiki/sources/2011-waterman-risc-v-instruction.html.md) (Waterman et al. 2011) · the first RISC-V manual, Berkeley, May 2011: an open ISA for research and teaching. design, introduction only.
- [Instruction Sets Should Be Free](https://silentzero.ooo/wiki/sources/2014-asanovic-instruction-sets-free.html.md) (Asanović and Patterson 2014) · why instruction sets should be free, and why RISC-V. position, full text.
- [The RISC-V Instruction Set Manual, Volume I](https://silentzero.ooo/wiki/sources/2024-riscv-unprivileged-isa-manual.html.md) (RISC-V International 2024) · the ratified ISA: base ISAs, standard extensions, harts. design, introduction only.
- [The RISC-V Instruction Set Manual, Volume II](https://silentzero.ooo/wiki/sources/2024-riscv-privileged-isa-manual.html.md) (RISC-V International 2024) · privilege levels M, S, U and the SBI. design, introduction only.
- [RISC-V International: About](https://silentzero.ooo/wiki/sources/nd-riscv-international-about.html.md) · who keeps the RISC-V standard: a Swiss non-profit; royalty-free ISA, no implementations. report, full text.
- [SiFive: RISC-V History](https://silentzero.ooo/wiki/sources/nd-sifive-risc-v-history.html.md) · SiFive's account of RISC-V and of itself. report, full text.
- [SiFive: HiFive Unleashed](https://silentzero.ooo/wiki/sources/nd-sifive-hifive-unleashed.html.md) · the HiFive Unleashed, discontinued: FU540, U54 cores and a monitor core. report, full text.
- [the HiFive Premier P550](https://silentzero.ooo/wiki/sources/2024-sifive-hifive-premier-p550.html.md) (SiFive 2024) · the HiFive Premier P550, announced in Nuremberg, April 2024. report, full text.
- [seL4 Foundation: Supported platforms](https://silentzero.ooo/wiki/sources/nd-sel4-supported-platforms.html.md) · the boards seL4 runs on; boot chain of the P550. report, RISC-V and board pages.
- [Fast, Secure, Adaptable: LionsOS Design, Implementation and Performance](https://silentzero.ooo/wiki/sources/2025-heiser-fast-secure-adaptable.html.md) (Heiser et al. 2025) · LionsOS design and benchmarks: a full gigabit on one Arm core where Linux plateaus at about 500 Mb/s; no worst-case figures. measurement, full text.
- [Verus, a practical foundation for systems verification](https://silentzero.ooo/wiki/sources/2024-lattuada-verus-practical-foundation.html.md) (Lattuada et al. 2024) · Verus: 3 to 61 times faster than other verifiers on list benchmarks; a page table at 13.3 lines of proof per line of code. measurement, full text.
- [agentOS, an operating system for agents on seL4](https://silentzero.ooo/wiki/sources/2026-hubbard-agentos-operating-system.html.md) (Hubbard 2026) · agentOS README: guests under QEMU proven by test, agent services not in the image. report, README as saved.
- [release 17.0.0](https://silentzero.ooo/wiki/sources/2026-sel4-release-17.html.md) (seL4 Foundation 2026) · seL4 17.0.0: C-level proof on every 64-bit platform, MCS on `hifive` only; an icache fix. report, CAVEATS and 17.0.0 notes.
- [Anthropic 2026a: Project Glasswing, securing critical software for the AI era](https://silentzero.ooo/wiki/sources/2026-anthropic-project-glasswing-securing.html.md) · an unreleased model finds thousands of high-severity flaws; the company's own claim, April 2026. report, full text.
- [Anthropic 2026b: Project Glasswing, an initial update](https://silentzero.ooo/wiki/sources/2026-anthropic-project-glasswing-initial.html.md) · over ten thousand partner findings; of 1,752 open-source findings assessed, 62.4 % confirmed high or critical. report, full text.
- [Cohesix, a research operating system for edge AI](https://silentzero.ooo/wiki/sources/2026-bower-cohesix-research-operating.html.md) (Bower 2026) · Cohesix: Queen and Workers on seL4, AI proposes and the target decides. report, landing page only.
- [CHERIoT, complete memory safety for embedded devices](https://silentzero.ooo/wiki/sources/2023-amar-cheriot-complete-memory.html.md) (Amar et al. 2023) · CHERIoT: CHERI on 32-bit RISC-V with its own RTOS; under 10 % more gates than a PMP core, 21 % CoreMark cost on Ibex. measurement, full text.
- [Nuvoton's OpenTitan chip](https://silentzero.ooo/wiki/sources/2025-cnx-nuvoton-introduces-first.html.md) (CNX Software 2025) · fabrication of the first production OpenTitan chip, by Nuvoton, February 2025. report, full text.
- [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md) (Costa et al. 2025) · FIDES: information-flow labels in the agent's planner; noninterference for integrity, explicit flows only. test, full text.
- [results of the AI Cyber Challenge](https://silentzero.ooo/wiki/sources/2025-darpa-ai-cyber-challenge.html.md) (DARPA 2025) · AIxCC final: 54 of 63 planted flaws found, 43 patched, 18 real ones, about $152 a task. report, full text.
- [Announcing KataOS and Sparrow](https://silentzero.ooo/wiki/sources/2022-google-announcing-kataos-sparrow.html.md) (Google 2022) · KataOS on seL4 in Rust for ML devices; Sparrow with OpenTitan planned. report, full text.
- [Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md) (Google 2025) · Gemini Robotics-ER 1.5: a reasoning model that calls an action model; safety filters no substitute for engineering. report, full text.
- [Indirect prompt injection](https://silentzero.ooo/wiki/sources/2023-greshake-not-what-you.html.md) (Greshake et al. 2023) · indirect prompt injection: instructions in retrieved data steer LLM applications; demonstrations, no rates. test, full text.
- [Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md) (He et al. 2026) · step-wise proof search with a small model proves 77.6 % of a seL4 benchmark sample, about 20 % of long proofs. measurement, full text.
- [Resurrecting seL4's WCET Analysis](https://silentzero.ooo/wiki/sources/2026-sillitoe-resurrecting-sel4-wcet.html.md) (Sillitoe et al. 2026) · seL4's WCET analysis runs again on RV64 MCS, with placeholder values; sound CVA6 latencies expected Q1 2027. progress, full text.
- [WCET analysis of seL4](https://silentzero.ooo/wiki/sources/nd-trustworthy-wcet-worst-case.html.md) (Trustworthy Systems (n.d.)) · the archived project page: the sound ARM11 analysis and why it stopped. report, full text.
- [seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md) (Klein et al. 2009) · the first proof that seL4's C code implements its specification; assumptions, cost, bugs found. proof, full text.
- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md) (Klein et al. 2018) · HACMS: security by architecture on seL4, a helicopter's mission computer under attack in flight. test, full text.
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md) · which properties are proved on which architecture; boot and IOMMU outside every proof. report, full text.
- [MCS functional-correctness proof completed on RISC-V](https://silentzero.ooo/wiki/sources/2026-sel4-functional-correctness-proof.html.md) (seL4 Foundation 2026) · MCS functional correctness proved on RISC-V, June 2026; Arm next. report, full text.
- [MCS safety, an OS perspective](https://silentzero.ooo/wiki/sources/2026-heiser-mcs-safety-os.html.md) (Heiser 2026) · mixed criticality on seL4: scheduling contexts, WCET, MCS dates, LionsOS. survey, slides only.
- [Trustworthy Systems: Guaranteeing timeliness of MCS on seL4](https://silentzero.ooo/wiki/sources/2026-trustworthy-guaranteeing-timeliness-mcs.html.md) · the project to get from budgets to provable deadlines on RISC-V. progress, full text.
- [seL4 Microkit: User Manual, v2.3.0](https://silentzero.ooo/wiki/sources/nd-sel4-microkit-user-manual.html.md) · Microkit 2.3.0: the static model, its rules for real time, build-time checks, what is not enforced. report, main chapters (board notes and API skimmed).
- [Trustworthy Systems: LionsOS](https://silentzero.ooo/wiki/sources/2026-trustworthy-lionsos.html.md) · LionsOS 0.4.0: composable components, static with a run-time swap, verification under way. report, full text (introduction page).
- [The seL4 Device Driver Framework](https://silentzero.ooo/wiki/sources/2022-parker-sel4-device-driver.html.md) (Parker 2022) · the seL4 device driver framework: user-level drivers, lock-free queues, performance claims. measurement, slides only.
- [SMT-based Deductive Verification of Device Drivers](https://silentzero.ooo/wiki/sources/2026-tyler-smt-based-deductive.html.md) (Tyler et al. 2026) · a LionsOS Ethernet driver proved with SMT-based verification: four properties, three bugs, 11.5 person-weeks. proof, full text.
- [Systematic Prevention of On-Core Timing Channels](https://silentzero.ooo/wiki/sources/2022-wistoff-systematic-prevention-core.html.md) (Wistoff et al. 2022) · fence.t on CVA6: resetting all non-architectural state closes on-core timing channels at under 1 % cost. measurement, full text.
- [Where are we with Time Protection?](https://silentzero.ooo/wiki/sources/2026-trustworthy-where-are-we.html.md) (Sison 2026) · time protection for seL4: proof approach revised, one-way channels on RISC-V. progress, slides and abstract.
- [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) (Nesti et al. 2025) · Simplex with learned controllers on a pendulum and a rover, isolated by a hypervisor. test, full text.
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md) (Black, Galliker and Levine 2025) · real-time chunking keeps task throughput under up to 200 ms of extra delay, where synchronous chunking pauses. measurement, full text.
- [OpenTitan shipping in production](https://silentzero.ooo/wiki/sources/2026-google-opentitan-shipping-production.html.md) (Google 2026) · OpenTitan ships in Chromebooks, March 2026. report, full text.
- [The Confused Deputy](https://silentzero.ooo/wiki/sources/1988-hardy-confused-deputy-or.html.md) (Hardy 1988) · the compiler that overwrote the billing file: why capabilities bundle naming and permission. position, full text.
- [Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md) (Miller 2006) · object capabilities, permission versus authority, revocable grants, revocation across machines. design, chapters 1–3, 8, 9, 11, 12.
- [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md) (Debenedetti et al. 2025) · CaMeL: capabilities and policies around an untrusted model; 77 % utility, no successful attacks within its threat model. test, main text and appendices D, E, I.
- [The Attacker Moves Second](https://silentzero.ooo/wiki/sources/2026-nasr-attacker-moves-second.html.md) (Nasr et al. 2026) · adaptive attacks break 12 prompt-injection and jailbreak defences, most above 90 %. test, full text.
- [coreboot: architecture and boot stages](https://silentzero.ooo/wiki/sources/nd-coreboot-architecture.html.md) · coreboot's stages from bootblock to a payload fixed at build time. report, full text.
- [coreboot: verified boot (vboot)](https://silentzero.ooo/wiki/sources/nd-coreboot-vboot.html.md) · verified boot rooted in write-protected flash, A/B slots, automatic recovery. report, full text.
- [coreboot: measured boot](https://silentzero.ooo/wiki/sources/nd-coreboot-measured-boot.html.md) · TPM measurements, a software-rooted first measurement, vendor hardware roots behind it. report, full text.
- [Chromium OS: Verified Boot (design document)](https://silentzero.ooo/wiki/sources/nd-chromeos-verified-boot.html.md) · Chromium OS's design: against the opportunistic attacker, the owner keeps control, rollback a weakness. design, full text.
- [Trusted Firmware-A: firmware design](https://silentzero.ooo/wiki/sources/nd-tfa-firmware-design.html.md) · Arm's boot stages BL1 to BL33; BL31 resident at EL3. report, cold boot and runtime services.
- [OpenSBI](https://silentzero.ooo/wiki/sources/nd-opensbi.html.md) · the SBI reference firmware for RISC-V machine mode. report, README.
- [U-Boot: verified boot](https://silentzero.ooo/wiki/sources/nd-uboot-verified-boot.html.md) · signed FIT images; the public key must be unchangeable. report, full text.
- [Raspberry Pi documentation: boot](https://silentzero.ooo/wiki/sources/nd-raspberrypi-boot.html.md) · ROM and EEPROM bootloader on Pi 4 and 5; secure-boot key hash in the Pi 4's OTP. report, boot chapters.
- [seL4 on PC99 (x86-64)](https://silentzero.ooo/wiki/sources/nd-sel4-x64-platform.html.md) · seL4 on PCs boots through a Multiboot loader. report, full text.
- [Trustworthy Systems n.d.: Proof Statistics](https://silentzero.ooo/wiki/sources/nd-trustworthy-proof-statistics.html.md) · the 2009 seL4 proof in numbers: 8,700 lines of C, 200,000 lines of proof, about 25 person-years, 160 bugs. report, full text.
- [Rust in Android](https://silentzero.ooo/wiki/sources/2025-vander-rust-android-move.html.md) (Vander Stoep 2025) · Android 2025: memory-safety flaws below 20 % of vulnerabilities, Rust at about 0.2 per million lines against 1,000 for C and C++. measurement, full text.
- [AutoVerus](https://silentzero.ooo/wiki/sources/2025-yang-autoverus-automated-proof.html.md) (Yang et al. 2025) · AutoVerus: model agents write Verus proofs, over 90 % of 150 Rust tasks. measurement, abstract only.
- [Caliptra](https://silentzero.ooo/wiki/sources/nd-caliptra.html.md) · open root of trust for measurement inside data-centre SoCs. report, README.
- [Model Checking Boot Code from AWS Data Centers](https://silentzero.ooo/wiki/sources/2018-cook-model-checking-boot.html.md) (Cook et al. 2018) · 783 lines of AWS boot code proved memory safe by bounded model checking. proof, full text.
- [Towards a Verified First-Stage Bootloader in Coq](https://silentzero.ooo/wiki/sources/2020-straznickas-verified-first-stage.html.md) (Straznickas 2020) · a RISC-V measurement root in Coq that signs what it loads; theorem stated, not fully proved. progress, full text.
- [DICE\*, a Formally Verified Implementation of DICE Measured Boot](https://silentzero.ooo/wiki/sources/2021-tao-dice-formally-verified.html.md) (Tao et al. 2021) · DICE, verify-and-measure boot, verified at the level of generated C; on an STM32. proof, full text.
- [PA-Boot, a Formally Verified Authentication Protocol for Multiprocessor Secure Boot under Hardware Supply-chain Attacks](https://silentzero.ooo/wiki/sources/2022-zhang-pa-boot-formally.html.md) (Zhang et al. 2022) · processor authentication for multi-chip secure boot, proved in Isabelle/HOL. proof, main sections.
- [Thunderclap](https://silentzero.ooo/wiki/sources/2019-markettos-thunderclap-exploring-vulnerabilities.html.md) (Markettos et al. 2019) · Thunderclap, NDSS 2019: attacks by a malicious device on macOS, FreeBSD and Linux with the IOMMU on; Windows mostly unprotected. test, full text.
- [CHERI is being standardised](https://silentzero.ooo/wiki/sources/2026-moore-cheri-is-being.html.md) (Moore 2026) · Moore, CHERI Blossoms 2026: CHERI for RISC-V is "being standardised"; criteria and open research. position, slides, full text.
- [seL4 Foundation: Development roadmap](https://silentzero.ooo/wiki/sources/nd-sel4-sel4-roadmap.html.md) · the seL4 roadmap: MCS C-level proof done on RISC-V, AArch64 Q3 2027; multikernel proofs Q3 2028. report, full text.
- [Microkit 2.4.0 release notes](https://silentzero.ooo/wiki/sources/2026-microkit-release-2-4-0.html.md) · Microkit 2.4.0 on seL4 17.0.0: reply capabilities and parent fault endpoints no longer leak authority. report, full text.
- [security proofs complete on AArch64](https://silentzero.ooo/wiki/sources/2026-proofcraft-sel4-security-proofs.html.md) (seL4 Foundation 2026) · seL4 news item, 24 August 2026: the confidentiality proof on AArch64 is finished, isolation complete under listed assumptions. report, full text.
- [FutureRTC](https://silentzero.ooo/wiki/sources/2026-jiang-futurertc-real-time.html.md) (Jiang et al. 2026) · FutureRTC: an adapter that predicts the inputs of the next action chunk to tolerate inference delay; preprint. measurement, full text.
- [MCP-38](https://silentzero.ooo/wiki/sources/2026-shen-mcp-38-comprehensive.html.md) (Shen, Toyoda and Leung 2026) · MCP-38: 38 threat categories for the Model Context Protocol and the coverage of five tools; preprint. survey, full text.
- [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md) (Zou et al. 2026) · AgentKernel: an agent OS on a conventional host with an external monitor and capability intersection; proofs deferred. design, partly read.
- [PROMISE](https://silentzero.ooo/wiki/sources/2026-ahn-promise-proof-automation.html.md) (Ahn et al. 2026) · PROMISE: structure-guided LLM proof search on 223 seL4 theorems, 55.7 % averaged over seven settings. measurement, partly read.
- [Linux kernel documentation: Landlock](https://silentzero.ooo/wiki/sources/nd-linux-landlock-unprivileged-access.html.md) · Landlock, the Linux self-sandboxing module, kernel documentation of October 2026. report, partly read.
- [Linux kernel documentation: real-time preemption](https://silentzero.ooo/wiki/sources/nd-linux-real-time-preemption.html.md) · PREEMPT_RT in the kernel documentation: sleeping locks, threaded interrupts, shared-hardware limits. report, partly read.
- [LeftoverLocals](https://silentzero.ooo/wiki/sources/2024-trail-leftoverlocals-listening-llm.html.md) (Khlaaf and Sorensen 2024) · LeftoverLocals: GPU local memory leaks between processes; 181 MB per LLM query on one AMD GPU. test, partly read.

## Not yet covered

The Silent Zero part *agents* has no page yet. Firmware on PCs (Intel ME, AMD PSP, FSP, open alternatives) and on Apple silicon is in the backlog. Also not yet covered: the multicore proof, the ratification status of CHERI for RISC-V, the seams between proven parts, the driver island, and most competing agent operating systems.
