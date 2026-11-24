---
type: index
updated: 2026-11-24
---

# zOS wiki

The catalogue of every page, with one line each. Read this first.

## zOS

- [[kernel]] · seL4 with MCS as the zOS kernel: proven (C-level correctness; MCS functional correctness on RISC-V), not stated for MCS (integrity, confidentiality), tested (HACMS), assumed (boot, IOMMU); no WCET bound on any 64-bit core yet; the roadmap dates MCS on AArch64 to Q3 2027. 20 sources.
- [[static-system]] · one description, one image: what Microkit checks, what is not proved, and the run-time swap in LionsOS, the kernel underneath. 6 sources.
- [[broker]] · the only component that hands out authority: capability patterns, CaMeL and FIDES, why model-based defences fail, three agent-OS designs for the same job, CaMeL between agents; nothing proven yet; the industry's agent sandboxes grant by resource. 31 sources.
- [[real-time-loops]] · the loops that move the motors: asynchronous chunks from slow models, policies trained for a delay range, observed timings, per-step costs of two barrier filters, no proven bound yet. 18 sources.
- [[safety-path]] · Simplex in zOS: the agent proposes, the loop disposes; tested, not proven; the paper's 2001 date disputed by a 1994 origin; certified real-time kernels sell the same split as products; two more barrier filters, guarantees conditional on perception. 19 sources.
- [[root-of-trust]] · the firmware below the kernel on Arm, RISC-V, PC and Raspberry Pi; OpenTitan, Caliptra, DICE; all *assumed* in the paper's terms. 13 sources.
- [[bootloader]] · where the zOS loader sits on each platform, signed and measured boot, proofs about boot code so far; the loader itself unproven. 16 sources.
- [[drivers]] · user-mode drivers, the first verified Ethernet driver, DMA and the IOMMU as assumed, attacked in 2019 although enabled; device models from Verilog and Windows on x86-64 as first steps; the Pancake paper adds the language and its limits. 13 sources.

## Not yet covered

The zOS part *agents* has no page yet; [[agent-operating-systems]] covers the designs that touch it. Firmware on PCs (Intel ME, AMD PSP, FSP, open alternatives) and on Apple silicon is in the backlog. Also not yet covered: the multicore proof, the ratification status of CHERI for RISC-V after April 2026 (the sources here stop there), the seams between proven parts and the driver island.

## Systems

- [[sel4]] · the verified microkernel zOS builds on: proofs per architecture and platform, cost, MCS, timing, HACMS; what its foundation says about certification; the 2026 releases. 18 sources.
- [[microkit]] · the build system for static seL4 systems: protection domains, channels, budgets, one image. 7 sources.
- [[lionsos]] · static OS from small components on seL4 and Microkit; first driver verified; Summit 2026 talks on x86-64 VMs and driver specifications. 9 sources.
- [[coreboot]] · open firmware in stages with a fixed payload; verified and measured boot; closed vendor parts on x86. 3 sources.
- [[tf-a]] · Arm's reference firmware; BL31 stays resident at EL3 below the kernel. 2 sources.
- [[opensbi]] · RISC-V firmware in machine mode below the kernel. 3 sources.
- [[raspberry-pi]] · the pib's board: closed ROM and EEPROM boot, secure-boot key in OTP on the Pi 4, seL4 verified without MCS. 4 sources.
- [[opentitan]] · open-source silicon root of trust, shipping in Chromebooks since March 2026. 5 sources.
- [[agentos]] · seL4-based I/O platform for agents: device-owning domains, Linux and FreeBSD guests under QEMU; agent services not yet booted. 1 source.
- [[verus]] · verifier for Rust code with SMT solving; case studies, no kernel; AutoVerus writes proofs for it. 2 sources.
- [[landlock]] · Linux sandbox a process applies to itself: filesystem, network, capability and namespace rules; part of the hardened-Linux route, and the base of OpenShell's filesystem layer. 3 sources.
- [[preempt-rt]] · the Linux real-time configuration: preemptible kernel, threaded interrupts; no latency bound stated. 1 source.
- [[elisa]] · the Linux Foundation's project for Linux in safety applications; NVIDIA joined as a premier member in February 2026; no certificate named. 1 source.
- [[cohesix]] · seL4-based control layer for edge AI fleets: a Queen decides what hosts' models may do; landing page only. 1 source.
- [[kataos]] · Google's seL4 and Rust OS for machine-learning devices, 2022; OpenTitan in its Sparrow plan. 1 source.
- [[cheriot]] · CHERI capabilities on small RISC-V cores with its own RTOS: memory safety in hardware, measured, not proven; the 1.0 ISA of November 2025; CHERI for RISC-V in architecture review in April 2026, not ratified in any source here. 4 sources.
- [[cva6]] · open 64-bit RISC-V core whose design lets latency bounds be proved; fence.t prototype. 7 sources.
- [[sifive-hifive]] · SiFive and its boards: the discontinued HiFive Unleashed with seL4's MCS proof, the HiFive Premier P550 one can buy. 5 sources.
- [[nvidia-halos]] · NVIDIA's safety stack for robots: IGX Thor with a safety island, Halos Core with Linux or Linux plus QNX; inspected for certification readiness, no robotics certificate claimed. 3 sources.
- [[qnx]] · commercial microkernel RTOS, the safety side of Halos on IGX Thor; leader in an analyst's ranking for robot safety. 3 sources.
- [[pikeos]] · commercial separation kernel and hypervisor; IEC 61508 SIL 3 and ISO 26262 ASIL D listed by the vendor; untrusted ROS 2 beside certified control. 3 sources.
- [[openshell]] · open-source sandbox runtime for agents: Landlock, seccomp, network namespaces and a policy engine; outbound traffic denied by default; credentials as placeholders; a Developer Preview in OpenShift AI 3.5. 3 sources.
- [[mxc]] · Microsoft's policy-driven containment for agents on Windows, macOS and Linux, generally available as of 7 October 2026, with OpenShell integrated; no assurance claimed. 3 sources.

