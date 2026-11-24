---
type: source
id: nd-mars-research-atmosphere
status: reviewed
read: full
kind: report
sources: [nd-mars-research-atmosphere]
updated: 2026-11-21
---

# Mars Research Group: the Atmosphere project page

Mars Research Group (the authors of the SOSP paper are at the University of Utah). "Atmosphere Verified Operating System", project page, undated, read on 21 November 2026. [Page](https://mars-research.github.io/projects/atmo/). Read in full; it is short. A project page.

## What it shows

- **What it is.** "A full-featured microkernel developed in Rust and verified with Verus", "conceptually similar to the line of L4 microkernels". Most functionality, such as device drivers, the network stack and file systems, is in user space.
- **Mechanisms.** Address spaces, page tables, coarse-grained memory management and threads; each process has a page table and schedulable threads; threads map and unmap pages and receive pages through communication endpoints. "To simplify verification, at the moment Atmosphere relies on a big-lock synchronization."
- **Proof.** It proves "functional correctness, i.e., refinement of a high-level specification" with Verus. "On average our code has proof-to-code ratio of 7.5:1 which is significantly lower than in prior approaches."
- **Publications.** The SOSP 2025 paper and an earlier workshop paper (KISV 2023).

## How

A short description with a link list; no figures other than the ratio, no repository link and no licence statement in the page.

## Limits

The page's ratio of 7.5:1 differs from the 3.32:1 in the SOSP 2025 paper ([[2025-chen-atmosphere-practical-verified]]); neither text explains the difference. The page gives no date and no state of the code.

## Against the wiki

- [[verus]]: **extends** together with the paper ([[atmosphere]]).

## For zOS

Where the two disagree, the wiki uses the paper's figure and names the other. See [[atmosphere]].
