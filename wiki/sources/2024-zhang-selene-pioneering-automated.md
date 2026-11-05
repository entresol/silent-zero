---
type: source
id: 2024-zhang-selene-pioneering-automated
status: reviewed
read: full
kind: measurement
sources: [2024-zhang-selene-pioneering-automated]
updated: 2026-11-05
---

# Zhang, Lu and Duan 2024: Selene

Lichen Zhang (Peking University), Shuai Lu and Nan Duan (Microsoft Research Asia). "Selene: Pioneering Automated Proof in Software Verification". [arXiv:2401.07663](https://arxiv.org/abs/2401.07663), version 2 of 5 June 2024. The PDF read carries no venue line. Read in full.

## What it shows

- **A benchmark from seL4.** The authors call it the first project-level benchmark for automated proofs, drawn from the Isabelle proofs of seL4's refinement sessions. From 5,464 extracted lemmas, sampled sets of four kinds were built: three levels of difficulty of lemmas in the procedural proof style (P1, P2, P3) and one set in the declarative style (D). After checking, 360 lemmas remain, 340 of them for evaluation once five per set serve as demonstrations (§3, Table 1).
- **Lemma isolation.** Checking a generated proof would need nearly the whole project rebuilt, tens of minutes per lemma. The benchmark puts each target in its own Isabelle session on top of fixed dependency sessions, which cuts the time to about a third and, per lemma, to minutes or seconds (§1, §3.2, Appendix C).
- **First results.** With five demonstrations in the prompt and no further help, GPT-4 proves 41.7 per cent of P1 on the first try and 51.8 per cent within five tries; on P2 7.7 and 12.5 per cent; on P3 0 and 1.7; on D 10.5 and 15.8. GPT-3.5-turbo reaches 28.1 and 35.3 per cent on P1, 2.9 and 5.8 on P2, 0 on P3 and 0 and 5.3 on D (§4.3, Table 2).
- **Where it fails.** Nearly half of GPT-4's failures are undefined facts, lemma names that do not exist; the dependency graph of seL4 is complicated and extracting the facts to apply from it is hard for models (§1, §4.3, §7).
- **Three augmentations.** Similar lemmas as examples, the true dependencies, and feedback from the prover to fix errors lift P1 to between 47.5 and 53.2 per cent; combining similar lemmas and fixing gives 61.9 per cent on P1 and 20.2 per cent on P2, while P3 stays at 1.7 or below (§5, Tables 4 and 6).
- **Cost of the real thing.** The paper cites 7 person-months for the specification and 11 person-years for the proofs of seL4, from Klein et al. 2014, a source this wiki does not cover (§1).

## How

A whole proof is generated per lemma in one go, with temperature sampling; success needs at least one of k tries to pass Isabelle. Outputs with "sorry" or "oops", over 2,048 tokens or over ten minutes of checking count as failures (§4.1, §4.2).

## Limits

What the authors say. The benchmark leaves out lemmas inside contexts and locales, because they do not fit lemma isolation. Its dependency augmentation hands the model the true dependencies, which a real tool would have to find. Only the proof stage is automated, not the writing of specifications, and whole-proof generation makes no use of intermediate proof states (§3.3, §7).

A careful reader adds:

- **Old models.** GPT-3.5-turbo and GPT-4 of 2023, with five fixed demonstrations. The figures say little about today's models.
- **An easy subset.** [[2026-he-neuro-symbolic-proof-osdi]] describes it as a small subset of relatively easy theorems and puts GPT-4's result at 20 per cent of a benchmark theorem set; Selene's own sets cover proofs of one line up to twenty lines, and its tables give results per set. Our reading: the 20 per cent is a weighted average of those.
- **Venue.** The text read does not state where it appeared.

## Against the wiki

- [[proof-automation]]: the earliest data point on seL4, cited as a baseline in [[2026-he-neuro-symbolic-proof-osdi]] and [[2026-ahn-promise-proof-automation]]. Those two use different benchmarks and metrics, and PROMISE re-ran Selene as a baseline; the figures cannot be compared.

## For zOS

The paper does not cite this source. No `design/` page changes state.
