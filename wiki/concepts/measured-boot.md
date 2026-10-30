---
type: concept
status: reviewed
sources: [nd-coreboot-measured-boot, 2021-tao-dice-formally-verified, nd-caliptra, 2020-straznickas-verified-first-stage]
updated: 2026-10-30
---

# Measured boot

Each boot stage records a hash of the next before handing over, so that afterwards someone can check what ran ([[nd-coreboot-measured-boot]]; [[2021-tao-dice-formally-verified]], §1). Our reading: measurement alone, as in coreboot's TPM chain, stops nothing from running; its value lies in the record being checked. Some designs combine it with verification; DICE does both.

## Two designs

- **With a TPM.** Measurements are extended into TPM registers. In coreboot the first measurement is taken by its own boot block, a root "rooted in software"; Intel Boot Guard and AMD Hardware Validated Boot move typically the *verification* root into hardware, and Boot Guard's measurement mode was never deployed ([[nd-coreboot-measured-boot]]).
- **With DICE.** A hardware engine first authenticates the next layer by signature, then derives an identity from a device secret and the hash of the next layer, then locks the secret; each layer derives its keys from that identity, so any firmware change changes the keys. It needs less hardware than a TPM ([[2021-tao-dice-formally-verified]], §1, §2). Caliptra provides such a measurement root inside data-centre SoCs ([[nd-caliptra]]).

## State, October 2026

DICE's engine and first layer have a verified implementation: memory safe, functionally correct and free of secret-dependent branches and memory accesses at the level of the generated C, with the compiler and about 850 lines of platform code trusted; it runs on an STM32 microcontroller ([[2021-tao-dice-formally-verified]]). A first-stage RISC-V measurement root that signs what it loads has a partial proof against instruction semantics ([[2020-straznickas-verified-first-stage]]).

## Open questions

- Where the zOS loader's measurement is recorded, if anywhere beyond its screen, and who checks it. See [[bootloader]].
