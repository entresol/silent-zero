---
type: source
id: 2026-liao-llvm-translation-validation
status: reviewed
read: partial
kind: measurement
sources: [2026-liao-llvm-translation-validation, 2026-rinard-testing-credible-compilation]
updated: 2026-11-10
---

# Liao et al. 2026: Trivet

Chunhao Liao, Hongxu Xu, Xintong Zhou, Yizhou Zhang and Chengnian Sun (University of Waterloo). "LLVM Translation Validation Automated with Large Language Models and Lean". [arXiv:2609.19583](https://arxiv.org/abs/2609.19583), version 1 of 17 September 2026, cs.PL. A preprint. Read in part: abstract, introduction, background, design, implementation and evaluation including the ablation. The related-work section and the references were only skimmed; this page makes no claim about them.

## What it shows

- **The claim.** Trivet checks that an LLVM optimisation preserves meaning (refinement) by generating a proof in Lean 4. It builds a theorem and a proof scaffold from the source and target code by a program that uses no language model, discharges what is mechanical, and leaves typed holes for the transformation-specific steps, which a model fills in using Lean's error messages. For an invalid transformation, the model proposes a counterexample and the scaffold turns it into a machine-checked proof of non-refinement. The Lean kernel checks every verdict, and the harness accepts nothing it has not checked (§1, §3.4).
- **Results.** On 148 transformations taken from the LLVM repository, 74 valid and 74 invalid, Trivet proves all 74 valid ones and refutes 73 of the 74 invalid ones. One invalid loop transformation stays unresolved after the counterexample attempts ran out (abstract, §4.4).
- **Beyond SMT.** The authors compare with Alive2, which uses an SMT solver. Alive2 handles the 30 fixed-bitwidth loop-free valid cases only in part: it validated 20, and 10 did not finish within two hours. It does not support symbolic bitwidths, and for loops it checks only up to an unrolling bound. Trivet's proofs for symbolic widths hold for every width meeting the stated constraints, and for the restricted class of loops in the 28 loop cases it proved all 14 valid ones, with proofs that hold for all iteration counts, and certified counterexamples for 13 of the 14 invalid ones (§4.2 to 4.4, §3.4).
- **Cost and time.** Alive2 was faster on the fixed-width cases it completes: under one second against a median of 463 s for Trivet on the 15 easier ones (§4.2.1). Proofs of valid loop-free cases took a mean of 684 s; refutations a mean of 61 s (§4.2, §4.3).
- **The scaffold matters.** Without it, the same model succeeded on 47 of 60 loop-free refinement cases and 49 of 60 counterexample cases and needed more time; with it, all 60 and 60. Across the evaluation the scaffold enabled 26 additional proofs and, on the cases both configurations solved, cut mean proof time by 75.9 per cent and mean cost by 88 per cent. Mean cost per valid loop-free case solved by both fell from $13.23 to $1.47 at September 2026 prices (§4.5, Table 6).

## How

A Lean 4 framework for compiler intermediate representations, extended by the authors for undefined behaviour, preconditions, bit-manipulation operations, several symbolic widths and multi-block code. A coding agent driven by a frontier language model proposes the proofs and counterexamples. One 32-core server, two hours per transformation (§3.4, §4.1). The 148 cases are described as real-world transformation instances from the LLVM repository; the symbolic-width valid cases were derived with earlier generalisation techniques, the symbolic-width invalid cases and the symbolic-width loop cases by hand from fixed-width ones (§4.1).

## Limits

What the authors say themselves:

- The formalisation covers integer instructions; memory operations, floating point and richer loops are future work (§3.4).
- Loop support is a restricted class: a three-block loop replaced by one straight-line block (§4.1).
- The comparison with Alive2 covers a dataset they chose, including cases picked because SMT solvers struggle with them (§4.1).

A careful reader adds: Trust rests on the Lean kernel and on the Lean formalisation of LLVM semantics the authors extended, which this page did not read; a wrong semantics would give a valid proof about the wrong thing. The evaluation is the authors' own, on 148 cases, with one model and one agent harness. It is a preprint, and the page does not claim that the results carry over to other compilers or targets.

## Against the wiki

- [[proof-automation]]: extends. The model proposes, a kernel accepts, as in the seL4 sources there, but the task is a compiler check and not a kernel proof, and a scaffold built without a model decides how much the model has to do.
- [[2026-rinard-testing-credible-compilation]]: the same pattern, a trusted checker around untrusted output from a model, applied to the optimisation passes of a compiler. Both are preprint reports on compilers, neither about seL4.

## For zOS

Our reading: checking a compiler's output instead of proving the compiler is translation validation, which the [[kernel]] page mentions for the old seL4 timing analysis. This source shows how a language model can lower the proof effort for one such check on LLVM. It touches no `design/` page and its state, and nothing in it contradicts the paper.
