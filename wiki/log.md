# Log

What happened in the wiki, newest last. Find the last entries with `grep "^## \[" log.md | tail -5`.

## [2026-10-25] setup | schema, index, log

Schema in `CLAUDE.md`. The wiki starts empty; the first sources are worked in one at a time, with a person, to settle the page format.

## [2026-10-25] ingest | 2026-sillitoe-resurrecting-sel4-wcet

Together with `nd-trustworthy-wcet-worst-case`, which it updates. Created: both source pages, [[wcet-analysis]], [[sel4]], [[cva6]], [[kernel]]. Question raised: does Section 4's "only on open RISC-V" still hold now that Arm publishes in-order latencies again? Fact check by a second agent: about 115 claims, 13 too strong or unsupported, all fixed. Pool candidate: Blackham et al. 2011 (RTSS), to settle ARM11 versus Armv7. Schema: evidence kind `progress`, rules on hedges, marked inferences and front matter in the linter.

## [2026-10-28] setup | rings, daily ingest

`rings.md` orders the backlog of 86 pool sources in three rings: 20 load-bearing sources (one group per part of the design), 50 neighbours, rivals and attacks, 18 on history and setting. Ring 1 is open. The daily run now works in its own new sources and up to three from the backlog per day, each with a second agent's fact check. Ring 2 still has to be sorted before it opens.

## [2026-10-29] ingest | ring 1, kernel group

Six sources: 2009-klein-sel4-formal-verification, nd-sel4-verified-configurations, 2026-sel4-functional-correctness-proof, 2026-heiser-mcs-safety-os (slides only), 2026-trustworthy-guaranteeing-timeliness-mcs, 2018-klein-formally-verified-software (full text now in the pool). Created: six source pages, [[functional-correctness]], [[mixed-criticality]]. Rewritten: [[sel4]], [[kernel]]. Changed: [[wcet-analysis]], [[nd-trustworthy-wcet-worst-case]], [[2026-sillitoe-resurrecting-sel4-wcet]]. Questions: the paper's "only for the ARM11 processor" is narrower than three sources (Armv6 and Armv7); the verified-configurations page still calls MCS ongoing after the June 2026 announcement. Pool candidates: Lyons et al. 2018, Mi et al. 2019, Sewell et al. 2011, 2013, 2016, Murray et al. 2013. Fact check by Claude in the session against the texts; vorfeld.py did not run (spacy missing).

## [2026-10-29] ingest | ring 1, static system and drivers

Four sources: nd-sel4-microkit-user-manual, 2026-trustworthy-lionsos (introduction page), 2022-parker-sel4-device-driver (slides only), 2026-tyler-smt-based-deductive. Created: four source pages, [[microkit]], [[lionsos]], [[static-system]], [[drivers]]. Changed: [[sel4]], [[kernel]]. Questions: the paper's "nothing is loaded at run time" is stricter than LionsOS, which swaps components at run time; whether 2025-heiser-fast-secure-adaptable, cited by the paper for the driver VM, should move from ring 2 to ring 1. Pool candidates: Åman Pohjola et al. 2023, Ryzhyk et al. 2009, Murphy et al. 2025. Fact check by Claude in the session; vorfeld.py did not run.

## [2026-10-29] ingest | ring 1, safety path, real time, timing, root of trust

Five sources: 2022-wistoff-systematic-prevention-core, 2026-trustworthy-where-are-we (slides fetched from the programme page), 2025-nesti-use-simplex-architecture, 2025-black-real-time-execution, 2026-google-opentitan-shipping-production. 2001-sha-using-simplicity-control is blocked: only bibliographic data is open. Created: five source pages, [[time-protection]], [[simplex]], [[action-chunking]], [[opentitan]], [[safety-path]], [[real-time-loops]], [[root-of-trust]]. Changed: [[kernel]], [[cva6]]. No contradiction with the paper; the paper's Simplex claim rests on a source the wiki cannot read yet. Fact check by Claude in the session; vorfeld.py did not run.

## [2026-10-29] ingest | ring 1, broker

Four sources: 1988-hardy-confused-deputy-or, 2006-miller-robust-composition-towards (chapters 1–3, 8, 9, 12 only), 2025-debenedetti-defeating-prompt-injections (main text; appendices not read), 2026-nasr-attacker-moves-second (arXiv v1). Created: four source pages, [[confused-deputy]], [[object-capabilities]], [[prompt-injection]], [[broker]]. Question: the paper's Table 1 says CaMeL has "provable security"; the source's guarantee is by design with an unverified interpreter. Ring 1 is done except Sha 2001, which is blocked. Fact check by Claude in the session; vorfeld.py did not run.

## [2026-10-29] lint | independent review of ring 1

