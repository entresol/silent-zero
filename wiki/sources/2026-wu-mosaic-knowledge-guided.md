---
type: source
id: 2026-wu-mosaic-knowledge-guided
status: reviewed
read: partial
kind: measurement
sources: [2026-wu-mosaic-knowledge-guided]
updated: 2026-11-07
---

# Wu et al. 2026: MOSAIC

Jiangrong Wu, Huaijin Wang, Yihao Zhang, Yuhong Nan and Shuai Wang (Sun Yat-sen University, Shandong University, Peking University, Hong Kong University of Science and Technology). "MOSAIC: Knowledge-Guided CLI Command Composition Attack in LLM Coding Agents", arXiv 2607.02857, 3 July 2026. A preprint. [arXiv](https://arxiv.org/abs/2607.02857). Read: the abstract, the introduction, the evaluation (§VIII) and the discussion (§IX). The method sections on how the knowledge base is built were read only in outline.

## What it shows

- **A new attack surface.** Coding agents run ordinary command-line tools that cooperate through shared operating-system state: environment variables, files, package lifecycle scripts, hooks. Commands that are each benign can form a producer and consumer chain in which a later command reads state an earlier one wrote and so crosses a security boundary. The authors call this CLI command-composition risk (abstract; §I).
- **Success rate.** The attack succeeded in 96.59 per cent of 2,525 trials: 101 exploit paths, five coding agents (Claude Code, Codex CLI, Gemini CLI, GitHub Copilot CLI, Trae Agent) and five back-end models. every agent stayed above 95.8 per cent (Table I). Success needed both the expected command trace and a deterministic marker or external effect, so a trace that only looked right did not count (§VIII.A).
- **Instruction-layer baselines.** Two attacks hide a malicious instruction in text the agent reads. The authors built them from the goals of their own 101 instances and wrapped them in one style (AIShellJack) or five (general injection). They succeeded in 2.18 and 0.79 per cent of the trials on Claude Code, against 96.63 per cent for MOSAIC (Table II).
- **Defences left it standing.** On Claude Code, a prompt-injection detector (PromptGuard 2), Progent for capability control and CaMeL for information flow each left the rate at 96.63 per cent, a drop of 0.00 points. CaMeL was run as an external monitor over the agent's trace with a source-to-sink policy, not as CaMeL's own interpreter (§VIII.D). A static scanner (Semgrep, with security and shell rule packs) lowered it to 86.73 and an alignment monitor (AlignmentCheck) to 82.57 per cent (Table V, §VIII.D).
- **Why, in the authors' words.** Progent governs tool calls only. CaMeL follows values that pass between tool-call arguments, while this attack passes state through the system between two separate commands, so the dependency is never observed (§VIII.D). The authors conclude that the defences watch the wrong level and that safety has to be judged on the state relations across a command trace (§IX).

## How

The authors distil command and state behaviours from CVEs, advisories and published proofs of concept into reusable summaries and compose them into exploit paths of two to four commands, each embedded in a realistic developer task. The attacker only plants content the agent reads and cannot run commands on the victim machine (§VIII.B). The five defences were deployed as hooks over the agent's tool calls. For Progent and CaMeL the authors used the strongest policy that still let the benign task run; Progent's allowed workspace reads and writes, dependency installation and version control, and denied network egress and writes outside the workspace (§VIII.D).

## Limits

The authors say the 101 paths are evidence-based and not an exhaustive catalogue (§IX). Their own check found that most failed trials ended because the agent finished the benign task by another valid command route, and that forcing the intended route made the attack succeed (§VIII.B). The authors chose the policies and adapted the defences to this setting; a policy covering shared state is not tested. Table V uses one agent, Claude Code; by our count of its 505 trials it covers five models. A careful reader adds that this is a preprint, that the targets are general-purpose coding agents on ordinary hosts, and that no robot, real-time or capability-kernel system was tested.

## Against the wiki

- [[prompt-injection]]: **extends** it. The instances carry no explicit malicious instruction, which the authors give as the reason the instruction scanner (PromptGuard 2) had no effect (§VIII.D); the other defences listed there were not tested.
- [[broker]]: **extends** the open question on sequences of allowed calls. [[2025-debenedetti-defeating-prompt-injections]] named the risk of such sequences (§9.3). Our reading: this source measures a related case, shell commands that cross system state, which need not be separately brokered tool calls. It adds a limit for defences around the model: they see what passes between tool calls and not what passes through the system beneath them.
- [[object-capabilities]]: Progent's policy lists tools and arguments, not the objects an agent's processes share. Our reading: a capability system bounds reach only if the objects reachable by two components are themselves part of the authority, which the authors' advice of ephemeral least-privilege environments points to without testing it. Their main proposal is a monitor that tags state from untrusted sources and checks where a later command consumes it; it too is untested (§IX).

## For zOS

[[broker]]: no change of state. Our reading: the paper requires its broker to enforce each permitted action "at every tool call" (Section 5), and this source shows that a check at that level alone is not enough when the agent can also write state that other commands read. In zOS the agent is meant to run in its own protection domain with only the capabilities it was given, so little shared state would exist by default; that is our design intent, not a statement of the paper, not something this source tests, and nothing in zOS is built. The static system ([[static-system]]) decides what two components share, so the question moves there.
