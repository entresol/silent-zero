---
type: concept
status: reviewed
sources: [1988-hardy-confused-deputy-or, 2006-miller-robust-composition-towards]
glossary: Confused deputy
updated: 2026-10-29
---

# Confused deputy

A program that acts with authority from more than one source, and cannot keep them apart, can be tricked into using one party's authority for another party's request. Hardy's compiler held a licence to write in its own directory and wrote a user's debugging output over the billing file there, because the user named it ([[1988-hardy-confused-deputy-or]]).

## Why it happens

The request names a resource, and the deputy resolves the name with its own authority. Naming and permission travel separately. Systems that pass references, which both designate and authorise, avoid this case; systems that pass names do not ([[1988-hardy-confused-deputy-or]]; [[2006-miller-robust-composition-towards]], §3.2, which calls these key-centric and name-centric).

## The remedy

Give the deputy a capability for each resource it may use, and have the requester hand over a capability for the resource it means. The deputy must then designate which authority it uses, and cannot use one it was not given ([[1988-hardy-confused-deputy-or]]).

## State, October 2026

The pattern and its remedy have been established since 1988; Miller generalises them into the distinction between name-centric and key-centric designation ([[2006-miller-robust-composition-towards]], §3.2, §3.5).

## Open questions

- How far the analogy to agents holds. The zOS paper argues that indirect prompt injection follows the same pattern (Section 2.4) and states that capabilities only limit how far a deceived agent can reach (Section 6). Our reading: the pattern matches, the remedy does not fully carry over. Hardy's deputy was confused by an ambiguous name; an injected agent is subverted in its own decisions and uses capabilities it really holds. See [[prompt-injection]] and [[broker]].
