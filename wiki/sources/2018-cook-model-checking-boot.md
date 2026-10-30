---
type: source
id: 2018-cook-model-checking-boot
status: reviewed
read: full
kind: proof
sources: [2018-cook-model-checking-boot]
updated: 2026-10-30
---

# Cook et al. 2018: Model Checking Boot Code from AWS Data Centers

Byron Cook, Kareem Khazem, Daniel Kroening, Serdar Tasiran, Michael Tautschnig and Mark R. Tuttle (Amazon Web Services, UCL, Oxford, Queen Mary). CAV 2018, LNCS 10982, pp. 467–486. [Publication page](https://www.amazon.science/publications/model-checking-boot-code-from-aws-data-centers).

## What it shows

- **A proof of memory safety for production boot code.** The authors prove that the initial boot code running in AWS data centres is memory safe: no buffer overflows, no null dereferences, no pointers into unallocated memory (abstract, §3.2).
- **What exactly is proved** (§5): for every boot configuration, every device configuration, each of three boot sources and every stage-2 binary, the stage-1 boot code shows no memory-safety error. This holds under four assumptions: the stage-2 and temporary buffers are 1,024 bytes; cryptographic, CRC and printf routines have no side effects and may return any value; CBMC's models of `memcpy` and `memset` are used; and a loop that flashes the console lights on failure is ignored.
- **Size and effort.** 783 lines of statically reachable code, with 98 loops; a 76-line test harness; CBMC finished in about 10 minutes on one core with 5 GiB of memory (§5.6, §5.7).
- **Soundness.** The bounded model checker is sound here because all loop-unwinding assertions hold: the loops run over arrays of known size or count down from bounded values (§2, §5.7).
- **What boot code needs from a tool.** Memory-mapped device registers, device behaviour behind them, byte-level memory access, memory copying and linker scripts. The authors extended CBMC for all five; it is "the first source-level static analysis tool to extract the memory layout described in a linker script" (abstract, §4).

## How

The C Bounded Model Checker (CBMC), extended for boot code, run against a test harness that declares more than 30 memory-mapped regions and models all devices as returning arbitrary values (§4, §5.2, §5.6).

## Limits

The authors state:

- The assumptions above mean that memory-safety errors in the cryptographic, CRC and printf routines may be missed; those can be checked separately (§5).
- Loop bounds for the `while (num)` loops come from "code inspection", a manual step in the soundness argument (§5.7).
- The code is proprietary; the authors point to the open-source rBoot, about 700 lines, as showing most of the same challenges (§5).

A careful reader adds:

- **Memory safety, not correctness.** The proof says the code cannot corrupt memory; it says nothing about whether it boots the right image.
- **Source level.** The analysis is of C source; the compiler is trusted.

## Against the wiki

- [[verified-boot]]: the first proof in the wiki about boot code in production.

## For zOS

- [[bootloader]]: the paper counts the loader in the trusted base as *assumed* (Section 3). This source shows that stage-1 boot code of a few hundred lines can be proved memory safe with an extended automatic tool, under assumptions that abstract away its cryptography. Our reading: memory safety is a realistic first property for the zOS loader. The comparison is rough: the paper gives the loader's size as just under 9 KB of binary, about two thirds of it renderer and font data, against 783 lines of C here, and the signature check the loader needs is exactly what Cook et al. abstracted.
