---
type: source
id: 2025-li-osvbench-benchmarking-llms
status: reviewed
read: full
kind: measurement
sources: [2025-li-osvbench-benchmarking-llms]
updated: 2026-11-20
---

# Li et al. 2025: OSVBench

Shangyu Li, Juyong Jiang, Tiancheng Zhao and Jiasi Shen (The Hong Kong University of Science and Technology, its Guangzhou campus, Georgia Institute of Technology). "OSVBench: Benchmarking LLMs on Specification Generation Tasks for Operating System Verification", arXiv 2504.20964v2, 7 December 2025. The text is marked as the extended version of a paper published at AAAI-26. [arXiv](https://arxiv.org/abs/2504.20964). Read in full, main text and appendices A to E.

## What it shows

- **A benchmark for the specification side.** OSVBench has 245 tasks built on Hyperkernel, a verified kernel with 49 system calls its verifier supports. Each task asks a model to write the state-machine specification of one system call, from the call's natural-language description and its C code. A prompt averages about 20k to 30k tokens (§1, §3.2); in the standard 5-shot setting the mean is 24,274 (Table 4). The authors say earlier work on LLMs in verification focuses mainly on proof generation and often overlooks specification generation (§1).
- **Bugs injected on purpose.** Of the 245 code implementations, 49 are correct and the others carry one to five injected bugs of five types taken from the xv6 kernel: incorrect pointer, incorrect privilege, memory leak, buffer overflow, bounds checking (§3.3, Appendix B). Our reading: the model is not asked to find the bugs; its specification must make the verifier report the same inconsistencies as the reference specification does (Figure 1, §4.1).
- **Low scores.** With a 5-shot prompt and greedy decoding, the best of 12 models, Doubao-1.5-pro, reached 55.10 per cent Pass@1 over all 245 tasks and 63.27 on the bug-free implementations. The best open-source model, DeepSeek-Chat, reached 46.53, Claude-3.5-sonnet 44.90, GPT-4o 38.78, o1 23.67 and Qwen2.5-Coder-7B-Instruct 4.90 (Table 1). The authors read this as limited performance of current models.
- **Bugs lower the score.** In 53 of 60 model and bug-type pairs the score was lower than on bug-free code (§4.2). The score generally fell as the number of injected bugs rose (Figure 5, §4.5).
- **Reasoning models did not lead.** o1 scored below QwQ-32B-Preview, and DeepSeek-R1 below DeepSeek-Chat (Table 1, §4.2). GPT-4o beat o1 and o3-mini at every bug count (§4.5). The authors speculate that long reasoning traces strain long-context handling; they do not test this.
- **Examples matter.** With no examples every model scored 0 per cent. Scores rose with 1, 3 and 5 examples, tested on five models (§4.4, Figure 4).
- **Errors and repair.** Syntax errors (a specification that does not run) ranged from 22.45 per cent (Claude-3.5-sonnet) to 86.12 (Qwen2.5-Coder-7B-Instruct); semantic errors from 9.39 to 32.65 (Table 3). In a two-round self-repair given the verifier's error messages, GPT-4o repaired 14.67 per cent of its erroneous specifications in round one and 1.56 in round two; DeepSeek-Chat 11.45 and 2.59 (Table 2, §4.3).
- **More attempts help.** For GPT-4o, DeepSeek-Chat and Llama-3.1-70B-Instruct the average pass rate rose from k = 1 to 3 to 5; the figure gives no table of values (Figure 3, §4.2).
- **Cost context.** The authors cite seL4 as 11 person-years for 10k lines of C and 7 person-months for its formal specification, and 9.25 person-months for two operations of the BilbyFs file system, to motivate automation (§1, citing Klein et al. 2009 and Amani et al. 2016).

## How

Each task prompt has five parts: a system prompt, the verification assumptions (such as a uniprocessor kernel), a programming model in Python and Z3 terms, few-shot examples, and the task question. The synthesis problem is confined to a small grammar of states, conditions and expressions (Figure 2, §3.2, §3.3). The declarative specification of Hyperkernel is held fixed, so only the state-machine specification is generated. A generated specification counts as correct if, on every kernel implementation, the Hyperkernel verifier gives the same result as with the reference specification (Figure 1, §3.2). The verifier uses symbolic execution of the compiled LLVM code and the Z3 solver (§3.2). Twelve models from six providers were run through official APIs; each Pass@1 figure is the mean of three runs (§4.1). Few-shot and repair experiments used fewer models (five and two) for cost (§4.4, §4.3).

## Limits

The authors name these. The benchmark rests on one kernel, Hyperkernel, so models may overfit it and the results may not carry to other architectures. The 20k to 30k token tasks test context handling, which may hide other abilities such as logical reasoning. The restricted syntax and semantics may not reflect how real kernel development works, and the metrics miss readability and adaptability (Limitations).

A careful reader adds the following.

- Correct means the same verifier output as the reference, so the score tests agreement with one specification. A specification that differs in form but is sound could be marked wrong; the paper does not discuss this.
- The text's own numbers disagree in one place: Appendix E says incorrect pointer is the most frequent bug type with 112 tasks, while Table 5 lists 112 for incorrect privilege and 71 for incorrect pointer.
- The models are those the authors name; later models are not measured. Our reading: the figures describe models available when the work was done and may not hold for newer ones.
- Greedy decoding and one prompt style were used; the paper reports no variance across the three runs.
- The seL4 effort figures are quoted from other work and differ from the wiki's own record (see below).
- Why reasoning models did worse is a guess by the authors, not a finding.

## Against the wiki

- [[proof-automation]]: **extends**. That page records proof generation for seL4 and Rust (He et al., Selene, PROMISE, AutoVerus), where a checker accepts or rejects. This source measures the step before: writing the specification. Its figures, up to 55.10 per cent Pass@1 on one kernel, 245 tasks and twelve named models, cannot be set against the 77.6 per cent of [[2026-he-neuro-symbolic-proof]], which is a different task, kernel and prover (our reading). The page's line that automated proofs "measure the cost of re-proving, not of specifying" gains a score for one kind of specification-writing; OSVBench does not measure the cost of specifying.
- [[2009-klein-sel4-formal-verification]] and [[sel4]]: **differs in a figure**. The source says 11 person-years for 10k lines of C; the wiki records about 20 person-years for the first proof, 11 of them seL4-specific ([[proof-automation]], citing that source's §5.2). Our reading: the OSVBench authors quote the seL4-specific part; the wiki's figure is the one to keep.
- [[2024-zhang-selene-pioneering-automated]]: related. OSVBench cites Selene as work on proof generation and is a different task.
- [[functional-correctness]]: **related**. The authors call kernel specifications often ad hoc and in need of domain expertise (§1), and they fix the declarative specification so correctness can be judged (§3.2). Our reading: this fits the zOS paper's remark (Section 6) that a proof is only as good as its seams and its specification, but the source does not say it.

## For zOS

[[kernel]]: no change of state. OSVBench is on a different kernel (Hyperkernel, verified with an automated prover, §3.1), not on seL4, and says nothing about seL4's proofs. The source gives no ground to plan on machine-written specifications: one kernel, 2025 models, no comparison with human work, and the declarative specification was held fixed, so the zOS paper's remark on invariants (Section 2.3) is not tested here. Nothing in zOS is built on this.
