# AMD openSIL

> AMD’s open C libraries for silicon start-up; a server proof of concept, MIT.

System · LLM reviewed · updated 2026-11-27 · 1 source · https://silentzero.ooo/wiki/systems/amd-opensil.html

AMD's open Silicon Initialisation Library is a set of three C libraries, xSIM, xPRF and xUSL, linked into x86 host firmware ([AMD openSIL (repository README)](https://silentzero.ooo/wiki/sources/nd-amd-opensil.html.md)).

## State, November 2026

The repository the wiki read is a proof of concept for 4th Gen EPYC on one reference board, under the MIT licence, not for production firmware. Its roadmap lists three evaluation phases as complete and a production phase "trending 2026"; the wiki has not checked that line against AMD's current plans ([AMD openSIL (repository README)](https://silentzero.ooo/wiki/sources/nd-amd-opensil.html.md)). The page does not say how it relates to the PSP; see [AMD Platform Security Processor (PSP)](https://silentzero.ooo/wiki/systems/amd-psp.html.md).

## Licence and code

MIT, copyright AMD, at github.com/openSIL/openSIL.

## Open questions

- Whether the production phase has shipped, and whether any client or desktop part gets such a library. See [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md) and [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md).

## Sources

- [AMD openSIL (repository README)](https://silentzero.ooo/wiki/sources/nd-amd-opensil.html.md)

## Related pages

- [Root of trust and firmware](https://silentzero.ooo/wiki/design/root-of-trust.html.md)
- [AMD Platform Security Processor (PSP)](https://silentzero.ooo/wiki/systems/amd-psp.html.md)
- [coreboot](https://silentzero.ooo/wiki/systems/coreboot.html.md)
