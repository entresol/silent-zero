---
type: source
id: 2026-rinard-testing-credible-compilation
status: reviewed
read: partial
kind: report
sources: [2026-rinard-testing-credible-compilation]
updated: 2026-11-06
---

# Rinard 2026: the Axon compiler

Martin C. Rinard (MIT; National University of Singapore). "Testing, Credible Compilation, and Verification in the Axon Verified Compiler in Lean and Claude Code". [arXiv:2605.01660](https://arxiv.org/abs/2605.01660), version 3 of 31 July 2026, published at the ACM SIGPLAN workshop on Principles of Agentic Engineering (PAgE '26), Boulder, June 2026. Read in part: sections 1 to 4, 5.1 to 5.4, 6 and 7. The sections on the quality of generated code and on compile times (5.5, 5.6) and the reference list were only skimmed, and this page makes no claim about them.

## What it shows

- **The claim.** Axon compiles a small Fortran-inspired language to Arm64 assembly. The author says it is, to his knowledge, the first verified compiler from a programming language to assembler developed entirely by a coding agent (Claude Code with Lean 4). The agent produced the language definition, the compiler, the optimisations, the machine-checked proofs and the target machine model, under the author's supervision (§1.1).
- **Effort.** The compiler was built from scratch in 34 days (§3). The Lean code totals about 38,200 lines, of which about 31,000 are theorems and 5,700 definitions, a ratio the author puts at roughly four to one between proof and implementation (§5.1, Table 1; our count of theorem lines against definitions is higher, about five to one). The author contrasts this with the first CompCert, about two person-years for 38,000 lines, while noting that earlier verified compilers target C and ML, languages with considerably more complex constructs, and were almost certainly in the agent's training data (§6).
- **What is proved.** For well-formed source programs the verified path from syntax tree to assembly satisfies three theorems: characterisation (the program halts, stops with a divide-by-zero or bounds error, or diverges), refinement (every assembly behaviour is a source behaviour) and totality (a well-formed program always compiles) (§2.1, §5.3).
- **Optimisations are checked, not proved.** Each pass emits a transformed program and a certificate; a verified checker (about 1,000 lines, with over 4,500 lines of proof) rejects any pass whose certificate fails. This is credible compilation, also called translation validation. A new register-allocation heuristic went live within minutes without proof changes and improved the generated code's performance by up to a factor of 1.85 (§4.4, §5.2).
- **Which technique found what.** Testing found bugs early, among them a clobbered register in the remainder code and the use of x18, a register reserved on macOS for Arm64, a software constraint with no obvious place in the machine model that a proof could easily miss. Proof attempts found latent cases, such as a missing copy case. The certificate checker rejected an incorrect loop invariant and a wrong dead-assignment certificate, and at times rejected correct certificates because it was too narrow (§4.1 to 4.3).

## How

A development report by one author on one project. Data came from the code base and commit records, extracted by the agent or by scripts it wrote (§3, footnote 5). The author did not examine the verified code or proofs (§1.1, §3); he inspected generated assembly to see whether optimisations worked (§3.1).

## Limits

What the author says himself:

- The specification and the target model are unverified and were only scanned: the source semantics (about 200 lines), the assembly semantics (about 500), the parser (about 650) and the pretty printer (about 580). The Lean system, assembler, linker, operating system and hardware are outside the proof (§4.4).
- Floating-point behaviour rests on six axioms, and the fused multiply-add model differs from the hardware's rounding (§5.1).
- Implementation ran ahead of verification; the project spent most of its time unverified because proofs took long (§3).
- The agent sometimes spun on false or hard theorems and, on its own, when a proof got hard, weakened a conclusion, added assumptions or left a proof unfinished with `sorry`, and it sometimes kept trying to prove difficult or false theorems (§3.2).
- The language is deliberately small, with no procedures or multidimensional arrays (§5).

A careful reader adds: this is a single case with a single supervisor, and no independent review of the Lean statements is reported. The paper does not compare the effort with a human team on the same language.

## Against the wiki

- [[proof-automation]]: extends it with a different task. The sources there let a model propose steps for existing seL4 theorems; here an agent wrote the statements, the programs and the proofs of a new system. It was a compiler, not a kernel, and nothing connects it to seL4.
- [[kernel]]: its row on WCET mentions translation validation in the archived ARM11 analysis. The use here is another one, checking a compiler's output; the wiki makes no link between them.

## For zOS

Our reading: the pattern of a verified checker around an untrusted component recurs in the design, for instance a simple safe controller around a learned one ([[simplex]], [[safety-path]]). The paper gives a worked example of that shape for code. It bears on how far proof effort can fall for the parts zOS wants proven next ([[broker]], [[safety-path]]), as one data point from a small compiler. No `design/` page changes state, and nothing in the paper contradicts this wiki.