Two further readings first: Miller chapter 11 and CaMeL appendices D, E and I (revocation across machines; policy triggering rates). Then five reviewers with fresh context, four checking one group each against the source texts and the paper, one checking the wiki as a whole; about 95 findings. Fixed: claims stronger than their sources (MCS proof level, budgets as proven, OpenTitan as tested, driver proof without its trusted parts, chunking credited with what RTC does), facts missing from pages (Nasr et al. skip CaMeL by design; CaMeL names a ROP-like attack on itself; Nesti et al. date Simplex to 1994; Microkit's paths between components beyond channels; integrity not stated for MCS), misread paper passages ("into the core"; Section 4, not 3, for Simplex), unmarked inferences, citations, front matter, index counts, a broken link, and workflow wording on public pages. Rewritten: static-system, drivers, safety-path, real-time-loops, broker, microkit, lionsos, simplex, action-chunking, prompt-injection, confused-deputy, object-capabilities and six source pages. Questions moved from the pages to the pull request. Not changed: list items that start with a bold label and a full stop, used across all pages since the first ingest; a decision for the team. vorfeld.py still did not run.

## [2026-10-29] lint | vorfeld, and Sha 2001 out of ring 1

`vorfeld.py` now runs through `uv run` without installing spaCy; the schema says how. Run on all 42 pages: most hits came from semicolons and merged lists; ten sentences without a verb or with a long opening were rewritten. 2001-sha-using-simplicity-control moved from ring 1 to ring 3: the pattern goes back to 1994 and is history, not part of the bare minimum. Ring 1 is complete.

## [2026-10-30] ingest | firmware and boot, core (14 sources)

nd-coreboot-architecture, nd-coreboot-vboot, nd-coreboot-measured-boot, nd-chromeos-verified-boot, nd-tfa-firmware-design (cold boot and runtime services), nd-opensbi (README), nd-uboot-verified-boot, nd-raspberrypi-boot (boot chapters, from the documentation's source repository), nd-sel4-x64-platform, nd-caliptra (README), 2018-cook-model-checking-boot, 2020-straznickas-verified-first-stage, 2021-tao-dice-formally-verified, 2022-zhang-pa-boot-formally (main sections). Created: fourteen source pages, [[bootloader]], [[coreboot]], [[tf-a]], [[opensbi]], [[raspberry-pi]], [[verified-boot]], [[measured-boot]]. Rewritten: [[root-of-trust]]. Changed: [[opentitan]]. The firmware group is split into core and periphery; nd-openbios moved to ring 3. Question: the paper's loader has no fallback, where vboot and Chromium OS recover automatically.

## [2026-10-30] lint | independent review of the firmware core

Three reviewers with fresh context checked the fourteen firmware sources and the pages built on them; 63 findings. Fixed: vboot's recovery described as automatic (only the switch between signed slots is); Boot Guard and AMD HVB credited with the measurement root (they root verification); Straznickas presented as a verifying loader (it is a measurement root that signs); DICE presented as measurement only (it authenticates first); the paper said to leave open whether its loader verifies or measures (it does both); Caliptra's licence and releases; the Pi's bootloader replaceable from the SD card and its own A/B fallback; missing author limits for PA-Boot and DICE\*; hedges and scopes. Rewritten: [[bootloader]], [[root-of-trust]], three source pages.

## [2026-10-30] lint | review of all 63 pages

Every figure and every quotation on every page was searched in its source or in the paper; all were found. The pages on concepts, systems and the design were read in full against their sources, the source pages for their limits and for what a partial reading leaves out. No page is held back. All pages are now `reviewed`. One fix: the Microkit manual's "does not provides" is quoted with [sic].

## [2026-10-30] move | into the public repository

The wiki moved from `wiki-draft/` of the private research repository to `wiki/` of the public one. `zos/` is now `design/`, and the page type `zos` is `design`. The status levels are `drafted`, `reviewed` and `doublechecked`. The project's name is written `zOS` and replaced by the build. The rings are a guide to the order, no longer a gate.

## [2026-10-30] update | bootloader

Added the project's boot video (seL4 16.0.0 release kernel to user space on RISC-V in QEMU, through OpenSBI and seL4's ELF loader) to [[bootloader]], with the reading that it shows seL4's boot chain, not the zOS loader. seL4 16.0.0's general verified RISC-V configurations are set for this platform (`hifive`); whether the video's kernel was built in one of them is open. [[nd-sel4-verified-configurations]] now notes that the documentation page lists fewer RISC-V platforms than the configuration files.

## [2026-10-30] update | bootloader

The boot video now shows the official seL4 16.0.0 kernel built with the preset `RISCV64_MCS_verified`, rebuildable from `loader/sel4-demo/`. [[bootloader]] says so, and that the proofs cover the C code, not the binary, the emulated hardware or the boot chain before the kernel.

## [2026-10-31] ingest | 2026-anthropic-project-glasswing-securing, 2026-anthropic-project-glasswing-initial, 2026-bower-cohesix-research-operating

Daily run, backlog of ring 2. Created: three source pages, [[ai-vulnerability-discovery]], [[cohesix]]. Changed: [[broker]] (Related), [[raspberry-pi]]. Cohesix was read from its landing page only (`partial`). 2023-amar-cheriot-complete-memory was skipped: the pool holds no text for it, only a landing-page link.

## [2026-10-31] rule | the daily run merges its own wiki pull request

The team decided that the daily run's pages go live without waiting for a person, once every page is `reviewed`, no open question concerns a wiki page and the build has run. It merges with squash; `wiki/.cache/` is now ignored, after a run had committed extracted source texts.
