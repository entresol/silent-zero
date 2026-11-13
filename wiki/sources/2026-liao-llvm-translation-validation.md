---
type: source
id: 2026-liao-llvm-translation-validation
status: reviewed
read: partial
kind: measurement
sources: [2026-liao-llvm-translation-validation]
updated: 2026-11-13
---

# Liao et al. 2026: Trivet

Chunhao Liao, Hongxu Xu, Xintong Zhou, Yizhou Zhang and Chengnian Sun (University of Waterloo). "LLVM Translation Validation Automated with Large Language Models and Lean". [arXiv:2609.19583](https://arxiv.org/abs/2609.19583), version 1 of 17 September 2026. Read in part: abstract, introduction, background on Alive2, the method's outline, implementation, the dataset and the first results (RQ1). The remaining results (RQ2 to RQ4) and the Lean proof details were skimmed, so this page quotes only the headline figures that the abstract and introduction state.

## What it shows

- **The tool.** Trivet checks that an LLVM transformation preserves the meaning of a program. It builds a proof outline in Lean 4 from the source and target functions, discharges the routine obligations by deterministic steps, and hands the transformation-specific ones to a language model. A valid transformation gets a refinement proof; an invalid one gets a counterexample that the framework checks. Every verdict is accepted only after Lean's kernel checks it (abstract, §1).
- **Results.** On 148 real transformations (74 valid, 74 invalid) Trivet proves all valid ones and refutes 73 of the invalid ones, leaving one unresolved. The set includes 60 loop-free transformations with symbolic bit widths, which the SMT-based checker Alive2 cannot handle, and a restricted class of transformations with loops. Alive2 validates 20 of 30 loop-free fixed-width cases. Against a baseline without the proof outline, the outline enables 26 more proofs and cuts mean proof time by 75.9 per cent and mean cost by 88 per cent on cases both solve (abstract, §1, §4).

## How

The model is an agent (the Codex command-line tool with the model gpt-5.5) that works inside a deterministic harness; the harness trusts Lean's kernel, not the agent. The semantics are an extension of Lean-MLIR (§3).

## Limits

What the authors say: the formalisation covers integer instructions; memory operations, floating point and richer loops are future work (§3). The symbolic-width invalid cases, and the symbolic-width loop cases, were derived by hand from fixed-width ones, because the generalisation techniques the authors use do not cover them (dataset description in §4). A careful reader adds: whether the Lean model of LLVM's semantics matches LLVM is not checked by the proofs, and the costs and times depend on one commercial model's pricing in September 2026.

## Against the wiki

- [[proof-automation]]: extends it with a third kind of task. The sources there write proofs for seL4 theorems or Verus code, or, in the Axon report, for one compiler; here the proofs are about LLVM transformations, with a proof checker in the loop.
- [[2026-rinard-testing-credible-compilation]]: both use translation validation. There a verified checker accepts certificates from untrusted compiler passes; here a model builds the proof for a given transformation.

## For zOS

Context only. No `design/` page changes. [[kernel]] lists binary correctness of seL4, which rests on translation validation of its own binary; nothing here bears on that, since Trivet concerns LLVM's transformations.
