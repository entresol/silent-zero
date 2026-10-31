---
type: design
status: reviewed
sources: [nd-coreboot-architecture, nd-coreboot-vboot, nd-chromeos-verified-boot, nd-uboot-verified-boot, nd-raspberrypi-boot, nd-tfa-firmware-design, nd-opensbi, nd-sel4-x64-platform, nd-sel4-microkit-user-manual, nd-sel4-verified-configurations, 2018-cook-model-checking-boot, 2020-straznickas-verified-first-stage, 2021-tao-dice-formally-verified, 2026-sel4-release-17, nd-sel4-supported-platforms, 2024-riscv-privileged-isa-manual]
updated: 2026-10-31
---

# The bootloader

In zOS the bootloader "checks one signed, static system image and starts it, or stops. There is no menu, no configuration and no fallback, and nothing of it stays resident." It draws the first screen, showing only compiled-in text and what it has measured itself, and marks as assumed what it cannot check, itself included. It belongs to the trusted base as *assumed*. A first prototype for RISC-V checks a hash rather than a signature and is just under 8 KB, more than two thirds of it the renderer and its font data (paper, Section 3).

## What it must do

- Accept only an image signed with a key the attacker cannot change.
- Start that image or stop; say why when it stops.
- Show what it measured.

## Where it sits

| Platform | What runs before it | How the kernel is started today | Source |
| --- | --- | --- | --- |
| PC (x86-64) | vendor firmware and, with coreboot, its stages up to the payload | a Multiboot loader such as GRUB or syslinux; Microkit requires a Multiboot 2 loader | [[nd-coreboot-architecture]], [[nd-sel4-x64-platform]], [[nd-sel4-microkit-user-manual]] |
| Arm boards | on Arm's reference platforms TF-A's BL1, BL2 and BL31; on vendor boards often a vendor ROM in place of BL1 and BL2 | U-Boot loads the Microkit image, and the Microkit loader starts seL4 | [[nd-tfa-firmware-design]], [[nd-sel4-microkit-user-manual]] |
| Raspberry Pi 4 and 5 | ROM and EEPROM bootloader, on the Pi 4 also the GPU firmware; on the Pi 5 the bootloader loads the kernel image itself | for Microkit on the Pi 4B, U-Boot, then the Microkit loader | [[nd-raspberrypi-boot]], [[nd-sel4-microkit-user-manual]] |
| RISC-V | OpenSBI in machine mode; on the HiFive Premier P550 firmware, then OpenSBI and U-Boot from SPI flash | U-Boot, or OpenSBI with the image as its payload, then the Microkit loader | [[nd-opensbi]], [[nd-sel4-microkit-user-manual]], [[nd-sel4-supported-platforms]] |

## What exists, and what kind of evidence it is

