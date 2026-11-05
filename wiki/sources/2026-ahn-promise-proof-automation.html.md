# PROMISE

> PROMISE: structure-guided LLM proof search on 223 seL4 theorems, 55.7 % averaged over seven settings. measurement, partly read.

Source · Ahn et al. 2026 · LLM reviewed · updated 2026-11-03 · https://silentzero.ooo/wiki/sources/2026-ahn-promise-proof-automation.html

Youngjoo Ahn, Sangyeop Yeo, Gijung Im, Jongmin Lee, Jinyoung Yeo and Jieung Kim (Yonsei University). "PROMISE: Proof Automation as Structural Imitation of Human Reasoning". [arXiv:2604.05399](https://arxiv.org/abs/2604.05399), version 2 of 9 April 2026. Read in part: the abstract, introduction, evaluation setup, results, related work and conclusion. The retrieval and search method of section 3 was only skimmed, and the definition of the difficulty levels P1 to P3 was not found in the text read.

## What it shows

- **The method.** A framework that mines proof states and tactic-transition traces from existing Isabelle proofs, retrieves structurally similar fragments and uses them to guide a beam search over Isabelle proof states with a language model proposing next steps. Candidates run in Isabelle (abstract, §3).
- **The benchmark.** 223 Isabelle/HOL theorems from the seL4 l4v development: 100 at level P1, 100 at P2 and 23 at P3, from theories including monads, invariants, information flow, capDL and access control (§4).
- **The results.** With Qwen2.5-Coder-7B-Instruct, PROMISE proves 77 of 100 at P1, 36 of 100 at P2 and 7 of 23 (30.4 per cent) at P3. With GPT-3.5-turbo it reaches 85 and 40, and with GPT-4.1 69 and 33. Level P3 was run only with Qwen2.5-Coder-7B, so the seven settings mix P1 and P2 on three models with P3 on one. Averaged over them it reaches 55.7 per cent, against 34.0 for Rango, 26.8 for Selene (five attempts) and 20.9 for Selene (one attempt). It is best in six of seven settings; Rango is ahead on GPT-4.1 at P2, 35 against 33 (§5).
- **Counting.** A theorem counts as solved only when the proof closes the local state and the whole theory builds in Isabelle (§4).

## How

The authors re-implemented both baselines: the Selene artifact is not public, and Rango targets Rocq, so they ported it to Isabelle/HOL. They state that the re-implementations may not fully match the originals. Selene gets five or thirty attempts; Rango gets 20 rollouts of up to 24 steps with a fixed step budget instead of a wall-clock timeout, because the bridge to Isabelle is slow. The authors call this budget conservative relative to PROMISE, which issues about 30 model queries per lemma. Verification times out after 600 seconds (§4).

## Limits

What the authors say themselves: evaluation on the full seL4 corpus is future work. A careful reader adds:

- **A subset, with the baselines re-run.** The 223 theorems are a chosen benchmark, and the comparison depends on the authors' settings for the baselines. Our reading: the numbers are not comparable to the share in [Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md), which uses another benchmark and another metric.
- **Known proofs.** Human proofs exist for every theorem tested, as in the other work on seL4. Proving a new statement for new code is a different task.
- **Preprint.** The text read carries no venue; we did not check whether it has been peer reviewed.

## Against the wiki

- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md): extends the state with a second method evaluated on seL4, with the caveat on comparability.
- [Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md): both start from the same observation that single-shot generation does not scale; neither confirms the other's figures.

## For Silent Zero

Section 2.3 of the paper cites He et al. for 77.6 per cent and the 20 per cent for long proofs. PROMISE's figures do not change those sentences; they show the field moving fast, on different benchmarks. No `design/` page changes state.

## Related pages

- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md)
