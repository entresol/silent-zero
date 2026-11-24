# TypeGo, an OS runtime for embodied agents

> TypeGo: asynchronous OS-style runtime for a quadruped robot, 50 per cent lower per-step delay. progress, partly read.

Source · Chen, Schott and Zhong 2026 · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/2026-chen-typego-os-runtime.html

Guojun Chen, Alex Schott and Lin Zhong (Yale University). "TypeGo: An OS Runtime for Embodied Agents", AgenticOS workshop at SOSP 2026, September 2026; arXiv:2607.05482. [Page](https://arxiv.org/abs/2607.05482), [PDF](https://os-for-agent.github.io/papers/AgenticOS_SOSP_2026_paper_1.pdf). Read in part: abstract, introduction, system overview, the sections on skills and the implementation, the results summary and the future-work section; not the evaluation in detail.

## What it shows

- **The argument.** "Treating the LLM as a request/response oracle on the critical path is fundamentally at odds with real-time control and concurrent goals." The authors propose a continuously running, asynchronous runtime that "works like a small OS for the agent".
- **The design.** A reflex layer (S0) and a process scheduler (S3) run globally; each task gets its own planning stack (S2 and S1) as a process with a process control block. A "Skill Kernel" arbitrates typed physical subsystems of the robot among the processes. S3 schedules "semantically rather than by fixed numeric priority". "Speculative skill streaming" overlaps planning with motion through a bounded queue. Users write tasks, a persona and reflexes in natural language; reflexes compile into Python condition and action functions that S0 evaluates at high frequency.
- **Skills.** Developers write and verify every skill; its control flow is "never synthesized at runtime". Interruptible skills stop "within a bounded time", which the authors say lets the runtime switch tasks with bounded delay.
- **Results.** On a Unitree Go2 quadruped, in the authors' task suite: per-step delay down by 50 per cent against step-by-step planning, time to first action down by 73 per cent against monolithic planning; about 200 ms for S3 scheduling, 50 ms for S0 reflex handling and 1.2 s of replanning when S3 switches between tasks.
- **Implementation.** A Python prototype; a process is a control block plus Python threads; language-model calls go to cloud services (the paper names GPT-5.4 and a Groq-hosted open model for the fast path).
- **Future work.** "Stronger isolation policies": "which processes may see which observations, which tools may externalize data, and which skills may run concurrently under safety constraints", which "moves the Skill Kernel closer to an OS protection boundary, not just a scheduler for actuators".

## How

An early prototype on one robot with a task suite the authors chose, compared with their own baselines.

## Limits

The paper describes no isolation between processes and no proof; it lists stronger isolation policies as future work. The bounded interruption of skills is a requirement on how skills are written, and the paper does not say the runtime verifies it. The runtime is Python on a conventional system. Results are preliminary and from one platform.

## Against the wiki

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md): **extends** with another system that keeps the language model off the critical path by layered asynchronous loops, measured on a robot.
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md): **extends** with an agent runtime for a robot body ([TypeGo](https://silentzero.ooo/wiki/systems/typego.html.md)).

## For Silent Zero

Our reading: it states the same premise as the paper's Section 4, a slow model that cannot sit in the control loop, and answers it in user-space software; the paper states no timing bound for the runtime as a whole and describes no protection boundary. The paper says none of the designs it names has real-time control as its aim; TypeGo has that aim and was not among the designs the paper names. See [TypeGo](https://silentzero.ooo/wiki/systems/typego.html.md).

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [TypeGo](https://silentzero.ooo/wiki/systems/typego.html.md)
