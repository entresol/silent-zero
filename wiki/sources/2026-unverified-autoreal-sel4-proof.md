---
type: source
id: 2026-unverified-autoreal-sel4-proof
status: reviewed
read: partial
kind: measurement
sources: [2026-unverified-autoreal-sel4-proof]
updated: 2026-11-25
---

# Zhang et al. 2026: AutoReal, LLM-driven theorem proving on seL4

Jianyu Zhang, Fuyuan Zhang, Jiayi Lu, Jilin Hu, Xiaoyi Yin, Long Zhang, Feng Yang and Yongwang Zhao (Zhejiang University; National Key Laboratory of Science and Technology on Information System Security, China). "Towards Real-World Industrial-Scale Verification: LLM-Driven Theorem Proving on seL4", arXiv 2602.08384 [cs.CR], v1 of 9 February 2026. A preprint. [arXiv](https://arxiv.org/abs/2602.08384). Read: the main text; the appendices (prompts, case studies of one proof) only skimmed, and no claim rests on them.

## What it shows

- **The method.** AutoReal fine-tunes a 7-billion-parameter open model (Qwen2.5-Coder-7B) into "AutoReal-Prover" with two additions: chain-of-thought training, in which each proof step carries a written explanation, and context augmentation, which supplies the theory context a theorem depends on. About 200,000 step-level explanations were generated from seL4 proof traces extracted by the earlier FVELER work, by the same 7B model (§3.2, §3.3). The theory context given to the prover is kept consistent with the context of the human-written proofs, so that the evaluation measures proof construction and not the search for relevant context (§3.4); extracting it is not automated and needs human input, which the authors name as future work (§6).
- **The seL4 result.** On 660 theorems, all those in one "Important Theory" per seL4 proof category, the first listed in the project's README (for capDL API, whose listed theories hold no theorems, the one with most theorems), Isabelle accepted a proof for 341, 51.67 per cent, within up to 256 attempts per theorem. A proof counts only if it contains no `sorry` or `oops` (§4.1, Table 2). Among categories with more than three theorems, rates run from 28.26 per cent (the C refinement theory, 13 of 46) to 72.36 per cent (capDL API, 89 of 123), with 43.35 per cent (101 of 233) on the noninterference theory. Two categories contribute one theorem each (one solved, one not).
- **Budget.** With 5 attempts the rate is 37.12 per cent, with 64 attempts 46.36, with 128 attempts 50.00 (§4.2).
- **Other proof libraries.** On three security-related projects of the Archive of Formal Proofs (451 theorems: Kyber security 64, RSA-PSS 278, elliptic-curve group law 109) the rate is 53.88 per cent (Table 3).
- **Ablation.** On the 105 theorems of one theory (invariants of the abstract specification): the base model proves 1 (0.95 per cent), with chain-of-thought training 24 (22.86), with context augmentation alone 6 (5.71), with both 57 (54.29) (Table 4).
- **Explanations and difference from human proofs.** Of 670 steps in the 341 proved theorems, 84 explanations of the final `done` step and 10 others were inaccurate; without `done` the error rate is 1.49 per cent. 93.55 per cent of the proofs differ from the human-written ones, with 6.018 applied methods, lemmas and definitions per proof against 6.123 (RQ3, RQ4).

## How

The evaluation uses the seL4 proofs as of 1 March 2024. Proof steps of the evaluated theorems are excluded from the explanation data, so the training data contains none of them (§4.1). Success is judged by Isabelle's checker, so a wrong proof cannot count; what the number measures is how often some proposed proof was accepted.

## Limits

The authors say: a direct comparison with earlier work is difficult, because Selene (340 sampled seL4 theorems, 27.06 per cent best averaged, GPT-4) used another selection and protocol; they state their set is unfiltered within the chosen theories. The proof context comes from a person; the approach is tested only in Isabelle/HOL (§3.4, §6).

A careful reader adds:

- The context supplied is that of the human proofs, so the figure is measured with a context that a new proof would first have to find (our reading).
- The 51.67 per cent needs up to 256 attempts per theorem; the authors say it saturates early, but at 5 attempts it is 37.12.
- The 660 theorems come from ten theories, one per category, and a theory's first-listed place does not make it typical; categories with one theorem say little.
- The test theorems are held out, but the model is trained on other seL4 proofs from the same development. Our reading: related lemmas may help it, which is the use case, but it tells us little about a new system's proof.
- The theorem statements already exist. The result measures re-proving, not finding the specification or invariants ([[proof-automation]] makes the same point of other work).
- It is not comparable with the other seL4 figures in the wiki, which use other benchmarks and counting (our reading; see below).

## Against the wiki

- [[proof-automation]]: **extends**. A third seL4 figure beside [[2026-he-neuro-symbolic-proof]] (77.6 per cent of valid theorems in the FVEL splits), [[2026-ahn-promise-proof-automation]] (55.7 per cent on 223 theorems) and the 2024 Selene baseline ([[2024-zhang-selene-pioneering-automated]]). It is the one with a small local model and per-step explanations. The numbers are not comparable: theorem sets, attempt budgets and counting differ.
- [[kernel]]: no change. The proofs of seL4 stay as the human-written ones; nothing here replaces them.

## For zOS

[[kernel]], [[broker]], [[safety-path]]: no change of state. Our reading: a 7B model on local hardware that re-proves about half of an existing development bears on the cost of keeping proofs up to date, not on the cost of the broker's or the safety controller's first specification.