## Concepts

- [[risc-v]] · the open instruction set: what is open (the ISA) and what need not be (cores, chips, boards); privilege levels and the SBI. 12 sources.
- [[iommu]] · the memory management unit for devices: what it limits, and the 2019 attacks that worked although it was on. 3 sources.
- [[wcet-analysis]] · upper bounds on execution time, what they need, and where seL4 stands. 7 sources.
- [[functional-correctness]] · what seL4's refinement proof gives, what it assumes, where it holds. 5 sources.
- [[object-capabilities]] · references that both designate and authorise; permission versus authority; caretaker and membrane. 7 sources.
- [[confused-deputy]] · a program misusing one party's authority for another's request; capabilities as the remedy. 4 sources.
- [[prompt-injection]] · instructions hidden in data an agent reads; heuristic defences fail, defences around the model hold within limits; benign command chains through shared state beat two of them; CaMeL does not carry over between agents; argument-level authorization and refusals as a leak; MCP measured. 14 sources.
- [[verified-boot]] · each stage checks the next against a key the attacker cannot change; proofs about boot code so far. 6 sources.
- [[measured-boot]] · each stage records what runs next; TPM and DICE; a verified DICE implementation. 4 sources.
- [[time-protection]] · closing timing channels between domains; prototypes on CVA6, proof for seL4 in progress. 5 sources.
- [[simplex]] · a simple safe controller guarding an untrusted one; tested with learned controllers. 4 sources.
- [[action-chunking]] · slow robot models emitting action sequences for a fast loop; RTC and three 2026 policy-side answers; no bound on delay. 7 sources.
- [[ai-vulnerability-discovery]] · AI models finding software flaws at scale: DARPA's challenge and Anthropic's figures, the bottleneck moving to patching. 3 sources.
- [[information-flow-control]] · labels for where data came from and who may see it; FIDES and CaMeL for agents; explicit flows only; refusals as a channel; Agent libOS. 8 sources.
- [[proof-automation]] · machines proposing proof steps, Isabelle checking them; 77.6 % of a seL4 benchmark sample; Verus as a faster verifier. PROMISE as a second method; AutoVerus for Rust; a coding agent's compiler proofs in Lean; the OSDI version and the Selene benchmark; specification writing (OSVBench), AutoRocq, and verified against checked compiler passes. 14 sources.
- [[memory-safe-code]] · new code in Rust instead of C: Android's memory-safety flaws below 20 % in 2025; a Rust microkernel without hardware isolation as a research rival; the hardening rival to a verified base. 2 sources.
- [[mixed-criticality]] · software of different criticality on one platform; processor time as a capability in seL4 MCS; partitions under a hypervisor in commercial robot stacks. 7 sources.
- [[model-context-protocol]] · the open protocol that connects agents to tools; three preprints measure its security, one runtime treats it as a client only; a vendor's guide to OWASP's MCP list. 6 sources.
- [[agent-operating-systems]] · designs that put the limit on an agent in the OS layer: agentOS, Cohesix, KataOS, AgentKernel, AgenticOS, Agent libOS, Quine, OpenShell and MXC as shipped products; IBM's Agent-OS position paper; IntentOS, a language-model planner beside the Linux kernel. 14 sources.
- [[control-barrier-functions]] · a filter that keeps a robot's commanded motion inside a safe set; three VLA filters, guarantees conditional on perception. 3 sources.
- [[safety-certification]] · proof versus certificate: what a certified kernel, a robot stack and seL4 each state; no certified seL4 product in the sources; ELISA's aim for Linux. 6 sources.

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
- [[nd-trustworthy-proof-statistics]] · the 2009 seL4 proof in numbers: 8,700 lines of C, 200,000 lines of proof, about 25 person-years, 160 bugs. report, full text.
- [[2025-vander-rust-android-move]] · Android 2025: memory-safety flaws below 20 % of vulnerabilities, Rust at about 0.2 per million lines against 1,000 for C and C++. measurement, full text.
- [[2025-yang-autoverus-automated-proof]] · AutoVerus: model agents write Verus proofs, over 90 % of 150 Rust tasks. measurement, abstract only.
- [[nd-caliptra]] · open root of trust for measurement inside data-centre SoCs. report, README.
- [[2018-cook-model-checking-boot]] · 783 lines of AWS boot code proved memory safe by bounded model checking. proof, full text.
- [[2020-straznickas-verified-first-stage]] · a RISC-V measurement root in Coq that signs what it loads; theorem stated, not fully proved. progress, full text.
- [[2021-tao-dice-formally-verified]] · DICE, verify-and-measure boot, verified at the level of generated C; on an STM32. proof, full text.
- [[2022-zhang-pa-boot-formally]] · processor authentication for multi-chip secure boot, proved in Isabelle/HOL. proof, main sections.
- [[2019-markettos-thunderclap-exploring-vulnerabilities]] · Thunderclap, NDSS 2019: attacks by a malicious device on macOS, FreeBSD and Linux with the IOMMU on; Windows mostly unprotected. test, full text.
- [[2026-moore-cheri-is-being]] · Moore, CHERI Blossoms 2026: CHERI for RISC-V is "being standardised"; criteria and open research. position, slides, full text.
- [[nd-sel4-sel4-roadmap]] · the seL4 roadmap: MCS C-level proof done on RISC-V, AArch64 Q3 2027; multikernel proofs Q3 2028. report, full text.
- [[2026-microkit-release-2-4-0]] · Microkit 2.4.0 on seL4 17.0.0: reply capabilities and parent fault endpoints no longer leak authority. report, full text.
- [[2026-proofcraft-sel4-security-proofs]] · seL4 news item, 24 August 2026: the confidentiality proof on AArch64 is finished, isolation complete under listed assumptions. report, full text.
- [[2026-jiang-futurertc-real-time]] · FutureRTC: an adapter that predicts the inputs of the next action chunk to tolerate inference delay; preprint. measurement, full text.
- [[2026-shen-mcp-38-comprehensive]] · MCP-38: 38 threat categories for the Model Context Protocol and the coverage of five tools; preprint. survey, full text.
- [[2026-zou-agentkernel-trust-native]] · AgentKernel: an agent OS on a conventional host with an external monitor and capability intersection; proofs deferred. design, partly read.
- [[2026-ahn-promise-proof-automation]] · PROMISE: structure-guided LLM proof search on 223 seL4 theorems, 55.7 % averaged over seven settings. measurement, partly read.
- [[nd-linux-landlock-unprivileged-access]] · Landlock, the Linux self-sandboxing module, kernel documentation of October 2026. report, partly read.
- [[nd-linux-real-time-preemption]] · PREEMPT_RT in the kernel documentation: sleeping locks, threaded interrupts, shared-hardware limits. report, partly read.
- [[2024-trail-leftoverlocals-listening-llm]] · LeftoverLocals: GPU local memory leaks between processes; 181 MB per LLM query on one AMD GPU. test, partly read.
- [[2026-zhang-agent-libos-runtime]] · Agent libOS: capability, ceiling, approval and budget must all agree before an operation runs; information flow checked apart; own suites pass. design, full text.
- [[2026-zhao-agenticos-intent-oriented]] · AgenticOS: an agent declares a manifest and only the semantic calls it names exist; a conceptual architecture, no implementation. design, full text.
- [[2026-ke-quine-realizing-llm]] · Quine: an agent as a POSIX process, renewed by exec; isolation inherited from the kernel, no capability model. design, full text.
- [[2026-narisetty-adaptive-evaluation-out]] · out-of-band defences compared; Progent against a hand-made adaptive attack on a 7B model: 25.8 % to 4.2 % to 2.6 %. test, full text.
- [[2026-maloyan-breaking-protocol-security]] · MCP's protocol-level weaknesses: attack success 26.4 % without MCP, 52.8 % with it; a signing extension brings it to 12.4 %. test, full text.
- [[2026-huang-model-context-protocol]] · seven MCP clients against poisoned tool descriptions: one failed all four attacks, the rest relied largely on the model's refusal. test, full text.
- [[2026-he-neuro-symbolic-proof-osdi]] · the OSDI version of the seL4 proof-search work: same 77.6 %, effort saving now 79.8 %. measurement, full text.
- [[2024-zhang-selene-pioneering-automated]] · Selene: a benchmark of 340 seL4 lemmas; GPT-4 proves 41.7 % of the easy set on the first try, almost none of the hard one. measurement, full text.
- [[2026-sharma-agent-operating-systems]] · AOS: an agentic control plane over Linux or Windows; reasoning untrusted, deny-by-default tool mediation; no implementation. design, partly read.
- [[2026-wu-mosaic-knowledge-guided]] · MOSAIC: benign CLI commands that compose through shared OS state beat Progent and CaMeL as tool-call hooks (96.63 % on Claude Code); preprint. measurement, partly read.
- [[2026-sharma-agent-operating-system]] · AOS-0001: a two-plane reference architecture for agent systems over Linux or Windows; monotone delegation; verification planned. design, partly read.
- [[2026-liao-llvm-translation-validation]] · Trivet: Lean proofs of LLVM optimisations built from a scaffold, with a model filling the holes; 74 valid proved, 73 of 74 invalid refuted. measurement, partly read.
- [[2026-peters-gill-can-camels]] · CaMeL's guarantee fails between agents (boundary laundering); multi-CaMeL fixes it for trees of agents; 0.2 to 0.0 % attack success. test, full text.
- [[2026-rinard-testing-credible-compilation]] · Axon: a compiler and its Lean proofs written by a coding agent in 34 days; optimisations checked by a verified certificate checker. report, partly read.
- [[2026-heiser-sel4-operating-systems]] · seL4 for reliability engineers: proof scope (single-core, MCS and Arm64 confidentiality pending in spring 2026), cost, LionsOS driver sizes. survey, full.
- [[2026-bansal-synergistic-simplex-cooperative]] · Synergistic Simplex: ML and safety layer exchange information in both directions; CARLA and nuPlan, ten runs per cell. test, partly read.
- [[2026-liao-llvm-translation-validation]] · Trivet: a model builds Lean proofs of LLVM transformations; 147 of 148 cases decided, against 20 of 30 for Alive2 on fixed-width loop-free cases. measurement, partly read.
- [[2026-liu-agentos-application-silos]] · AgentOS: a personal agent OS with an Agent Kernel and a semantic firewall over a legacy kernel; vision, no implementation. design, partly read.
- [[2026-heiser-trustworthy-systems-update]] · seL4 Summit 2026 slides: WCET revival scales (cache analysis from infeasible to about an hour), Microkit runs x86-64 UEFI, SMP against multikernel benchmarks. progress, partly read.
- [[2026-murphy-formalising-device-protocols]] · seL4 Summit 2026 talk: device models from a device's Verilog in HOL4, a rely-guarantee format for Pancake drivers; no device proved end to end on the slides. progress, partly read.
- [[2026-nguyen-booting-windows-x86-64]] · seL4 Summit 2026 talk: libvmm boots unmodified Windows 11 on x86-64 through UEFI; APICv cuts the boot from over ten minutes to 60 seconds; no isolation claim. report, partly read.
- [[2026-li-toolfence-fine-grained]] · ToolFence: a typed authorization blueprint from the user's request, a deterministic monitor and a model judge for gaps; 0.20 % attack success on AgentDojo with Qwen3-max; preprint. measurement, partly read.
- [[2026-chinaei-causality-laundering-denial]] · causality laundering: a denied tool call leaks what exists; a monitor that records denials; three constructed scenarios, single author. design, partly read.
- [[2026-lide-arsenal-assured-robotics]] · ARSENAL, seL4 Summit 2026 talk abstract: ROS 2 on seL4 for Army ground vehicles, two configurations, a proof of concept each; security services planned. report, abstract only.
- [[2026-steinder-towards-agent-operating]] · IBM position paper: an Agent-OS with 13 primitives on a Kubernetes control plane; no measurements. position, full text.
- [[2025-hu-vlsa-vision-language]] · AEGIS: a barrier-function layer behind a VLA policy; collision avoidance 18.7 to 77.9 % on SafeLIBERO, theorem conditional on perception. measurement, full text.
- [[2026-park-your-model-already]] · KNOWS: the policy's own attention names the target; collisions with moving obstacles 70.8 to 26.9 % against the authors' baseline, simulation only. measurement, full text.
- [[2026-elisa-enabling-linux-safety]] · ELISA's press release of February 2026: NVIDIA joins; the project aims to help certify Linux-based safety systems. report, full text.
- [[2026-agarwal-multi-link-safety]] · a barrier-function shield between a frozen VLA and the arm; collisions with moving hazards 65.62 to 27.27 % in simulation. measurement, full text.
- [[2026-rinard-quantitative-comparison-credible]] · credible compilation against verification: verified optimisations took about an order of magnitude more agent effort. measurement, full text.
- [[2025-li-osvbench-benchmarking-llms]] · OSVBench: 245 Hyperkernel tasks for LLM specification writing; best Pass@1 55.10 %, 0 % on five models without examples. measurement, full text.
- [[2025-tu-agentic-verification-software]] · AutoRocq: an agent proves 48.0 % of CoqGym lemmas, 30.9 % of SV-COMP C lemmas. measurement, full text.
- [[2025-zhao-verifying-device-drivers]] · Pancake: language, compiler and a verified Ethernet driver; the transpiler is unverified. proof, full text.
- [[2026-li-pace-provenance-aware]] · PACE: tool calls checked against a capability compiled from the authenticated request; 0 of 30 out-of-authority goals succeeded in a reduced adaptive search; premises unproved. test, full text.
- [[2026-nikolaou-camelot-camel-orchestrated]] · CaMeLoT: a static temporal check of the agent's plan before execution, on top of CaMeL; coverage and agreement with CaMeL, no attack-success figures. test, full text.
- [[2026-jager-context-dependent-runtime]] · a Simplex whose switching rule is built from design-time artifacts with several safe controllers; one-step prediction enough in simulation, about 15 periods needed on hardware. test, full text.
- [[2026-zheng-assuring-learning-enabled]] · a research agenda for learning-enabled CPS: the learned side holds capability, a monitor and a safe controller hold authority; no results. position, full text.
- [[2026-sison-two-interfaces-sel4]] · seL4 verification abstract: hardware flushes made time-protection proofs feasible; system-call Hoare triples that userland proofs assume are not yet proved. progress, full text.
- [[2024-wistoff-fence-t-s]] · fence.t.s on out-of-order OpenC910: three on-core channels closed at 1.0 % average overhead on Splash-2. measurement, slides only.
- [[2026-lu-faster-rethinking-real]] · FASTER: a flow policy that samples its first action in one step to shorten reaction time; measured on two consumer GPUs and one real arm. measurement, partly read.
- [[2026-nvidia-announces-halos-robotics]] · Halos for Robotics, the launch: IGX Thor, Halos OS, an ANAB-accredited inspection lab, Agility as first adopter; readiness inspection, no robotics certificate. report, full text.
- [[2026-nvidia-inside-halos-robotics]] · the architecture: SIL 3 capable safety island, Halos Core with Linux or Linux plus QNX under a hypervisor, an open outside-in safety blueprint, the lab's route to certification. report, full text.
- [[2026-qnx-nvidia-deepen-collaboration]] · QNX OS for Safety 8.0 integrated with IGX Thor and Halos for real-time control beside AI compute; no level or certificate named. report, full text.
- [[nd-sysgo-robotics-humanoids]] · PikeOS for robots: an untrusted ROS 2 and Linux partition separated in memory and CPU time from certified control; no proof mentioned. report, full text.
- [[nd-sysgo-safety-certification]] · PikeOS 5.1.3: DO-178C DAL A, IEC 61508 SIL 3, ISO 26262 ASIL D and more, pre-certified by TÜV SÜD; no scopes. report, full text.
- [[2026-abi-research-rtos-robotics-ranking]] · an analyst names QNX, Wind River, SYSGO and Green Hills leaders in robot-safety RTOS; the category exists. report, press release only.
- [[nd-sel4-proofs-certification]] · the seL4 Foundation on proof and certification: beyond EAL 7 and ASIL-D evidence by its reading, no certificate named, Isabelle/HOL not yet DO-178C qualified. position, full text.
- [[2024-dickson-limitations-formal-verification]] · proofs about AI in the physical world will stay approximate; verification will still have a role. position, partly read.
- [[nd-nvidia-openshell-overview]] · OpenShell's four protection layers and the mechanisms behind them; no assurance claim. report, full text.
- [[2026-red-hat-beyond-container-boundaries]] · OpenShell in OpenShift AI 3.5: default-deny outbound, an agent that proposes its own rule, four automatic checks; a vendor post. report, full text.
- [[2026-microsoft-windows-platform-security-agents]] · Build 2026: the MXC SDK in early preview, containment, identity and manageability as Windows primitives. report, full text.
- [[2026-microsoft-execution-containers-policy-driven]] · MXC generally available: backends, policy areas, modes, "an agent cannot be its own security authority"; OpenShell integrated. report, full text.
- [[2026-microsoft-windows-security-ignite-2026]] · Ignite 2026: the same direction for agents in one section of a broader security post. report, full text.
- [[2026-sel4-sel4-16-0]] · the seL4 news page for 2026: releases 15.0.0, 16.0.0 and 17.0.0 with their breaking changes, the AArch64 confidentiality item, Foundation members. report, full text.
- [[2026-wang-real-time-robot]] · REMAC: masked fine-tuning so a chunking policy copes with delay; beats RTC on one real arm; needs a maximum delay fixed in advance. measurement, full text.
- [[2026-liu-learning-native-continuation]] · Legato: continuation between chunks trained into the policy; 14 to 23 % faster than RTC on five dual-arm tasks, in its own runs. measurement, partly read.
- [[2026-chen-ravel-asynchronous-rolling]] · RAVEL: rolling inference cuts the time to the first action by 2.6 to 2.9 times on one GPU; real-world dynamic tasks. measurement, full text.
- [[2026-xu-safel4-rethinking-safe]] · safeL4: a Rust microkernel without hardware isolation between safe domains, primitives 1.91 times faster than seL4's on average on a Raspberry Pi 3B+; trusts the toolchain and DMA devices. measurement, partly read.
- [[2026-wang-agentic-os-kernel]] · IntentOS: a language model beside Linux composes micro-syscalls; safety rests on new per-call checks. measurement, partly read.
- [[2026-kurd-cheri-standardisation-status]] · Kurd, April 2026: CHERI for RISC-V in architecture review before its freeze; ratification intended for Q2, thought more likely Q3, on a slide marked out of date. progress, slides, full text.
- [[2025-cheriot-cheriot-isa-1]] · CHERIoT ISA 1.0, November 2025: stable since December 2024, two implementations, first chips from the fab; the RISC-V CHERI base "tentatively Y". report, full text.
- [[2026-owasp-owasp-mcp-top]] · a security vendor's guide to the OWASP MCP Top 10 (version 0.1): ten risks, 30-plus CVEs in two months, figures without method. report, full text.
