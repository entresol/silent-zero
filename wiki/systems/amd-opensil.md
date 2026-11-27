---
type: system
status: reviewed
sources: [nd-amd-opensil]
short: AMD's open C libraries for silicon start-up
updated: 2026-11-27
---

# AMD openSIL

AMD's open Silicon Initialisation Library is a set of three C libraries, xSIM, xPRF and xUSL, linked into x86 host firmware ([[nd-amd-opensil]]).

## State, November 2026

The repository the wiki read is a proof of concept for 4th Gen EPYC on one reference board, under the MIT licence, not for production firmware. Its roadmap lists three evaluation phases as complete and a production phase "trending 2026"; the wiki has not checked that line against AMD's current plans ([[nd-amd-opensil]]). The page does not say how it relates to the PSP; see [[amd-psp]].

## Licence and code

MIT, copyright AMD, at github.com/openSIL/openSIL.

## Open questions

- Whether the production phase has shipped, and whether any client or desktop part gets such a library. See [[root-of-trust]] and [[coreboot]].
