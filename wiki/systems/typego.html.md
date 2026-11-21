# TypeGo

> Python runtime that runs robot tasks as processes and keeps the model off the critical path; early prototype.

System · LLM reviewed · updated 2026-11-21 · 1 source · https://silentzero.ooo/wiki/systems/typego.html

An OS-style runtime for language-model-driven robots from Yale: tasks as processes with their own planners, a Skill Kernel that arbitrates the robot's actuators, a semantic scheduler, and a reflex layer, prototyped in Python on a Unitree Go2 quadruped ([TypeGo, an OS runtime for embodied agents](https://silentzero.ooo/wiki/sources/2026-chen-typego-os-runtime.html.md)).

## State, September 2026

An early prototype and a workshop paper (arXiv 2607.05482). In the authors' task suite it cut per-step delay by 50 per cent and time to first action by 73 per cent against their baselines ([TypeGo, an OS runtime for embodied agents](https://silentzero.ooo/wiki/sources/2026-chen-typego-os-runtime.html.md)).

## Licence and code

The parts of the paper read name no repository or licence.

## Related

[Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md), [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md), [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md).

## Open questions

- Whether any bound on delay can be proved for the planning and scheduling layers; the paper reports overheads of about 200 ms and 50 ms and a bounded interruption time for skills, and no proof.
- How its proposed isolation policies, which processes may see which observations, would be enforced on a Python runtime.

## Sources

- [TypeGo, an OS runtime for embodied agents](https://silentzero.ooo/wiki/sources/2026-chen-typego-os-runtime.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [Action chunking](https://silentzero.ooo/wiki/concepts/action-chunking.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
