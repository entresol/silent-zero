# Object capabilities

> References that both designate and authorise; permission versus authority; caretaker and membrane.

Concept · LLM reviewed · updated 2026-10-31 · 5 sources · https://silentzero.ooo/wiki/concepts/object-capabilities.html

A capability is a reference that indivisibly combines designating an object, the permission to use it, and the means to use it. In the object-capability model, a program can obtain a reference only by holding it from the start, by creating the object, by being created with it, or by being handed it by someone who holds it: "only connectivity begets connectivity" ([Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md), §9.1, §9.2).

## Permission and authority

Permission is what a program may invoke directly. Authority is every effect it can cause, including through others who act on its behalf. Least authority, not least permission, is what limits damage ([Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md), §8.1).

## Restricting what a capability grants

A capability by itself gives full and lasting access. Restrictions are built from small programs placed in between: a caretaker that forwards calls until it is switched off makes a grant revocable; a membrane that wraps everything passing through keeps the restriction even against a target that tries to hand out direct access ([Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md), §9.3). Between machines, a revocation that does not arrive fails unsafe, so a grant should lapse by itself when contact is lost (§11.5.3).

## State, October 2026

- In [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md), all kernel objects are reached through capabilities, and the authority-confinement proof shows that no component gains more authority than the access-control policy predicts ([Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md), §3.1, §3.2). Our reading: in Miller's terms this bounds permission at the kernel level.
- CaMeL attaches tags for provenance and allowed readers to every value an agent handles and checks them before tool calls, calling them capabilities in "the standard security definition" ([Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md), §1, §5.3). Our reading: these are labels for information flow; they designate no resource and convey no authority, so they are related to object capabilities but are not the same thing.
- In hardware, CHERI makes every pointer a capability with bounds and permissions that the processor checks on each memory access and that cannot be forged or widened. CHERIoT adapts it to 32-bit RISC-V embedded cores and adds revocation of capabilities to freed memory ([CHERIoT, complete memory safety for embedded devices](https://silentzero.ooo/wiki/sources/2023-amar-cheriot-complete-memory.html.md), §2.4, §3.3). See [CHERIoT](https://silentzero.ooo/wiki/systems/cheriot.html.md).
- FIDES, like CaMeL, labels data for information flow; the labels convey no authority ([Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md); our reading). See [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md).

## Open questions

- How kernel capabilities in seL4 map onto credentials for external services an agent calls. See [The broker](https://silentzero.ooo/wiki/design/broker.html.md).

## Sources

- [CHERIoT, complete memory safety for embedded devices](https://silentzero.ooo/wiki/sources/2023-amar-cheriot-complete-memory.html.md)
- [Defeating Prompt Injections by Design (CaMeL)](https://silentzero.ooo/wiki/sources/2025-debenedetti-defeating-prompt-injections.html.md)
- [Formally Verified Software in the Real World](https://silentzero.ooo/wiki/sources/2018-klein-formally-verified-software.html.md)
- [Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md)
- [Securing AI agents with information-flow control](https://silentzero.ooo/wiki/sources/2025-costa-securing-ai-agents.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Information-flow control](https://silentzero.ooo/wiki/concepts/information-flow-control.html.md)
- [CHERIoT](https://silentzero.ooo/wiki/systems/cheriot.html.md)
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md)
- [seL4](https://silentzero.ooo/wiki/systems/sel4.html.md)
- [AgentKernel](https://silentzero.ooo/wiki/sources/2026-zou-agentkernel-trust-native.html.md)
- [Linux kernel documentation: Landlock](https://silentzero.ooo/wiki/sources/nd-linux-landlock-unprivileged-access.html.md)
- [MCP-38](https://silentzero.ooo/wiki/sources/2026-shen-mcp-38-comprehensive.html.md)
