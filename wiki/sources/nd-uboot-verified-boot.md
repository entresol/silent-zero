---
type: source
id: nd-uboot-verified-boot
status: reviewed
read: full
kind: report
sources: [nd-uboot-verified-boot]
updated: 2026-10-30
---

# U-Boot: verified boot

A page of the U-Boot documentation, undated, read on 30 October 2026. [Page](https://docs.u-boot.org/en/latest/usage/fit/verified-boot.html).

## What it shows

- **Definition.** Verified boot means verifying all software loaded during boot, from reset "to as far as you wish". An example chain: U-Boot from read-only memory, then a signed kernel, then a signed root file system through dm-verity.
- **Updates.** Because only correctly signed software runs, software may be read from updatable media, and a second signed firmware image in read-write memory allows secure upgrades.
- **The key.** "It is critical that the public key be secure and cannot be tampered with." It can sit in read-only memory, "or perhaps" be protected by on-chip crypto that some SoCs provide; "if the public key can be changed, then the verification is worthless".
- **Chaining.** A master key in read-only memory verifies the first stage; a secondary key in that stage verifies the next. A different key per stage is recommended, so that a compromise in one place does not affect the whole chain.
- **FIT.** U-Boot's Flattened Image Tree format already carries hashes; signatures are added, and the public key can be stored in U-Boot's control device tree. Multiple keys and signatures are supported.

## How

A short user-guide page; details are in a separate document on FIT signature verification, not covered here.

## Limits

A careful reader adds: the page is an introduction. It does not discuss rollback, revocation of keys, or how U-Boot itself is protected.

## Against the wiki

- [[verified-boot]]: **confirms** the chain-of-keys model.

## For zOS

- [[bootloader]]: the zOS loader prototype checks a hash, not yet a signature, and the paper says it "so far checks a hash rather than a signature" (Section 3). This page states the condition that decides whether a signature is worth anything: the public key must be in memory the attacker cannot change.
