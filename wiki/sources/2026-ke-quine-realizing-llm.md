---
type: source
id: 2026-ke-quine-realizing-llm
status: reviewed
read: full
kind: design
sources: [2026-ke-quine-realizing-llm]
updated: 2026-11-05
---

# Ke 2026: Quine

Hao Ke (independent researcher). "Quine: Realizing LLM Agents as Native POSIX Processes". [arXiv:2603.18030](https://arxiv.org/abs/2603.18030), version 2 of 9 April 2026. A preprint; code at github.com/kehao95/quine. Read in full.

## What it shows

- **The mapping.** An agent is a POSIX process. Its identity is the process id, its mission the arguments, its material standard input, its deliverable standard output, its diagnostics standard error and its outcome the exit status. State has three tiers: process memory, environment variables, and the file system. Its lifecycle is fork to delegate, exec to renew itself and exit to finish (§2).
- **One executable.** The runtime is a single binary that starts fresh copies of itself, so a parent builds a child's world with the same program it runs in. The host is about 3,100 lines of Go (5,700 with the model-provider code, a binary of about 9.8 MB). It keeps the control loop and calls a remote model as a stateless oracle that returns tool calls: `sh`, `fork`, `exec` and `exit` (§3).
- **What it inherits.** Memory isolation, scheduling, resource limits and composition with shell pipelines and exit codes. The mission and the data travel in different channels, and the host puts the first into the system prompt and the second into the user message. The author calls this a structural basis that "may reduce some" manipulation risks and says it is not a complete security guarantee (§3.1, §4.1).
- **Renewal.** When the context fills, the agent saves progress in environment variables or files and replaces itself with a fresh copy; by default the mission is kept (§4.3).
- **Where POSIX stops.** The author names task-relative "worlds" and revisable time, meaning rollback of effects without forgetting what was learned, as what processes cannot express (§5).
- **Evidence.** Qualitative runs, which the paper says show feasibility and are not benchmarks. A search task produced a three-level tree of 36 sessions. On long-context retrieval tasks (MRCR, 4K to 279K tokens), a run on 178K tokens used nine renewals; a baseline that loaded the whole context failed 5 of 8 samples, while Quine passed all of them (§4.4, Appendix A).

## How

A reference implementation and a design argument; there is no controlled comparison of isolation. The paper makes no claim of better task performance (§1.4).

## Limits

What the author says. It is a design point and not a replacement for frameworks; the "world" and "time" extensions are directions without a mechanism (§1.4, §5.2, §5.3).

A careful reader adds:

- **Ambient authority.** The paper claims containment is inherited from the kernel, which can enforce limits, capabilities, namespaces and seccomp; it does not report that Quine configures any of them, only turn, context and timeout limits in the host (§3.1, §4.1). Our reading: the agent's `sh` tool then runs with the user's authority, the opposite of a capability design, and isolation protects processes from each other, not the user's files from the agent.
- **Eight samples.** The baseline comparison is small and the paper calls it qualitative.
- **Weak separation.** Putting data in a different message channel does not stop a model from following instructions found in it ([[prompt-injection]]).

## Against the wiki

- [[agent-operating-systems]]: the lightest of the designs, in that it adds no new kernel mechanism and takes the existing process model as the substrate.
- [[object-capabilities]], [[broker]]: no change; Quine has no capability model, and the paper's own related-work section sorts other systems by where identity, lifecycle, interface and isolation are realized (§5.1).

## For zOS

The paper does not cite this source. Our reading: it shows what an agent runtime looks like when isolation and authority are left to a general-purpose kernel, the opposite end from a static system with a broker. No `design/` page changes state.
