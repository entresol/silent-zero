# AutoRocq

> AutoRocq: an agent proves 48.0 % of CoqGym lemmas, 30.9 % of SV-COMP C lemmas. measurement, full text.

Source · Tu et al. 2026 · LLM reviewed · updated 2026-11-20 · https://silentzero.ooo/wiki/sources/2025-tu-agentic-verification-software.html

Haoxin Tu, Huan Zhao, Yahui Song, Mehtab Zafar, Ruijie Meng and Abhik Roychoudhury (National University of Singapore). "Agentic Verification of Software Systems", Proc. ACM on Software Engineering 3 (FSE), article FSE157, July 2026; arXiv 2511.17330, version 3 of 11 April 2026. [arXiv](https://arxiv.org/abs/2511.17330), [DOI](https://doi.org/10.1145/3808164). Read: the whole text; the reference list was only skimmed. The authors release the tool and benchmarks at github.com/NUS-Program-Verification/AutoRocq.

## What it shows

- **The idea.** AutoRocq is an LLM agent that proves lemmas in the Rocq (formerly Coq) prover. It does not train on proof examples; it learns on the fly during a proving campaign. Three parts do the work (§4, Figure 2): the agent decides at each step whether to propose a tactic or to ask Rocq for more context (Search, Print, Locate, About, Check; Table 1); it keeps an explicit proof tree instead of a flat goal list; and it feeds Rocq's error messages back, switching to a context search when the same error persists. Successful proofs go into an archive it reuses. The certificate is the tactic script that Rocq's kernel accepts and that can be replayed (§2.1, §4).
- **Mathematical lemmas (RQ.1, Figure 4).** On 1,717 lemmas from the intersection of the CoqGym and CoqStoq test sets, AutoRocq proved 824 (48.0 per cent). The best baseline, Rango, proved 715 (41.6 per cent); the margin over the five baselines is 15.2 to 172.8 per cent (§6.1).
- **Program-derived lemmas (RQ.2, Figure 5).** On 641 lemmas the authors extracted from 131 C programs of SV-COMP, AutoRocq proved 198 (30.9 per cent), 10.6 per cent more than the best baseline, Copra, and 204.6 per cent more than PALM. Rango, QEDCartographer and Proverbot9001 proved about 135 each. AutoRocq proved 28 lemmas that no other tool proved; 19 lemmas proved by some baseline escaped it (§6.2). Copra proved slightly more than AutoRocq in the 150 to 224 term and 15 to 22 hypothesis buckets (§6.2, Figure 6).
- **Time and cost.** For successful proofs on the SV-COMP lemmas the mean time was 21.3 seconds for AutoRocq, against 105.5 for Rango, 45.4 for PALM, 49.1 for Copra and 22.6 for Proverbot9001; QEDCartographer took 5.1 (§6.2). The authors give 1.22 US dollars on average to prove a single lemma without token caching (§6.5); the text does not say whether failed attempts are in the average.
- **Ablation (RQ.3, Table 3).** On 70 randomly sampled verification lemmas the full agent succeeded on 44.3 per cent. Without context search 30.0, without proof-tree awareness 40.0, without error feedback 38.6, without the history manager 41.4. Asking for context after one error gave 37.1 and after five errors 38.6; three is the setting used. The authors conclude that context search matters most (§6.3).
- **Model against agent.** Rango with its fine-tuned model replaced by GPT-4.1 proved 11.43 per cent of those 70 lemmas against 44.29 for AutoRocq. The authors read this as evidence that the gain comes from the agent layer rather than the model (§6.5).
- **Linux kernel modules (Table 4, §7).** On 60 lemmas for functional correctness of kernel functions (memmove, strcpy, hex2bin and others) AutoRocq proved 12 (20 per cent); PALM 10, Copra 7, Rango 3, QEDCartographer 3, Proverbot9001 2. PALM's proofs all leaned on the CoqHammer plug-in; a variant of AutoRocq with CoqHammer called once per proof state proved 18 (30 per cent).
- **One worked comparison (RQ.4, §6.4, Figures 1 and 9).** For one integer-bounds lemma an expert with over six years of verification experience took 20 minutes; AutoRocq took 156.7 seconds, after 48 failed tactic applications in 59 attempts (§3). The authors say the agent's proof used fewer steps; this is a single example, and they could not compare more because the extracted lemmas have no human proofs (§6.4).
- **Benchmark shape (§5.1.4).** 48 per cent of the SV-COMP lemmas have more than 100 terms and 52 per cent more than 7 hypotheses, against under 1 per cent of the mathematical lemmas for either (Figure 3).
- **Cited costs.** The introduction cites 22 person-years for the seL4 verification (§1, after Klein et al. 2009). For CompCert it cites 6 person-years and 100,000 lines of Rocq, eight times the implementation (§1, after Leroy et al. 2016; not checked by the wiki).

## How

AutoRocq is about 8,000 lines of Python on the CoqPyt library, with GPT-4.1 at temperature 0 (§4.4). The five baselines (Rango, PALM, Copra, QEDCartographer, Proverbot9001) run in Docker on Ubuntu 22.04 with their default settings, Rocq 8.18 except 8.12 for PALM; Rango and Copra stop after 10 minutes, QEDCartographer after 512 steps (§5.2). The mathematical set leaves out CoqGym test projects that are in CoqStoq's training set (§5.1.1); Rango was fine-tuned on CoqStoq (§6.2). The verification lemmas come from a pipeline the authors built: Frama-C's RTE plug-in adds contracts, a model proposes loop invariants that are checked only by property testing with Eva, and Frama-C's WP plug-in turns the proof obligations into Rocq lemmas (§5.1.3). The properties are unreachability of error calls and absence of integer overflow. 203 lemmas concern overflow, 153 functional correctness and 285 loop invariants (§5.1.3).

## Limits

The authors name these. PALM ran on an older Rocq and several lemmas do not work there, so its results may understate it; the authors argue the Rocq version differences do not materially affect the comparison (§6.1, §6.5). CoqGym is public and the model may have seen it, so the mathematical figures may be inflated; the authors rely on the SV-COMP lemmas, whose proofs did not exist, to limit the risk (§6.5). Multi-threaded programs and properties such as memory safety are not covered, and some program types may pose problems they do not know of (§6.5). Loop invariants are not proved, only tested (§5.1.3). On the kernel lemmas the stronger result needs the CoqHammer plug-in; the authors present it as a variant (§7).

A careful reader adds the following.

- **Most lemmas stay open.** Under a third of the extracted lemmas and a fifth of the kernel lemmas were proved. The authors' phrase "push-button verification" (§9) describes the pipeline; our reading: it promises more than a 30.9 per cent rate.
- **Each certificate covers one lemma.** Whether the lemmas together say what one wants depends on the contracts, the invariants a model proposed and testing checked, and Frama-C's translation, which the paper does not examine. The claim that all generated proofs are "true positives" (§6.5) holds for the lemma as stated. Our reading.
- **Small samples in the ablation.** 70 lemmas make each variant differ by a few lemmas; 44.3 per cent is 31 of 70 and 41.4 per cent is 29 (our arithmetic). The text reports no repeated runs or intervals; we found none.
- **One model.** The model-swap check is for Rango only, and both tools ran with a single backbone, GPT-4.1, so the effect of a different model on AutoRocq is untested here.
- **Own benchmark, own baseline runs.** The SV-COMP lemma set is new and built by the authors, and they ran the baselines themselves with default settings. Our reading: this is common, but it leaves no outside check of the comparison.
- **One worked comparison with a human.** The expert comparison is a single lemma, and the cost figure is one average per lemma (§6.5).

## Against the wiki

- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md): **extends**. It adds a third kind of method next to proof search in Isabelle and agents for Verus: an agent that proves Rocq lemmas drawn from C programs through Frama-C. Our reading: the figures (48.0 and 30.9 per cent) cannot be set beside 77.6 per cent on seL4 theorems in Isabelle or 90 per cent on Rust tasks, because benchmarks, provers and tasks differ.
- [Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md), [PROMISE](https://silentzero.ooo/wiki/sources/2026-ahn-promise-proof-automation.html.md), [Selene](https://silentzero.ooo/wiki/sources/2024-zhang-selene-pioneering-automated.html.md): **related; the figures do not compare**. Same family of method on other provers; none is run on seL4 here.
- [AutoVerus](https://silentzero.ooo/wiki/sources/2025-yang-autoverus-automated-proof.html.md): **related**. Both use agent loops with prover feedback; the verifier differs ([Verus](https://silentzero.ooo/wiki/systems/verus.html.md) against Rocq with Frama-C).
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md) and [seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md): the source cites 22 person-years for the seL4 verification, which matches the 2009 paper's total of about 22 recorded in [seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md); the wiki's narrower figures (about 20 for the proof, 11 of them specific to seL4) differ in scope, not in value.
- [the Axon compiler](https://silentzero.ooo/wiki/sources/2026-rinard-testing-credible-compilation.html.md): **related**. Another case of a model producing proofs the checker accepts; there the specifications were not verified, Our reading: here the extracted lemmas carry the same kind of gap.

## For Silent Zero

[The kernel](https://silentzero.ooo/wiki/design/kernel.html.md), [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md) and [The broker](https://silentzero.ooo/wiki/design/broker.html.md): no change of state. Our reading: the paper bears on the question the wiki leaves open in [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md), whether proof effort falls enough to verify a broker or a controller. It gives a small positive datum for C code in the style of kernel utilities (12 of 60 lemmas, 18 with a hammer) and a negative one for anything more complex: most lemmas were not proved, the targets are single functions or small programs, and no system with scheduling, devices or concurrency is touched. Nothing in Silent Zero rests on it, and our paper's remark (Section 2) that short proofs are getting cheap while long ones stay expensive is neither confirmed nor contradicted.

## Related pages

- [Drivers](https://silentzero.ooo/wiki/design/drivers.html.md)
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [The kernel](https://silentzero.ooo/wiki/design/kernel.html.md)
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md)
- [AutoVerus](https://silentzero.ooo/wiki/sources/2025-yang-autoverus-automated-proof.html.md)
- [Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md)
- [PROMISE](https://silentzero.ooo/wiki/sources/2026-ahn-promise-proof-automation.html.md)
- [seL4, Formal Verification of an OS Kernel](https://silentzero.ooo/wiki/sources/2009-klein-sel4-formal-verification.html.md)
- [Selene](https://silentzero.ooo/wiki/sources/2024-zhang-selene-pioneering-automated.html.md)
- [the Axon compiler](https://silentzero.ooo/wiki/sources/2026-rinard-testing-credible-compilation.html.md)
