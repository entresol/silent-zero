---
type: source
id: nd-chromeos-verified-boot
status: reviewed
read: full
kind: design
sources: [nd-chromeos-verified-boot]
updated: 2026-10-30
---

# Chromium OS: Verified Boot (design document)

A design document of the Chromium OS project, undated, read on 30 October 2026. [Page](https://www.chromium.org/chromium-os/chromiumos-design-docs/verified-boot/).

## What it shows

- **The aim.** Verified boot "is focused on stopping the opportunistic attacker"; it is not expected to detect every attack. It should detect changes to the read-write firmware and to the files the boot depends on, and allow updates in the field.
- **Not a lock-in.** "Restraining the boot path to only Chromium-project-supplied code is not a goal"; the user must be able to reset the device to a known-good state. There is no dependence on remote attestation. "Users will always own their computers."
- **The chain.** A small read-only stub hashes the read-write firmware and checks an RSA signature against a permanently stored public key, ideally of 2048 bits or more. The read-write firmware has its own subkey and checks the kernel and initial RAM disk, so updates need not use the write-protected key.
- **Above the kernel.** Checking the whole root file system before boot would add at least 5 seconds on the netbooks of the time, so blocks are checked on access against a tree of hashes whose root is fixed in the kernel or a verified RAM disk.
- **On failure.** The firmware starts recovery, or the user may choose to proceed, which suits a development install. There is no plan to support remote inspection of whether a device booted verified.
- **Known weaknesses.** Writable state on the stateful partition can make verified code "take a wrong turn". Rolling back the hash partition to an older, vulnerable version is hard to detect. A determined local attacker who opens the device and enables writing to the protected firmware is not stopped.

## How

A design document with a threat model and a list of attack cases; it describes the intended design and reports no measurements beyond estimates.

## Limits

The authors name the weaknesses listed above. They call management of the key that signs the read-only firmware "of utmost importance" and leave out of scope only how to keep it off network-enabled machines. A TPM tickstamp could address the rollback of the hash partition "to some degree".

A careful reader adds: the document is old (it speaks of netbooks and SHA-1) and describes a plan; [[nd-coreboot-vboot]] shows how it is implemented in coreboot today.

## Against the wiki

- [[verified-boot]], [[nd-coreboot-vboot]]: **extends** them with the threat model and the stance on ownership.

## For zOS

- [[bootloader]]: the paper's loader "checks one signed, static system image and starts it, or stops" (Section 3). Our reading: this document's weaknesses, rollback and writable state that steers verified code, apply to any loader that verifies images, the zOS loader included. Whether zOS should follow its stance on ownership, reset without remote attestation, is a choice for the project.
