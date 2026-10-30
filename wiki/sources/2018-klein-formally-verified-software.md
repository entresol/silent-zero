---
type: source
id: 2018-klein-formally-verified-software
status: reviewed
read: full
kind: test
sources: [2018-klein-formally-verified-software]
updated: 2026-10-29
---

# Klein et al. 2018: Formally Verified Software in the Real World

Gerwin Klein, June Andronick, Matthew Fernandez, Ihor Kuz, Toby Murray and Gernot Heiser (Data61, CSIRO, UNSW Sydney, University of Melbourne). Communications of the ACM, 2018. [Abstract](https://trustworthy.systems/publications/abstracts/Klein_AKMHF_18.abstract), [full text](https://trustworthy.systems/publications/full_text/Klein_AKMHF_18.pdf).

## What it shows

- **The flight under attack.** In February 2017 Boeing's autonomous Unmanned Little Bird (AH-6) flew a mission while its mission computer was attacked by rogue camera software and by a virus planted from a compromised USB stick during maintenance. The attack compromised some subsystems but could not affect safe operation (§1). In 2013, a red team hired by DARPA under the HACMS programme had compromised the baseline vehicle to the point where it could have crashed or diverted it (§1).
- **Containment under a white-box attack.** The red team had all code and documentation and was given root access to the camera's Linux virtual machine; the compromise stayed contained (§6.4).
- **Security by architecture.** The approach works for systems whose security property follows from the component architecture alone, with a few small trusted components on a kernel that enforces isolation (§1, §4). The article calls the result "highly robust against cyber attacks, even without formal proof of its overall security" (abstract).
- **Retrofit by non-specialists.** Boeing engineers did most of the re-engineering themselves, in four steps: run the existing system in a virtual machine on seL4, split it into several VMs, replace critical parts with native components, analyse the assurance of the whole (§6). The authors call this "seismic security retrofit".
- **What was proved, as of 2018** (§3.2):
  - functional correctness of the C code (Klein et al. 2009, see [[2009-klein-sel4-formal-verification]]);
  - authority confinement and integrity (Sewell et al. 2011);
  - intransitive non-interference, covering explicit flows and in-kernel covert storage channels but not timing channels (Murray et al. 2013);
  - functional correctness at binary level for ARMv7 (Sewell et al. 2013);
  - a sound WCET profile (Blackham et al. 2011; Sewell et al. 2016).
  The proofs were current for the whole stack on ARMv7, and for functional correctness on ARMv7 with hypervisor extensions.
- **Generated code and proofs.** The component framework CAmkES generates glue code, a capDL description of the initial capabilities, and Isabelle proofs that the glue code meets its specification and that the capDL description refines the architecture. The system initialiser is proved correct against a precise model; the proof does not yet reach its implementation (§5.2).
- **Cost.** Adding up all seL4-specific proofs gives 18 person-years for 8,700 lines of C; design and code took 2 person-years. The authors compare with 6 person-years for L4Ka::Pistachio without assurance, and with an estimate of over 45.9 person-years for a Common Criteria EAL7 certification of the same code (sidebar).

## How

An overview article on what HACMS built and tested: a quadcopter as research vehicle and the Unmanned Little Bird as the real one, with attacks by a professional red team. The evidence for robustness is that the red team failed; there is no system-level proof.

## Limits

The authors state (§7):

- The link between the proofs and the system-level security analysis is informal.
- The generated communication proofs cover only the RPC connector.
- The approach only reaches properties the component architecture enforces. If the architecture changes at run time, or if the property depends on too many or too large trusted components, returns diminish.

A careful reader adds:

- **A failed red team is evidence of a weaker kind than proof.** The article reports one white-box attack on the camera VM in flight. It does not report attacks on the trusted components themselves.
- **The proof state is of 2018.** The architectures and properties have changed since; see [[nd-sel4-verified-configurations]].
- **The cost differs from 2009.** Klein et al. 2009 gave about 20 person-years for the proof, 11 of them seL4-specific ([[2009-klein-sel4-formal-verification]]); this article gives 18 for all seL4-specific proofs up to 2018. The two count different things.

## Against the wiki

- [[sel4]]: **extends** it with the security proofs and the field test.
- [[2009-klein-sel4-formal-verification]]: **extends** it. Several gaps named in 2009 (binary level, security model) were closed by 2018 for ARMv7.
- [[wcet-analysis]]: names Blackham et al. 2011 as the source of the sound WCET profile; see the note there.

## For zOS

- [[kernel]]: the paper (Section 4) says that in HACMS the mission computer was rebuilt on seL4, that the helicopter came under cyberattack mid-flight in 2017, that compromised subsystems could not affect safe operation, and that a red team with root access to the camera VM stayed confined. The full text confirms each part.
- Our reading: HACMS is the nearest precedent for the zOS argument. Safety follows from the architecture and a few trusted components, while the payload stays untrusted. HACMS kept the system-level argument informal; zOS aims at an end-to-end argument across the seams. The article's limit, that run-time changes to the architecture erode the approach, argues for zOS's static system.
- The paper's Section 6 cites this article for seL4's best-known field test being a military one. The article confirms the DARPA funding and the military vehicle.
