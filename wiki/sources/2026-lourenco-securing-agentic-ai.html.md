# securing agentic AI with OS-level intent-driven capabilities

> Intent-driven capabilities enforced at the system-call boundary; challenges listed. design, full text.

Source · Lourenço et al. 2026 · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/2026-lourenco-securing-agentic-ai.html

Miguel Lourenço, Matthias Neugschwandtner, Nuno Santos and Rodrigo Bruno (INESC-ID, Instituto Superior Técnico, University of Lisbon; Oracle Labs). "Securing Agentic AI with OS-Level Intent-Driven Capabilities", AgenticOS workshop at SOSP 2026, September 2026, vision paper of four pages with references. [PDF](https://os-for-agent.github.io/papers/AgenticOS_SOSP_2026_paper_20.pdf). Read in full.

## What it shows

- **The claim.** Authorisation in operating systems is by identity and static permissions, which fits agents poorly; "authorization can no longer be determined solely by who is executing, but increasingly by why code is executing". Policies enforced only at the tool-invocation layer can be bypassed through subprocesses, shell commands or compiled payloads.
- **The proposal.** "Intent-driven capabilities": a task-specific capability set derived from the user's prompt, enforced at the system-call boundary and discarded when the task ends, in an "intent-driven sandbox" with a capability planner (derives the set from the prompt) and a capability validator (checks every system call, blocks or escalates). Enforcement by "kernel probes or syscall interposition", with eBPF, Linux security modules or gVisor-style user-space kernels named as substrates.
- **An example.** A poisoned calendar skill makes the agent run a backup script that downloads and runs a payload; the user only asked to schedule a meeting, so connections to unknown endpoints and unrelated binaries fall outside the derived set.
- **Challenges it lists.** Bridging a semantic goal to OS resources (calendar services sit behind rotating addresses; a runtime start touches hundreds of libraries), representing capabilities that change as subtasks begin and end, and operating under uncertainty, where escalation "must avoid the permission-fatigue failure mode" of UAC or Android dialogs. For the first, it suggests a cache of "meta-skills" whose creation must be isolated within the trusted base.

## How

A vision paper with one figure of an architecture and an example. It has no implementation and no evaluation.

## Limits

Everything is future work. The paper names as its central challenge translating a user's objective into OS resources; the manipulation of that step comes up only in its remark that the creation of meta-skills must sit in the trusted base.

## Against the wiki

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): **extends** with a second published neighbour on deriving grants from the user's intent, at the system-call boundary and not at the tool layer.
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md): **extends**; compare [AgenticOS](https://silentzero.ooo/wiki/sources/2026-zhao-agenticos-intent-oriented.html.md), which derives what exists from a declared manifest.

## For Silent Zero

Our reading: its vision is the broker's job, minus the guarantee. It places the planner's output at the syscall boundary of a conventional OS; the paper puts the grant beneath the agent and has proof as the broker's target (Section 3), and it leaves open the same question of where a grant comes from. The paper does not name this work. See [agent capabilities should follow task intent (IntentCap)](https://silentzero.ooo/wiki/sources/2026-zheng-llm-agent-capabilities.html.md).

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [Intent-bound capabilities (IntentCap and its neighbour)](https://silentzero.ooo/wiki/systems/intentcap.html.md)
- [agent capabilities should follow task intent (IntentCap)](https://silentzero.ooo/wiki/sources/2026-zheng-llm-agent-capabilities.html.md)
- [AgenticOS](https://silentzero.ooo/wiki/sources/2026-zhao-agenticos-intent-oriented.html.md)
