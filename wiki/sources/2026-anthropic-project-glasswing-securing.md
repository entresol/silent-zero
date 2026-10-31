---
type: source
id: 2026-anthropic-project-glasswing-securing
status: drafted
read: full
kind: report
sources: [2026-anthropic-project-glasswing-securing]
updated: 2026-10-31
---

# Anthropic 2026a: Project Glasswing, securing critical software for the AI era

Anthropic, announcement of 7 April 2026, with a notice dated 6 October 2026 at its top. [Page](https://www.anthropic.com/glasswing). Read from the page as saved on 23 October 2026.

## What it shows

- **The claim.** An unreleased general-purpose model, Claude Mythos Preview, "has already found thousands of high-severity vulnerabilities, including some in every major operating system and web browser". Anthropic says such models now surpass all but the most skilled humans at finding and exploiting software vulnerabilities.
- **Three examples**, all reported and patched: a 27-year-old flaw in OpenBSD that let an attacker crash a machine remotely; a 16-year-old flaw in FFmpeg, in a line that automated testing had reached five million times; and a chain of several Linux kernel flaws that took an attacker from ordinary user access to full control of the machine. The page says the model found nearly all of these vulnerabilities, and developed many related exploits, without human steering.
- **One benchmark for the security claim.** On CyberGym (vulnerability reproduction) Mythos Preview scores 83.1 per cent, Claude Opus 4.6 66.6 per cent. The page also lists coding and reasoning scores, for instance 93.9 against 80.8 per cent on SWE-bench Verified.
- **The programme.** Twelve launch partners (Amazon Web Services, Anthropic, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks) and more than 40 further organisations get access to find and fix flaws in their own and open-source software. Anthropic commits up to $100M in usage credits and $4M in donations to open-source security organisations.
- **No general release.** Anthropic does not plan to make Mythos Preview generally available and wants safeguards first, to be launched with a coming Claude Opus model.
- **Promised next.** A public report within 90 days, and practical recommendations on, among others, disclosure, updates, supply-chain security and secure-by-design practice.
- **The notice of 6 October 2026** announces an expanded Cyber Verification Program with three access tiers; it does not bear on the claims above.

## How

A company announcement with partner statements. It reports no method and no counts of what was found beyond "thousands". Technical details of a subset of patched flaws are said to be on Anthropic's Frontier Red Team blog, which this page does not reproduce. For flaws not yet fixed, the page says it publishes a cryptographic hash of the details.

## Limits

What the page says itself: the examples are only a subset, and most findings are withheld until patched.

A careful reader adds:

- **The vendor's own word.** Every figure is Anthropic's, and the benchmark numbers compare its own models. The partner quotes are statements of support, not measurements.
- **No counts yet.** "Thousands" is the only number for findings; the later post gives more ([[2026-anthropic-project-glasswing-initial]]).
- **Author and wiki share a maker.** Anthropic makes the Claude models that write and check this wiki. This is one more reason to read the figures as claims.
- **Offence and defence.** The page treats the same capability as a threat and as a tool for defenders; which effect dominates is the authors' expectation, not a result.

## Against the wiki

- [[ai-vulnerability-discovery]]: created with this source.
- [[kernel]], [[sel4]]: no change. The page names no formally verified system among its findings.

## For zOS

The paper cites this page for the 2026 claim in its Section 1 that an unreleased model found thousands of high-severity vulnerabilities, among them a 27-year-old OpenBSD flaw (Anthropic 2026a). Confirmed as stated. The paper's Section 1 also marks these as the company's own figures, which fits this page. No `design/` page changes state: the source is context for why zOS stays small and proven rather than patched, and our reading is that it says nothing about any proof.
