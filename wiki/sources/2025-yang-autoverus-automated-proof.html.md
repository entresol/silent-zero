# AutoVerus

> AutoVerus: model agents write Verus proofs, over 90 % of 150 Rust tasks. measurement, abstract only.

Source · Yang et al. 2025 · LLM reviewed · updated 2026-11-04 · https://silentzero.ooo/wiki/sources/2025-yang-autoverus-automated-proof.html

Chenyuan Yang, Xuheng Li, Md Rakib Hossain Misu, Jianan Yao, Weidong Cui, Yeyun Gong, Chris Hawblitzel, Shuvendu Lahiri, Jay Lorch, Shuai Lu, Fan Yang, Ziqiao Zhou and Shan Lu: [AutoVerus: Automated Proof Generation for Rust Code](https://www.microsoft.com/en-us/research/publication/autoverus-automated-proof-generation-for-rust-code/), OOPSLA, October 2025.

Read in part: the Microsoft Research publication page, with the abstract. The paper itself was not read, so everything below is what the abstract says.

## What it shows

- **The tool.** AutoVerus uses language models to generate correctness proofs for Rust code that [Verus](https://silentzero.ooo/wiki/systems/verus.html.md) checks. It is a network of model agents that imitate three phases of a human expert: a first proof, refinement guided by general tips, and debugging guided by verification errors.
- **The benchmark.** The authors built a suite of 150 "non-trivial" proof tasks from existing code-generation and verification benchmarks.
- **The result.** AutoVerus produces a correct proof for more than 90 per cent of the tasks, and more than half of them in under 30 seconds or three model calls.
- **Standing.** The page lists a Distinguished Artifact Award and a VS Code plugin; the tool page is dated 25 September 2024.

## How

Not known from the page beyond the three phases above. The abstract does not say how correctness was judged. Our reading: Verus is the checker, so a correct proof is one Verus accepts.

## Limits

The abstract states no models, no definition of a task's specification and no failure analysis. A careful reader adds:

- **Task size.** The tasks come from code-generation and verification benchmarks. Our reading: they are small programs, not kernel components; the abstract does not say.
- **Specification.** A proof shows the code meets its specification. The abstract does not say who wrote the specifications or how they were checked.

## Against the wiki

- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md): **extends**. A second line of work beside [Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md), aimed at Rust and Verus instead of Isabelle and seL4. The two success rates use different tasks and tools: over 90 per cent of 150 tasks here, 77.6 per cent of theorems in three splits there. Our reading: they cannot be compared.
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md): **extends** with a tool that writes proofs for it.

## For Silent Zero

Table 1 of the paper lists AutoVerus with "over 90 % of 150 Rust proof tasks". Confirmed by the abstract. The wiki cannot say more until the paper is read. No `design/` page changes state.

## Related pages

- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md)
- [Neuro-symbolic proof generation for seL4](https://silentzero.ooo/wiki/sources/2026-he-neuro-symbolic-proof.html.md)
