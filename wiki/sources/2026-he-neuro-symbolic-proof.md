---
type: source
id: 2026-he-neuro-symbolic-proof
status: reviewed
read: full
kind: measurement
sources: [2026-he-neuro-symbolic-proof]
updated: 2026-10-31
---

# He et al. 2026: Neuro-symbolic proof generation for seL4

Baoding He, Zenan Li, Wei Sun, Yuan Yao, Taolue Chen, Xiaoxing Ma and Zhendong Su (Nanjing University, ETH Zurich, Birkbeck), in the order of the OSDI version; arXiv version 2 lists Xiaoxing Ma before Yuan Yao. "Neuro-Symbolic Proof Generation for Scaling Systems Software Verification". [arXiv:2603.19715](https://arxiv.org/abs/2603.19715), version 2 of 7 May 2026, whose acknowledgements thank reviewers and a shepherd. The zOS paper cites the version in Proc. OSDI '26, which is not yet covered here.

## What it shows

- **The method.** Instead of writing whole proofs, a small fine-tuned language model proposes the next proof step for the current proof state in Isabelle/HOL; Isabelle executes each step, counterexample finders (QuickCheck, Nitpick) discard states that cannot be proved, and a best-first tree search, with Sledgehammer as a fallback, looks for a complete proof (§1, §3).
- **On seL4.** On the validation, test and test-hard splits of the FVEL benchmark, drawn from seL4's proofs, the method with a fine-tuned Mistral-7B proves 2,167 theorems: 77.6 per cent "of all still valid theorems across the three evaluated sets", 37.3 percentage points above the best baseline, Sledgehammer. With Qwen3-1.7B it proves 70.4 per cent (§4, Table 1). Selene proved 156 and FVEL's own method 219 (§4).
- **Longer proofs are harder.** Success falls as proofs grow longer; it "remains around 20%" for the 393 theorems whose human proofs exceed ten lines (§4, Figure 3).
- **Unseen code.** On SysInitGroup, derived from a session kept out of training, it reaches 67.6 per cent (§4, Figure 4).
- **Effort.** The proved theorems account for 36.2 per cent of the human proof lines in the evaluated corpus; in a simulated collaboration where a person writes the first part of each proof, the authors estimate about 71 per cent of expert effort saved, which they also gloss as "roughly two-thirds" (§1, §4).
- **Elsewhere.** The method also improves on the baselines in three developments from the Archive of Formal Proofs (x86 semantics, IEEE floating point, a SAT-solver verification) and on Code2Inv loop invariants translated to Isabelle (§4).
- **Context.** The authors put seL4's verification at about 20 person-years and over 100,000 lines of proof for about 10,000 lines of C (§1).

## How

The models are fine-tuned on the 26,081 theorems of FVEL's training split; evaluation uses the other three splits of 1,115, 1,077 and 852 theorems (§4). Isabelle executes every proof step. Our reading: a proof found is a proof, though steps closed by Sledgehammer, as the authors note, place additional trust in its external solvers (§6). All methods get a limit of 120 minutes; the paper also reports an average of 139.1 minutes per successful proof, which it does not reconcile with that limit.

## Limits

What the authors say themselves: the search is computationally expensive, as every step calls Isabelle; success degrades with proof length; step revision relies on heuristics that "may introduce misleading candidates" (§7).

A careful reader adds:

- **Proofs, not specifications.** The theorem statements are given; the method finds proofs for existing statements in an existing development. Writing the specification and the lemmas, the other half of the effort the authors name in §1, stays with people.
- **77.6 per cent of three splits.** The share is of the "still valid" theorems in three benchmark splits, about 2,790 by our arithmetic from 2,167 and 77.6 per cent, not of the 29,125 seL4 theorems in the dataset (§4.2); §1 speaks of around 20,000 theorems and lemmas in seL4. What "still valid" excludes is not explained, and the test-hard split is a chosen set of sessions.
- **Re-proving known results.** Human proofs exist for every theorem tested, and a model trained on the rest of the same development may benefit from that. The test-hard split and the unseen session are the authors' answer; new proofs for new code are a different task.

## Against the wiki

- [[proof-automation]]: created with this source.
- [[sel4]]: extends "Size and cost" with a first measured route to cheaper proofs.
- [[functional-correctness]]: no change; Isabelle still checks every proof.

## For zOS

Section 2.3 of the paper: "A neuro-symbolic method, for instance, proves 77.6 per cent of the seL4 theorems in the FVEL benchmark, though only about 20 per cent of those whose proofs exceed ten lines (He et al. 2026)." Confirmed, with the caveat that the 77.6 per cent covers three evaluation splits of FVEL, not the whole benchmark. Table 1 (Section 5) repeats "77.6 % of seL4 theorems in FVEL". No `design/` page changes state.