| Claim | State in the paper's terms | Evidence | Source |
| --- | --- | --- | --- |
| Signed-image checking with a public key in protected memory | assumed; documented in U-Boot, deployed with coreboot's vboot in Chromebooks | design | [[nd-uboot-verified-boot]], [[nd-coreboot-vboot]] |
| Boot code memory safe | proven for 783 lines of AWS stage-1 boot code, with its cryptography abstracted | proof by bounded model checking | [[2018-cook-model-checking-boot]] |
| A first-stage RISC-V measurement root against instruction semantics | not proven: theorem stated, some proofs admitted | progress | [[2020-straznickas-verified-first-stage]] |
| Verify-and-measure boot (DICE) with a verified implementation | proven at the level of generated C on a microcontroller | proof | [[2021-tao-dice-formally-verified]] |
| Kernel boot inside seL4's proofs | outside every verified configuration | assumed | [[nd-sel4-verified-configurations]] |
| The zOS loader | prototype for RISC-V, hash only | assumed | paper, Section 3 |
| The official seL4 kernel, release 17.0.0, built with the unmodified preset `RISCV64_MCS_verified`, booting to user space on RISC-V | demonstrated in QEMU's model of the SiFive HiFive Unleashed, a board from 2018: OpenSBI, then seL4's ELF loader, then the kernel and a root task that maps a UART through capabilities; one of five harts used; the build checks all 22 preset settings and the kernel's SHA-256 | test (a recorded serial console, rebuildable) | [the project's video](/assets/video/sel4-riscv-boot.mp4) and [its build](https://github.com/entresol/silent-zero/tree/main/loader/sel4-demo), 30 October 2026 with 16.0.0, again on 31 October 2026 with 17.0.0 |
| The zOS loader in front of that kernel | demonstrated in the same QEMU model: OpenSBI, then the zOS loader, which hashes the image holding seL4's ELF loader, kernel and root task, shows the result and starts it; the same image with one bit flipped is stopped before seL4's ELF loader; the model has no display, so the loader's pictures are copied out of guest memory | test (recorded serial console and pictures, rebuildable) | [the video](https://github.com/entresol/silent-zero/blob/main/loader/recording/loader-sel4-boot.mp4) and [the loader](https://github.com/entresol/silent-zero/tree/main/loader), 31 October 2026 |

Our reading: the video shows seL4's own boot chain, not the zOS loader. The kernel is built with the preset seL4 provides for its MCS verification on this platform, `hifive` ([configuration files](https://github.com/seL4/seL4/tree/17.0.0/configs)); the preset files are the same in 16.0.0 and 17.0.0. So the video shows that kernel booting. It does not show a proof of the binary: the proofs are about the C code, and the compiler is trusted. QEMU stands in for the hardware, and firmware and ELF loader lie outside every proof.

Release 17.0.0 of seL4 (30 October 2026) fixes a missing instruction-cache flush that affected all RISC-V configurations, the verified ones included ([[2026-sel4-release-17]]). Both videos were recorded first with 16.0.0 and again, on 31 October 2026, with 17.0.0; the kernel grew from 58,300 to 58,428 bytes.

Our reading of the second video: the zOS loader now sits where the paper puts it, between the firmware and the kernel, and the check works on the real kernel image, not on a stand-in. It is still a hash stored next to the image, so it catches accidents, not someone who can rewrite both; the signature is the next step. The loader itself, OpenSBI and seL4's ELF loader remain assumed. Built with GCC 15.2 the loader is 7,333 bytes for this model and 7,809 bytes for QEMU's `virt` machine, between seven tenths and three quarters of it the renderer and its font data ([loader README](https://github.com/entresol/silent-zero/tree/main/loader#size)).

## The paper and its sources

- Section 3's "Boot code lies outside seL4's verified configurations" is confirmed by [[nd-sel4-verified-configurations]].
- "No fallback": coreboot's vboot falls back automatically between two signed read-write slots, and to a read-only recovery firmware that reinstalls from external media, possibly with the user's help ([[nd-coreboot-vboot]]). The Raspberry Pi's own firmware offers `tryboot` and partition walks for A/B schemes below any loader ([[nd-raspberrypi-boot]]). Our reading: the paper's loader has one image, so a failed update leaves the robot stopped where vboot would boot the previous signed version; once nothing verifies, both end with a person. On a Pi, the firmware's fallback would have to be configured off, or accepted below the loader.
- "What the loader has measured itself": our reading: on the PC, Arm and Pi rows above, firmware has run before the loader, some of it closed. The loader can hash stored firmware images, as coreboot's measurements do, but cannot attest what actually ran before it; the first screen can only mark that as assumed, as the paper says.

## Open

- Where the public key lives on each platform: write-protected flash, OTP fuses or a root-of-trust chip. "If the public key can be changed, then the verification is worthless" ([[nd-uboot-verified-boot]]).
- The paper has the loader verify and show what it measured. Whether that measurement is recorded anywhere, in a TPM or through a DICE-style derivation of keys, or only displayed, is open; DICE combines verification and measurement in a small verified design ([[2021-tao-dice-formally-verified]]).
- Rollback to an older signed image is named as a weakness in the Chromium OS design ([[nd-chromeos-verified-boot]]); how the zOS loader handles versions is not stated.
- Our reading: memory safety by model checking is a realistic first proof for the loader, but the closest result abstracts exactly the cryptography a signature check needs ([[2018-cook-model-checking-boot]]); a proof against instruction semantics has been attempted for a measurement root and not finished ([[2020-straznickas-verified-first-stage]]).
