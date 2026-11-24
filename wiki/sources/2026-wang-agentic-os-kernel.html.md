# IntentOS, an agentic OS kernel

> IntentOS: a language model beside Linux composes micro-syscalls; safety rests on new per-call checks. measurement, partly read.

Source · Wang et al. 2026 · LLM reviewed · updated 2026-11-22 · https://silentzero.ooo/wiki/sources/2026-wang-agentic-os-kernel.html

Haocheng Wang, Xinyue Sun, Hao Yi, Dong Du, Yubin Xia and Haibo Chen (Shanghai Jiao Tong University, Zhejiang University). "An Agentic OS Kernel for Flexible and Enhanced Semantics", arXiv 2611.00002v1 [cs.OS]; the PDF's arXiv stamp reads 2 August 2026, which does not fit an identifier of the November series, and the date is not settled here. [arXiv](https://arxiv.org/abs/2611.00002). Read: abstract, introduction, design, implementation overview, discussion and the set-up and headline results of the evaluation; the related work and the per-benchmark details were skimmed.

## What it shows

- **The idea.** A kernel with a new entry point, the intent syscall (isyscall): an application states a goal, and the kernel asks a language model to compose a plan out of fine-grained "micro-syscalls". The model runs in a separate component, the LLMSidecar, which has no execution capability; the kernel executes the plan. A plan that works is cached and reused without the model (abstract, §1, §3).
- **Safety claim, by design.** The abstract says the kernel's safety guarantees do not depend on the model being right. The reasons given: each micro-syscall carries argument checks inspired by those of ordinary syscalls (user-pointer validity, existence, length and overflow, permission or capability or ownership, resource limits, illegal flag combinations), resources are reached only through handles, a micro-syscall may not keep global kernel locks, and new plans pass a verifier that checks that loops terminate (§4.1, §4.3, §4.4). A failed step is rolled back. The evaluation covers accuracy, compatibility and performance; the text read reports no attack or fuzzing test of the safety claim.
- **Implementation.** IntentOS is an add-on patch to Linux with three sets of tools for process, file and memory management (§5). Accuracy was tested on about ten intents in each of three domains with four planner models: DeepSeek-V4-Pro, Qwen3.6-Plus, Gemini-3.1-Pro-Preview and GPT-5.4 (§6.1, §6.3), against an "oracle" baseline that receives the kernel source: 98.38 per cent against 66.74 per cent on average. Compatibility was tested on four Linux versions (§6.6).
- **Performance.** The abstract reports up to 17.55 per cent lower latency for creating backend processes, up to 6.97 per cent for multi-file operations and up to 75.52 per cent less performance impact on a front-end Nginx server during background memory operations. The gains come from removing redundant kernel work, for example avoiding the page-table copy in fork before exec and batching directory updates, not from safety (§2, §6). Planning with a model for an unseen intent takes tens of seconds in the authors' ablation, and the cache avoids it for repeated intents (§1, §6.7).
- **Other kernels.** The discussion says the idea would map onto microkernels such as seL4, where tools would become kernel object methods or user-space endpoints. It is stated as feasible, not built (§7).

## How

Comparison with baseline Linux and the oracle planner on bare metal with Linux 6.18.6. The plan format is a linked list of nodes with arguments kept apart, so a cached plan can be reused with new values.

## Limits

The authors say the planner improves flexibility but is limited by cold-path latency and by probabilistic errors on unseen intents (§7). For severe hallucinations a developer can review and patch cached plans offline (§4.2).

A careful reader adds:

- "Verified plans" in the abstract means plans that passed the loop-termination verifier (§4.1, §4.4); it is not a formal proof of the kernel or of what a plan does.
- The safety argument is that each micro-syscall is checked like a syscall, in any order. It does not address what an authorised combination of calls does to the data or the user, which is the question the [The broker](https://silentzero.ooo/wiki/design/broker.html.md) answers.
- Linux is the trusted base, and the add-on patch (plan executor, cache, verifier, tool sets, the channel to the sidecar) adds to it; the text read gives no size.
- The 17.55, 6.97 and 75.52 per cent figures are best cases from specific set-ups. The oracle baseline is a naive coding agent with the kernel source, not an upper bound. The paper says it does not intend to replace faster process-creation calls such as vfork or posix_spawn (§7).

## Against the wiki

- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md): **extends**. A new design in the table: a planner beside the kernel, a kernel add-on that executes its plans, enforcement by new checks modelled on the syscall checks.
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): **related**. Here a model plans next to the kernel and safety rests on per-call checks; in Silent Zero the model sits outside and authority is granted per request. Our reading: the paper does not bind authority to a user's request.
- [AgenticOS](https://silentzero.ooo/wiki/sources/2026-zhao-agenticos-intent-oriented.html.md): related. In both an intent shapes what runs; in IntentOS the micro-syscalls stay callable directly and the intent selects a composition, and there is an implementation with measurements.

## For Silent Zero

[The broker](https://silentzero.ooo/wiki/design/broker.html.md): no change of state. Our reading: the design puts a language model next to the enforcement point but keeps it without execution authority, which is the broker's shape; its enforcement is new, unproven code on Linux. The source shows no test against an adaptive attacker and claims none.

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [AgenticOS](https://silentzero.ooo/wiki/sources/2026-zhao-agenticos-intent-oriented.html.md)
