---
type: source
id: 2026-liao-llvm-translation-validation
status: drafted
read: partial
kind: measurement
sources: [2026-liao-llvm-translation-validation]
updated: 2026-11-09
---

# Liao and others 2026: Trivet, LLVM translation validation with models and Lean

Chunhao Liao, Hongxu Xu, Xintong Zhou, Yizhou Zhang and Chengnian Sun (University of Waterloo). "LLVM Translation Validation Automated with Large Language Models and Lean". [arXiv:2609.19583](https://arxiv.org/abs/2609.19583), version 1 of 17 September 2026. Read in part: abstract, introduction, background, the proof construction in §3.1 and §3.2, the implementation paragraph in §3.4 and the first part of the evaluation. The remaining evaluation, related work and the reference list were searched for key terms only, and this page makes no claim about them. For that reason the page stays `drafted`.

## What it shows

- **The claim.** Trivet checks that an LLVM optimisation keeps a program's meaning by having a model fill proof holes in a Lean refinement theorem, or propose a counterexample; the Lean kernel checks every verdict (abstract, §1).
- **Result.** On 148 transformations (74 valid, 74 invalid) it validates all 74 valid ones and refutes 73 invalid ones, leaving one invalid case open. Successes include 60 loop-free transformations with symbolic bitwidths, 27 from a restricted class with loops, and 10 hard fixed-bitwidth cases on which Alive2, an SMT-based validator, times out (abstract, §1; the 10 follow from Alive2 validating 5 of 15 such cases in two hours, §4).
- **Scaffolding helps.** Against an unscaffolded baseline, the generated scaffold gives 26 more proofs and cuts mean proof time by 75.9 per cent and mean cost by 88 per cent on cases both solve (abstract).
- **Cost in time.** Symbolic-bitwidth proofs took 138 to 1748 seconds, median 614. On 15 easy fixed-bitwidth cases Alive2 needed under one second each and Trivet a median of 463 seconds (§4).
- **What is trusted.** The model only completes holes or proposes a counterexample; a deterministic harness accepts a result only after Lean's kernel checks it. In the proof-completion branch a proof is accepted only without `sorry` or `admit` and with the standard axioms only (§3.1.3); in the counterexample branch a deterministic scaffold builds the proof, adds no axioms, and the proof is accepted once it passes the kernel (§3.2).

## How

A framework built on the LLVM dialect of the Lean-MLIR project, which the authors extended with immediate undefined behaviour, preconditions, more bit operations and multiple symbolic bitwidths. The model runs as an agent through a command-line tool with the GPT-5.5 model (§3.4). All 148 cases are real-world transformation instances from the LLVM repository (§4.1). The valid symbolic cases come from generalising fixed-bitwidth ones with techniques of earlier work, and the authors built the invalid symbolic cases by hand by replacing the concrete bitwidth (§4).

## Limits

What the authors say: the formalisation covers integer instructions, loop-free single-block transformations and a restricted class with loops; memory operations, floating point and richer loops are future work; the deprecated `undef` is not supported (§2.1, §3.4). A careful reader adds: it checks single transformations of a compiler, not a whole compiler; it validates the rewrite rule, so a mistake in the Lean model of LLVM's semantics would pass unnoticed; and the evaluation is on 148 cases, some of them generalised or constructed by the authors.

## Against the wiki

- [[proof-automation]]: extends it with a case where the model proposes and a proof kernel decides, as with seL4's Isabelle proofs, but for compiler rewrites rather than kernel theorems.
- [[2026-rinard-testing-credible-compilation]]: related, since both check compiler output with a small trusted checker. There, an agent wrote the whole compiler and a verified checker accepts certificates; here, a model completes proofs per transformation.
- [[kernel]]: nothing in it touches seL4; the wiki makes no link.

## For zOS

Our reading: another instance of the pattern of an untrusted generator behind a trusted checker, the shape of [[simplex]] and of the machine-made proofs in [[proof-automation]]. It changes the state of no `design/` page.
