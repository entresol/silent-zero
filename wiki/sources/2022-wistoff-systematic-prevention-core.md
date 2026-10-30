---
type: source
id: 2022-wistoff-systematic-prevention-core
status: reviewed
read: full
kind: measurement
sources: [2022-wistoff-systematic-prevention-core]
updated: 2026-10-29
---

# Wistoff et al. 2022: Systematic Prevention of On-Core Timing Channels

Nils Wistoff, Moritz Schneider, Frank K. Gürkaynak, Gernot Heiser and Luca Benini (ETH Zürich, UNSW Sydney, University of Bologna). IEEE Transactions on Computers, 2022; read in the arXiv version 2 of 13 October 2025. [arXiv](https://arxiv.org/abs/2202.12029).

## What it shows

- **Even a simple in-order core leaks.** On an unmodified [[cva6]], a prime-and-probe attack through the L1 data cache transmits more than 1.6 bits per attack round, enough to leak a 256-bit key in under 320 ms with 1 ms time slices (§5.2.3). The branch history table leaks more than 4 bits per iteration (§5.2.4).
- **Software alone does not close the channels.** Using only instructions the RISC-V ISA defined at the time, the OS reduces the cache channel but cannot close it, partly because the cache's pseudo-random replacement defeats reliable eviction, and the attempt makes a context switch about 40,000 cycles long (§5.2.3; Table 2 in §5.3.1).
- **A temporal fence does.** The authors add an instruction, `fence.t`, and compare three implementations: flushing the known components, flushing an extended hand-picked set, and *Microreset*, which resets every flip-flop except the architectural state. Only Microreset closed all measured channels consistently, across cache configurations and attacks (§5.2, Table 1). The basic flush left channels through the replacement policy's random generator and round-robin arbiters (§5.2.3.3); the full flush cleared those but still leaked sporadically, because its single-cycle reset did not reach all pipelined components at once and through the cache's miss handler (§5.2.3.4).
- **The flush itself can leak, whichever implementation is used.** Writing back a dirty cache takes time that depends on the secret, which made the context-switch latency a channel close to its 8-bit maximum. Padding the switch to its worst case removed it: 22,000 cycles for a write-back cache, 3,700 for write-through (§5.2.5).
- **Cost.** Splash-2 slowed down by under 1 per cent, 0.7 per cent on average. The authors switched context every 10 million cycles and equate that to a 10 ms time slice at 1 GHz; the FPGA itself ran at 50 MHz (§5.1, §5.3.4). Area overhead is given as 0.13 per cent in the introduction and as 0.4 per cent in §5.3.3, with no effect on the critical path.

## How

CVA6 on a Xilinx Kintex-7 FPGA (Genesys II) at 50 MHz, with the L2 cache partitioned by colouring so that only on-core channels remain. The OS is an experimental version of [[sel4]] with time protection that "has not yet been formally verified" (footnote 1). Leakage is measured as mutual information over one million runs, against a bound for noise (§5.1, §5.2.2). Area figures come from synthesis in 22 nm at 1 GHz (§5.3.3).

## Limits

The authors state:

- Cross-core leakage is out of scope; the Trojan and the spy share one core (§2.2).
- Only timing channels are covered, not power or other physical channels (§2.2).
- The seL4 version used is unverified.
- Identifying architectural state was simple for CVA6; for out-of-order cores it may be harder (§4.2.3).

A careful reader adds:

- **An FPGA prototype.** `fence.t` is a custom instruction on a research core; it is not part of the ratified RISC-V ISA. The paper's Section 4 says the instruction exists "only as prototypes", which matches.
- **The area figure appears twice with different values.** 0.13 per cent (§1) and 0.4 per cent (§5.3.3).

## Against the wiki

- [[cva6]]: **extends** it with timing-channel protection.
- [[time-protection]]: created with this source.

## For zOS

- [[kernel]]: the paper (Section 4) says closing timing side channels needs a hardware instruction that exists only as prototypes, citing this paper and Wistoff et al. 2024 (`fence.t.s` for out-of-order cores, not covered here). Confirmed for on-core state; off-core caches can be partitioned in software by colouring, as the paper here does for its L2.
- Our reading: for zOS the agent and the control loop share hardware. Timing channels matter for confidentiality, the agent learning what it should not. For the loop's deadlines, the padded context switch is the relevant part: it makes switching cost a fixed, known quantity.
