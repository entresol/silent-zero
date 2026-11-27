---
type: source
id: nd-me-cleaner
status: reviewed
read: full
kind: report
sources: [nd-me-cleaner]
updated: 2026-11-27
---

# me_cleaner (repository README)

The README of the me_cleaner project, a Python script that modifies an Intel ME firmware image; undated. [github.com/corna/me_cleaner](https://github.com/corna/me_cleaner). The pool holds a snapshot of 2 November 2026. Read in full; it is a short page. The text is the project's own description, written by its authors.

## What it shows

- **What the ME is.** The README calls Intel ME a co-processor in all post-2006 Intel boards, the base of features such as AMT, Boot Guard and PAVP, which requires, in its words, full access to the system including memory through DMA and network access invisible to the user. Its firmware can be neither disabled nor reimplemented, because it is signed and tied into the boot.
- **What can be done, by generation.** Before Nehalem (ME version 6, 2008/2009) the ME could be removed by setting bits in the flash descriptor. From Nehalem on a missing valid firmware makes the PC shut off after 30 minutes, which the README guesses to be an anti-theft measure. The tool reduces the firmware to the modules the boot needs: ROMP and BUP for versions 6 to 10 (about 90 kB, from 1.5 or 5 MB), and four modules (rbe, kernel, syslib, bup) from version 11 on, Skylake onwards (about 300 kB, from 2 or 7 MB). It says the aim is that the ME is then active only during boot.
- **Side effects.** On some boards the vendor firmware does not boot without a valid ME; elsewhere there may be longer boot times or warnings. The ME's features stop working.
- **Practice.** Reading and rewriting the image usually needs an external SPI programmer, because the region is often not writable from the operating system.

## How

A description of a tool and its results by generation; no measurement or test table. The README says the tool is reliable "on a great number" of boards without listing them.

## Limits

The README is the authors' own account, undated, and written by people reducing the ME, not by Intel; it gives no evidence for the DMA and network claims. It does not say what a reduced ME can still do while running, and the claim that it is active only during boot is the tool's goal, not a proof. The README is undated and names no generation after "version >= 11"; whether it still holds for the newest ones is not covered.

## Against the wiki

- [[coreboot]]: **extends**. The README names the problem the page's PC row only implies: free firmware relies on a proprietary, always-on blob.
- [[intel-me]]: this source gives the page its content.

## For zOS

[[root-of-trust]]: no change of state, but an open point gains a source. Our reading: on Intel PCs a signed co-processor with memory access sits outside any proof of the kernel, and the project's own description of it cannot be checked by the wiki.
