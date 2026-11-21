---
type: source
id: 2024-dickson-limitations-formal-verification
status: reviewed
read: partial
kind: position
sources: [2024-dickson-limitations-formal-verification]
updated: 2026-11-21
---

# Dickson 2024: limitations on formal verification for AI safety

Andrew Dickson. "Limitations on Formal Verification for AI Safety", essay on the Alignment Forum and LessWrong, 19 August 2024. [Page](https://www.lesswrong.com/posts/B2bg677TaS4cmDPzL/limitations-on-formal-verification-for-ai-safety). Read in part: the introduction, the Perseverance example, the first two limitations and the closing outlook; the other sections were not read. A single author's argument, not a measurement.

## What it shows

- **The target.** Proposals that formal verification could give strong guarantees against major AI threats, such as the "Provably Safe Systems" paper by Tegmark and Omohundro. The essay argues that one should be extremely sceptical of such claims for the near term.
- **Limitation 1.** "We will not obtain strong proofs or formal guarantees about the behavior of AI systems in the physical world"; at best guarantees about rough approximations over short periods. **Limitation 2:** the same for AI threats that are hard to model formally, which the author says includes "most or all" of the threats of greatest concern.
- **An example from space.** For a computer system that helped land the Perseverance rover in 2021, a formal property-checking tool was used on one design, which the essay calls the TRN design, to complement simulation. The essay reads this as a guarantee only against flaws internal to the software. It says that Mars missions have failed about half the time historically, and that software failure types account for about 20 per cent of the total failure risk "according to one analysis", so that even fully verified software leaves about 80 per cent of the risk.
- **Outlook.** The author expects that safety for vehicles and drones will keep improving and that formal verification "will have a role to play", by generating and verifying real-time onboard proofs about approximate world models, without proofs that a vehicle will not crash.

## How

A reasoned essay with one worked example. Its figures come from sources it cites; the 20 per cent is one analysis it cites for Mars missions.

## Limits

A forum essay; the text mentions no peer review. It is about provably safe AI in general; it does not mention seL4 or any kernel proof (the word does not occur in it). Our reading: its objection targets proofs about physical behaviour, while the wiki's pages on proofs concern the correctness of code against a specification ([[functional-correctness]]); the essay does not argue against that kind of proof, and itself expects formal verification to have a role.

## Against the wiki

- [[functional-correctness]]: **extends** with the limit that a proof about code does not cover the world the code acts in. The wiki's pages already mark firmware and devices as assumed.
- [[safety-path]]: **extends**; our reading: it is compatible with keeping the safety function simple, though the essay does not discuss Simplex.

## For zOS

This essay is the wiki's source for the objection "a proof does not make a physical system safe". The answer in the wiki's terms is the labelling of what is proven, tested or assumed; whether the paper states it as clearly as the essay asks is for [[safety-certification]] and the paper's text, not for this page.
