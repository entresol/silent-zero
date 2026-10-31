---
type: source
id: 2025-google-building-next-generation
status: reviewed
read: full
kind: report
sources: [2025-google-building-next-generation]
updated: 2026-10-31
---

# Google 2025: Gemini Robotics-ER 1.5

Google Developers Blog, 25 September 2025. [Post](https://developers.googleblog.com/building-the-next-generation-of-physical-agents-with-gemini-robotics-er-15/). Read from the page as saved on 23 October 2026.

## What it shows

- **A reasoning model for robots.** Google makes it available to developers in preview, the first Gemini Robotics model offered broadly. It is described as "the high level brain for your robot": it understands the scene, plans multi-step tasks, estimates progress and detects success.
- **It calls tools.** The model can call Google Search, user-defined functions, a robot's hardware API, a grasping model or a vision-language-action model (VLA) for motor control. A request such as "clean up the table" becomes a plan and a sequence of such calls.
- **A thinking budget.** Developers trade latency against accuracy by setting how long the model thinks, or switch thinking off; simple spatial tasks need little budget, complex reasoning more.
- **Safety at the model level.** Better refusal of dangerous or harmful plans, evaluated against benchmarks such as ASIMOV, and better recognition of requests that violate a physical constraint the developer defines, such as payload capacity or workspace limits.
- **And beyond the model.** The post says these safeguards "are not a substitute for the rigorous safety engineering required for physical systems" and advocates a "Swiss cheese approach" of several layers; developers remain responsible for emergency stops, collision avoidance and risk assessment.

## How

A product post with code examples for pointing, trajectories and video understanding. Benchmark results are said to be in a technical report, which is not read here.

## Limits

A careful reader adds:

- **The vendor's own word.** "State-of-the-art" claims rest on benchmarks named in a report this page does not reproduce.
- **No timing figures.** The post speaks of low latency and quick responses, and shows a chart of latency against thinking budget, but gives no figures, deadlines or real-time guarantees.
- **Refusal is not a guarantee.** Our reading: safety filters in a model are probabilistic by nature; the post itself asks for layers outside it.

## Against the wiki

- [[action-chunking]], [[real-time-loops]]: the slow reasoning layer above the action model. Our reading: its thinking budget makes its latency a parameter, so the loop below must tolerate late plans by design.
- [[safety-path]]: the vendor itself puts model-level safety beside, not instead of, safety engineering outside the model, the position the safety path takes.

## For zOS

Section 2.4 of the paper: "Robot stacks now separate a reasoning model that plans and calls tools from an action model that drives the motors (Google 2025)." Confirmed: the post describes the model calling a VLA "for motor control". Our reading: one vendor's stack, which the paper's "robot stacks" generalises. No `design/` page changes state.
