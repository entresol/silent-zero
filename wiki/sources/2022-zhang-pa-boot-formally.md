---
type: source
id: 2022-zhang-pa-boot-formally
status: reviewed
read: partial
kind: proof
sources: [2022-zhang-pa-boot-formally]
updated: 2026-10-30
---

# Zhang et al. 2022: PA-Boot, a Formally Verified Authentication Protocol for Multiprocessor Secure Boot under Hardware Supply-chain Attacks

Zhuoruo Zhang, Rui Chang, Mingshuai Chen, Wenbo Shen, Chenyang Yu, He Huang, Qinming Dai and Yongwang Zhao (Zhejiang University). Read in arXiv version 3 of 21 April 2025, whose header names IEEE Transactions on Information Forensics and Security without volume or issue. [arXiv](https://arxiv.org/abs/2209.07936). The abstract, introduction, background, assumptions, implementation and discussion were read; the protocol and proof chapters were skimmed.

## What it shows

- **The attack surface.** In a multiprocessor system the bootstrap processor starts the system and the application processors join later. Secure boot trusts the processors as its root; the authors argue that an attacker in the hardware supply chain can replace an application processor or insert a chip into the inter-processor link and so bypass secure boot (abstract, §I, §II).
- **The protocol.** PA-Boot authenticates the application processors and protects inter-processor communication during early boot, and aborts the boot when it detects a replaced processor or a man-in-the-middle (§I).
- **The proof.** Formalised and proved in Isabelle/HOL with 306 lemmas and theorems in about 7,100 lines, covering functional correctness and security properties such as processor authenticity and certificate integrity; about 8 person-months of proof effort (abstract, §I, §VI).
- **The implementation.** A C implementation, CPA-Boot, of about 1,400 lines, related to the model by a code-to-spec review and by tests against code extracted from the Isabelle model, and run on Arm's simulated Fixed Virtual Platforms with an overhead of 4.98 per cent on Linux boot (abstract, §VII).

## How

A protocol design with a mechanised proof and a simulated evaluation.

## Limits

The authors state:

- Assumptions: the bootstrap processor is trusted, its authenticity ensured by the baseboard management controller; the boot ROM is immutable; the application processors' private keys cannot be extracted (§III-A). The adversary is Dolev-Yao with black-box cryptography (§V).
- Deployment needs the protocol embedded in the CPU's immutable boot ROM during manufacturing (§VIII).
- The simulator has no inter-processor bus, so the channel is mimicked through main memory (§VII).
- Generating verified C code is future work (§VIII).

A careful reader adds: the setting assumes processors in physically separate chips.

## Against the wiki

- [[verified-boot]]: extends the picture to the hardware supply chain, which secure boot otherwise trusts.

## For zOS

- [[root-of-trust]]: our reading: the paper's hardware profile trusts the processor; PA-Boot shows that this trust is itself an assumption that can be attacked on boards with several processor chips, and that a defence needs changes to the CPU's boot ROM. On a single system-on-chip such as the Raspberry Pi's, the attack as described does not apply.
