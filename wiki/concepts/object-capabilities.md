---
type: concept
status: reviewed
sources: [2006-miller-robust-composition-towards, 2018-klein-formally-verified-software, 2025-debenedetti-defeating-prompt-injections]
updated: 2026-10-29
---

# Object capabilities

A capability is a reference that indivisibly combines designating an object, the permission to use it, and the means to use it. In the object-capability model, a program can obtain a reference only by holding it from the start, by creating the object, by being created with it, or by being handed it by someone who holds it: "only connectivity begets connectivity" ([[2006-miller-robust-composition-towards]], §9.1, §9.2).

## Permission and authority

Permission is what a program may invoke directly. Authority is every effect it can cause, including through others who act on its behalf. Least authority, not least permission, is what limits damage ([[2006-miller-robust-composition-towards]], §8.1).

## Restricting what a capability grants

A capability by itself gives full and lasting access. Restrictions are built from small programs placed in between: a caretaker that forwards calls until it is switched off makes a grant revocable; a membrane that wraps everything passing through keeps the restriction even against a target that tries to hand out direct access ([[2006-miller-robust-composition-towards]], §9.3). Between machines, a revocation that does not arrive fails unsafe, so a grant should lapse by itself when contact is lost (§11.5.3).

## State, October 2026

- In [[sel4]], all kernel objects are reached through capabilities, and the authority-confinement proof shows that no component gains more authority than the access-control policy predicts ([[2018-klein-formally-verified-software]], §3.1, §3.2). Our reading: in Miller's terms this bounds permission at the kernel level.
- CaMeL attaches tags for provenance and allowed readers to every value an agent handles and checks them before tool calls, calling them capabilities in "the standard security definition" ([[2025-debenedetti-defeating-prompt-injections]], §1, §5.3). Our reading: these are labels for information flow; they designate no resource and convey no authority, so they are related to object capabilities but are not the same thing.

## Open questions

- How kernel capabilities in seL4 map onto credentials for external services an agent calls. See [[broker]].
