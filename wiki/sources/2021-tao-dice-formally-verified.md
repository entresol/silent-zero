---
type: source
id: 2021-tao-dice-formally-verified
status: reviewed
read: full
kind: proof
sources: [2021-tao-dice-formally-verified]
updated: 2026-10-30
---

# Tao et al. 2021: DICE\*, a Formally Verified Implementation of DICE Measured Boot

Zhe Tao, Aseem Rastogi, Naman Gupta, Kapil Vaswani and Aditya V. Thakur (UC Davis, Microsoft Research). USENIX Security 2021. [Paper](https://www.usenix.org/conference/usenixsecurity21/presentation/tao).

## What it shows

- **DICE in brief.** The Device Identifier Composition Engine is a measured-boot architecture that needs less hardware than a TPM. A hardware engine, typically in ROM, first authenticates the next firmware layer (L0) by signature, then derives a compound device identifier from a unique device secret and a hash of L0, locks the secret away until the next reset, and hands over. Each layer derives keys from its identifier, so a firmware change changes the keys (§1, §2.1, §2.2). DICE thus verifies and measures.
- **What is proved.** The authors prove four properties for the DICE engine and L0: memory safety, functional correctness against a formal specification of the standard, no secrets in the outputs, and resistance to timing and cache side channels, in the sense that no branch or memory access depends on a secret (abstract, §1.1, §2.4).
- **A verified certificate library.** L0 must produce X.509 certificates and signing requests; the authors built a verified serialiser for the needed fragment of ASN.1 and X.509, whose encoding is proved injective, so a certificate cannot be made to describe different firmware (§5).
- **Size.** The engine is 533 lines of F\* extracting to 205 lines of C; L0 is 24,241 lines of F\*, 16,564 of them for ASN.1 and X.509, extracting to 5,051 lines of C (§6, Table 1).
- **On hardware.** Integrated into the boot firmware of an STM32H753ZI microcontroller (Cortex-M7, 480 MHz). Against a hand-written implementation, boot time was 689 ms against 786 for the engine and 208 against 313 for L0; binary size 68 KB against 72 and 92 against 92 (§7.2, Table 2). The authors attribute the engine's difference to different signature curves (Ed25519 against P-256) and L0's to the X.509 code (§7.2).

## How

Written in Low\*, a C-like subset of F\*, using the verified cryptographic library HACL\* and the parser library LowParse; the code is extracted to C (§3).

## Limits

The authors state:

- Guarantees, side-channel resistance included, reach the generated C; the F\* toolchain with the Z3 solver and the KreMLin compiler is trusted, and so is the C compiler unless a verified one is used (§2.5).
- Also trusted: the platform-specific functions, the bootloader, drivers and a declassification routine, and a manufacturer PKI that issues certificates only to genuine devices (§2.5). The bootloader and platform interface on the STM32 are 38 lines of assembly and 815 lines of C; there, the function that disables the device secret is empty, and secure access mode does the locking (§7.1).
- Out of scope: speculative execution, fault injection, cold-boot attacks, physical probing, and attacks in manufacturing and the supply chain (§2.3).
- The two implementations use different curves, because the libraries offered no common one (§7.2).

A careful reader adds: the timings are single figures, without repetitions or variance.

## Against the wiki

- [[measured-boot]]: **extends** it with DICE, a measured boot without a TPM that also authenticates, and a verified implementation of it.

## For zOS

- [[bootloader]], [[root-of-trust]]: the paper wants the root of trust to measure the first code and the loader to show what it measured (Section 3). Our reading: DICE is a design small enough for a microcontroller that both verifies and measures, and this work shows its first two layers can be verified at the level of generated C. It bears on the open question on [[bootloader]] of where the loader's measurement is recorded.
