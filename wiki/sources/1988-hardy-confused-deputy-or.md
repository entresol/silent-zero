---
type: source
id: 1988-hardy-confused-deputy-or
status: reviewed
read: full
kind: position
sources: [1988-hardy-confused-deputy-or]
updated: 2026-10-29
---

# Hardy 1988: The Confused Deputy

Norm Hardy (Key Logic). ACM SIGOPS Operating Systems Review 22(4), 1988 (venue from the zOS paper's reference list); read in the web copy of MIT's course 6.566. [Text](https://css.csail.mit.edu/6.566/2011/readings/confused-deputy.html).

## What it shows

- **The story.** At Tymshare, about eleven years before the essay, a compiler was given a "home files license" so it could write a statistics file in its own directory. A user named the billing file in the same directory as the compiler's debugging output, and the compiler overwrote it, because the system saw that it had the licence. The essay calls it "a nearly true story (inessential details have been changed)".
- **The diagnosis.** The compiler runs with authority from two sources, its invoker and its own licence, and "has no way to keep them apart". It is a deputy serving two masters. No check on the file name fixes this without breaking legitimate uses; the rules for opening a file grew to fourteen boolean operators.
- **The patch that did not scale.** A system call to "switch hats" let the compiler choose which authority to use, but more than two authorities were soon needed, and other mechanisms besides files had the same problem.
- **The capability answer.** The compiler holds a capability to the statistics file and receives from the invoker a capability to the output file. A capability both designates and authorises, so naming and permission can no longer come apart, and the compiler must designate which authority it is using.
- **A claim from practice.** In Key Logic's systems, capabilities replaced so many other mechanisms that capability-based systems "were usually smaller than equivalent access-list based systems", with excellent performance. Systems that added capabilities to traditional mechanisms "sometimes suffered more from the combined disadvantages than benefitted from the combined advantages".

## How

An essay built on one incident, with the author's experience of KeyKOS. It offers no measurement; the size claim is the author's observation.

## Limits

A careful reader adds:

- **An anecdote, by the author's own account altered in detail.** Its strength is the argument, which later work cites widely ([[2006-miller-robust-composition-towards]], §3.5, calls it the first explanation of why designation and permission must be bundled).
- **The essay leaves the access-list case as an exercise** ("Show that access lists do not solve this problem").

## Against the wiki

- [[confused-deputy]]: created with this source.

## For zOS

- [[broker]]: the paper (Section 2.4) cites this essay for the confused deputy and argues that indirect prompt injection follows the same pattern, citing Greshake et al. 2023 for the phenomenon. The essay supports the first half; the analogy is the paper's. The paper itself limits it in Section 6: capabilities limit how far a deceived agent can reach, "and that is all they do".
- Our reading: the analogy holds for the pattern, a party without authority steering one that has it, but not for the remedy. Hardy's compiler was correct and confused only by an ambiguous name, so passing capabilities removed the attack. An injected agent is subverted in its own decisions and uses capabilities it really holds; capabilities then bound the damage rather than prevent it.
