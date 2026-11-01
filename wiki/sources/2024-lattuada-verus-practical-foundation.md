---
type: source
id: 2024-lattuada-verus-practical-foundation
status: reviewed
read: full
kind: measurement
sources: [2024-lattuada-verus-practical-foundation]
updated: 2026-11-01
---

# Lattuada et al. 2024: Verus, a practical foundation for systems verification

Andrea Lattuada, Travis Hance, Jay Bosamiya and eleven further authors. Proceedings of SOSP '24, 4 to 6 November 2024, Austin. [DOI](https://doi.org/10.1145/3694715.3695952). Read in full.

## What it shows

- **The tool.** [[verus]] verifies Rust code against specifications written in Rust, using an SMT solver. It relies on Rust's ownership types for memory reasoning, keeps its solver queries small, and adds automation for bit-vectors, nonlinear arithmetic and proof by computation, and a language (VerusSync) for reasoning about shared-memory concurrency (§2, §3).
- **Speed.** In millibenchmarks the other tools take 3 to 28 times longer than Verus on a singly linked list and 24 to 61 times longer on a doubly linked list; the abstract gives the range as 3 to 61 times (§4.1.3, Figure 7a). With four lists updated repeatedly, Verus's time grows linearly, at about 1.6 ms per push (about 1.8 for doubly linked lists), while the other Rust-based tools grow super-linearly (Figure 7b).
- **Ported systems.** The authors port IronKV (a key-value store from IronFleet) and a NUMA-aware replication library from IronSync and compare verification time and effort with the originals (§4.2.1, §4.2.2).
- **New systems.** They verify an x86-64 page table (400 lines of code, 5,329 lines of proof, a ratio of 13.3 to 1; it matches an unverified reference for mapping but its unmap is much slower, which the authors trace to reclaiming emptied directories, §4.2.3), a concurrent memory allocator, and a crash-safe persistent log (12 s to verify, ratio 3.9 to 1; throughput comparable to the PMDK library, §4.2.5). In all, the case studies are 6.1K lines of implementation and 31K lines of proof (abstract).
- **Other users.** The paper says other research groups have used Verus for cluster-management controllers, a verified microkernel (reported proof-to-code ratio 7.5 to 1, §4.2.3), a security module for confidential VMs, and to verify LLM-produced code (§1).

## How

Millibenchmarks of three data structures in Verus and five other tools, then five case studies. The list timings are medians of 20 single-threaded runs (Figure 7); the error-reporting times of Figure 8 use eight threads.

## Limits

What the authors say themselves: a verification result is limited by its trusted base, which here is the top-level specifications, the Verus verifier, the solvers and the Rust compiler (§1). For the page table's ratio of 13.3 to 1 they say it may come from this being their first large development, or may be inevitable for a complex OS component (§4.2.3). On the whole evaluation: "the true evaluation will come from future projects" (§1).

A careful reader adds:

- **Speed is for small programs.** The 3 to 28 times (singly linked list) and 24 to 61 times (doubly linked list) come from two list benchmarks; the same verified API is used across tools. The case studies compare effort and time in prose and tables, not one factor.
- **Not a kernel result.** None of the systems is a kernel or a driver. The page table is one OS component, written to a trusted model of the MMU.
- **Authors as evaluators.** The benchmarks were designed and run by the Verus group.

## Against the wiki

- [[proof-automation]]: Verus is a tool with automation inside the verifier, not a model proposing proofs; the page now says so and separates the two.
- [[drivers]], [[kernel]]: nothing changes. No seL4 component is verified with Verus in this source.

## For zOS

The paper (Section 2.3 and the table of building blocks in Section 5) says Verus checks systems code 3 to 61 times faster than earlier tools. That is the abstract's wording and the range of the two list benchmarks; for larger systems the paper reports effort ratios, not that factor. Our reading: "systems code" in the paper's sentence should carry "in benchmarks". No `design/` page changes state.
