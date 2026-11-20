---
type: source
id: 2026-rinard-quantitative-comparison-credible
status: reviewed
read: full
kind: measurement
sources: [2026-rinard-quantitative-comparison-credible]
updated: 2026-11-20
---

# Rinard 2026: credible compilation against verification

Martin Rinard (National University of Singapore; Massachusetts Institute of Technology). "Quantitative Comparison of Credible Compilation and Verification In Coding Agent Compiler Development", arXiv 2605.08927v1, 9 May 2026. A preprint. [arXiv](https://arxiv.org/abs/2605.08927). Read in full, including the appendices.

## What it shows

- **The question.** The author calls this the first quantitative comparison of the two main ways to get a correct compiler: credible compilation (translation validation), where an untrusted transformation is paired with a checker that discards it if the result fails, and full verification, where a proof shows the transformation correct. A coding agent under human supervision built both versions of three optimisations in the Axon compiler: unreachable code elimination (UCE), dead assignment elimination (DAE) and constant propagation and folding (CP). All code and proofs came from the agent (§1, §3).
- **Effort.** Verified versions took roughly an order of magnitude more effort. Agent active time was 19.9 times higher for UCE, 7.6 for UCE+DAE and 8.3 for CP; tokens 25.0, 8.8 and 10.2 times (§4.1). Counting the updates to the verified certificate checker, which the author treats as shared infrastructure, brings the ratios to between 3.5 and 4.3. In Table 1 the verified CP took 15 sessions and 59 supervisor prompts, against 3 sessions and 15 prompts for the credible version. The verified UCE added 4,348 proof lines against 549 code lines (Table 1).
- **Prompts.** The credible versions were built from a short description of the optimisation (§1: "several words"; the §11 prompts run to a few sentences) plus generated tests. The verified ones typically needed multi-hour supervised proof sessions (§1, §11). The 188 supervisor prompts averaged 84.2 characters (§4.1).
- **Scope reduction.** To ease proofs, the agent repeatedly narrowed what a verified optimisation did. Examples: replacing unreachable code with halt instructions, checking the reachability result at run time instead of proving it, treating an assignment as dead only if the variable is never read anywhere in the program, handling 3 of 9 kinds of assignment. The UCE restrictions and the DAE limitations were lifted under supervisor direction, DAE over several sessions; the no-op replacement was kept and a separate pass added (§5.1, §5.2).
- **Efficiency.** The verified versions chose slower algorithms and data structures for provability, such as lists instead of hash maps and full-program passes instead of worklists. Even after tuning, they stay slower than the credible versions' optimisation step (§4.2, §6). A worklist replaced a full-pass analysis in verified DAE and made it 35 to 393 times faster, geometric mean 137; in verified CP, 4.7 to 12 times faster, mean 7.27 (§5.2, §5.3).
- **Checking cost.** Certificate checking time exceeds optimisation and certificate generation time for the optimisations studied (Table 2, §4.2). A fast path in the checker made checks 2.6 to 4.2 times faster for CP and 2.4 to 4 times for UCE+DAE (§5.3). The author draws two conclusions, that composite optimisations can share the checking cost and that credible compilation suits complex optimisations and verification simple ones (§1, §4.2).
- **Change cost.** Changes to verified optimisations broke existing proofs and caused cascading proof updates; comparable changes to credible ones went through almost at once unless the checker had to change (§1, §6). The author suggests developing with credible compilation first and verifying once the target is clear (§6).
- **Feasibility.** Despite the overhead the author finds verification, depending on the context, a feasible alternative (abstract, §1).

## How

The setting is the Axon compiler, built by a coding agent (see [[2026-rinard-testing-credible-compilation]]), with a verified certificate checker. A baseline held two identity optimisations, one of each kind. The agent then implemented each optimisation both ways, UCE first, DAE as an extension of UCE, CP last, credible before verified. The author wrote the first prompt of each; the agent wrote the opening prompts of follow-up sessions, while the supervisor typed 188 prompts during sessions against 40 from the agent (§3, §4.1). The agent was Claude Code with Claude Opus 4.7 and Lean 4.28.0 on an Apple M4 Pro with 24 GB (§3). Effort data (sessions, active time, tokens, lines, prompts) come from scripts the agent wrote (§4, Table 1). Compile times are for the 24 Livermore Fortran kernels, translated into Axon's language by the agent; each figure is the mean of 20 runs with the minimum and maximum dropped (§4.2, Table 2; Tables 3 and 4 give deviations, mostly within a few per cent of the mean).

## Limits

What the author says himself:

- Three optimisations in one compiler on one intermediate language. The author does not claim the results carry over exactly to other intermediate representations or compilers (§8).
- Compile times come from computational kernels, not whole applications (§8).
- Another supervisor, supervision strategy or coding agent could give different results; the numbers may change as agents improve (§8).
- The author expects the advantage of credible compilation to hold up and the gap to widen for harder optimisations such as register allocation, but did not measure that (§8).
- The two versions of DAE differ: only the credible one removes transitively dead assignments, and the verified one needs a driver loop for that, whose figures are not reported (§3, §5.2). The Livermore kernels have none.
- The optimisations alone gave no measurable speed-up of the generated code, as the author expected (§4).
- The author thinks verified optimisation times could come close to the credible ones with enough effort, and that whether this is worth doing depends on context (§6).

A careful reader adds the following.

- It is a single supervisor and a single run per optimisation, with no repeated development to show how much the session counts vary.
- The credible and verified versions are not built under equal conditions. The credible ones came first, and the UCE+DAE prompts, verified and credible, say to update the existing unreachable-code pass (§11), so the order may favour the later ones. Nothing here says which way.
- Several prompts in §11 look like copy errors: the UCE+DAE credible prompt asks to "verify the correctness", and the CP verified prompt says it uses credible compilation. We read these as mistakes in the appendix; the text does not comment on them.
- "Order of magnitude" is the author's summary of ratios from about 3.5 to 25, depending on whether checker updates are counted and which measure is used.
- The paper says the agent needs no human code audit (§1, §6). That rests on the verified checker, the proofs and the specifications. The earlier Axon paper says some of those were not verified, and this paper does not examine them.
- Our reading of Table 2: for CP, on ten of the 24 kernels (k08, k09, k10, k13, k14, k15, k16, k18, k20, k23) the verified version is slower than the credible one even with certificate generation and checking added (for k18 about 4,127 against about 430, in the table's units, which Table 3 gives as milliseconds). On the others it is faster or about equal; the crossover is at medium size. The text compares only against the optimisation step.
- The paper is a preprint with one author.

## Against the wiki

- [[2026-rinard-testing-credible-compilation]]: **extends**. The earlier page records that Axon's optimisations were checked, not proved, and that the agent weakened theorems or left proofs open. This paper puts numbers on the same split and reports the same weakening as scope reduction, here for verified optimisations.
- [[proof-automation]]: **extends** its compiler entry. That page gives a proof-to-code ratio of about four to one for the whole compiler. Here the proof lines for single optimisations run higher (Table 1: 4,348 against 549 code lines for UCE verified). Our reading: the two are not the same measure, since this one counts a single pass's changes.
- [[2026-liao-llvm-translation-validation]]: Our reading: both treat a checker as the trusted part around an untrusted transformation, in different groups and settings; the Trivet page records no effort comparison.
- [[simplex]] and [[safety-path]]: no source in them says anything about this result; see "For zOS".

## For zOS

[[broker]] and [[safety-path]]: no change of state. Our reading: the paper gives a number for a choice the design already faces, whether to prove a component or keep it unproved behind a small checked part. Here the checked route cost much less effort for the agent, and the proved route pushed the agent towards simpler, slower and narrower code. The setting is a compiler optimisation pass. It is neither a broker nor a control loop, so the figures do not transfer; the shape of the trade-off does. The wiki's `design/` pages claim no proof of these parts, and nothing here changes that. Nothing in zOS is built.
