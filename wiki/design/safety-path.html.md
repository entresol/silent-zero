# The safety path

> Simplex in Silent Zero: the agent proposes, the loop disposes; tested, not proven; the paper’s 2001 date disputed by a 1994 origin.

Design · LLM reviewed · updated 2026-10-31 · 4 sources · https://silentzero.ooo/wiki/design/safety-path.html

In Silent Zero the agent and its action model play the complex controller of a [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md) architecture: powerful, unproven, isolated and lower in criticality. The safety controller and the switching logic play the simple one; they are small, run at the highest criticality and are candidates for proof. "The agent may suggest any motion. Only the loop moves the motor." (paper, Section 4).

## What it must do

- Decide, for one robot and one task, when the learned controller's command is safe to pass on.
- Hand over to a safe controller before the system leaves the region from which it can recover.
- Rely on nothing the learned side controls: not its inputs, not its timing.
- Stay useful: degrade before it stops.

## What exists, and what kind of evidence it is

| Claim | State | Evidence | Source |
| --- | --- | --- | --- |
| Simplex as a pattern | traced to 1994 and 1998 by a recent paper; the paper's own source, Sha 2001, not read | secondary account | [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) |
| Simplex with learned controllers on a pendulum and a rover, AI isolated by a hypervisor | demonstrated | tests on two systems; switching rule designed per system | [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) |
| Safe side owns the sensors; camera input only on the learned side | demonstrated on the rover | test | [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) |
| A proven safety controller and switching logic | not found in the sources | none | — |

A robot model's vendor says its model-level safety filters "are not a substitute for the rigorous safety engineering required for physical systems" and asks for several layers, with emergency stops and collision avoidance outside the model ([Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md)). Related evidence that is not Simplex: a robot's protective stop caught an oscillating learned controller in an experiment ([Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md), §4.2), and HACMS showed a compromised component contained in flight ([Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)).

## The paper and its sources

- Section 4 cites Sha 2001 and dates the pattern "twenty-five years ago"; Table 1 says "Established since 2001", and the Epilogue "the Simplex pattern from 2001". [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) traces Simplex to Sha, Rajkumar and Gagliardi 1994. Our reading: the pattern is older than the paper says. Sha 2001 itself is not covered here; for the design of Silent Zero the pattern matters, not its first source.
- Section 4's "Most of the engineering lies in deciding what it can reliably detect, for one robot and one task" matches Nesti et al.: the switching rule "requires to be designed for each use case".
- The abstract and Section 4 speak of a "verified loop", while Section 4 also calls the safety controller and switching logic "candidates for proof". Our reading: the paper should keep one of the two; the sources support only the second.

## Open

- The sources show the pattern working in tests. None proves a safety controller or its switching logic against a model of the plant.
- A single bad command can leave the safe region before the monitor reacts; a one-step prediction guards against it and was left out in [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md) (§4.2).
- Safety margins can rest on properties of the learned side, as the rover's lateral zones rested on the network's output bound ([The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md), §5.4).

## Sources

- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)
- [Gemini Robotics-ER 1.5](https://silentzero.ooo/wiki/sources/2025-google-building-next-generation.html.md)
- [Real-Time Execution of Action Chunking Flow Policies](https://silentzero.ooo/wiki/sources/2025-black-real-time-execution.html.md)
- [The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems](https://silentzero.ooo/wiki/sources/2025-nesti-use-simplex-architecture.html.md)

## Related pages

- [Real-time loops](https://silentzero.ooo/wiki/design/real-time-loops.html.md)
- [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html.md)
- [Simplex architecture](https://silentzero.ooo/wiki/concepts/simplex.html.md)
- [Verus](https://silentzero.ooo/wiki/systems/verus.html.md)
