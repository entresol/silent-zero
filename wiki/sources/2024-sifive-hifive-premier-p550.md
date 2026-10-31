---
type: source
id: 2024-sifive-hifive-premier-p550
status: reviewed
read: full
kind: report
sources: [2024-sifive-hifive-premier-p550]
updated: 2026-10-31
---

# SiFive 2024: the HiFive Premier P550

SiFive press release, "SiFive Unveils the HiFive Premier P550, the First Commercially Available Out-of-order RISC-V Development Board", Nuremberg, 9 April 2024, at Embedded World. Read on 31 October 2026. [Release](https://www.sifive.com/press/sifive-unveils-the-hifive-premier-p550-the-first-commercially).

## What it shows

- **The chip.** The board carries an Eswin EIC7700 SoC with four SiFive P550 cores: 64-bit, three-issue, out-of-order, 256 KB L2 and 4 MB L3 cache. The SoC also has a 2D/3D GPU, video encoder and decoder, an NPU, a DSP, MIPI DSI, a security subsystem and PCI Express Gen 3 x4.
- **The board.** 16 GB LPDDR5-6400, 128 GB eMMC, a PCIe x16 slot wired as Gen3 x4, five USB 3 ports, and a replaceable system-on-module.
- **Software.** SiFive's Freedom U-SDK "including Linux"; Canonical works with SiFive on Ubuntu for the board.
- **Availability.** Expected through Arrow Electronics in July 2024, with pre-orders open. The release also names the HiFive Unmatched Rev. B as "available today".
- **Claims.** SiFive calls it "the highest performance RISC-V development board on the market" and the first commercially available out-of-order RISC-V development board.

## How

A press release with quotes from SiFive's and Canonical's representatives and a feature list.

## Limits

A vendor's announcement; the performance claims are not backed by figures here. A careful reader adds: the release names no display connector on the board; the GPU and MIPI DSI are features of the SoC. The release predates shipping; it gives an expected month, July 2024, and no price.

## Against the wiki

- [[sifive-hifive]]: created with this source.
- [[nd-sel4-supported-platforms]], [[2026-sel4-release-17]]: seL4 supports this board and, since release 17.0.0, lists it among the platforms with a C-level proof (without MCS).

## For zOS

- [[bootloader]]: a board seL4 supports that was announced for sale; whether it can still be ordered in 2026 is not shown here. Whether it can show a picture before the kernel runs, which the zOS loader needs, is not answered here.
