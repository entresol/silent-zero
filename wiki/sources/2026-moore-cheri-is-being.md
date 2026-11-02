---
type: source
id: 2026-moore-cheri-is-being
status: reviewed
read: full
kind: position
sources: [2026-moore-cheri-is-being]
updated: 2026-11-02
---

# Moore 2026: CHERI is being standardised

Simon W. Moore (University of Cambridge), "CHERI is being standardised, so why do we still need to do research?", slides, CHERI Blossoms 2026, Cambridge, 27 March 2026 (venue and event name from the pool entry; the slides show the date and the university). [Slides](https://cheri-alliance.org/wp-content/uploads/2026/04/D2-1.6-Simon-Moore-CHERI-RvsD-CHERI-Blossoms-2026.pdf). Read in full: the text of the slides; the file has no speaker notes, and the talk itself was not heard.

## What it shows

- **Criteria for standardising CHERI for RISC-V.** Compelling use cases; implementations in hardware with software support; a specification in Sail; simulation support; a test suite. For the status the slides point to a talk by Tariq Kurd, "CHERI RISC-V Standardisation Status", which is not in the pool.
- **What is understood.** Moore lists the compressed capability format and capabilities for spatial memory safety, temporal memory safety and compartmentalisation as well understood. For all of these, he says, three things are understood: the added instructions, the compiler, linker and debugger support, and the way to build applications, run-times and operating systems.
- **Why research continues.** He compares CHERI with page tables and branch prediction, which industry and academia still refine. Open topics: new uses of capabilities (the slides cite Ericsson and list conditional, blinded and coloured capabilities; that all three are Ericsson's is our reading); faster temporal memory safety; new compartmentalisation models; tools that evaluate where compartment boundaries lie; single-address-space operating systems that use CHERI for isolation.
- **Conclusion.** The base CHERI mechanisms are ready for standardisation, many use cases exist and many more are to be invented.

## How

A conference talk in slides, about 270 words in all. It states criteria and opinions; it reports no measurement and gives no date.

## Limits

A careful reader adds:

- The slides do not say that the standard is ratified, nor when it will be. "Being standardised" is the only status they give, and the criteria they list are those the work has to meet.
- The slides name no CHERI product, core or operating system. They mention Ericsson's ideas and, as a comparison, Intel SGX.
- Whether the "ready" in the conclusion is the group's view or Moore's alone is not stated.

## Against the wiki

- [[cheriot]]: **extends**. The open question on standardisation now has a source, with the status "being standardised".

## For zOS

- [[root-of-trust]]: the paper cites these slides for CHERI "being standardised for RISC-V", and they say so. They give no basis for a firmer statement.
- Our reading: the last research topic, single-address-space operating systems isolated by CHERI, differs from a proven kernel on an MMU. The slides do not compare the two.
