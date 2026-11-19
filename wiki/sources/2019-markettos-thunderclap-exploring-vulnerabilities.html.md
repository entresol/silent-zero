# Thunderclap

> Thunderclap, NDSS 2019: attacks by a malicious device on macOS, FreeBSD and Linux with the IOMMU on; Windows mostly unprotected. test, full text.

Source · Markettos et al. 2019 · LLM reviewed · updated 2026-11-02 · https://silentzero.ooo/wiki/sources/2019-markettos-thunderclap-exploring-vulnerabilities.html

Markettos, Rothwell, Gutstein, Pearce, Neumann, Moore and Watson (Cambridge, Rice, SRI), "Thunderclap: Exploring Vulnerabilities in Operating System IOMMU Protection via DMA from Untrustworthy Peripherals", NDSS 2019. [Paper](https://dev.ndss-symposium.org/ndss-paper/thunderclap-exploring-vulnerabilities-in-operating-system-iommu-protection-via-dma-from-untrustworthy-peripherals). Read in full.

## What it shows

The authors ask whether switching on the IOMMU makes a computer safe from a malicious device that can read and write memory directly (see [IOMMU](https://silentzero.ooo/wiki/concepts/iommu.html.md)). Their answer is no. A device that behaves like a working network card gets the operating system's own cooperation, and the shared memory between driver and device is a large attack surface (Sections I, VI, VII).

- **Many systems did not use the IOMMU.** Only macOS enabled it by default. Red Hat Enterprise Linux 7.1, which the paper says is certified at Common Criteria EAL4+, did not. On the Linux and FreeBSD machines the authors switched the IOMMU on themselves (Section IV, Table II).
- **Windows.** Versions 7, 8.1 and 10 Home and Pro did not use the IOMMU, so all memory was open to a device. Windows 10 Enterprise used it only for its optional virtualization-based security, with one page map shared by all devices and nearly all pages mapped read and write. In 2018 Microsoft announced Kernel DMA Protection for Thunderbolt devices, for machines that shipped with version 1803 (Section V-A).
- **macOS.** One page map serves all devices, so memory exposed to one is exposed to all; the network buffers (mbufs) stay exposed at all times. The authors read cleartext from a VPN connection and obtained a root shell by overwriting a function pointer in an mbuf, after defeating address randomisation with pointers that the AHCI and USB drivers leak (Section VI-D). Apple fixed this in 10.12.4 by blinding the pointers (Section XI).
- **FreeBSD.** It gives each device its own page map, yet an adapted mbuf attack, with extra steps for a reference count and a stack-pointer gadget, gave kernel privilege on TrueOS 10.3 (Section VI-E).
- **Linux.** Its buffer structure keeps function pointers on other pages than the data, which stopped that attack. Three others worked. Network data buffers shared a page with unrelated kernel data, including the dispatch table of the NAT code, which the device could write. A device that never acknowledged a transfer kept its window open and saw kernel stacks, UNIX domain socket traffic and plaintext VPN traffic. A device that advertised the PCIe feature Address Translation Services made Linux enable it, and with the "already translated" bit set it reached memory without restriction. Only the authors' server and one laptop supported ATS, and PCIe Access Control Services could block such requests but were not enabled by default (Section VII).
- **Remedies and their cost.** The authors recommend three measures: expose to a device only what it needs, with the least permission; destroy each mapping before the host uses or reuses the memory; and give each device its own address space. They rate the costs differently. Per-device address spaces need small changes to the IOMMU driver. Synchronous invalidation needs trivial code changes but can cut throughput by as much as 80 per cent for high-performance I/O, according to prior work they cite. Exposing only the minimum means a significant implementation and performance cost and non-trivial code changes. They find no general-purpose solution without significant performance degradation (Section IX).
- **Vendor response.** After disclosure from 2016, the abstract says vendors shipped substantial improvements. Apple blinded the pointers in macOS 10.12.4, which leaves other fields open. Microsoft announced Kernel DMA Protection. Intel's work, which the paper dates to kernel "4.21", enables the IOMMU for Thunderbolt ports and disables ATS. The Linux kernel security team treated the attacks as within its threat model; the FreeBSD project said malicious peripherals were not then within its own (Section XI).

## How

The authors built an open FPGA platform: an Arm Cortex-A9 on an Intel Arria 10 SoC that runs the device model of an Intel 82574L Ethernet controller taken from QEMU, plus logic that can send arbitrary PCIe packets (Section III). They attached it by PCIe or Thunderbolt to nine machines (Table I) and compared eleven operating-system builds (Table II). They studied memory use of network, storage and graphics devices on Windows and Ubuntu with a PCIe analyser (Section IX-B).

## Limits

What the authors say:

- They studied Intel and AMD IOMMUs. The Arm SMMU "applies broadly the same concepts"; they did not test it, but argue that their study already covers the Android and iOS kernels (Section III-C).
- Message-passing devices (USB, SATA) are out of scope, and so is the hypervisor use of the IOMMU (Section III-A).
- Their fixes were partial: Apple's blinding leaves data pointers and other fields open (Section XI).

A careful reader adds:

- The paper is from 2019. Later changes in the operating systems are not assessed here.
- Every attack runs against a general-purpose operating system with its drivers in the kernel. The paper says nothing about a microkernel with user-mode drivers.

## Against the wiki

- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md): **confirms** the paper's use of it, with two qualifications now stated there.
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md): no change; it excludes the IOMMU from the proof, which this source gives reason to care about.
- [IOMMU](https://silentzero.ooo/wiki/concepts/iommu.html.md): created with this source.

## For Silent Zero

- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md), [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md): the source supports listing the IOMMU configuration as *assumed*. Our reading: the attacks use mapping granularity of a page, buffers that share pages with kernel data, and a device-controlled translation feature. A system with user-mode drivers and page-aligned device buffers meets the first two differently, but nothing in the source shows that, and the third depends on the kernel's IOMMU code, which no proof covers.

## Related pages

- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md)
- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [IOMMU](https://silentzero.ooo/wiki/concepts/iommu.html.md)
- [seL4 Foundation: Verified Configurations](https://silentzero.ooo/wiki/sources/nd-sel4-verified-configurations.html.md)
