---
type: source
id: nd-coreboot-measured-boot
status: reviewed
read: full
kind: report
sources: [nd-coreboot-measured-boot]
updated: 2026-10-30
---

# coreboot: measured boot

A page of the coreboot documentation (version 26.09), undated, read on 30 October 2026. [Page](https://doc.coreboot.org/security/vboot/measured_boot.html).

## What it shows

- **Measured boot without verified boot.** Measured boot began as part of vboot and has since been decoupled; it no longer requires vboot.
- **Static root of trust for measurement.** The initial boot block measures itself before measuring the next block; the page notes that this makes its root of trust "rooted in software".
- **Vendor hardening.** To move the root into hardware, CPU makers added an external root of trust the CPU validates at boot, which then validates the initial boot block: Intel Boot Guard and AMD Hardware Validated Boot, also called Platform Secure Boot. These move typically the *verification* root into hardware. Intel also designed a measurement mode for Boot Guard that would have made its module the start of the measurement chain, but it "was never deployed".
- **What is measured.** CBFS files are hashed as raw data before decompression, into PCR 2 by default; data that changes at run time goes into PCR 3. Measurements are cached in an event log until the TPM is set up, unless TPM initialisation is moved into the bootblock.
- **Dynamic root.** Intel TXT and AMD-V can start a measurement chain at any time with the CPU as its root, using PCRs 17 to 22.
- **Limits stated.** Measuring the initial boot block dynamically and measuring flash partitions are not yet possible, and SoCs that use `VBOOT_RETURN_FROM_VERSTAGE` cannot use measured boot because of platform constraints.

## How

Developer documentation, with event-log formats and an example log whose measured regions include `SI_ME` (in our reading the Intel ME region) and the FSP binaries.

## Limits

The page states that some measurement features are not yet implemented (Known Limitations).

A careful reader adds: a measurement records what ran; it does not stop anything from running. Its value depends on someone checking the record, locally or by attestation.

## Against the wiki

- [[measured-boot]]: created with this source.

## For zOS

- [[root-of-trust]]: the paper wants a root of trust "that measures the first code to run" (Section 3). On x86, coreboot's first measurement is taken by its own boot block; Boot Guard and AMD's mechanism root only the *verification* of that block in hardware, and Boot Guard's measurement mode was never deployed. The measurement root stays in software.
- [[bootloader]]: the paper's loader checks a signed image and shows "what the loader has measured itself" (Section 3), so it verifies and measures. Our reading: what is open is whether the measurement is recorded anywhere, in a TPM or by DICE, or only displayed.
