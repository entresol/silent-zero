---
type: source
id: 2026-he-neuro-symbolic-proof-osdi
status: reviewed
read: full
kind: measurement
sources: [2026-he-neuro-symbolic-proof-osdi, 2026-he-neuro-symbolic-proof]
updated: 2026-11-05
---

# He et al. 2026: neuro-symbolic proof generation, OSDI version

Baoding He, Zenan Li, Wei Sun, Yuan Yao, Taolue Chen, Xiaoxing Ma and Zhendong Su (Nanjing University, ETH Zurich, Birkbeck), in the order of the proceedings cover; the article's own header lists Xiaoxing Ma before Yuan Yao, and the two are marked as corresponding authors. "Neuro-Symbolic Proof Generation for Scaling Systems Software Verification", Proc. 20th USENIX OSDI, Seattle, 13 to 15 July 2026. [Paper](https://www.usenix.org/system/files/osdi26-he-baoding.pdf). Read in full. This is the peer-reviewed version of the preprint in [[2026-he-neuro-symbolic-proof]], which says what the method is; this page records the OSDI text and what differs from the preprint.

## What it shows

- **Unchanged.** The OSDI text keeps the method, the benchmark and the headline figures. FVEL has 29,125 seL4 theorems in four splits, 26,081 for training and 1,115, 1,077 and 852 to evaluate (§4.2). A fine-tuned Mistral-7B proves 2,167 theorems, 77.6 per cent of "all still valid theorems across the three evaluated sets", which is 37.3 points above Sledgehammer; Qwen3-1.7B reaches 70.4 per cent (§4.3.1, Table 1). The unseen SysInitGroup reaches 67.6 per cent, and about 20 per cent of the 393 theorems with proofs over ten lines are proved (§4.3.1, Figure 3). Selene proved 156 and FVEL 219 (§4.3.1).
- **Effort figure changed.** In a simulated collaboration where a person writes the first part of each proof, the OSDI text reports an average saving of 79.8 per cent, "roughly 80%". The preprint (version 2) says 71.1 per cent, "roughly two-thirds". The 36.2 per cent of human proof lines covered by fully automatic proofs, 6,235 lines, is the same (§4.3.2, Table 2).
- **Time.** The preprint has the same figures, which its wiki page records only in part. The average time to a successful proof is 139.1 minutes, skewed by a few very long ones; 58.4 per cent of the theorems are proved within 10 minutes, 73.4 per cent within 30 and 80.8 per cent within 2 hours (§4.3.2). The limit for all methods is 120 minutes, "as we observed no noticeable improvement" beyond (§4.2).
- **A leak check.** The preprint has it too. Because seL4's proofs are public and a pretrained model may have seen them, the authors compare generated proofs with the human ones by sequence and Jaccard similarity. Both stay low and fall as proofs grow longer; among one- and two-line proofs, 16.7 per cent are identical to the original (§4.3.3, Figure 6).
- **Other developments.** Three projects of the Archive of Formal Proofs (x86 semantics, IEEE floating point, a SAT-solver verification) and Code2Inv loop invariants translated to Isabelle (§4.3.3).
- **Context.** seL4's verification needed about 20 person-years and over 100,000 lines of proof for about 10,000 lines of C and 3,000 in its simplest abstract specification (§1). The seL4 project contains "only around 20K theorems and lemmas" (§1).
- **Artifacts.** A repository named seL4-proof-search and a Docker image with the verification environment, named in the closing availability note.

## How

As in the preprint: step-wise proposals by a fine-tuned model, execution in Isabelle through a new REPL, counterexample finders to discard states, best-first search, and Sledgehammer on the 16 best states when the search stalls (§3, §4.1, §4.2). Training pairs: 181,887 proof states and steps from the training split (§4.2).

## Limits

What the authors say. The search is expensive because every step calls Isabelle; success falls with proof length; step revision is heuristic and "may introduce misleading candidates". They name a hybrid with a frontier model as future work (§7).

A careful reader adds:

- **The time figure.** An average of 139.1 minutes sits above the stated limit of 120; the text does not say how the two fit.
- **Still valid.** What the 77.6 per cent excludes as "still valid" is not explained in the text, and the arithmetic gives about 2,790 theorems, not the 29,125.
- **Proofs, not specifications.** The theorem statements are given; see [[2026-he-neuro-symbolic-proof]] for the argument.
- **Leak check is indirect.** Low similarity shows the model does not copy, not that it never profited from the rest of the same development.

## Against the wiki

- [[2026-he-neuro-symbolic-proof]]: the OSDI text confirms its figures except the effort saving. It also carries the time distribution and the leak check, which the preprint has as well.
- [[proof-automation]]: updates the state with the peer-reviewed version and the new effort figure.
- [[2024-zhang-selene-pioneering-automated]]: the work's earlier baseline, as the text describes it.

## For zOS

Section 2.3 of the paper: "A neuro-symbolic method, for instance, proves 77.6 per cent of the seL4 theorems in the FVEL benchmark, though only about 20 per cent of those whose proofs exceed ten lines (He et al. 2026)". Confirmed against the OSDI version, which the paper's bibliography names, with the same caveat as for the preprint: the 77.6 per cent covers three evaluation splits, not the whole benchmark. The paper's Table 1 does not use the effort figure that changed. No `design/` page changes state.
