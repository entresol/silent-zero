# Formalising device protocols for sDDF driver verification

> SeL4 Summit 2026 talk: device models from a device’s Verilog in HOL4, a rely-guarantee format for Pancake drivers; no device proved end to end on the slides. progress, partly read.

Source · Murphy 2026 · LLM reviewed · updated 2026-11-16 · https://silentzero.ooo/wiki/sources/2026-murphy-formalising-device-protocols.html

Liam Murphy (UNSW Sydney, Trustworthy Systems). Talk at the 8th seL4 Summit, Vancouver, September 2026 (venue and month from the abstract page; the slides' footers say "Sep'26"). [Abstract and slides](https://trustworthy.systems/publications/papers/Murphy_26:sel4s.abstract). There is no paper behind it; the wiki has read the 36 slides, which are largely diagrams, so the page records what the slides say and where they do not say enough.

## What it shows

- **The problem (slides 2 to 4).** The talk argues that drivers are a frequent source of operating-system bugs ("the majority of Linux CVEs from 2018 to 2022", slide 2, without a citation on the slide) and that formal methods cannot prevent device-protocol violations without a formal model of the protocol. A chart from Ryzhyk et al. 2009 on Linux driver bugs of 2002 to 2008 puts device-protocol violations at 38 per cent, ahead of generic causes (23), software-protocol (20) and concurrency (19). The slides call datasheets imprecise, incomplete and possibly incorrect, hence "unreliable" as a basis for a device model.
- **The idea (slides 4 and 7).** Derive the device model from the device's own Verilog instead of its manual, prove it there, and use it as the specification against which a Pancake driver is verified. The test bed (slides 5 to 6) is Serengeti, a fork of Cheshire, an open-source RISC-V system on chip from the PULP project, running on Digilent FPGA boards. The slides list features added to it: time protection (fence.t, last-level-cache partitioning), a high-speed Ethernet MAC (work in progress) and an open-source root of trust with secure boot (work in progress). The first target is an I²C controller.
- **Hardware side (slides 10 to 11).** The proofs use HOL4 and a Verilog formalisation by Lööw, which has semantics for the Verilog syntax tree and for a functional representation, and a proof-producing translator whose slide text reads "from Verilog to AST" while its diagram places it between the functional representation and the syntax tree. The slides name the problem as a missing opposite direction: the workflow needs a path from Verilog to the functional model. The workaround is to translate by hand, print the model back to Verilog, check its equivalence with the original by an equivalence checker, and prove that the functional model refines the specification. A decompiler is listed as future work (slide 33).
- **Specification format (slides 12 to 20).** A device is described by a state, and by the register reads and writes it accepts and the bus symbols it produces. The example is the I²C controller of OpenTitan, whose state holds command and receive FIFOs. Interference is expressed in rely-guarantee style, with a relation R for what the environment may change and G for what a component guarantees (slides 18 to 20). Our reading: the environment of a driver includes the device.
- **Driver side (slides 21 to 29).** Pancake programs are translated to Viper (the transpiler of [SMT-based Deductive Verification of Device Drivers](https://silentzero.ooo/wiki/sources/2026-tyler-smt-based-deductive.html.md)); loads and stores to device registers become calls with pre- and postconditions, for example a write to a command FIFO that requires the FIFO to hold fewer than 64 entries. The slides lift the proof obligations over interference: a new precondition together with the rely relation must imply the old precondition, and the old postcondition together with the relations must imply the new postcondition (slides 27 to 29).
- **Status (slide 30).** The slide shows Serengeti, I²C, SPI, i.MX and Ethernet as targets and carries the note "only shared address-decoding logic verified". The device-model side carries the note "proved against lower-level model". It also marks a "PLOS'26 paper" (our reading: [SMT-based Deductive Verification of Device Drivers](https://silentzero.ooo/wiki/sources/2026-tyler-smt-based-deductive.html.md)) and one box as "closed source", without saying what the latter refers to.
- **Future work (slides 31 to 35).** End-to-end proofs from device to driver (the slides list I²C, SPI, i.MX and Ethernet, in no stated order); the decompiler (slide 33); in our reading of a diagram with only a legend as text, proving Pancake's semantics rather than assuming them (slide 34); and a system specification composed of client, virtualiser and driver specifications, each with its own proof.

## How

A talk on work in progress: a device-model workflow in HOL4 and an annotation scheme for Pancake drivers. The slides state no figures for effort, proof size or runtime, and no device has a completed end-to-end proof on them.

## Limits

- The slides give the status only as a diagram; our reading is that on the hardware side only the address-decoding logic of the shared infrastructure had been verified by September 2026, and that the driver side was shown for an example, not as a finished proof. The slides do not say so in these words.
- The Verilog route removes the manual as the source of the device model, but the model becomes a hand translation checked by equivalence (slide 11) until the decompiler exists. The equivalence checker and the HOL4 Verilog semantics join the trusted base; the slides do not discuss them.
- The unreferenced claim about Linux CVEs is not checked here.
- Serengeti is a research system on an FPGA. Whether the approach carries to commercial devices without their Verilog, such as the SoC on the board of the pib, is not addressed.

## Against the wiki

- [SMT-based Deductive Verification of Device Drivers](https://silentzero.ooo/wiki/sources/2026-tyler-smt-based-deductive.html.md): **extends**. That paper names the hand translation of the device protocol as a limit and the Verilog route as concurrent work (§3.3.1); this talk is that work, at an earlier stage.
- [The seL4 Device Driver Framework](https://silentzero.ooo/wiki/sources/2022-parker-sel4-device-driver.html.md): **extends**. The client, virtualiser and driver structure of sDDF reappears in the future system specification (slide 35); the queues are not on the slide.
- [CVA6](https://silentzero.ooo/wiki/systems/cva6.html.md), [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md): no change. Serengeti carries fence.t and cache partitioning as features, as a statement on a slide; the wiki has no further source on it.

## For Silent Zero

[Drivers](https://silentzero.ooo/wiki/design/drivers.html.md): confirms the direction behind the line "specifications from the device's Verilog are work in progress" and adds what the first steps look like. No driver is verified end to end on these slides, so the state of the table stays. The paper's statement on the verified Ethernet driver is untouched.

## Related pages

- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md)
- [Time protection](https://silentzero.ooo/wiki/concepts/time-protection.html.md)
- [CVA6](https://silentzero.ooo/wiki/systems/cva6.html.md)
- [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md)
- [SMT-based Deductive Verification of Device Drivers](https://silentzero.ooo/wiki/sources/2026-tyler-smt-based-deductive.html.md)
- [The seL4 Device Driver Framework](https://silentzero.ooo/wiki/sources/2022-parker-sel4-device-driver.html.md)
