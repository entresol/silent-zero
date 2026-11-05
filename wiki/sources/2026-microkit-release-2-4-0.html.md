# Microkit 2.4.0 release notes

> Microkit 2.4.0 on seL4 17.0.0: reply capabilities and parent fault endpoints no longer leak authority. report, full text.

Source · LLM reviewed · updated 2026-11-03 · https://silentzero.ooo/wiki/sources/2026-microkit-release-2-4-0.html

Release notes for [Microkit 2.4.0](https://docs.sel4.systems/releases/microkit/2.4.0) on the seL4 documentation site. The GitHub releases page of Microkit shows the release as of 30 October, without a year; we take it to be 2026, since the notes name seL4 17.0.0. Read from the page as saved on 3 November 2026.

## What it shows

- **Breaking release on a new kernel.** The notes call the release breaking. Microkit moves from seL4 16.0.0 to 17.0.0, whose changes are breaking for virtual machines.
- **Two security fixes.** Reply capabilities no longer carry the grant-reply permission, which had let a server send capabilities over a reply. A protection domain no longer receives its parent's fault endpoint capability. The notes say that in 2.3.1 such a domain could send its parent fake faults with arbitrary messages, and that in 2.3.0 and earlier it could receive, and so consume, fault messages meant for the parent.
- **Bug fix.** Virtual machines on x86-64 now work with more than one VM per system and in the multicore configuration `x86_64_generic_vtx`. The notes trace the earlier failure to an seL4 bug fixed in kernel pull request 1732.

## How

A release note: a short list of changes with a link to the full changelog. It gives no test results and does not say how the fixes were found.

## Limits

Our reading: the notes describe what changed, not whether the two leaks could be exploited in a real system, or whether the new behaviour is covered by any proof. [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md) states that its tool, loader and initialiser are not verified.

## Against the wiki

- [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md): replaces version 2.3.0 as the current release and adds the two fixes.
- [The static system](https://silentzero.ooo/wiki/design/static-system.html.md): the static layer's authority rules held two gaps up to 2.3.1; the page now says so.
- [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md), [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md): both build on Microkit; the notes do not say which Microkit version they use.

## For Silent Zero

Section 3 of the paper names Microkit as the static system but no version. No claim of the paper changes. The fault-endpoint fix touches the design rule that a child gets only the authority its description declares ([The static system](https://silentzero.ooo/wiki/design/static-system.html.md)).

## Related pages

- [The static system](https://silentzero.ooo/wiki/design/static-system.html.md)
- [agentOS](https://silentzero.ooo/wiki/systems/agentos.html.md)
- [LionsOS](https://silentzero.ooo/wiki/systems/lionsos.html.md)
- [Microkit](https://silentzero.ooo/wiki/systems/microkit.html.md)
