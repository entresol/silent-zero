# Confused deputy

> A program misusing one party’s authority for another’s request; capabilities as the remedy.

Concept · LLM reviewed · updated 2026-10-31 · 3 sources · https://silentzero.ooo/wiki/concepts/confused-deputy.html

A program that acts with authority from more than one source, and cannot keep them apart, can be tricked into using one party's authority for another party's request. Hardy's compiler held a licence to write in its own directory and wrote a user's debugging output over the billing file there, because the user named it ([The Confused Deputy](https://silentzero.ooo/wiki/sources/1988-hardy-confused-deputy-or.html.md)).

## Why it happens

The request names a resource, and the deputy resolves the name with its own authority. Naming and permission travel separately. Systems that pass references, which both designate and authorise, avoid this case; systems that pass names do not ([The Confused Deputy](https://silentzero.ooo/wiki/sources/1988-hardy-confused-deputy-or.html.md); [Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md), §3.2, which calls these key-centric and name-centric).

## The remedy

Give the deputy a capability for each resource it may use, and have the requester hand over a capability for the resource it means. The deputy must then designate which authority it uses, and cannot use one it was not given ([The Confused Deputy](https://silentzero.ooo/wiki/sources/1988-hardy-confused-deputy-or.html.md)).

## State, October 2026

The pattern and its remedy have been established since 1988; Miller generalises them into the distinction between name-centric and key-centric designation ([Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md), §3.2, §3.5).

## Open questions

- How far the analogy to agents holds. The Silent Zero paper argues that indirect prompt injection follows the same pattern (Section 2.4), citing [Indirect prompt injection](https://silentzero.ooo/wiki/sources/2023-greshake-not-what-you.html.md), which frames retrieved prompts as "arbitrary code" and does not use the term, and states that capabilities only limit how far a deceived agent can reach (Section 6). Our reading: the pattern matches, the remedy does not fully carry over. Hardy's deputy was confused by an ambiguous name; an injected agent is subverted in its own decisions and uses capabilities it really holds. See [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md) and [The broker](https://silentzero.ooo/wiki/design/broker.html.md).

## Sources

- [Indirect prompt injection](https://silentzero.ooo/wiki/sources/2023-greshake-not-what-you.html.md)
- [Robust Composition](https://silentzero.ooo/wiki/sources/2006-miller-robust-composition-towards.html.md)
- [The Confused Deputy](https://silentzero.ooo/wiki/sources/1988-hardy-confused-deputy-or.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md)
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md)
- [Linux kernel documentation: Landlock](https://silentzero.ooo/wiki/sources/nd-linux-landlock-unprivileged-access.html.md)
